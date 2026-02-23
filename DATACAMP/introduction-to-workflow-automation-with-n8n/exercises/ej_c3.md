# Chapter 3
- Activar flujos a partir de eventos externos
- Uso de datos de API y LLMs
- Crear automatizaciones robustas para el mundo real
- Elegir la estrategia de automatización adecuada

---

## Elegir el disparador adecuado
Acme Education quiere recopilar comentarios de los asistentes justo después de cada webinar. Necesitan una forma sencilla para que la gente envíe su nombre y comentarios a través de un formulario, y que cada envío inicie el flujo de trabajo automáticamente.

¿Qué disparador deberías usar si quieres que el flujo de trabajo empiece automáticamente cuando una persona usuaria envía comentarios mediante un formulario?

### Responder a la pregunta

**Respuestas posibles**
Selecciona una respuesta

- [ ] Webhook Trigger (escucha eventos de sistema a sistema)
- [ ] Manual Trigger (la persona desarrolladora lo ejecuta para probar flujos)
- [x] Form Trigger (empieza cuando una persona usuaria envía una entrada)

---

## Crea una conexión con Webhook
Comprobación inteligente
En Acme Support, el equipo de atención al cliente quiere enviar automáticamente los datos de los tickets desde su sistema interno a un flujo de automatización que procese cada envío en tiempo real. Para simular este escenario, crearás dos flujos de trabajo conectados:

Workflow A (Receptor): escucha nuevas solicitudes de tickets mediante un Webhook Trigger.
Workflow B (Emisor): simula el sistema de tickets enviando esa información a través de un HTTP Request.
Así aprenderás cómo distintos flujos (o sistemas externos) pueden comunicarse usando webhooks, una habilidad esencial para automatizaciones reales.

### Instrucciones

Crea un flujo de trabajo nuevo e importa el archivo 3.1.3_webhook_events.json desde la carpeta Resources/CH3 del escritorio de la VM.

Verás que la primera sección del flujo, A, es el Webhook Receiver. Esta sección recibe mensajes de un emisor; en este caso, Workflow B, el Webhook Sender.

> **Resource:** [3.1.3_webhook_events.json](./resources/ch3/3.1.3_webhook_events.json)

---

Primero, configuremos correctamente el workflow A antes de continuar con otras tareas.

Abre el nodo Webhook y, en la pestaña Parameters, elimina cualquier texto de la sección Path y déjalo en blanco.
Como vamos a activar este flujo, necesitaremos usar la Production URL del nodo Webhook.
En la sección Webhook URLs, haz clic en la opción Production URL y luego en la URL disponible para copiarla.

---

Vuelve al lienzo del flujo y abre el nodo HTTP Request.

En la sección Parameters, borra la URL de ejemplo en la sección URL y pega la "Production URL" que copiaste del Workflow A.
Examina el resto de ajustes del nodo en la sección Parameters. Verás que estamos enviando un campo con un valor enviado en el nodo anterior, almacenado como json.message.

---

Ahora revisemos el nodo anterior que proporciona datos al nodo HTTP Request.

Vuelve al lienzo del flujo y abre el nodo Edit Fields.
Verás que estamos creando un campo con el nombre "message", que actualmente tiene un valor de ejemplo.
Borra el texto "hello world!" y sustitúyelo por:
"Server outage in EU region"

---

Vuelve al lienzo del flujo.

Cambia el flujo de "Inactive" a "Active" usando el interruptor de la esquina superior derecha. Haz clic en Got it en la ventana emergente.
Ahora ejecuta solo Workflow B y abre el nodo HTTP Request para confirmar que se ejecutó correctamente.

---

De vuelta en el lienzo del flujo, navega a la pestaña Executions usando la opción en la parte superior de la pantalla. Aquí puedes revisar las ejecuciones de los flujos.

Revisa la ejecución más cercana a tu hora actual (el primer resultado de la lista de ejecuciones)
Haz clic en el nodo Webhook en Workflow A
Ahora puedes revisar la sección Output y ver el objeto query. Verás el mensaje definido en el nodo Edit Fields (Set).

### Solution
> **Resource:** [3.1.3_webhook_events_solved](./resources/ch3/3.1.3_webhook_events_solved.json)

---

## Filtra los datos entrantes
Comprobación inteligente
Tu automatización de Acme Support ya recibe datos entrantes a través de un webhook. Sin embargo, no todos los eventos deberían activar el mismo procesamiento. Algunos eventos, como "purchase", requieren un seguimiento inmediato, mientras que otros deberían continuar por una ruta diferente.

