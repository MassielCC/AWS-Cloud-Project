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

## Motores de ElastiCache
### ElastiCache para Redis
<p align="justify">ElastiCache para Redis es un servicio web que facilita el despliegue y gestión de cachés Redis en la nube. Permite administrar y supervisar nodos de Redis mediante la consola de ElastiCache, la CLI de AWS o las API del servicio web.</p>

#### Características y Ventajas
Almacena datos en memoria RAM para ofrecer alta velocidad y baja latencia.
Permite escalar horizontalmente automáticamente según la demanda.
Soporta estructuras avanzadas como listas y hashes para operaciones eficientes.
Proporciona opciones de persistencia para asegurar la durabilidad de los datos.
- Almacenamiento en formato clave-valor.
- Soporta diferentes estructuras de datos (hash tables, sets).
- Permite operaciones en las estructuras de datos.

### ElastiCache para Memcached
<p align="justify"></p>

#### Características y Ventajas
Facilita la implementación sin configuraciones complicadas.
Optimiza el acceso a datos con alta velocidad y baja latencia.
Escala horizontalmente de forma automática según la carga de trabajo.
Distribuye la carga entre nodos para mantener un rendimiento consistente.
- Arquitectura cliente-servidor.
- Almacenamiento en formato clave-valor.
- Usa tabla hash y algoritmo LRU.
- Escalable y distribuible en varios servidores.

