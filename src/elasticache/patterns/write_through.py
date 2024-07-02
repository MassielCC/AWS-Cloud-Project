import logging  # Importa el módulo de logging para registrar eventos

def write_through_get(redis_client, key, slow_database_get):
    """
    Implementa el patrón Write-Through para operaciones de lectura.
    
    En Write-Through, las lecturas son similares a Cache-Aside y Read-Through.
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
        logging.error(f"Error en write_through_get: {e}")  # Registra un error si ocurre alguna excepción
        return slow_database_get(key)  # Retorna el valor obtenido directamente de la base de datos en caso de error

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
        redis_client.set(key, value, ex=3600)  # Actualiza el valor en la caché con expiración de 1 hora
        
        logging.info(f"Valor actualizado en base de datos y caché para {key}")  # Registra el evento de actualización exitosa
    except Exception as e:
        logging.error(f"Error en write_through_set: {e}")  # Registra un error si ocurre alguna excepción
        redis_client.delete(key)  # Invalida la entrada en la caché en caso de error
