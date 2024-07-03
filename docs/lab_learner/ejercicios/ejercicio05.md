<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicio 5: Estrategias de Caché</h1>
</p>
<p align="justify">En esta parte, nos enfocamos en desarrollar estrategias efectivas de caché para diferentes escenarios de aplicación. Utilizamos AWS Lab Learner para simular cargas y realizar pruebas de rendimiento, lo que nos permitió evaluar y refinar nuestras estrategias.</p>

### 1. Selección de estrategias de caché
<p align="justify">Basándonos en nuestro análisis, seleccionamos estrategias de caché apropiadas para diferentes tipos de datos:</p>

- **Datos de lectura frecuente y escritura poco frecuente:** Implementamos una estrategia de caché con un tiempo de expiración largo.
- **Datos que cambian con frecuencia:** Utilizamos tiempos de expiración más cortos o implementamos un mecanismo de invalidación de caché basado en eventos.
- **Datos críticos en tiempo real:** Consideramos el uso de una estrategia Write-Through para mantener la consistencia.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/dee72c09-f7cd-43cb-ae1a-7ff2446c887a" width="400">
</p>

### 2. Optimización de la configuración de ElastiCache
<p align="justify">Ajustamos la configuración de ElastiCache basándonos en nuestras pruebas de rendimiento:</p>

- Selección del tipo de instancia adecuado según la carga de trabajo.
- Configuración de la replicación para mejorar la disponibilidad y el rendimiento de lectura.
- Ajuste de políticas de evicción y tamaño de la caché para optimizar el uso de la memoria.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/40a97b3f-02bc-4064-b6b2-49e90d0d463f" width="800">
</p>

### 3. Implementación de estrategias de precarga y actualización de caché
- Desarrollamos scripts para precargar datos frecuentemente accedidos en la caché durante períodos de baja actividad.
- Implementamos un sistema de actualización de caché  para mantener la coherencia de los datos.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/f5a54ea1-ac96-4179-b4df-816b4b5327a6" width="700">
</p>

### 4. Monitoreo y ajuste continuo
- Pensamos en configurar alarmas en CloudWatch para monitorear métricas clave como la tasa de aciertos de caché, la latencia y el uso de memoria.
- Establecimos un proceso de revisión y ajuste periódico de nuestras estrategias de caché basado en los datos de rendimiento recopilados.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/1b8fc8a7-cb5a-44d8-bd8d-35d991b11250" width="700">
</p>

### 5. Optimización para diferentes tipos de contenido
Desarrollamos estrategias específicas para diferentes tipos de contenido:
- **Contenido estático:** Uso intensivo de CloudFront con tiempos de expiración largos.
- **Contenido dinámico pero poco cambiante:** Caché en ElastiCache con invalidación basada en eventos.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/d2470bef-312c-46b9-bd34-fcc884824738" width="700">
</p>

A través de estas estrategias y pruebas exhaustivas, logramos mejorar significativamente el rendimiento y la escalabilidad de nuestra aplicación, reduciendo la carga en la base de datos y mejorando los tiempos de respuesta para los usuarios finales.
