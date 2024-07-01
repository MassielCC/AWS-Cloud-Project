<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Conceptos Fundamentales de Amazon CloudFront</h1>
</p>

## Concepto de Amazon CloudFront
<p align="justify">Amazon CloudFront es un servicio de red de entrega de contenido (CDN) rápido, seguro y programable que acelera la distribución de contenido estático y dinámico a usuarios de todo el mundo con baja latencia y altas velocidades de transferencia. CloudFront entrega el contenido a través de una red global de centros de datos llamados ubicaciones de borde, mejorando significativamente la experiencia del usuario final.</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/0c5876cd-ff9f-446c-903f-4e02ec1d4c60" width="900">
</p>

### Características y Ventajas
- Mejora la velocidad de carga y el rendimiento de sitios web y aplicaciones.
- Reduce la carga en los servidores de origen al almacenar en caché el contenido en las ubicaciones de borde.
- Proporciona seguridad integrada con protección contra DDoS y compatibilidad con HTTPS.
- Ofrece personalización avanzada mediante Lambda@Edge.
- Integración sencilla con otros servicios de AWS como S3, EC2 y ELB.

### Casos de uso
- Distribución de contenido web estático y dinámico.
- Streaming de video bajo demanda o en vivo.
- Aceleración de sitios web completos.
- Distribución de software y actualizaciones.
- API y cargas de aplicaciones móviles.

## CloudFront Functions
<p align="justify">CloudFront Functions es una característica de CloudFront que permite ejecutar código JavaScript ligero en las ubicaciones de borde para manipulaciones simples de solicitudes y respuestas, ofreciendo personalización a escala masiva con latencia ultrabaja.</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/12d628ba-a650-4493-ae2c-49f6333c9783" width="900">
</p>

### Componentes clave de CloudFront
- **Distribuciones:** Configuración que define cómo CloudFront entrega el contenido.
- **Orígenes:** Servidores desde donde CloudFront obtiene los archivos para distribuir.
- **Comportamientos de caché:** Reglas que determinan cómo CloudFront maneja las solicitudes.
- **Ubicaciones de borde:** Centros de datos globales que almacenan y entregan el contenido.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/9debffbb-7988-4422-b6a5-57bf96891bfe" width="900">
</p>

### Opciones de seguridad
- **AWS WAF:** Se integra para proteger contra ataques web comunes.
- **Certificados SSL/TLS:** Soporta HTTPS para conexiones seguras.
- **Signed URLs y Signed Cookies:** Para controlar el acceso al contenido.
- **Field-Level Encryption:** Protege datos sensibles durante la transmisión.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/70a3e879-485f-45af-95cf-66fcf3a13697" width="900">
</p>

### Optimización del rendimiento
- **Compresión automática:** Reduce el tamaño de los archivos para una entrega más rápida.
- **TCP Anycast:** Mejora la conectividad y reduce la latencia.
- **Origin Shield:** Capa adicional de caché para reducir la carga en el origen.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/54f7fdfa-0139-4e2a-a119-185bd3ac5006" width="900">
</p>
