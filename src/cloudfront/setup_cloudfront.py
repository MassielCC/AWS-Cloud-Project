import boto3  # Importa el módulo boto3 para interactuar con los servicios de AWS
import datetime  # Importa el módulo datetime para manejar fechas y tiempos
import time  # Importa el módulo time para manejar funciones de tiempo
import logging  # Importa el módulo de logging para registrar eventos
import os  # Importa el módulo os para interactuar con el sistema operativo
from manage_cloudfront import create_invalidation #Importa la función para crear una invalidación de caché
from manage_cloudfront import get_cloudfront_metrics #Importa la función para acceder a las métricas de cloudfront

# Configurar logging para registrar eventos importantes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Guardar la informacion en un archivo
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

# Crear distribución de CloudFront
def create_cloudfront_distribution(bucket_name, origin_id, distribution_comment):
    """
    Crea una distribución de CloudFront para un bucket de S3.

    Parámetros
    ---
    bucket_name: Nombre del bucket de S3.
    origin_id: ID del origen para la distribución.
    distribution_comment: Comentario para la distribución.

    Retorna
    ---
    Respuesta de la creación de la distribución o None si ocurre un error.
    """
    client = boto3.client('cloudfront')  # Crea un cliente de CloudFront

    try:
        response = client.create_distribution(
            DistributionConfig={
                'CallerReference': str(time.time()),  # Referencia única para la solicitud
                'Comment': distribution_comment,  # Comentario de la distribución
                'Enabled': True,  # Habilita la distribución
                'Origins': {
                    'Items': [
                        {
                            'Id': origin_id,  # ID del origen
                            'DomainName': f'{bucket_name}.s3.amazonaws.com',  # Nombre de dominio del origen
                            'S3OriginConfig': {
                                'OriginAccessIdentity': ''  # Identidad de acceso del origen
                            }
                        }
                    ],
                    'Quantity': 1  # Cantidad de orígenes
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': origin_id,  # ID del origen de destino
                    'ViewerProtocolPolicy': 'redirect-to-https',  # Política de protocolo del visor
                    'ForwardedValues': {
                        'QueryString': False,  # No reenvía la cadena de consulta
                        'Cookies': {
                            'Forward': 'none'  # No reenvía las cookies
                        }
                    },
                    'TrustedSigners': {
                        'Enabled': False,  # No habilita firmantes de confianza
                        'Quantity': 0  # Cantidad de firmantes de confianza
                    },
                    'MinTTL': 0,  # Tiempo mínimo de vida (TTL)
                    'AllowedMethods': {
                        'Quantity': 2,  # Cantidad de métodos permitidos
                        'Items': ['GET', 'HEAD'],  # Métodos permitidos
                        'CachedMethods': {
                            'Quantity': 2,  # Cantidad de métodos en caché
                            'Items': ['GET', 'HEAD']  # Métodos en caché
                        }
                    },
                    'Compress': True  # Habilita la compresión
                }
            }
        )
        logging.info("Creación exitosa de distribución CloudFront")  # Registra el éxito de la creación
        return response  # Retorna la respuesta de la creación
    except client.exceptions.DistributionAlreadyExists as e:
        logging.error("La distribución de CloudFront ya existe.")  # Registra si la distribución ya existe
        return None  # Retorna None en caso de error

# Crear el bucket s3 
def create_s3_bucket(bucket_name):
    """
    Crea un bucket en S3.

    Parámetros
    ---
    bucket_name: Nombre del bucket a crear.

    Retorna
    ---
    Respuesta de la creación del bucket o None si ocurre un error.
    """
    s3 = boto3.client('s3')  # Crea un cliente de S3
    try:
        response = s3.create_bucket(
            Bucket=bucket_name  # Nombre del bucket
        )
        logging.info(f"Bucket S3 '{bucket_name}' creado exitosamente.")  # Registra el éxito de la creación
        return response  # Retorna la respuesta de la creación
    except s3.exceptions.BucketAlreadyExists as e:
        logging.error(f"El bucket S3 '{bucket_name}' ya existe.")  # Registra si el bucket ya existe
        return None  # Retorna None en caso de error
    
bucket_name = 'mi-bucket-cloud'  # Nombre del bucket
region = "us-east-1"  # Región de AWS
response_s3 = create_s3_bucket(bucket_name)  # Crea el bucket S3

origin_id = bucket_name + ".s3." + region + ".amazonaws.com"  # ID del origen
distribution_comment = 'Distribution for serving static content from S3'  # Comentario de la distribución

response = create_cloudfront_distribution(bucket_name, origin_id, distribution_comment)  # Crea la distribución de CloudFront
if response:
    distribution_id = response['Distribution']['Id']  # Obtiene el ID de la distribución
    distribution_domain_name = response['Distribution']['DomainName']  # Obtiene el nombre de dominio de la distribución
    save_to_file('distribution_id.txt', distribution_id)  # Guarda el ID de la distribución en un archivo
    save_to_file('distribution_domain_name.txt', distribution_domain_name)  # Guarda el nombre de dominio de la distribución en un archivo
    print(f'Distribution ID: {distribution_id}')  # Imprime el ID de la distribución
    print(f'Distribution Domain Name: {distribution_domain_name}')  # Imprime el nombre de dominio de la distribución
    logging.info("Guardando el id y nombre de dominio de la distribución")  # Registra la acción
