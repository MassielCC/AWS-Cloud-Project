import logging  # Importa el módulo de logging para registrar eventos

def cache_aside_get(redis_client, key, slow_database_get):
    """
    Implementa el patrón Cache-Aside para operaciones de lectura.
    
    1. Intenta obtener el valor de la caché.
    2. Si no está en la caché, lo obtiene de la base de datos y lo guarda en la caché.
    """
    try:
        value = redis_client.get(key)  # Intenta obtener el valor desde la caché
        if value is None:
            logging.info(f"Cache miss para {key}")  # Registra un cache miss si el valor no está en la caché
            value = slow_database_get(key)  # Obtiene el valor de la base de datos
            redis_client.set(key, value, ex=3600)  # Guarda el valor en la caché con expiración de 1 hora
        else:
            logging.info(f"Cache hit para {key}")  # Registra un cache hit si el valor está en la caché
        return value  # Retorna el valor obtenido (ya sea de la caché o de la base de datos)
    except Exception as e:
        logging.error(f"Error en cache_aside_get: {e}")  # Registra un error si ocurre alguna excepción
        return slow_database_get(key)  # Retorna el valor obtenido directamente de la base de datos en caso de error

def cache_aside_set(redis_client, key, value, slow_database_set):
    """
    Implementa el patrón Cache-Aside para operaciones de escritura.
    
    1. Escribe el valor en la base de datos.
    2. Actualiza o invalida la entrada en la caché.
    """
    try:
        slow_database_set(key, value)  # Escribe el valor en la base de datos de manera lenta
        redis_client.set(key, value, ex=3600)  # Actualiza el valor en la caché con expiración de 1 hora
        logging.info(f"Valor actualizado en caché y base de datos para {key}")  # Registra el evento de actualización exitosa
    except Exception as e:
        logging.error(f"Error en cache_aside_set: {e}")  # Registra un error si ocurre alguna excepción
        redis_client.delete(key)  # Invalida la entrada en la caché en caso de error
