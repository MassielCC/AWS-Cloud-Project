<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Ejercicio 6: Implementación de CloudFront para caché y seguridad de aplicaciones</h1>
</p>

## Objetivos
- Configuración de CloudFront para la protección de aplicaciones mediante WAF (Web Application Firewall).
- Experimentación con reglas de seguridad y políticas de caché.

No se cuentan con los permisos para usar Web Application Firewall (WAF) ni en Lab Learner ni el laboratorio que se utilizó para crear la distribución de CloudFront
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/b6068f10-992a-40ff-9519-cf42d2c66f6e" width="800">
</p>

## WAF: Web Application Firewall
Es un farewall que permite monitorear las solicitudes HTTP y HTTPS que se realizan a nuestras aplicaciones. Esto se logra mediante la configuración de reglas de seguridad.
![image](https://github.com/EdwinJaraOFC/AWS-Cloud-Project/assets/73445717/1e1cad55-cb7a-4ae2-8462-d55df1ae78de)

Componente de AWS WAF:
- **ACL web:** Listas de control de acceso web. Nos permite añadir reglas, las cuales sirven para definir bajo que criterios se inspeccionarán las solicitudes web y qué acciones se tomarán en cada que cumplan dado criterio. Dentro de las opciones que nos ofrece están: Permitir el paso de las solicitudes, bloquearlas, contar el número de solicitudes y realizar comprobaciones CAPTCHA.
- **Reglas:** Cada regla contiene una instrucción que define los criterios de inspección y la acción a tomar si una solicitud web cumple con dichos criterios.
- **Grupos de reglas:** Se pueden definir reglas directamente dentro de una ACL web o en grupos de reglas reutilizables. También el propio usuario puede definir su grupo de reglas.

  ## Políticas de caché**
Una política de caché contiene:
- Nombre que nos permite identificarla y una descripción para saber el propósito de la misma
- Configuraciones de TTL (tiempo de vida): el tiempo mínimo y el tiempo máximo  que nuestros objetos permanecen en el caché de CloudFront antes de que este consulte al servidor de origen si el objeto ha sido actualizado. También tenemos el TTL por default.
- Configuraciones de la clave de caché

AWS CloudFront proporciona algunas políticas de caché predefinidas, conocidas como políticas administradas, para casos de uso comunes.

- CachingDisabled: Esta política desactiva el almacenamiento en caché, es recomendado cuando las solicitudes de nuestros clientes no se pueden almacenar en caché
- CachingOptimized: Optimizada para el almacenamiento de caché eficiente. Permite configurar reglas de invalidación para eliminar objetos obsoletos
- CachingOptimizedForUncompressedObjects: Diseñada para la optimización del almacenamiento en caché de objetos sin comprimir.

De acuerdo al tipo de contenido podemos seleccionar la política administrada por AWS que mejor se adapta a nuestras necesidades. 

**Integración de CloudFront y AWS WAF**
Se puede usar AWS WAF para proteger las distribuciones de CloudFront. Podemos habilitar el uso de AWS WAF al crear la distribución o editando la configuración de seguridad de una distribución ya creada.
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

