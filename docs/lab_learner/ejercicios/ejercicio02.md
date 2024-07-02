<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicio 2: Caché con Amazon ElastiCache</h1>
</p>

## Objetivos
- Configuración de un entorno ElastiCache utilizando Redis y Memcached.<br>- Redis: Tablas hash.<br>- Memcached: clave-valor no relacional.
- Prácticas de implementación y optimización de caché para aplicaciones de datos.

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

