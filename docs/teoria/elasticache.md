<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Conceptos Fundamentales de Amazon ElastiCache</h1>
</p>

## Concepto de Amazon ElastiCache
<p align="justify">Amazon ElastiCache es un servicio web de almacenamiento en caché completamente administrado que proporciona una capa de almacenamiento de alto rendimiento y baja latencia en la nube. Facilita la implementación, el funcionamiento y el escalado de cachés en memoria, mejorando el rendimiento de aplicaciones web al recuperar rápidamente información almacenada en memoria, en lugar de depender de bases de datos más lentas basadas en disco.</p>

## Beneficios y Características
- Mejora el rendimiento de aplicaciones al reducir la latencia.
- Optimiza costes al reducir la carga en bases de datos.
- Elimina la necesidad de administrar la capacidad manualmente.
- Soporta los motores de caché Redis y Memcached.

## Casos de uso
- Almacenamiento en caché de datos de aplicaciones en tiempo real.
- Almacenes de sesiones distribuidos.
- Clasificaciones y tablas de líderes en tiempo real.
- Transacciones en tiempo real, chat, análisis e inteligencia empresarial.

## ElastiCache Serveless
<p align="justify">ElastiCache sin servidor es una opción que permite implementar una caché en menos de un minuto sin necesidad de aprovisionar infraestructura ni planificar la capacidad. Supervisa continuamente la utilización de la red, memoria y procesamiento, permitiendo una escalabilidad instantánea para satisfacer la demanda sin tiempo de inactividad ni degradación del rendimiento.</p>
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/a050d9e2-ebd5-4565-8616-1c075b5e5c60" width="500">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/40a3d8d0-928d-4f52-8b36-4eeb3fe49d02" width="500">
</div>

## Motores de ElastiCache
### ElastiCache para Redis
<p align="justify">Amazon ElastiCache para Redis es un servicio web que facilita la implementación, operación y escalado de una infraestructura compatible con Redis en la nube. Redis es una estructura de datos en memoria, de código abierto, que puede utilizarse como una base de datos, caché y agente de mensajes, conocida por su alto rendimiento y flexibilidad.</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/149522e1-43c9-4710-8460-78575294fb21" width="900">
</p>

#### Características y Ventajas
- Almacena datos en memoria RAM para ofrecer alta velocidad y baja latencia.
- Soporta estructuras avanzadas como listas y hashes para operaciones eficientes.
- Proporciona opciones de persistencia para asegurar la durabilidad de los datos.

### ElastiCache para Memcached
<p align="justify">
Amazon ElastiCache para Memcached es un servicio web que facilita la implementación, operación y escalado de un almacén de datos en memoria compatible con Memcached en la nube. Memcached es un sistema de caché distribuido y de código abierto que acelera aplicaciones web dinámicas al reducir la carga de la base de datos al almacenar en caché datos y objetos en la memoria RAM.</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/7b7d1500-50f6-4be0-8226-10f5a4c71f0e" width="900">
</p>

#### Características y Ventajas
- Facilita la implementación sin configuraciones complicadas.
- Optimiza el acceso a datos con alta velocidad y baja latencia.
- Distribuye la carga entre nodos para mantener un rendimiento consistente.
