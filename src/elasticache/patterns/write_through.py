import logging

def write_through_get(redis_client, key, slow_database_get):
    """
    Implementa el patrón Write-Through para operaciones de lectura.
    
    En Write-Through, las lecturas son similares a Cache-Aside y Read-Through.
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
        logging.error(f"Error en write_through_get: {e}")
        return slow_database_get(key)

def write_through_set(redis_client, key, value, slow_database_set):
    """
    Implementa el patrón Write-Through para operaciones de escritura.
    
    En Write-Through, las escrituras se realizan primero en la base de datos
    y luego se actualiza la caché.
    """
    try:
        # Primero, escribir en la base de datos
        slow_database_set(key, value)
        
        # Luego, actualizar la caché
        redis_client.set(key, value, ex=3600)  # Expira en 1 hora
        
        logging.info(f"Valor actualizado en base de datos y caché para {key}")
    except Exception as e:
        logging.error(f"Error en write_through_set: {e}")
        # En caso de error, asegurarse de que la caché y la base de datos estén sincronizadas
        redis_client.delete(key)