else:
    # Recuperar la distribución existente
    client = boto3.client('cloudfront')  # Crea un cliente de CloudFront
    distributions = client.list_distributions()  # Lista las distribuciones existentes
    for distribution in distributions['DistributionList']['Items']:
        if distribution['Origins']['Items'][0]['DomainName'] == f'{bucket_name}.s3.amazonaws.com':
            distribution_id = distribution['Id']  # Obtiene el ID de la distribución existente
            distribution_domain_name = distribution['DomainName']  # Obtiene el nombre de dominio de la distribución existente
            save_to_file('distribution_id.txt', distribution_id)  # Guarda el ID de la distribución existente en un archivo
            save_to_file('distribution_domain_name.txt', distribution_domain_name)  # Guarda el nombre de dominio de la distribución existente en un archivo
            print(f'Using existing Distribution ID: {distribution_id}')  # Imprime el ID de la distribución existente
            print(f'Using existing Distribution Domain Name: {distribution_domain_name}')  # Imprime el nombre de dominio de la distribución existente
            logging.info("Guardando el id y nombre de dominio de la distribución")  # Registra la acción
            break

# Actualizar configuración de caché
def update_cache_behavior(distribution_id, cache_behavior_settings):
    """
    Actualiza la configuración de comportamiento de caché de una distribución de CloudFront.

    Parámetros
    ---
    distribution_id: ID de la distribución de CloudFront.
    cache_behavior_settings: Configuración de comportamiento de caché a actualizar.

    Retorna
    ---
    Respuesta de la actualización de la distribución o None si ocurre un error.
    """
    client = boto3.client('cloudfront')  # Crea un cliente de CloudFront

    try:
        # Obtener la configuración actual de la distribución
        response = client.get_distribution_config(Id=distribution_id)
        etag = response['ETag']  # Obtiene el ETag de la configuración
        distribution_config = response['DistributionConfig']  # Obtiene la configuración de la distribución

        # Actualizar el comportamiento de caché
        distribution_config['DefaultCacheBehavior'].update(cache_behavior_settings)

        response = client.update_distribution(
            Id=distribution_id,
            IfMatch=etag, # Usa el ETag para asegurar la actualización
            DistributionConfig=distribution_config  # Pasa la configuración actualizada
        )
        return response  # Retorna la respuesta de la actualización
    except client.exceptions.NoSuchDistribution as e:
        print("La distribución de CloudFront no existe.")  # Imprime si la distribución no existe
        return None  # Retorna None en caso de error

cache_behavior_settings = {
    'MinTTL': 86400,  # 1 día
    'MaxTTL': 31536000,  # 1 año
    'DefaultTTL': 86400,  # 1 día
    'ForwardedValues': {
        'QueryString': False,  # No reenviar cadena de consulta
        'Cookies': {
            'Forward': 'none'  # No reenviar cookies
        }
    },
    'Compress': True  # Habilitar compresión
}

response = update_cache_behavior(distribution_id, cache_behavior_settings)  # Actualiza el comportamiento de caché
if response:
    save_to_file('updated_distribution_config.txt', str(response))  # Guarda la respuesta en un archivo
    print(f'Distribution {distribution_id} cache behavior updated successfully.')  # Imprime el éxito de la actualización
    logging.info("Distribución de CloudFront actualizada exitosamente.")  # Registra la acción
else:
    print(f'Failed to update distribution {distribution_id} cache behavior.')  # Imprime el fallo de la actualización
    logging.error("No se pudo actualizar la distribución de CloudFront.")  # Registra el error

# Gestión y monitorio de CloudFront
# Crear invalidación de caché
paths = ['/index.html', '/images/*'] # Las rutas que recibe la función para crear la invalidación
response = create_invalidation(distribution_id, paths) # Crea una invalidación de caché
if response:
    invalidation_id = response['Invalidation']['Id'] # Obtiene el id de la invalidación y la asigna a una variable
    logging.info(f"Se ha creado la invalidación con ID {invalidation_id}") # Registra la acción

# Configuración de las variables
end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(days=1)  # Último día
period = 3600  # 1 hora

# Obtener métricas
metrics = ['Requests', 'BytesDownloaded', 'BytesUploaded', 'TotalErrorRate'] 
for metric in metrics:
    response = get_cloudfront_metrics(distribution_id, metric, start_time, end_time, period)  # Obtiene las estadísticas para cada métrica
    if response:
        print(f"Métrica: {metric}")
        for datapoint in response['Datapoints']:
            timestamp = datapoint['Timestamp']
            sum_value = datapoint['Sum'] 
            average_value = datapoint['Average']
            print(f"Timestamp: {timestamp}, Sum: {sum_value}, Average: {average_value}") # Imprime los resultados
            logging.info(f"Se han obtenido las estadísticas para la metrica {metric}") # Registra la acción
    else:
        logging.error(f"No se pudieron obtener las estadísticas para la metrica {metric}") # Registra la acción
