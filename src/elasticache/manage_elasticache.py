import redis
import os
import random
import string
import timeit
import time
import logging
from patterns.cache_aside import cache_aside_get, cache_aside_set
from patterns.read_through import read_through_get, read_through_set
from patterns.write_through import write_through_get, write_through_set

# Configurar logging para registrar eventos importantes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def load_from_file(filename):
    """Carga el contenido de un archivo desde el directorio 'data'."""
    filepath = os.path.join('data', filename)  # Obtiene la ruta completa del archivo en el directorio 'data'
    with open(filepath, 'r') as f:  # Abre el archivo en modo lectura
        return f.read().strip()  # Lee el contenido del archivo y elimina espacios en blanco al inicio y final

def slow_database_get(key):
    """Simula una lectura lenta de base de datos."""
    time.sleep(0.1)  # Simula una operación de lectura lenta
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))  # Genera un valor aleatorio

def slow_database_set(key, value):
    """Simula una escritura lenta en base de datos."""
    time.sleep(0.1)  # Simula una operación de escritura lenta

def measure_performance(pattern_get, pattern_set, redis_client, num_operations=500, read_ratio=0.8):
    """Mide el rendimiento de un patrón de caché."""
    keys = [f"key-{i}" for i in range(num_operations)]  # Genera claves para operaciones
    values = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(num_operations)]  # Genera valores aleatorios para operaciones

    start_time = timeit.default_timer()  # Inicia el contador de tiempo
    cache_hits = 0  # Contador de aciertos en caché
    cache_misses = 0  # Contador de fallos en caché

    for i in range(num_operations):
        if random.random() < read_ratio:
            # Operación de lectura
            result = pattern_get(redis_client, random.choice(keys), slow_database_get)  # Realiza una operación de lectura usando el patrón de caché
            if result is not None:
                cache_hits += 1  # Incrementa el contador si la operación fue un acierto en caché
            else:
                cache_misses += 1  # Incrementa el contador si la operación fue un fallo en caché
        else:
            # Operación de escritura
            pattern_set(redis_client, keys[i], values[i], slow_database_set)  # Realiza una operación de escritura usando el patrón de caché

    elapsed = timeit.default_timer() - start_time  # Calcula el tiempo transcurrido
    ops_per_second = num_operations / elapsed  # Calcula operaciones por segundo
    hit_ratio = cache_hits / (cache_hits + cache_misses) if (cache_hits + cache_misses) > 0 else 0  # Calcula el ratio de aciertos en caché

    return {
        'elapsed_time': elapsed,
        'operations_per_second': ops_per_second,
        'hit_ratio': hit_ratio
    }

def save_results(filename, results):
    """Guarda los resultados en un archivo."""
    content = "\n".join([f"{name}:\n  Tiempo: {data['elapsed_time']:.2f} segundos\n  Operaciones/seg: {data['operations_per_second']:.2f}\n  Ratio de aciertos: {data['hit_ratio']:.2f}" for name, data in results.items()])
    filepath = os.path.join('data', filename)  # Obtiene la ruta completa del archivo en el directorio 'data'
    with open(filepath, 'w') as f:  # Abre el archivo en modo escritura
        f.write(content)  # Escribe el contenido en el archivo
    logging.info(f"Resultados guardados en '{filepath}'")  # Registra un evento de guardado exitoso

def main():
    cluster_id = input("ID del clúster: ")  # Solicita al usuario el ID del clúster
    redis_endpoint = load_from_file(f'{cluster_id}_redis_endpoint.txt')  # Carga el endpoint de Redis desde un archivo

    try:
        redis_client = redis.StrictRedis(host=redis_endpoint, port=6379, decode_responses=True)  # Crea un cliente Redis
    except redis.ConnectionError as e:
        logging.error(f"Error al conectar con Redis: {e}")  # Registra un error si no se puede conectar con Redis
        return

    patterns = {
        'Cache-Aside': (cache_aside_get, cache_aside_set),
        'Read-Through': (read_through_get, read_through_set),
        'Write-Through': (write_through_get, write_through_set)
    }

    results = {}
    for name, (pattern_get, pattern_set) in patterns.items():
        logging.info(f"Midiendo rendimiento para {name}...")  # Registra un evento de inicio de medición
        performance = measure_performance(pattern_get, pattern_set, redis_client)  # Mide el rendimiento usando el patrón de caché
        results[name] = performance  # Guarda los resultados
        logging.info(f"Resultados para {name}: {performance}")  # Registra los resultados obtenidos

    # Cambiar el nombre del archivo para incluir el ID del clúster
    filename = f"{cluster_id}_cache_patterns_performance.txt"
    save_results(filename, results)  # Guarda los resultados en un archivo

if __name__ == "__main__":
    main()
