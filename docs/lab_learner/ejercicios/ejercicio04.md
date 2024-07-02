<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicio 4: Caché con Amazon CloudFront</h1>
</p>

## Objetivos
- Configuración de CloudFront para distribuir contenido estático y dinámico.
- Integración de CloudFront con S3 y EC2 para mejorar la entrega de contenido.

## Integración de CloudFront con S3
### 1. Crear bucket S3
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/af7fbaa2-8190-4649-ab19-da906e12a44a" width="800">
</p>

### 2. Crear distribución CloudFront (con Lab Learner)
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/63665336-f80a-41d7-8bdc-17a34a447db2" width="800">
</p>

- **Origin:** Son las ubicaciones desde las que CloudFront va a proveer la información
-	**Origin domain:** Es el nombre de dominio DNS del bucket S3. Si el bucket S3 esta configurado como sitio web estático, es recomendado usar el punto de enlace de sitio web.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/707d5644-7611-4dba-b6be-76c8d5717475" width="800">
</p>

**Protocol:** Se elige el protocolo que usará CloudFront al obtener los objetos desde el origen.
- **HTTP only:** Es la configuración por default y la única disponible cuando se trabaja con puntos de enlace a sitios web estáticos alojados en Amazon S3
-	HTTPS only
-	Match viewer:  Se adapta al protocolo usado por el cliente que visita la página
**Puerto 80:** el puerto estándar para conexiones HTTP
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/dea1f1e8-fc75-4d94-ad86-2cda0fb4e47e" width="800">
</p>

**Origin path:** Cuando el contenido está almacenado en un directorio en particular dentro del origen 
**Name:** Es el nombre con el que se va a identificar el origen en la distribución

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/5b478470-6a45-4ebd-a6cb-09f76ab5abfe" width="800">
</p>

- **Connection attempts:** El número de veces que CloudFront intenta conectarse al origen
- **Connection timeout:** El tiempo que CloudFront esperará por una respuesta del origen

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/991693e1-d1c6-4031-a9f5-953cbc5f9d6c" width="800">
</p>

- **Path pattern:** Indica a la solicitud de que ruta se aplicará el comportamiento de caché
- **Viewer protocol policy:** El protocolo que se desea usen los usuarios al acceder al contenido en las ubicaciones de borde de CloudFront 
- **HTTP Methods:**
  - GET=recupera un recurso
  - HEAD=cabecera de un objeto
  - OPTIONS: Lista las opciones que admite el servidor de origen
  - PUT= Reemplaza un recurso
  - DELETE=Borrar objetos
  - POST=envía datos, crear recursos
  - PATCH= modificaciones parciales a un recurso

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/81a3bdad-cdb3-4c42-aff7-823d1415f587" width="800"></p>
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/055b2527-65f2-4e16-b738-ea2374507453" width="800"></p>
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/e3f7664d-6317-4d99-875b-fe81c3a3e1d7" width="800"></p>

Nota: No se cuenta con los permisos para crear una política de caché
