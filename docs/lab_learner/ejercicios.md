<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicios desarrollados en AWS Lab Learner</h1>
</p>


## 4. Caché con Amazon CloudFront
•	Configuración de CloudFront para distribuir contenido estático y dinámico.
•	Integración de CloudFront con S3 y EC2 para mejorar la entrega de contenido.

### Integración de CloudFront con S3
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

## WAF: Web Application Firewall

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/e665d02c-48d6-43d6-ab36-5ebb48d2a8d0" width="800"></p>

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

### Integración de CloudFront con EC2
### 1. Crear instancia EC2 y conectarlo por SSH
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/c2b572b2-7068-40fb-b421-872579d91378" width="800">
</p>

### 2. Configurar la instancia EC2 como servidor web
**Grupo de seguridad**
Se debe configurar el grupo de seguridad de la instancia EC2
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/1036e804-ef09-4f31-a612-e15ae1161ad5" width="800">
</p>

**Servidor web**
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/c2b572b2-7068-40fb-b421-872579d91378" width="800"></p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/cbd7b4b2-8d0d-48c9-ac53-e4697f090ea2" width="800"></p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/ef73dcb7-a357-4269-a7f5-45716feb336e" width="800"></p>

Podemos acceder al servidor web con el Dominio de IPv4 público de la instancia EC2 

Accedemos a la carpeta en la que se almacenan los recursos que se mostrarán desde el servidor web
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/f06d65a1-c70c-49c4-a402-43370e18b6a7" width="800"></p>

Creamos una página HTML sencilla
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/1f4860df-220f-4456-8f93-da15c5acfcce" width="800"></p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/9188b92c-31d6-47e6-9e86-82270bf911ff" width="800"></p>

### 3. Creación de la distribución CloudFront
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/c62cac88-8728-4d4f-b3bf-5a1648aa1b87" width="800"></p>
<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/499fee74-3184-4f3d-b803-eccf5e116efd" width="800"></p>

Debido a la falta de permisos para la creación de una distribución de CloudFront del Lab Learner se optó por usar el laboratorio del módulo 5 y se uso como origin la instancia EC2 previamente creada con la cuenta de Lab Learner. El origin que se usa para crear una distribución de CloudFront no debe ser necesarimente un servicio de AWS y tampoco es requisito que se hayan creado con la misma cuenta.

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/2f49f372-be3e-44d1-9cfe-cddeda7b4d7f" width="800"></p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/c17c0ccd-ed9f-465f-87b2-78500b2d119a" width="800"></p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/9367e11c-f066-4b90-acfe-3e1ff48992e1" width="800"></p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/91a6e24e-26c1-4199-b6e1-0c552d76971a" width="800"></p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/7fa038bc-d1c2-482f-a893-5b62d540e6ed" width="800"></p>

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/d4db5635-efbb-4c05-8e0c-b64cda8d67a7" width="800"></p>

Si se quiere acceder al servidor web a través de HTTPS, el necesario contar con un certificado SSL. Podemos solicitarselo a Amazon

<p align= "center"><img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/fd77aa21-cca4-45f0-b811-929684514062" width="800"></p>

## 6. Implementación de CloudFront para caché y seguridad de aplicaciones
•	Configuración de CloudFront para la protección de aplicaciones mediante WAF (Web Application Firewall).
•	Experimentación con reglas de seguridad y políticas de caché.

- No se cuentan con los permisos para usar Web Application Firewall (WAF) ni en Lab Learner ni el laboratorio que se utilizó para crear la distribución de CloudFront
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/b6068f10-992a-40ff-9519-cf42d2c66f6e" width="800">
</p>



