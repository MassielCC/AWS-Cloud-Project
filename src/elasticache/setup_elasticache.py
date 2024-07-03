import boto3
import botocore
import os
import time
import logging

# Configurar logging para registrar eventos importantes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def save_to_file(filename, content):
    """
    Guarda el contenido en un archivo dentro del directorio 'data'.

    Parámetros
    ---
    filename: Nombre del archivo donde se guardará el contenido.
    content: Contenido a guardar en el archivo.
    """
    directory = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(directory):  # Verifica si el directorio 'data' existe
        os.makedirs(directory)  # Crea el directorio 'data' si no existe
    filepath = os.path.join(directory, filename)  # Obtiene la ruta completa del archivo
    with open(filepath, 'w') as f:  # Abre el archivo en modo escritura
        f.write(content)  # Escribe el contenido en el archivo

def create_security_group(client, group_name, description):
    """
    Crea un grupo de seguridad o recupera uno existente.

    Parámetros
    ---
    client: Cliente de AWS para interactuar con EC2.
    group_name: Nombre del grupo de seguridad a crear/recuperar.
    description: Descripción del grupo de seguridad.

    Retorna
    ---
    ID del grupo de seguridad creado/recuperado.
    """
    try:
        response = client.create_security_group(
            Description=description,
            GroupName=group_name
        )
        group_id = response['GroupId']  # Obtiene el ID del grupo de seguridad creado
        save_to_file(f'{group_name}_security_group_id.txt', group_id)  # Guarda el ID en un archivo
        logging.info(f"Grupo de seguridad creado: {group_name}")  # Registra un evento de creación exitosa
        return group_id
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'InvalidGroup.Duplicate':
            response = client.describe_security_groups(GroupNames=[group_name])
            group_id = response['SecurityGroups'][0]['GroupId']  # Obtiene el ID del grupo de seguridad existente
            save_to_file(f'{group_name}_security_group_id.txt', group_id)  # Guarda el ID en un archivo
            logging.info(f"Grupo de seguridad existente recuperado: {group_id}")  # Registra un evento de recuperación exitosa
            return group_id
        else:
            logging.error(f"Error al crear grupo de seguridad: {error}")  # Registra un error si no se puede crear el grupo
            raise

def configure_security_group(client, group_id):
    """
    Configura las reglas de entrada para el grupo de seguridad.

    Parámetros
    ---
    client: Cliente de AWS para interactuar con EC2.
    group_id: ID del grupo de seguridad a configurar.
    """
    try:
        client.authorize_security_group_ingress(
            GroupId=group_id,
            IpPermissions=[
                {
                    'IpProtocol': 'tcp',
                    'FromPort': 6379,
                    'ToPort': 6379,
                    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                }
            ]
        )
        logging.info(f"Reglas de entrada configuradas para el grupo {group_id}")  # Registra un evento de configuración exitosa
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'InvalidPermission.Duplicate':
            logging.info("Las reglas de entrada ya están configuradas")  # Registra un evento si las reglas ya están configuradas
        else:
            logging.error(f"Error al configurar reglas de entrada: {error}")  # Registra un error si no se pueden configurar las reglas
            raise

def create_cache_subnet_group(client, subnet_group_name, subnet_ids, description):
    """
    Crea un grupo de subredes para ElastiCache o recupera uno existente.

    Parámetros
    ---
    client: Cliente de AWS para interactuar con ElastiCache.
    subnet_group_name: Nombre del grupo de subredes a crear/recuperar.
    subnet_ids: IDs de las subredes asociadas al grupo.
    description: Descripción del grupo de subredes.

    Retorna
    ---
    Nombre del grupo de subredes creado/recuperado.
    """
    try:
        response = client.create_cache_subnet_group(
            CacheSubnetGroupName=subnet_group_name,
            CacheSubnetGroupDescription=description,
            SubnetIds=subnet_ids
        )
        subnet_group = response['CacheSubnetGroup']['CacheSubnetGroupName']  # Obtiene el nombre del grupo de subredes creado
        save_to_file(f'{subnet_group_name}_subnet_group_name.txt', subnet_group)  # Guarda el nombre en un archivo
        logging.info(f"Grupo de subredes creado: {subnet_group}")  # Registra un evento de creación exitosa
        return subnet_group
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'CacheSubnetGroupAlreadyExists':
            response = client.describe_cache_subnet_groups(CacheSubnetGroupName=subnet_group_name)
            subnet_group = response['CacheSubnetGroups'][0]['CacheSubnetGroupName']  # Obtiene el nombre del grupo de subredes existente
            save_to_file(f'{subnet_group_name}_subnet_group_name.txt', subnet_group)  # Guarda el nombre en un archivo
            logging.info(f"Grupo de subredes existente recuperado: {subnet_group}")  # Registra un evento de recuperación exitosa
            return subnet_group
        else:
            logging.error(f"Error al crear grupo de subredes: {error}")  # Registra un error si no se puede crear el grupo de subredes
            raise

