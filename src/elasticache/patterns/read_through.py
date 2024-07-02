import logging  # Importa el módulo de logging para registrar eventos

def read_through_get(redis_client, key, slow_database_get):
    """
    Implementa el patrón Read-Through para operaciones de lectura.
    
    En este patrón, la caché es responsable de cargar los datos faltantes
    desde la base de datos.

    Parámetros
    ---
    redis_client: Cliente Redis para operaciones de caché.
    key: Clave para la operación de lectura.
    slow_database_get: Función que simula una lectura lenta desde la base de datos.

    Retorna
    ---
    Valor obtenido, ya sea desde la caché o desde la base de datos.
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
        logging.error(f"Error en read_through_get: {e}")  # Registra un error si ocurre alguna excepción
        return slow_database_get(key)  # Retorna el valor obtenido directamente de la base de datos en caso de error

def read_through_set(redis_client, key, value, slow_database_set):
    """
    Implementa el patrón Read-Through para operaciones de escritura.
    
    En Read-Through, las escrituras se manejan de manera similar a Cache-Aside.

    Parámetros
    ---
    redis_client: Cliente Redis para operaciones de caché.
    key: Clave para la operación de escritura.
    value: Valor a escribir en la base de datos y en la caché.
    slow_database_set: Función que simula una escritura lenta en la base de datos.

    Retorna
    ---
    No retorna ningún valor explícito.
    """
    try:
        slow_database_set(key, value)  # Escribe el valor en la base de datos de manera lenta
        redis_client.set(key, value, ex=3600)  # Actualiza el valor en la caché con expiración de 1 hora
        logging.info(f"Valor actualizado en caché y base de datos para {key}")  # Registra el evento de actualización exitosa
    except Exception as e:
        logging.error(f"Error en read_through_set: {e}")  # Registra un error si ocurre alguna excepción
        redis_client.delete(key)  # Invalida la entrada en la caché en caso de error