En este ejercicio, filtrarás la entrada del webhook para que solo los eventos relacionados con compras continúen por tu flujo de trabajo. Esto refleja una configuración real en la que los sistemas reciben tipos de eventos mixtos (registros, actualizaciones, compras) y solo actúas sobre los relevantes.

### Instrucciones

Crea un flujo de trabajo nuevo e importa el archivo 3.1.4_webhook_filtering.json desde la carpeta Resources/CH3 en el escritorio de la VM.

Los flujos de trabajo que verás te resultarán familiares, y deberías tener un nodo Webhook fijado que ha conservado los datos de las ejecuciones previas que hiciste en el flujo.
Abre el nodo Webhook y despliega la sección Output para inspeccionar los campos de query:
eventType
user
timestamp

> **Resource:** [3.1.4_webhook_filtering.json](./resources/ch3/3.1.4_webhook_filtering.json)

---

Vuelve al lienzo del flujo de trabajo.

Añade un nodo If y conéctalo después del nodo Webhook.
Abre el nuevo nodo y configúralo así:
value1 : {{$json.query.event_type}}
Operation: is equal to
value2 : "purchase"
Ejecuta el flujo de trabajo.

---

De vuelta en el lienzo del flujo de trabajo, deberías ver 1 elemento atribuido a la rama true.

Añade un nuevo nodo Edit Fields (Set) y conéctalo a la rama true.
Renombra el nuevo nodo como "Purchase Detected" y añade un campo nuevo con la siguiente configuración:
name: "message"
value: "Purchase event detected!"

---

Ve al lienzo del flujo de trabajo y añade un nuevo nodo Edit Fields (Set) a la rama false.

Renombra el nuevo nodo como "Other Events".
Añade un campo nuevo con la siguiente configuración:
name: "event_type_info"
value: event_type (usa la variable de la sección Input)
Ejecuta el flujo de trabajo una vez más.

### Solution
> **Resource:** [3.1.4_webhook_filtering_solved](./resources/ch3/3.1.4_webhook_filtering_solved.json)

---

## Planifica tu automatización con APIs
El equipo de Marketing de Acme quiere extraer datos de campañas desde APIs, transformarlos y resumir comentarios de clientes con IA. Clasifica cada tarea en la categoría correcta para planificar la estructura del flujo de trabajo.

### Instrucciones

Arrastra cada elemento a la zona donde mejor encaja.

### Solución

- HTTP Request 
    - Consulta el tiempo por ID de ciudad desde una API pública de meteorología.
    - Extrae los últimos 50 resultados de campañas de anuncios desde la API de analítica de Acme.
- Transform/Filter
    - Convierte "20000" (cadena) en un número y conserva solo las campañas con presupuesto > 20000.
    - Pasa solo los registros de campaña cuyo estado sea "active".
- LLM Call
    - Resume una reseña de cliente de 5 párrafos en una sola frase.
    - Clasifica un correo de soporte como bug / feature / praise.

---

## Añade lógica a los datos de la API
Comprobación inteligente
En Acme, estás creando un flujo de trabajo que filtra datos de clientes devueltos por un servicio externo.

Marcarás a los clientes de alto valor (con presupuestos superiores a 20.000) para darles prioridad en el contacto.

### Instrucciones

En un flujo de trabajo nuevo, importa el archivo 3.2.4_APIDecisions.json desde la carpeta Resources/CH3 en el escritorio de la VM y ejecuta el flujo de trabajo.

Abre el nodo Account Details y observa el esquema de la salida en la sección Output, en particular el presupuesto, el nombre del cliente y el número de cuentas en cartera.
Lo que ves refleja cómo se estructuran la mayoría de respuestas de API: con varios elementos, distintos tipos de datos y, a veces, valores anidados.

> **Resource:** [3.2.4_APIDecisions.json](./resources/ch3/3.2.4_APIDecisions.json)

---

Conecta un nodo If al flujo de trabajo y abre la ventana de parámetros.

Cambia la condición a Number > Is greater than. Configura los valores así:
value1: budget (de la sección Input)
value2: "20000"
Ejecuta el flujo de trabajo.

---

En el lienzo del flujo de trabajo, conecta un nodo Edit Fields (Set) a la rama true del nodo If y renómbralo "High Priority". Añadirás cuatro campos en el nodo nuevo con estas configuraciones:

Campo 1:
Nombre: "Status"
Valor: "High Priority Client"
Campo 2:
Nombre: "Reason"
Valor: "Budget above 20k"
Campo 3:
Nombre: "Name"
Valor: name (del campo client en la sección Input)
Campo 4:
Nombre: "Budget"
Valor: budget (de la sección Input)
Ejecuta el flujo de trabajo y observa la salida.

---

Ahora conecta un nodo Edit Fields (Set) a la rama false del nodo If y renómbralo "Standard Priority". Añadirás cuatro campos en el nodo nuevo con estas configuraciones:

Campo 1:
Nombre: "Status"
Valor: "Standard Client"
Campo 2:
Nombre: "Reason"
Valor: "Budget below 20k"
Campo 3:
Nombre: "Name"
Valor: name (del campo client en la sección Input)
Campo 4:
Nombre: "Budget"
Valor: budget (de la sección Input)
Ejecuta el flujo de trabajo y observa la salida.

### Solution
> **Resource:** [3.2.4_APIDecisions_solved](./resources/ch3/3.2.4_APIDecisions_solved.json)

---

## Generar respuestas con IA

Comprobación inteligente
Acme Support está desbordado con los tickets entrantes. En lugar de escribir a mano cada respuesta, el equipo quiere redactar automáticamente respuestas amables que los agentes puedan revisar y enviar.

Vas a crear un workflow donde se simulan mensajes entrantes y se pasan por un LLM que genera una respuesta para cada uno.

### Instrucciones

En un workflow nuevo, carga el archivo 3.2.5_LLMCall.json desde la carpeta Resources/CH3 del escritorio de la VM y ejecútalo.

Abre el nodo Generate Messages para ver el resultado. Este workflow habrá generado 12 mensajes de correo.
Lee algunos mensajes en la sección Output, usando la vista más adecuada.

> **Resource:** [3.2.5_LLMCall.json](./resources/ch3/3.2.5_LLMCall.json)

---

Desde el lienzo del workflow, abre el menú del panel de nodos y selecciona la categoría AI para ver la amplia gama de acciones que la IA puede realizar en n8n.

Selecciona el nodo OpenAI y luego elige Message a model. Vuelve al lienzo del workflow.
Verás que está en estado de error, porque necesita credenciales y la selección de un modelo para poder ejecutarse.
Asegúrate de conectarlo al nodo Generate Messages y ábrelo para ver los parámetros y ajustes.

---

En Parameters, asegúrate de que están seleccionadas las credenciales "OpenAI account".

En la sección Model, cambia la opción del desplegable a "By ID".
Luego, en la caja junto al desplegable, tendrás que escribir "gpt-4o-mini".

---

Ahora añadiremos dos prompts para dos roles distintos: un prompt de usuario y un prompt de sistema.

Primero, en el menú desplegable Role, selecciona el rol "User". En este desplegable puedes ver descripciones de lo que hace cada rol.
En la sección Prompt, añade el campo email_text desde la sección Input.

---

Para añadir un segundo rol, tenemos que crear un nuevo mensaje.

Selecciona Add Message.
Establece Role en "System". Este rol indicará al LLM qué hacer con el mensaje/prompt del usuario.
Vuelve al lienzo del workflow y copia el prompt guardado en la nota adhesiva. También puedes copiar y pegar desde aquí:
Copy system prompt from here
En la configuración del nodo OpenAI, pega el mensaje del prompt en la sección Prompt del usuario de sistema.
Ejecuta el workflow. El LLM (GPT-4o-mini) generará respuestas para los 12 mensajes de correo. Cuando termine la ejecución, podrás ver el resultado y revisar las respuestas creadas.

### Solution
> **Resource:** [3.2.5_LLMCall_solved](./resources/ch3/3.2.5_LLMCall_solved.json)

---

## ¿Reutilizable o no?
En DevLabs, una persona desarrolladora entrega un flujo de trabajo de n8n al equipo de soporte justo cuando se lanza un producto crítico. Si el flujo falla o no se puede reutilizar, todo el equipo se arriesga a sufrir retrasos, clientes enfadados y horas extra resolviendo incidencias.

Algunas decisiones de diseño facilitan que otros reutilicen el flujo, mientras que otras generan caos cuando hay que actualizarlo. Tu tarea: clasifica cada práctica como Reutilizable o No reutilizable para que el flujo se pueda compartir con seguridad en todo el equipo sin crear cuellos de botella.

### Instrucciones

