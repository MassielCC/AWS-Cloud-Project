import subprocess  # Importa el módulo subprocess para ejecutar comandos externos
import time  # Importa el módulo time para gestionar el tiempo de espera

def check_container_status():
    """
    Verifica el estado actual del contenedor Docker 'redis-cache-container'.

    Retorna
    ---
    Estado actual del contenedor (por ejemplo, 'running', 'exited', etc.).
    """
    result = subprocess.run(
        ["docker", "inspect", "-f", "{{.State.Status}}", "redis-cache-container"],
        capture_output=True, text=True
    )
    return result.stdout.strip()  # Retorna el estado del contenedor como una cadena sin espacios adicionales

def get_container_stats():
    """
    Obtiene estadísticas del contenedor Docker 'redis-cache-container'.

    Retorna
    ---
    Un diccionario con las siguientes estadísticas:
    {
        "CPU": porcentaje de uso de CPU,
        "Memoria": uso de memoria,
        "Red I/O": operaciones de red,
        "Disco I/O": operaciones de disco
    }
    Retorna None si no se pueden obtener las estadísticas.
    """
    result = subprocess.run(
        ["docker", "stats", "redis-cache-container", "--no-stream", "--format", "{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        stats = result.stdout.strip().split('\t')
        return {
            "CPU": stats[0],        # Devuelve el porcentaje de uso de CPU
            "Memoria": stats[1],    # Devuelve el uso de memoria
            "Red I/O": stats[2],    # Devuelve las operaciones de red
            "Disco I/O": stats[3]   # Devuelve las operaciones de disco
        }
    return None  # Retorna None si no se pudieron obtener las estadísticas

def monitor_cache():
    """
    Monitorea el estado y las estadísticas del contenedor Docker 'redis-cache-container'.

    Esta función imprime el estado del contenedor y, si está en ejecución, muestra las estadísticas
    de uso de CPU, memoria, red y disco cada 5 segundos.
    """
    print("Iniciando monitoreo del contenedor redis-cache-container...")
    while True:
        status = check_container_status()  # Obtiene el estado actual del contenedor
        print(f"\nEstado del contenedor: {status}")  # Imprime el estado actual del contenedor

        if status == "running":
            stats = get_container_stats()  # Obtiene las estadísticas del contenedor si está en ejecución
            if stats:
                print("Estadísticas del contenedor:")
                for key, value in stats.items():
                    print(f"  {key}: {value}")  # Imprime cada estadística del contenedor
            else:
                print("No se pudieron obtener las estadísticas del contenedor.")
        else:
            print("El contenedor no está en ejecución.")

        time.sleep(5)  # Espera 5 segundos antes de la siguiente verificación

if __name__ == "__main__":
    monitor_cache()
