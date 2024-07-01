<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Conceptos Fundamentales de Seguridad de Caché con AWS WAF</h1>
</p>

## Concepto de AWS WAF
AWS WAF es un firewall de aplicaciones web que ayuda a proteger sus aplicaciones web o APIs contra exploits comunes que podrían afectar la disponibilidad, comprometer la seguridad o consumir recursos excesivos. AWS WAF se integra con servicios como Amazon CloudFront y ElastiCache para proporcionar una capa adicional de seguridad para sus cachés y aplicaciones.

### Características y Ventajas
- Protege contra ataques web comunes como inyección SQL y cross-site scripting (XSS).
- Permite crear reglas personalizadas para filtrar el tráfico malicioso.
- Se integra fácilmente con CloudFront, Application Load Balancer y API Gateway.
- Ofrece monitoreo en tiempo real y registro detallado de solicitudes web.
- Proporciona control granular sobre qué tráfico accede a su contenido.

### Casos de uso
- Protección de cachés de ElastiCache contra accesos no autorizados.
- Filtrado de solicitudes maliciosas antes de que lleguen a la caché.
- Prevención de ataques de denegación de servicio (DDoS) en la capa de aplicación.
- Control de acceso geográfico a contenido en caché.

### Integración con ElastiCache
WAF puede proteger el acceso a los endpoints de ElastiCache cuando se usa junto con CloudFront o Application Load Balancer.
Ayuda a prevenir el envenenamiento de caché al filtrar solicitudes maliciosas.
Permite implementar políticas de seguridad consistentes en toda la infraestructura de caché.

### Componentes clave de WAF para seguridad de caché
- **Web ACLs (Listas de Control de Acceso Web):** Conjunto de reglas que definen las acciones para el tráfico web.
- **Reglas:** Condiciones que examinan partes específicas de las solicitudes web.
- **Conjuntos de reglas administrados:** Colecciones predefinidas de reglas para protección contra amenazas comunes.
- **Rate-based rules:** Limitan el número de solicitudes de una IP en un período de tiempo.

### Estrategias de implementación
- Implementar WAF delante de CloudFront para proteger el contenido en caché.
- Utilizar reglas geográficas para restringir el acceso a cierto contenido en caché por región.
- Configurar rate limiting para prevenir abusos y sobrecarga de la caché.
- Usar reglas personalizadas para filtrar patrones de ataque específicos a su aplicación.

### Monitoreo y registro
- Integración con Amazon CloudWatch para métricas en tiempo real.
- Logging detallado de solicitudes para análisis de seguridad y cumplimiento.
- Alertas configurables para notificaciones de actividad sospechosa.
Mejores prácticas

Implementar el principio de menor privilegio en las reglas de acceso.
Mantener actualizados los conjuntos de reglas administrados.
Realizar pruebas exhaustivas antes de implementar nuevas reglas en producción.
Utilizar AWS WAF en conjunto con otras medidas de seguridad como encriptación en tránsito.