Arrastra cada práctica a la zona correcta: Reutilizable o No reutilizable.

### Solución
- Reutilizable
    - Usar nodos Edit para almacenar información compartida
    - Usar la misma credencial de forma segura en varios nodos
    - Añadir comentarios o documentación
    - Validar entradas antes de procesar
- No Reutilizable
    - Dejar salidas inconsistentes entre ejecuciones
    - Codificar valores fijos dentro de varios nodos

---

## Crea un prototipo funcional
Comprobación inteligente
El equipo de Logística de Acme necesita ayuda para completar su flujo de trabajo de informes diarios de incidencias. Han compartido un borrador y necesitan que lo termines y lo pruebes.

Tu tarea es finalizar la lógica de validación y la preparación de datos para el siguiente paso con el LLM.

### Instrucciones

En un flujo de trabajo nuevo, carga el archivo 3.3.3_start.json desde la carpeta Resources/CH3 en el escritorio de la VM. Este archivo te lo ha pasado una persona del equipo que quiere que le ayudes a ordenar los nodos correctamente y ejecutar con éxito todo el flujo de trabajo.

Primero, ejecuta manualmente el flujo para ver la salida del Code Node.
Usando la vista Schema o Table en la sección de salida de los nodos, puedes ver los datos que se pasarán por el flujo de trabajo.

> **Resource:** [3.3.3_start.json](./resources/ch3/3.3.3_start.json)

---

Una de las primeras tareas que quieres que realice el flujo es validar los datos y asegurarte de que cualquier elemento incompleto o faltante se filtre al principio del proceso.

Conecta el nodo If al Code Node para continuar construyendo el flujo de trabajo.
En la configuración de parámetros, actualiza las condiciones para que las variables order_id y message no estén vacías. Esto garantiza que se filtren los elementos incompletos o no válidos.
Nota: En este flujo, la rama true representa datos válidos que continúan por el proceso, mientras que la rama false captura los registros no válidos o faltantes.

---

Ahora conecta el resto de los nodos de la sección "To add after the Code Node". Recuerda que el objetivo es pasar datos válidos por un LLM.

