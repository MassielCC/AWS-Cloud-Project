![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/ef051abc-e3e5-464d-a273-867cf0ff80c4)<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicios desarrollados en AWS Lab Learner</h1>
</p>

## 2. Caché con Amazon ElastiCache
•	Configuración de un entorno ElastiCache utilizando Redis y Memcached.
  o	Redis: Tablas hash.
  o	Memcached: clave-valor no relacional.
•	Prácticas de implementación y optimización de caché para aplicaciones de datos.

### Configuración de ElastiCache utilizando Redis

### Configuración de ElastiCache utilizando Memcached
### 1.	Configurar instancia EC2**
Requisitos: Deben tener el mismo VPC y grupo de seguridad. Amazon ElastiCache crea el caché en el VPC por default y usa el grupo de seguridad por default.
  
![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/c2d393cc-6bd3-446a-a5dd-847e297899e8)

Conectar la instancia EC2 con SSH
`ssh -i “ubicación de la llave privada de la instancia EC2” <dirección IP pública de la instancia>`
![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/d9816914-16ac-4894-9f32-d4cc4c51c912)

**SSH= Secure Shell**
Protocolo de red que nos permite conectarnos a la instancia EC2 de forma segura. Provee comunicación encriptada entre la computadora y la instancia EC2. 

La clave privada asociada a la instancia EC2 solo se puede descargar durante el lanzamiento inicial, está se debe almacenar en un lugar seguro. Para asegurar el éxito de la conexión también es importante configurar el grupo de seguridad de la instancia de forma que permita tráfico desde el puerto 22; que es el puerto utilizado por SSH.

### 2.	ElastiCache con Memcached**
![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/d4a4b831-663d-4aa4-95ea-0b95b045241c)

![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/44a62595-1511-490c-bfa1-ee08ae4e1914)

![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/90bc5e07-45fe-4f0e-92c6-1c78542f4bec)

![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/a9e5a474-c885-4af9-9e6f-13523115af47)

**Puerto 11211:** Puerto estándar utilizado por Memcached. La configuración de seguridad debe permitir la conexión desde este puerto.

![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/fb491a31-8af4-49cf-aa16-112483d30de3)

![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/77b5ed01-8ec4-43b2-a142-d92f87adca63)

![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/04edf6d8-edbc-4de1-a5e0-48c6d3119ade)

![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/47afb456-e5ef-45f1-8ec1-104c586e2e94)

Grupo de seguridad
![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/a92be97d-9e8b-455c-915d-51e9fabbf203)

### 3. Conectar instancia EC2 con el clúster de Memcached
Instalamos memcached desde Cloud9 debido a dificultades de configuración desde Windows
![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/2c882e0a-e1e1-4cef-bf03-9961ffada58e)

**Cloud9**
Es un entorno de desarrollo integrado (IDE) de Amazon que se crea como una instancia de Amazon EC2
-	Evita la necesidad de configurar un entorno de desarrollo local, se usó como solución al problema de conexión con instancias EC2 de manera local desde Windows 
-	Facilita el acceso a los recursos de AWS

![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/36a74af9-e83a-4a4a-9827-4ebca261896d)

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



