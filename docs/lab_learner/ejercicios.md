## 4. Caché con Amazon CloudFront
•	Configuración de CloudFront para distribuir contenido estático y dinámico.
•	Integración de CloudFront con S3 y EC2 para mejorar la entrega de contenido.

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

## WAF

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/e665d02c-48d6-43d6-ab36-5ebb48d2a8d0" width="800">
</p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/ee11fb38-e1b8-49bc-a6bd-01e592c93dd0" width="800"></p>
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/ba37cfa7-53f4-47ec-81b7-8bc40680c270" width="800"></p>

- Faltan los permisos necesarios para Crear una Distribución de Amazon CloudFront desde el Lab Learner
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/6a1fc6c5-7d01-4c3e-a14a-b0d0d01a6ff0" width="800">
</p>

- Falta de permisos para crear un rol con permisos para crear una Distribución de Amazon CloudFront
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/e5f9a11a-0c6c-4150-8675-c5ade2b1cacd" width="800">
</p>

### 3. Crear distribución CloudFront (desde el laboratorio del semestre 2)
Debido a la falta de permisos para crear la distribución en Amazon CloudFront, se utilizó el laboratorio del módulo 5 del curso AWS Academy Introduction to Cloud: Semester 2
A continución se muestran las principales diferencias:
- Primero se tuvo que crear un nuevo bucket en S3

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/231d2581-a61c-4d88-86dc-876460ebfe39" width="800">
</p>

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/76b546f1-640c-4730-9454-24fea62265c8" width="800">
</p>

- Creación exitosa de la distribución de CloudFront
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/23b87feb-2453-45f4-8db0-018cf63c6016" width="800"></p>
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/739e1c53-dd14-4713-9c80-7b15067d5752" width="800"></p>

- Probar la distribución de AmazonCloudFront para un sitio web estático almacenado en un bucket de Amazon S3
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/8e113f0a-21a0-4289-904c-b386dbd5df23" width="800">
</p>


- No se cuentan con los permisos para usar Web Application Firewall (WAF) ni en Lab Learner ni el laboratorio que se utilizó para crear la distribución de CloudFront
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/b6068f10-992a-40ff-9519-cf42d2c66f6e" width="800">
</p>





