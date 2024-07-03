import subprocess  # Importa el módulo subprocess para ejecutar comandos externos
import os  # Importa el módulo os para interactuar con el sistema operativo

def check_existing_container():
    """
    Verifica si existe un contenedor Docker con el nombre 'redis-cache-container'.

    Retorna
    ---
    ID del contenedor si existe, o cadena vacía si no hay contenedor.
    """
    result = subprocess.run(["docker", "ps", "-a", "--filter", "name=redis-cache-container", "--format", "{{.ID}}"], capture_output=True, text=True)
    return result.stdout.strip()  # Retorna el ID del contenedor si existe, o cadena vacía si no hay contenedor

def remove_container(container_id):
    """
    Elimina un contenedor Docker dado su ID.

    Parámetros
    ---
    container_id: ID del contenedor Docker a eliminar.
    """
    subprocess.run(["docker", "rm", "-f", container_id], capture_output=True)  # Ejecuta el comando para eliminar el contenedor

def deploy_cache():
    """
    Despliega un contenedor Docker para Redis.

    Esta función cambia al directorio 'Docker', verifica la existencia del Dockerfile,
    verifica la existencia de un contenedor previo con nombre 'redis-cache-container',
    y luego procede a construir la imagen Docker 'redis-cache' y ejecutar el contenedor
    'redis-cache-container'.
    """
    # Cambiar al directorio Docker
    os.chdir('Docker')

    # Verificar si el Dockerfile existe
    if not os.path.exists('Dockerfile'):
        print("Error: Dockerfile no encontrado en el directorio Docker.")
        return

    # Verificar si existe un contenedor previo
    existing_container = check_existing_container()
    if existing_container:
        response = input("Existe un contenedor previo. ¿Desea eliminarlo? (s/n): ").lower()
        if response == 's':
            remove_container(existing_container)
            print("Contenedor previo eliminado.")
        else:
            print("Operación cancelada. El contenedor existente no fue eliminado.")
            return

    # Construir la imagen Docker
    build_result = subprocess.run(["docker", "build", "-t", "redis-cache", "."], capture_output=True, text=True)
    if build_result.returncode != 0:
        print("Error al construir la imagen Docker:")
        print(build_result.stderr)
        return

    print("Imagen Docker construida exitosamente.")

    # Ejecutar el contenedor
    run_result = subprocess.run([
        "docker", "run", 
        "-d",  # Modo detached
        "--name", "redis-cache-container",
        "-p", "6379:6379",  # Mapear puerto
        "redis-cache"
    ], capture_output=True, text=True)

    if run_result.returncode != 0:
        print("Error al ejecutar el contenedor:")
        print(run_result.stderr)
    else:
        print("Contenedor de Redis desplegado exitosamente.")
        print(f"ID del contenedor: {run_result.stdout.strip()}")

if __name__ == "__main__":
    deploy_cache()
