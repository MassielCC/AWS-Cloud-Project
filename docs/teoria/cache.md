<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Conceptos básicos de caché y su importancia en el rendimiento de las aplicaciones</h1>
</p>

## ¿Qué es la memoria caché?
<p align="justify">Una caché o memoria caché es una capa de almacenamiento de datos de alta velocidad que funciona como una memoria intermedia entre el solicitante de datos (como un procesador o cliente) y el origen de los datos (como la memoria principal, base de datos o servidor web).</p>

## ¿Dónde se encuentra la memoria caché?
<p align="justify">En un sistema informático, la caché se encuentra ubicada entre el procesador y la memoria principal. En aplicaciones web, la caché se sitúa estratégicamente en el flujo de datos entre el cliente y el servidor.</p>

## ¿Cómo funciona la memoria caché?
<p align="justify">La caché almacena un subconjunto de datos, normalmente transitorios, de modo que las solicitudes futuras de esos datos se entregan mucho más rápido sin tener que consultar a la fuente original de datos. Esto mejora el rendimiento general del sistema al reducir el tiempo de acceso a los datos.</p>

## ¿Cuál es su importancia?
<p align="justify">La memoria caché es crucial para el rendimiento de las aplicaciones y sistemas informáticos debido a varias razones:</p>
<p align="justify">Reducción de latencia: Al almacenar datos frecuentemente accedidos en una memoria de acceso rápido, se reduce significativamente el tiempo de respuesta.</p>
<p align="justify">Disminución de carga: Al servir datos desde la caché, se reduce la carga en los sistemas de origen, como bases de datos o servidores web.</p>
<p align="justify">Optimización de recursos: La caché permite un uso más eficiente de recursos computacionales y de red.</p>
<p align="justify">Escalabilidad: Sistemas con caché bien implementada pueden manejar más carga sin necesidad de aumentar proporcionalmente los recursos.</p>
<p align="justify">Ahorro de ancho de banda: En aplicaciones web, la caché puede reducir significativamente el tráfico de red.</p>

## Capas de la caché
<p align="justify">En el desarrollo de software la caché no está en un solo lugar, sino que puede implementarse en diferentes capas. Las principales son:</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/150296803/9e1ced23-9cc1-47bf-8e5f-700d59ec1477" width="700">
</p>

| Capa  | Descripción  |
| :------------: | :------------: |
| Cliente  | <p align="justify">La caché en el cliente se refiere al almacenamiento temporal de datos en el dispositivo desde el cual se accede a la aplicación. Por ejemplo, en navegadores web, los datos pueden ser almacenados en la caché del navegador para acelerar la carga de páginas web y recursos como imágenes y scripts.</p>  |
| Servidores DNS  | <p align="justify">Los servidores DNS mantienen una caché de las consultas de resolución de nombres de dominio (DNS). Esta caché permite responder rápidamente a solicitudes repetidas convirtiendo nombres de dominio en direcciones IP sin necesidad de consultar repetidamente a servidores remotos.</p>  |
| Web  | <p align="justify">Las CDN almacenan copias en caché de contenido web en servidores distribuidos geográficamente. Esto permite entregar contenido a los usuarios desde ubicaciones cercanas, reduciendo la latencia y mejorando la velocidad de carga de páginas web, videos, y otros contenidos multimedia.</p>  |
| Aplicación  | <p align="justify">Las aplicaciones móviles y de escritorio pueden almacenar datos en caché localmente para mejorar el rendimiento y la experiencia del usuario. Esto es crucial en aplicaciones que requieren acceso rápido a datos, como redes sociales, e-commerce, y juegos.</p>  |
| Base de Datos  | <p align="justify">Las bases de datos utilizan cachés para almacenar resultados de consultas frecuentemente ejecutadas y datos accedidos con regularidad. Esto reduce la carga en los sistemas de almacenamiento principal (como bases de datos SQL o NoSQL), mejorando la velocidad de respuesta de las aplicaciones.</p>  |

## Tipos de caché y casos de uso
### Caché de CPU
<p align="justify">Descripción: La caché de CPU es una memoria de acceso rápido situada dentro o muy cerca del procesador. Está diseñada para almacenar datos y comandos a los que la CPU necesita acceder con frecuencia. Existen varios niveles de caché (L1, L2, L3), siendo L1 la más rápida y pequeña, y L3 la más grande y lenta.</p>
<p align="justify">Caso de uso: Mejora la eficiencia de la CPU al reducir el tiempo que tarda en acceder a la memoria principal (RAM). Ideal para operaciones repetitivas y procesamiento de datos intensivo.</p>

### Caché de disco
<p align="justify">Descripción: La caché de disco utiliza una porción de la memoria RAM para almacenar datos que se leen y escriben con frecuencia desde el disco duro. Los SSDs también tienen su propia caché integrada.</p>
<p align="justify">Caso de uso: Acelera el acceso a datos almacenados en discos duros o SSD, mejorando el rendimiento del sistema en general. Utilizado en sistemas operativos y aplicaciones que manejan grandes volúmenes de datos.</p>

### Caché de CDN
<p align="justify">Descripción: Las redes de entrega de contenido (CDN) utilizan servidores distribuidos en diferentes ubicaciones geográficas para almacenar en caché contenido estático, como imágenes, videos y archivos CSS/JS.</p>
<p align="justify">Caso de uso: Mejora el rendimiento de la entrega de contenido web al reducir la latencia y distribuir la carga del servidor. Es crucial para sitios web con alto tráfico y contenido multimedia.</p>

### Caché de DNS
<p align="justify">Descripción: La caché DNS almacena temporalmente los registros de las direcciones IP que corresponden a los nombres de dominio. Esto ocurre tanto en los clientes (dispositivos de usuarios) como en los servidores DNS.</p>
<p align="justify">Caso de uso: Acelera la resolución de nombres de dominio, reduciendo el tiempo necesario para acceder a sitios web y servicios de internet. Útil para mejorar la experiencia del usuario y reducir la carga en los servidores DNS.</p>

### Caché web
<p align="justify">Descripción: La caché web almacena copias de páginas web y sus recursos asociados (imágenes, scripts, etc.) para su uso futuro. Esto puede hacerse en el navegador del usuario, en servidores intermedios (proxies) o en los propios servidores web.</p>
<p align="justify">Caso de uso: Mejora la velocidad de carga de las páginas web al evitar descargas repetidas de los mismos recursos. Es beneficioso tanto para usuarios finales como para reducir la carga en los servidores web.</p>

### Caché de bases de datos
<p align="justify">Descripción: La caché de bases de datos almacena resultados de consultas frecuentes en una memoria de acceso rápido (RAM). Esto puede hacerse a nivel de aplicación o utilizando soluciones dedicadas como Redis o Memcached.</p>
<p align="justify">Caso de uso: Mejora significativamente el rendimiento de las aplicaciones al reducir la latencia de acceso a los datos y aligerar la carga en las bases de datos subyacentes. Es crucial para aplicaciones que requieren alta disponibilidad y rapidez en la respuesta.</p>
