import logging

def cache_aside_get(redis_client, key, slow_database_get):
    """
    Implementa el patrón Cache-Aside para operaciones de lectura.
    
    1. Intenta obtener el valor de la caché.
    2. Si no está en la caché, lo obtiene de la base de datos y lo guarda en la caché.
    """
    try:
        value = redis_client.get(key)
        if value is None:
            logging.info(f"Cache miss para {key}")
            value = slow_database_get(key)
            redis_client.set(key, value, ex=3600)  # Expira en 1 hora
        else:
            logging.info(f"Cache hit para {key}")
        return value
    except Exception as e:
        logging.error(f"Error en cache_aside_get: {e}")
        return slow_database_get(key)

def cache_aside_set(redis_client, key, value, slow_database_set):
    """
    Implementa el patrón Cache-Aside para operaciones de escritura.
    
    1. Escribe el valor en la base de datos.
    2. Actualiza o invalida la entrada en la caché.
    """
    try:
        slow_database_set(key, value)
        redis_client.set(key, value, ex=3600)  # Expira en 1 hora
        logging.info(f"Valor actualizado en caché y base de datos para {key}")
    except Exception as e:
        logging.error(f"Error en cache_aside_set: {e}")
        redis_client.delete(key)  # Invalida la entrada en caso de error