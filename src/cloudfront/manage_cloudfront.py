import boto3  # Importa el módulo boto3 para interactuar con los servicios de AWS
import time  # Importa el módulo time para manejar funciones de tiempo
import logging  # Importa el módulo de logging para registrar eventos

# Crear invalidación de caché
def create_invalidation(distribution_id, paths):
    """
    Crea una invalidación de caché para una distribución CloudFront

    Parámetros
    ---
    distribution_id: Id de la distribución CloudFront
    paths: rutas de los objetos a invalidar
    """
    client = boto3.client('cloudfront') # Crea un cliente de CloudFront
    try:
        response = client.create_invalidation(
            DistributionId=distribution_id, # Id de la distribución
            InvalidationBatch={
                'Paths': {
                    'Quantity': len(paths),  # Nro de rutas de invalidación
                    'Items': paths # Lista de las rutas que se invalidarán
                },
                'CallerReference': str(time.time()) # Referencia única para la solicitud
            }
        )
        return response
    except client.exceptions.NoSuchDistribution as e:
        logging.error(f"La distribución {distribution_id} de CloudFront no existe.") # Registra el error
        return None

# Obtener métricas de CloudFront desde CloudWatch
def get_cloudfront_metrics(distribution_id, metric_name, start_time, end_time, period):
    cloudwatch = boto3.client('cloudwatch') # Crea un cliente de Cloudwatch
    try:
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/CloudFront', 
            MetricName=metric_name, # Metrica de la que se obtendrá las estadísticas
            Dimensions=[
                {
                    'Name': 'DistributionId', 
                    'Value': distribution_id
                },
                {
                    'Name': 'Region',
                    'Value': 'Global'
                }
            ],
            StartTime=start_time, 
            EndTime=end_time,
            Period=period,
            Statistics=['Sum', 'Average'] # Estadísticas diferentes al percentil
        )
        logging.info(f"Obteniendo las métricas de la distribución {distribution_id}") # Registra la acción
        return response
    except Exception as e:
        logging.error(f"Error obteniendo métricas: {e}") # Registra el error
        return None
