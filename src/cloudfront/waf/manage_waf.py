import boto3  # Importa el módulo boto3 para interactuar con los servicios de AWS
import logging  # Importa el módulo de logging para registrar eventos
from setup_cloudfront import save_to_file

# Configurar logging para registrar eventos importantes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Definir reglas
rules = [
    {
        'Name': 'SQLInjectionRule', 
        'Priority': 1,
        'Statement': {
            'ManagedRuleGroupStatement': {
                'VendorName': 'AWS',
                'Name': 'AWSManagedRulesSQLiRuleSet'
            }
        },
        'Action': {
            'Block': {}
        },
        'VisibilityConfig': {
            'SampledRequestsEnabled': True,
            'CloudWatchMetricsEnabled': True,
            'MetricName': 'SQLInjection'
        }
    },
    {
        'Name': 'XSSRule',
        'Priority': 2,
        'Statement': {
            'ManagedRuleGroupStatement': {
                'VendorName': 'AWS',
                'Name': 'AWSManagedRulesXSSRuleSet'
            }
        },
        'Action': {
            'Block': {}
        },
        'VisibilityConfig': {
            'SampledRequestsEnabled': True,
            'CloudWatchMetricsEnabled': True,
            'MetricName': 'XSS'
        }
    }
]

rule_group_name = "my-rules"

# Crear un grupo de reglas
def create_rule_group(rule_group_name, rules):
    """
    Crea un grupo de reglas en AWS WAFv2.

    Parámetros
    ---
    rule_group_name: Nombre del grupo de reglas a crear.
    rules: Lista de reglas a incluir en el grupo.

    Retorna
    ---
    Respuesta de la creación del grupo de reglas o None si ocurre un error.
    """
    try:
        client = boto3.client('wafv2')  # Crea un cliente de WAFv2
        
        # Crear el grupo de reglas
        response = client.create_rule_group(
            Name=rule_group_name,
            Capacity=100,
            Scope='REGIONAL',  # Ámbito del grupo de reglas
            Description=f'Rule Group for {rule_group_name}',
            Rules=rules,
            VisibilityConfig={
                'SampledRequestsEnabled': True,
                'CloudWatchMetricsEnabled': True,
                'MetricName': f'{rule_group_name}Metrics'
            }
        )

        logging.info(f"Grupo de reglas '{rule_group_name}' creado correctamente.")
        return response

    except Exception as e:
        logging.error(f"Error al crear el grupo de reglas {rule_group_name}: {e}")
        return None

rule_group_response = create_rule_group(rule_group_name, rules)
save_to_file('rule_group.txt', rule_group_response)

# Obtener la configuración actual de una Web ACL
def get_web_acl(web_acl_name, scope, web_acl_id):
    """
    Obtiene la configuración actual de una Web ACL en AWS WAFv2.

    Parámetros
    ---
    web_acl_name: Nombre de la Web ACL.
    scope: Ámbito de la Web ACL ('REGIONAL' o 'CLOUDFRONT').
    web_acl_id: ID de la Web ACL.

    Retorna
    ---
    Configuración de la Web ACL y el LockToken o (None, None) si ocurre un error.
    """
    client = boto3.client('wafv2')  # Crea un cliente de WAFv2
    try:
        response = client.get_web_acl(
            Name=web_acl_name,
            Scope=scope,
            Id=web_acl_id
        )
        web_acl_config = response['WebACL']
        lock_token = response['LockToken']

        return web_acl_config, lock_token 

    except Exception as e:
        logging.error(f"Error al obtener la configuración de la Web ACL {web_acl_id}: {e}")
        return None, None

# Actualizar una Web ACL con un grupo de reglas
def update_web_acl_with_rule_group(web_acl_name, scope, web_acl_id, rule_group_arn):
    """
    Actualiza una Web ACL en AWS WAFv2 con un nuevo grupo de reglas.

    Parámetros
    ---
    web_acl_name: Nombre de la Web ACL.
    scope: Ámbito de la Web ACL ('REGIONAL' o 'CLOUDFRONT').
    web_acl_id: ID de la Web ACL.
    rule_group_arn: ARN del grupo de reglas a añadir.

    Retorna
    ---
    Respuesta de la actualización de la Web ACL o None si ocurre un error.
    """
    client = boto3.client('wafv2')  # Crea un cliente de WAFv2

    web_acl_config, lock_token = get_web_acl(web_acl_name, scope, web_acl_id)

    if not web_acl_config or not lock_token:
        logging.error(f"No se pudo obtener la configuración de la Web ACL '{web_acl_name}'.")
        return None

    # Añadir el Rule Group a la lista de reglas
    rule_group_rule = {
        'Name': 'MyRuleGroupRule',
        'Priority': len(web_acl_config['Rules']) + 1,
        'Statement': {
            'RuleGroupReferenceStatement': {
                'ARN': rule_group_arn
            }
        },
        'Action': {
            'Allow': {}  # Puede ser Block o Allow dependiendo de tu necesidad
        },
        'VisibilityConfig': {
            'SampledRequestsEnabled': True,
            'CloudWatchMetricsEnabled': True,
            'MetricName': 'MyRuleGroupRule'
        }
    }

    web_acl_config['Rules'].append(rule_group_rule)

    try:
        response = client.update_web_acl(
            Name=web_acl_name,
            Scope=scope,
            Id=web_acl_id,
            DefaultAction=web_acl_config['DefaultAction'],
            Rules=web_acl_config['Rules'],
            VisibilityConfig=web_acl_config['VisibilityConfig'],
            LockToken=lock_token
        )
        logging.info(f"Web ACL '{web_acl_name}' actualizada correctamente.")
        return response
    except Exception as e:
        logging.error(f"Error al actualizar la Web ACL {web_acl_name}: {e}")
        return None

# Variables de configuración
web_acl_name = 'id-web-acl'
scope = 'CLOUDFRONT'
web_acl_id = 'web-acl-id'
rule_group_arn = rule_group_response['Summary']['ARN']

# Actualizar la Web ACL con las nuevas reglas gestionadas
update_response = update_web_acl_with_rule_group(web_acl_name, scope, web_acl_id, rule_group_arn)  
if update_response:
    logging.info(f'Web ACL {web_acl_id} actualizado correctamente')
else:
    logging.error('Error al actualizar la Web ACL.')
