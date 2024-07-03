import subprocess  # Importa el módulo subprocess para ejecutar comandos externos
import time  # Importa el módulo time para gestionar el tiempo
import os  # Importa el módulo os para interactuar con el sistema operativo

CONTAINER_NAME = "redis-cache-container"  # Nombre del contenedor Redis

def check_container_status():
    """
    Verifica el estado actual del contenedor Docker.

    Retorna
    ---
    Estado actual del contenedor (ej. 'running', 'exited').
    """
    result = subprocess.run(
        ["docker", "inspect", "-f", "{{.State.Status}}", CONTAINER_NAME],
        capture_output=True, text=True
    )
    return result.stdout.strip()  # Retorna el estado actual del contenedor

def get_container_stats():
    """
    Obtiene estadísticas del contenedor Docker.

    Retorna
    ---
    Diccionario con estadísticas de CPU, Memoria, Red I/O y Disco I/O del contenedor.
    None si no se pudieron obtener las estadísticas.
    """
    result = subprocess.run(
        ["docker", "stats", CONTAINER_NAME, "--no-stream", "--format", "{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        stats = result.stdout.strip().split('\t')
        return {
            "CPU": stats[0],
            "Memoria": stats[1],
            "Red I/O": stats[2],
            "Disco I/O": stats[3]
        }
    return None

def save_stats_to_file(stats):
    """
    Guarda las estadísticas del contenedor en un archivo de texto.

    Parámetros
    ---
    stats: Diccionario con las estadísticas del contenedor.
    """
    container_name_clean = CONTAINER_NAME.replace("/", "_").replace(":", "_")  # Limpiar el nombre para evitar problemas con el sistema de archivos
    file_name = f"{container_name_clean}_stats.txt"
    data_dir = os.path.join(os.path.dirname(__file__), 'data')  # Directorio 'data' dentro del directorio actual del script
    os.makedirs(data_dir, exist_ok=True)  # Crea el directorio 'data' si no existe
    file_path = os.path.join(data_dir, file_name)  # Ruta completa del archivo de estadísticas

    with open(file_path, 'a') as file:
        if stats:
            file.write("Estadísticas del Contenedor Redis:\n")
            file.write(f"  CPU: {stats['CPU']}\n")
            file.write(f"  Memoria: {stats['Memoria']}\n")
            file.write(f"  Red I/O: {stats['Red I/O']}\n")
            file.write(f"  Disco I/O: {stats['Disco I/O']}\n")
            file.write("\n")
        else:
            file.write("No se pudieron obtener las estadísticas del contenedor Redis.\n\n")

def monitor_and_save_stats():
    """
    Monitorea el estado del contenedor Redis y guarda las estadísticas en un archivo.
    """
    while True:
        status = check_container_status()  # Verifica el estado del contenedor

        if status == "running":
            stats = get_container_stats()  # Obtiene las estadísticas del contenedor
            save_stats_to_file(stats)  # Guarda las estadísticas en un archivo
            print("Guardando estadísticas...")  # Muestra un mensaje indicando que se están guardando las estadísticas
        else:
            print("El contenedor Redis no está en ejecución.")  # Informa que el contenedor no está en ejecución

        time.sleep(5)  # Espera 5 segundos antes de la siguiente verificación

if __name__ == "__main__":
    monitor_and_save_stats()
