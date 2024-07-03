import boto3  # Importa el módulo boto3 para interactuar con los servicios de AWS
import logging  # Importa el módulo de logging para registrar eventos
import os  # Importa el módulo os para interactuar con el sistema operativo

# Configurar logging para registrar eventos importantes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Guardar la información en un archivo
def save_to_file(filename, content):
    """
    Guarda el contenido en un archivo dentro del directorio 'data'.

    Parámetros
    ---
    filename: Nombre del archivo donde se guardará el contenido.
    content: Contenido a guardar en el archivo.
    """
    dir_actual = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio actual del archivo
    ruta = os.path.join(dir_actual, 'data')  # Crea la ruta para el directorio 'data'
    
    if not os.path.exists(ruta):
        os.makedirs(ruta)  # Crea el directorio 'data' si no existe
    
    filepath = os.path.join(ruta, filename)  # Crea la ruta completa para el archivo
    with open(filepath, 'w') as f:  # Abre el archivo en modo escritura
        f.write(content)  # Escribe el contenido en el archivo

# Crear un Web ACL
def create_web_acl(nombre_webacl):
    """
    Crea un Web ACL en AWS WAFv2 para CloudFront.

    Parámetros
    ---
    nombre_webacl: Nombre del Web ACL a crear.

    Retorna
    ---
    Respuesta de la creación del Web ACL o None si ocurre un error.
    """
    client = boto3.client('wafv2')  # Crea un cliente de WAFv2
    try:
        response = client.create_web_acl(
            Name=nombre_webacl,
            Scope='CLOUDFRONT',  # Para CloudFront
            DefaultAction={'Allow': {}},
            Description='Web ACL for CloudFront',
            Rules=[],
            VisibilityConfig={
                'SampledRequestsEnabled': True,
                'CloudWatchMetricsEnabled': True,
                'MetricName': 'myWebACL'
            }
        )
        logging.info("Creación exitosa del Web ACL")  # Registra el éxito de la creación
        return response  # Retorna la respuesta de la creación
    except client.exceptions.WAFInvalidParameterException as e:
        logging.error(f"{e} Los parámetros no son válidos. No se pudo crear el Web ACL")  # Registra el error de parámetros inválidos
        return None
    except client.exceptions.WAFDuplicateItemException as e:
        logging.error(f"{e} Ya existe un Web ACL con el mismo nombre")  # Registra si ya existe un Web ACL con el mismo nombre
        return None

# Obtener el ARN de un Web ACL
nombre_webacl = "my-web-acl"
response_web_acl = create_web_acl(nombre_webacl)  # Crea el Web ACL
web_acl_arn = response_web_acl['Summary']['ARN']  # Obtiene el ARN del Web ACL
print(f'Web ACL ARN: {web_acl_arn}')  # Imprime el ARN del Web ACL
save_to_file('web_acl_arn.txt', web_acl_arn)  # Guarda el ARN del Web ACL en un archivo

# Asociar un Web ACL con una distribución de CloudFront
# Asumimos que la distribución existe
distribution_id = "123"

# Función para obtener la configuración actual de una distribución de CloudFront
def obtener_config_distribution(distribution_id):
    """
    Obtiene la configuración actual de una distribución de CloudFront.

    Parámetros
    ---
    distribution_id: ID de la distribución de CloudFront.

    Retorna
    ---
    Respuesta de la obtención de la configuración o None si ocurre un error.
    """
    client = boto3.client('cloudfront')  # Crea un cliente de CloudFront
    try:
        response = client.get_distribution_config(Id=distribution_id)
        return response  # Retorna la respuesta de la obtención de la configuración
    except client.exceptions.NoSuchDistribution as e:
        logging.error(f"No existe la distribución {distribution_id}")  # Registra si no se encuentra la distribución
        return None
    except client.exceptions.AccessDenied as e:
        logging.error(f"Acceso denegado. No tiene los permisos para ejecutar esta acción")  # Registra si se deniega el acceso
        return None

# Función para actualizar la configuración de una distribución de CloudFront
def update_distribution_cloudfront(distribution_id, distribution_config, etag):
    """
    Actualiza la configuración de una distribución de CloudFront.

    Parámetros
    ---
    distribution_id: ID de la distribución de CloudFront.
    distribution_config: Configuración actualizada de la distribución.
    etag: ETag de la configuración actual de la distribución.

    Retorna
    ---
    Respuesta de la actualización de la distribución o None si ocurre un error.
    """
    client = boto3.client('cloudfront')  # Crea un cliente de CloudFront
    try:
        response = client.update_distribution(
            DistributionConfig=distribution_config,
            Id=distribution_id,
            IfMatch=etag
        )
        logging.info(f"Distribución {distribution_id} de CloudFront actualizada correctamente")  # Registra el éxito de la actualización
        return response  # Retorna la respuesta de la actualización
    except client.exceptions.NoSuchDistribution as e:
        logging.error(f"No se encontró la distribución con ID {distribution_id}")  # Registra si no se encuentra la distribución
        return None
    except client.exceptions.AccessDenied as e:
        logging.error(f"Acceso denegado. No tiene los permisos para ejecutar esta acción")  # Registra si se deniega el acceso
        return None

# Función para asociar un Web ACL con una distribución de CloudFront
def asociar_waf_cloudfront(distribution_id, web_acl_arn, response_distribution):
    """
    Asocia un Web ACL con una distribución de CloudFront.

    Parámetros
    ---
    distribution_id: ID de la distribución de CloudFront.
    web_acl_arn: ARN del Web ACL a asociar.
    response_distribution: Respuesta de la configuración actual de la distribución de CloudFront.

    Retorna
    ---
    Respuesta de la asociación o None si ocurre un error.
    """
    etag = response_distribution['ETag']  # Identificador de versión de la configuración actual
    distribution_config = response_distribution['DistributionConfig']  # Configuración actual de la distribución
    distribution_config["WebACLId"] = web_acl_arn  # Asigna el ARN del Web ACL a la distribución
    
    response = update_distribution_cloudfront(distribution_id, distribution_config, etag)  # Actualiza la distribución de CloudFront
    if response:
        print('Distribución se ha asociado al Web ACL correctamente')  # Imprime el éxito de la asociación
        return response  # Retorna la respuesta de la asociación
    else:
        print('Error al asociar el Web ACL con la distribución')  # Imprime si hay un error en la asociación
        return None

response_distribution = obtener_config_distribution(distribution_id)  # Obtiene la configuración actual de la distribución
if response_distribution:
    response = asociar_waf_cloudfront(distribution_id, web_acl_arn, response_distribution)  # Asocia el Web ACL con la distribución
    if response:
        save_to_file('distribution_config.txt', str(response))  # Guarda la configuración de la distribución en un archivo
