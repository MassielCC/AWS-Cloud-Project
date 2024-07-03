<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicio 5: Estrategias de Caché</h1>
</p>
<p align="justify">En esta parte, nos enfocamos en desarrollar estrategias efectivas de caché para diferentes escenarios de aplicación. Utilizamos AWS Lab Learner para simular cargas y realizar pruebas de rendimiento, lo que nos permitió evaluar y refinar nuestras estrategias.</p>

### 1. Análisis de patrones de acceso a datos
<p align="justify">Comenzamos analizando los patrones de acceso a datos de nuestra aplicación. Identificamos los datos más frecuentemente accedidos, los que cambian más a menudo y los críticos para el rendimiento de la aplicación.</p>

### 2. Selección de estrategias de caché
<p align="justify">Basándonos en nuestro análisis, seleccionamos estrategias de caché apropiadas para diferentes tipos de datos:</p>

- **Datos de lectura frecuente y escritura poco frecuente:** Implementamos una estrategia de caché con un tiempo de expiración largo.
- **Datos que cambian con frecuencia:** Utilizamos tiempos de expiración más cortos o implementamos un mecanismo de invalidación de caché basado en eventos.
- **Datos críticos en tiempo real:** Consideramos el uso de una estrategia Write-Through para mantener la consistencia.

### 3. Implementación de múltiples niveles de caché
<p align="justify">Diseñamos una arquitectura de caché de varios niveles:</p>

- **Nivel 1:** Caché en memoria de la aplicación para datos de acceso ultra-rápido.
- **Nivel 2:** ElastiCache para datos compartidos entre múltiples instancias de la aplicación.
- **Nivel 3:** CloudFront para el almacenamiento en caché de contenido estático y dinámico cerca de los usuarios finales.

### 4. Optimización de la configuración de ElastiCache
<p align="justify">Ajustamos la configuración de ElastiCache basándonos en nuestras pruebas de rendimiento:</p>

- Selección del tipo de instancia adecuado según la carga de trabajo.
- Configuración de la replicación para mejorar la disponibilidad y el rendimiento de lectura.
- Ajuste de políticas de evicción y tamaño de la caché para optimizar el uso de la memoria.

### 5. Implementación de estrategias de precarga y actualización de caché
- Desarrollamos scripts para precargar datos frecuentemente accedidos en la caché durante períodos de baja actividad.
- Implementamos un sistema de actualización de caché basado en eventos para mantener la coherencia de los datos.

### 6. Monitoreo y ajuste continuo
- Configuramos alarmas en CloudWatch para monitorear métricas clave como la tasa de aciertos de caché, la latencia y el uso de memoria.
- Establecimos un proceso de revisión y ajuste periódico de nuestras estrategias de caché basado en los datos de rendimiento recopilados.

### 7. Pruebas de carga y rendimiento
Utilizamos AWS Lab Learner para simular diferentes escenarios de carga:
- Pruebas de carga gradual para identificar cuellos de botella.
- Pruebas de pico de tráfico para evaluar la capacidad de respuesta del sistema.
- Pruebas de recuperación para verificar el comportamiento del sistema después de fallos de caché.

### 8. Optimización para diferentes tipos de contenido
Desarrollamos estrategias específicas para diferentes tipos de contenido:
- **Contenido estático:** Uso intensivo de CloudFront con tiempos de expiración largos.
- **Contenido dinámico pero poco cambiante:** Caché en ElastiCache con invalidación basada en eventos.

A través de estas estrategias y pruebas exhaustivas, logramos mejorar significativamente el rendimiento y la escalabilidad de nuestra aplicación, reduciendo la carga en la base de datos y mejorando los tiempos de respuesta para los usuarios finales.