Abre el nodo Data for LLM y revisa qué parámetros se han creado y qué campos se han definido para usarlos más adelante en un nodo LLM.
Termina esta fase de construcción conectando los dos nodos restantes a la rama false del nodo If.
Revisa los parámetros de los nodos conectados a la rama _false` y luego ejecuta todo el flujo de trabajo.
Cuando se ejecute correctamente:

La rama True debe contener registros válidos con datos completos.
La rama False mostrará que se han filtrado las entradas no válidas.

### Solution
> **Resource:** [3.3.3_start_solved](./resources/ch3/3.3.3_start_solved.json)

---

## Añade toma de decisiones con IA
Comprobación inteligente
Acme Logistics ha estado recibiendo informes de incidencias desde varias ubicaciones de entrega y ahora el equipo quiere categorizarlas automáticamente usando IA.

Tu tarea es mejorar el flujo existente añadiendo un nodo OpenAI que clasifique cada informe (por ejemplo, como "Delay", "Damage" o "Customer Complaint"). También configurarás un manejo de errores adecuado para que el flujo continúe incluso si la llamada a la IA falla.

### Instrucciones

Se han revisado los primeros pasos de tu flujo de trabajo, pero ahora has recibido una actualización.

Crea un flujo nuevo e importa el flujo desde el archivo 3.3.4_start.json en la carpeta Resources/CH3 del escritorio de la VM.
Este flujo contiene los pasos necesarios para configurar la recepción de datos de incidencias entrantes.

> **Resource:** [3.3.4_start.json](./resources/ch3/3.3.4_start.json)

---

Añade un nodo OpenAI (opción Message a model) al flujo para clasificar las descripciones de incidencias con un modelo de IA.

Configura el nodo usando la siguiente información en la sección Parameters:
Elige las credenciales "OpenAI account".
En la sección Model, cambia la opción del desplegable a "By ID".
Luego, en la caja junto al desplegable, tendrás que escribir "gpt-4o-mini".

---

Ahora añadiremos dos prompts para dos roles distintos: un prompt de usuario y un prompt de sistema. La información para los prompts está en notas adhesivas en el lienzo del flujo.

Para el primer mensaje, selecciona el rol "User" en el menú desplegable.
Selecciona la sección Prompt y, usando las opciones de la parte superior derecha de la caja, elige "Expression". Esto permitirá que el prompt haga referencia dinámicamente al texto de descripción desde nodos anteriores.
Copia y pega lo siguiente para el prompt de "User":

Copy user prompt from here
```js
Incident Report:
Email: {{$json.email}}
Order ID: {{$json.order_id}}
City: {{$json.city}}
Message: {{$json.incoming_message}}
```

Nota: Copia con Ctrl + C (o Cmd + C en Mac) y pega con Ctrl + V dentro de la VM. O haz clic derecho y elige Copy y Paste.

---

Añade un segundo mensaje con la opción Add Message y establece el Role en "System".
Igual que antes, asegúrate de que la caja del prompt esté en "Expression".
Asegúrate de que la salida del OpenAI sea JSON y de activar Simplify Output usando los conmutadores debajo del botón Add Message.
Copia y pega lo siguiente para el prompt de "System":

Copy system prompt from here
```js
You are helping a logistics team quickly understand incident reports.
Always reply in JSON with 3 parts:
{
  "summary": "short description of the problem (max 20 words)",
  "urgency": "high or normal",
  "action": "contact_customer, escalate_ops, or monitor"
}
If you are not sure, use urgency="normal" and action="monitor".
```

---

Asegúrate de que tu flujo continúe ejecutándose incluso si el nodo OpenAI falla, para así gestionar los errores correctamente.

En la sección Settings del nodo OpenAI, cambia la opción On Error a "Continue (using error output)".
Ejecuta el flujo y revisa la salida del nodo OpenAI.

### Solution
> **Resource:** [3.3.4_start_solved](./resources/ch3/3.3.4_start_solved.json)

---

## Prueba la automatización completa
Comprobación inteligente
Has llegado a la fase final del flujo de trabajo de Acme Logistics. Toca decidir qué ocurre con cada registro tras la clasificación. Conectarás la salida del LLM a la lógica condicional, mostrarás los resultados y te asegurarás de que el flujo gestione los errores correctamente.

### Instrucciones

Empieza importando el archivo de flujo preparado 3.3.5_start.json que contiene la configuración de clasificación con OpenAI.

Esto servirá como base para la lógica final de decisión y salida.

> **Resource:** [3.3.5_start.json](./resources/ch3/3.3.5_start.json)

---

Desarrolla la lógica de decisión para determinar qué registros clasificados deben continuar por el flujo y cuáles deben detenerse. Verás que hay dos ramas del flujo que deben crearse usando la salida del nodo OpenAI.

Tendrás que arrastrar los nodos desde la parte inferior derecha del lienzo a las áreas correspondientes.

---

La rama Success del nodo OpenAI se enviará al nodo llamado OpenAI If para ayudarte a decidir y comprobar los valores de urgencia de la salida del LLM.
Configura las condiciones del nodo OpenAI If para añadir el valor de campo correcto en el nodo y asegurar que solo los registros con urgencia "high" (establecida por el LLM) pasen por el resto del flujo.
Esta sección también tendrá un nodo Edit Fields (Set) y un nodo HTML.
El nodo No Operation, do nothing (decide) deberá conectarse a la rama false del nodo OpenAI If.
Nota: Los nodos HTML se usan para mostrar los resultados de forma visual en los Resultados.

---

Para la sección "If Error Branch" asegúrate de conectar los nodos correctos a la rama Error del nodo OpenAI.

Esta sección tendrá los dos nodos restantes que se te han proporcionado.

---

Prueba tu flujo completo para verificar que la lógica de decisión y el manejo de errores funcionan como esperas.

Empieza con una ejecución normal.
También puedes editar las credenciales del nodo OpenAI y crear una credencial nueva incorrecta usando cualquier número como clave de API

### Solution
> **Resource:** [3.3.5_start_solved](./resources/ch3/3.3.5_start_solved.json)

---

## Evalúa si conviene automatizar
No todos los procesos de negocio merecen ser automatizados. Algunas tareas ahorran horas cuando se automatizan; otras son raras o demasiado complejas para justificar el esfuerzo.

En este ejercicio, leerás escenarios de Acme Corp y decidirás si son buenos candidatos para automatizar. Piensa en el tiempo ahorrado, la reducción de errores y la escalabilidad.

### Instrucciones

Arrastra cada tarjeta de escenario a "Automatizar" o "Mantener manual".
Basa tu elección en si automatizar la tarea reduciría de forma significativa el esfuerzo o los riesgos, frente a ser más rápido dejarla como está.

### Solución
- Automatizar
    - Generar el resumen diario de ventas a partir de datos del CRM.
    - Enviar correos de bienvenida a cada nuevo empleado.
    - Registrar los envíos de formularios web en una hoja de cálculo.
- Mantener Manual
    - Aprobar un contrato de colaboración de alto valor.
    - Escribir una nota personal a un cliente de larga trayectoria.
    - Decidir qué becario debería unirse a cada equipo.

---

## Prepárate para compartir con el equipo
Comprobación inteligente
Estás preparando documentación para AxisGroup, un cliente empresarial de Acme. El objetivo es renombrar nodos y añadir notas adhesivas para que el flujo de trabajo sea claro y accesible para usuarios no técnicos antes de compartirlo.

### Instrucciones

En un flujo de trabajo nuevo, carga el archivo 3.4.3_finance_start.json desde la carpeta Resources/CH3 en el escritorio de la VM.

Abre el nodo OpenAI Chat Model que está conectado al nodo Basic LLM Chain para comprobar que se han configurado las credenciales correctas.
Ahora, ejecuta el flujo de trabajo e inspecciona todos los nodos para entender cómo funciona todo.
Verás que se ha añadido una nota adhesiva en la última sección del flujo. Además, los nodos de esa sección se han renombrado. El nodo de código del inicio también se ha renombrado por ti.

> **Resource:** [3.4.3_finance_start.json](./resources/ch3/3.3.5_start.json)

---

Realiza comprobaciones de entrada y salida en distintos nodos del flujo de trabajo.

Asegúrate de revisar Basic LLM Chain. La User Message pasa las entradas al LLM y la System Message define las instrucciones que el LLM debe considerar.
Revisa el último nodo del flujo para entender cómo encaja todo: piensa en cómo se rellena la última columna Action en la fila generada en el nodo anterior y cómo se rellenan también las tres primeras columnas en la tabla.

---

Una vez que hayas entendido el proceso del flujo, es buena práctica renombrar los nodos para que se entienda a primera vista qué está ocurriendo.

Renombra los siguientes nodos con los nuevos nombres indicados:
Basic LLM Chain a "Classify Expenses"
Nodo Switch a "Classify by Expense Type"
Nodo Edit Fields a "Set Normal Action"
Nodo Edit Fields3 a "Set High Value Action"
Nodo Edit Fields4 a "Set Suspicious Action"

---

Además de renombrar nodos, añadir notas adhesivas que agrupen secciones del flujo te permite señalizar y documentar mejor los procesos que se llevan a cabo.

Crea una nota adhesiva nueva haciendo clic derecho en una zona vacía del lienzo y seleccionando la opción Add sticky note.
Las notas adhesivas se pueden formatear con lenguaje markdown, así que un "#" creará un encabezado grande. Siéntete libre de probar el formato.
Añade las siguientes notas adhesivas con estos títulos en las secciones correspondientes:
"Trigger and Generating Records" está al inicio del flujo
"Classify Incoming Records" utiliza el nodo LLM
"Setting Action Values" tiene lugar antes de mostrar cualquier dato

---

Cuando termines de renombrar nodos y añadir notas adhesivas, es momento de exportar el archivo para que tu equipo pueda descargar y usar el flujo.

Primero, guarda el flujo de trabajo, dándole el nombre que prefieras.
Usando el menú de puntos suspensivos en la esquina superior, descarga el archivo .json.
Para asegurarte de que tu equipo recibe el flujo tal y como lo esperas, es buena idea importar el flujo que acabas de descargar.
Usa el proceso habitual de importación de archivos, trayendo el archivo desde la carpeta Download de tu instancia de VM.

### Solution
> **Resource:** [3.4.3_finance_start_solved](./resources/ch3/3.4.3_finance_start_solved.json)

---

### Planificación para la automatización
Acme HR sube un CSV con las nuevas incorporaciones cada viernes, y necesitas crear en n8n una automatización de onboarding que envíe el mensaje de correo correcto según el rol de cada empleado.

Antes de empezar a trabajar en el flujo, ¿cuál es el ÚNICO mejor siguiente paso a dar?

### Responder a la pregunta

**Respuestas posibles**
Selecciona una respuesta

- [x] Primero planifica el proceso: define la entrada, los resultados y los pasos clave entre medias.
- [ ] Empieza a crear nodos en n8n de inmediato y ajusta el flujo sobre la marcha.
- [ ] Retrasa la automatización y pide a RR. HH. que siga enviando correos manualmente por ahora.
