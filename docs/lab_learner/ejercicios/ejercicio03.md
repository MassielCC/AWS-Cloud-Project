<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicio 3: Caché de datos de aplicación con ElastiCache</h1>
</p>

<p align="justify">En esta parte del proyecto, implementamos patrones de caché en aplicaciones simuladas utilizando Amazon ElastiCache. Utilizamos AWS LabLearner para experimentar con diferentes configuraciones de caché y analizar su impacto en el rendimiento de nuestras aplicaciones.</p>

<p align="justify">Primero, nos familiarizamos con tres patrones de caché fundamentales:</p>

<p align="justify"><strong>1. Cache-Aside:</strong> En este patrón, nuestra aplicación es responsable de leer y escribir desde/hacia la caché. Cuando necesitamos leer datos, primero verificamos si están en la caché. Si no están, los recuperamos de la base de datos y los almacenamos en la caché para futuras consultas. Para las operaciones de escritura, actualizamos primero la base de datos y luego invalidamos o actualizamos la entrada en la caché.</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/4078dda7-9e0b-43d8-9df8-fae5d6140aef" width="900">
</p>

<p align="justify"><strong>2. Read-Through:</strong> Este patrón es similar al Cache-Aside, pero la responsabilidad de cargar los datos faltantes en la caché recae en la propia capa de caché, no en la aplicación. Cuando solicitamos datos que no están en la caché, esta se encarga automáticamente de obtenerlos de la base de datos y almacenarlos.</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/f2b173e3-f115-4922-b5be-22f1d96195fc" width="900">
</p>

<p align="justify"><strong>3. Write-Through:</strong> En este patrón, cada operación de escritura se realiza tanto en la caché como en la base de datos. Primero escribimos en la base de datos y luego actualizamos la caché. Esto garantiza que la caché siempre esté sincronizada con la base de datos, pero puede aumentar la latencia de las operaciones de escritura.</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/667f7638-eba7-45f0-b3b9-95777ae20e46" width="900">
</p>

<p align="justify">Utilizando AWS LabLearner, configuramos un entorno de ElastiCache con Redis y realizamos pruebas con cada uno de estos patrones. Observamos cómo cada patrón afecta el rendimiento de nuestra aplicación en diferentes escenarios:</p>

- Para aplicaciones con alta frecuencia de lectura y baja frecuencia de escritura, el patrón Cache-Aside resultó ser muy eficiente.
- En situaciones donde necesitábamos una capa de abstracción adicional entre nuestra aplicación y la base de datos, el patrón Read-Through demostró ser útil.
- Para aplicaciones que requieren consistencia inmediata entre la caché y la base de datos, el patrón Write-Through fue la mejor opción, aunque notamos un ligero aumento en la latencia de escritura.

<p align="justify">Para demostrar la implementación práctica de estos patrones y cómo afectan el rendimiento, más adelante realizaremos un ejercicio de código utilizando boto3 para interactuar con los servicios de AWS y la biblioteca redis para manejar las operaciones de caché. Este ejercicio nos permitirá experimentar directamente con diferentes configuraciones y observar su impacto en el rendimiento de nuestra aplicación simulada.</p>