def create_cache_cluster(client, cluster_id, node_type, engine_version, subnet_group_name, security_group_ids):
    """
    Crea un clúster de ElastiCache o recupera uno existente.

    Parámetros
    ---
    client: Cliente de AWS para interactuar con ElastiCache.
    cluster_id: ID del clúster de ElastiCache a crear/recuperar.
    node_type: Tipo de nodo del clúster.
    engine_version: Versión del motor de ElastiCache.
    subnet_group_name: Nombre del grupo de subredes asociado al clúster.
    security_group_ids: IDs de los grupos de seguridad asociados al clúster.

    Retorna
    ---
    ID del clúster de ElastiCache creado/recuperado.
    """
    try:
        response = client.create_cache_cluster(
            CacheClusterId=cluster_id,
            NumCacheNodes=1,
            CacheNodeType=node_type,
            Engine='redis',
            EngineVersion=engine_version,
            CacheSubnetGroupName=subnet_group_name,
            SecurityGroupIds=security_group_ids,
            Port=6379
        )
        cluster_id = response['CacheCluster']['CacheClusterId']  # Obtiene el ID del clúster de ElastiCache creado
        save_to_file(f'{cluster_id}_cache_cluster_id.txt', cluster_id)  # Guarda el ID en un archivo
        logging.info(f"Clúster de ElastiCache creado: {cluster_id}")  # Registra un evento de creación exitosa
        return cluster_id
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'CacheClusterAlreadyExists':
            response = client.describe_cache_clusters(CacheClusterId=cluster_id)
            cluster_id = response['CacheClusters'][0]['CacheClusterId']  # Obtiene el ID del clúster de ElastiCache existente
            save_to_file(f'{cluster_id}_cache_cluster_id.txt', cluster_id)  # Guarda el ID en un archivo
            logging.info(f"Clúster de ElastiCache existente recuperado: {cluster_id}")  # Registra un evento de recuperación exitosa
            return cluster_id
        else:
            logging.error(f"Error al crear clúster de ElastiCache: {error}")  # Registra un error si no se puede crear el clúster
            raise

def wait_for_node_info(client, cluster_id, max_attempts=10, delay=200):
    """
    Espera a que la información del nodo esté disponible.

    Parámetros
    ---
    client: Cliente de AWS para interactuar con ElastiCache.
    cluster_id: ID del clúster de ElastiCache.
    max_attempts: Número máximo de intentos antes de lanzar un error.
    delay: Tiempo de espera entre intentos en segundos.

    Retorna
    ---
    Dirección del endpoint Redis del clúster.
    """
    for attempt in range(max_attempts):
        try:
            cluster_info = client.describe_cache_clusters(CacheClusterId=cluster_id, ShowCacheNodeInfo=True)
            redis_endpoint = cluster_info['CacheClusters'][0]['CacheNodes'][0]['Endpoint']['Address']  # Obtiene la dirección del nodo Redis
            save_to_file(f'{cluster_id}_redis_endpoint.txt', redis_endpoint)  # Guarda la dirección en un archivo
            logging.info(f"Endpoint de Redis disponible: {redis_endpoint}")  # Registra un evento de disponibilidad del endpoint
            return redis_endpoint
        except (KeyError, IndexError):
            logging.info(f"Esperando información del nodo... Intento {attempt + 1}/{max_attempts}")  # Registra intentos de espera
            time.sleep(delay)  # Espera antes de intentar nuevamente
    logging.error("Tiempo de espera agotado para obtener información del nodo")  # Registra un error si se agota el tiempo de espera
    raise TimeoutError("No se pudo obtener la información del nodo en el tiempo esperado")

def setup_elasticache():
    """Función principal para configurar ElastiCache."""
    clienteEC2 = boto3.client('ec2')
    clienteElasticache = boto3.client('elasticache')

    # Obtener nombres y descripciones del usuario para configurar grupos y clústeres
    security_group_name = input("Nombre del grupo de seguridad: ")
    security_group_description = input("Descripción del grupo de seguridad: ")
    security_group_id = create_security_group(clienteEC2, security_group_name, security_group_description)
    configure_security_group(clienteEC2, security_group_id)

    subnet_ids = ['subnet-0a7c988fd9507f575', 'subnet-07a9ebb4c8a79f2d0']  # Asegúrate de usar IDs de subred válidos
    subnet_group_name = input("Nombre del grupo de subredes: ")
    subnet_group_description = input("Descripción del grupo de subredes: ")
    create_cache_subnet_group(clienteElasticache, subnet_group_name, subnet_ids, subnet_group_description)

    cluster_id = input("ID del clúster de ElastiCache: ")
    node_type = 'cache.t2.micro'
    engine_version = '7.0'
    security_group_ids = [security_group_id]

    create_cache_cluster(clienteElasticache, cluster_id, node_type, engine_version, subnet_group_name, security_group_ids)
    wait_for_node_info(clienteElasticache, cluster_id)

if __name__ == "__main__":
    setup_elasticache()
