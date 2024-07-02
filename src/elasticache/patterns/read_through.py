import logging

def read_through_get(redis_client, key, slow_database_get):
    """
    Implementa el patrón Read-Through para operaciones de lectura.
    
    En este patrón, la caché es responsable de cargar los datos faltantes
    desde la base de datos.
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
        logging.error(f"Error en read_through_get: {e}")
        return slow_database_get(key)

def read_through_set(redis_client, key, value, slow_database_set):
    """
    Implementa el patrón Read-Through para operaciones de escritura.
    
    En Read-Through, las escrituras se manejan de manera similar a Cache-Aside.
    """
    try:
        slow_database_set(key, value)
        redis_client.set(key, value, ex=3600)  # Expira en 1 hora
        logging.info(f"Valor actualizado en caché y base de datos para {key}")
    except Exception as e:
        logging.error(f"Error en read_through_set: {e}")
        redis_client.delete(key)  # Invalida la entrada en caso de error