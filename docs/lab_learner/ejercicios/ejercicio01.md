<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicio 1: Introducción al caché</h1>
</p>

## Concepto de caché
<p align="justify">En informática, una caché es una capa de almacenamiento de datos de alta velocidad que almacena un subconjunto de datos, normalmente transitorios, de modo que las solicitudes futuras de esos datos se entregan mucho más rápido sin tener que consultar a la fuente original de datos. En aplicaciones web, la caché se sitúa estratégicamente en el flujo de datos entre el cliente (solicitante de datos) y el servidor web (origen de los datos).</p>
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/38b46004-eb53-4772-8e9c-6339f937d2cf" width="520">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/5b1ecfa6-8bef-4eb5-b08e-6024d289e86e" width="451">
</div>

## Almacenamiento de datos en caché
<p align="justify">El almacenamiento de datos en caché permite reutilizar de forma eficaz los datos recuperados o calculados anteriormente. Los datos en una memoria caché suelen almacenarse en hardware de acceso rápido, como la memoria de acceso aleatorio (RAM).</p>
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/a25714df-111e-4c46-9698-8432d3b075a1" width="500">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/1dbf480c-d4b7-40ea-a008-7564c877d2c4" width="500">
</div>

## Importancia de la caché en el rendimiento de las aplicaciones
<p align="justify">La memoria caché es crucial para el rendimiento de las aplicaciones y sistemas informáticos debido a varias razones:</p>

- La caché optimiza el acceso a datos frecuentemente solicitados, reduciendo tiempos de respuesta.
- Mejora la experiencia del usuario al acelerar tiempos de carga y navegación.
- Alivia la carga en los servidores al minimizar consultas repetitivas a fuentes de datos originales.
- Reduce el consumo de ancho de banda al mantener datos cercanos al usuario, mejorando la eficiencia global de las aplicaciones.

## Tipos de caché y casos de uso
### Almacenamiento en caché de CPU
- Almacenar instrucciones y datos frecuentemente utilizados.
- Reducir la latencia de acceso a memoria principal.
- Mejorar el rendimiento en cálculos intensivos y procesamiento de datos.
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/f828be53-d5fc-4036-8c17-a4e802385a86" width="490">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/23452963-6e20-43f8-9d93-5fbb7217d722" width="510">
</div>

### Almacenamiento en caché de disco
- Acelerar el acceso a archivos frecuentemente utilizados.
- Mejorar el rendimiento de sistemas de archivos.
- Optimizar operaciones de lectura/escritura en discos duros o SSD.
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/c5f35726-439b-41ca-a66d-165ccf3451c0" width="565">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/81741eae-cb24-4b2a-b4f2-9d303405a2da" width="435">
</div>

### Almacenamiento en caché de CDN
- Distribuir contenido estático (imágenes, CSS, JavaScript) globalmente.
- Reducir la latencia para usuarios geográficamente distantes.
- Aliviar la carga del servidor de origen.
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/843a596d-0d76-414d-b7eb-68a7e71994f7" width="484">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/328eb46f-6ab4-4ae4-8c71-5475bec2fa26" width="516">
</div>

### Almacenamiento en caché de DNS
- Reducir el tiempo de resolución de nombres de dominio.
- Disminuir el tráfico hacia servidores DNS autoritativos.
- Mejorar la velocidad de carga de páginas web.
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/3776f9b2-9534-4703-a28c-7f1465a291b2" width="605">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/6af2e6a1-8e36-464a-8267-50bc9fdc804a" width="395">
</div>

### Almacenamiento en caché web
- Almacenar páginas HTML generadas dinámicamente.
- Reducir la carga del servidor web.
- Mejorar los tiempos de respuesta para contenido frecuentemente solicitado.
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/e0dc6b21-8b3d-420c-b16b-853dde6af9e3" width="394">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/43ee9169-45d9-4a37-9986-cf2dc31b4553" width="606">
</div>

### Almacenamiento en caché de bases de datos
- Almacenar resultados de consultas frecuentes.
- Reducir la carga en el servidor de base de datos.
- Mejorar el rendimiento de aplicaciones con uso intensivo de datos.
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/4313c09a-49a6-40b3-b7d9-8617822cd3e4" width="594">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/a14f7793-fea6-43ff-b4a5-e45d0f5f5eae" width="406">
</div>
