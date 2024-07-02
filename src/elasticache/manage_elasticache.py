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
    filepath = os.path.join('data', filename)
    with open(filepath, 'r') as f:
        return f.read().strip()

def slow_database_get(key):
    """Simula una lectura lenta de base de datos."""
    time.sleep(0.1)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def slow_database_set(key, value):
    """Simula una escritura lenta en base de datos."""
    time.sleep(0.1)

def measure_performance(pattern_get, pattern_set, redis_client, num_operations=500, read_ratio=0.8):
    """Mide el rendimiento de un patrón de caché."""
    keys = [f"key-{i}" for i in range(num_operations)]
    values = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(num_operations)]

    start_time = timeit.default_timer()
    cache_hits = 0
    cache_misses = 0

    for i in range(num_operations):
        if random.random() < read_ratio:
            # Operación de lectura
            result = pattern_get(redis_client, random.choice(keys), slow_database_get)
            if result is not None:
                cache_hits += 1
            else:
                cache_misses += 1
        else:
            # Operación de escritura
            pattern_set(redis_client, keys[i], values[i], slow_database_set)

    elapsed = timeit.default_timer() - start_time
    ops_per_second = num_operations / elapsed
    hit_ratio = cache_hits / (cache_hits + cache_misses) if (cache_hits + cache_misses) > 0 else 0

    return {
        'elapsed_time': elapsed,
        'operations_per_second': ops_per_second,
        'hit_ratio': hit_ratio
    }

def save_results(filename, results):
    """Guarda los resultados en un archivo."""
    content = "\n".join([f"{name}:\n  Tiempo: {data['elapsed_time']:.2f} segundos\n  Operaciones/seg: {data['operations_per_second']:.2f}\n  Ratio de aciertos: {data['hit_ratio']:.2f}" for name, data in results.items()])
    filepath = os.path.join('data', filename)
    with open(filepath, 'w') as f:
        f.write(content)
    logging.info(f"Resultados guardados en '{filepath}'")

def main():
    cluster_id = input("ID del clúster: ")
    redis_endpoint = load_from_file(f'{cluster_id}_redis_endpoint.txt')
    
    try:
        redis_client = redis.StrictRedis(host=redis_endpoint, port=6379, decode_responses=True)
    except redis.ConnectionError as e:
        logging.error(f"Error al conectar con Redis: {e}")
        return

    patterns = {
        'Cache-Aside': (cache_aside_get, cache_aside_set),
        'Read-Through': (read_through_get, read_through_set),
        'Write-Through': (write_through_get, write_through_set)
    }

    results = {}
    for name, (pattern_get, pattern_set) in patterns.items():
        logging.info(f"Midiendo rendimiento para {name}...")
        performance = measure_performance(pattern_get, pattern_set, redis_client)
        results[name] = performance
        logging.info(f"Resultados para {name}: {performance}")

    # Cambiar el nombre del archivo para incluir el ID del clúster
    filename = f"{cluster_id}_cache_patterns_performance.txt"
    save_results(filename, results)

if __name__ == "__main__":
    main()