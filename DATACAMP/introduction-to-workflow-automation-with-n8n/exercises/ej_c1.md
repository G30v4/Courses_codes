# Chapter 1
- Interfaz de n8n
- Activar un flujo de trabajo
- Aplicaciones Externas y Credenciales

## Observa el flujo de datos en acción
Comprobación inteligente
Acabas de incorporarte a Acme Corp como consultor de automatización para ayudar a los equipos a entender cómo la automatización de flujos puede simplificar su día a día.

En esta primera tarea, explorarás un flujo de ejemplo para ver cómo se mueven los datos entre nodos y cómo cada paso afecta al resultado. Importarás, ejecutarás e inspeccionarás un ejemplo interno de Acme que muestra un enrutamiento de datos sencillo y manejo de errores.

### Instrucciones

Bienvenido a la página Overview de n8n

¡Has iniciado sesión automáticamente en tu propia cuenta de n8n!
La página debería cargarse mostrando el área Overview de n8n.
Para empezar, haz clic en Create Workflow.

> **Resource:** [1.1.3_routing.json](./resources/ch1/1.1.3_routing.json)
---

Para este ejercicio, comenzarás con un flujo de trabajo de plantilla.

Para importar un flujo, ve a la esquina superior derecha del lienzo.
Haz clic en el icono de los tres puntos y selecciona Import from File…
En el Desktop de la VM, ve a Resources/CH1 y abre 1.1.3_routing.json.
Ejecuta el flujo de trabajo.

---

El flujo incluye un nodo Set, que te permite crear o modificar datos dentro de tu flujo. Es útil para configurar valores que otros nodos usarán más adelante.

Después de ejecutar el flujo, abre el nodo Set Fields haciendo doble clic sobre él.

En Parameters, revisa las entradas de Fields to Set.
Luego, consulta los paneles Input y Output para comparar los datos antes y después de que se ejecute el nodo.
Esto te ayuda a entender cómo n8n transforma los datos, una habilidad clave para depurar.

Nota: Si no ves Input/Output, ajusta el zoom o redimensiona el panel.

---

Vuelve al lienzo haciendo clic en la opción Back to canvas en la parte superior izquierda y luego revisa la configuración del nodo If.

Examina la sección Input, los Parameters y, sobre todo, la sección Output.
Observa que el Output aparece en la True Branch en lugar de la False Branch.
Nota: Si no puedes ver las secciones Input y Output, puedes redimensionar la caja de configuración del nodo If y hacerla más estrecha o más ancha.

---

Quieres empezar a poner nombres más informativos a los nodos de tu flujo para que sea más fácil entender qué hacen.

De vuelta en el lienzo, cambia el nombre del último nodo haciendo clic derecho sobre él y seleccionando "Rename".
Cambia el nombre de If a If Contains Error.
Después de renombrar el nodo, guarda el flujo de trabajo.

---

## Crea tu primera automatización
Comprobación inteligente
Te has unido al equipo de soporte de Acme, que está probando un flujo de trabajo para un próximo bot de automatización de atención al cliente. El objetivo del flujo es registrar los mensajes entrantes de soporte, marcarlos como "URGENT" o "NOT URGENT" según su contenido y registrar cada ejecución con una marca de tiempo.

Esto garantiza que cada mensaje de soporte se clasifique correctamente y que ningún problema pase desapercibido. Empezarás probando una versión simplificada del bot que clasifica los mensajes según si contienen errores.

### Instrucciones

Ve a la sección Overview, crea un flujo de trabajo nuevo e importa el archivo llamado 1.2.2_automation desde la carpeta Resources/CH1 en el escritorio de la VM.

Nota: Si tienes problemas para ver algún elemento de la interfaz, puedes cambiar el zoom e incluso redimensionar las cajas de configuración de los nodos para hacerlas más estrechas o anchas.

> **Resource:** [1.2.2_automation.json](./resources/ch1/1.2.2_automation.json)
---

Haz clic en el botón + de la barra de herramientas del lienzo a la derecha para añadir un nodo Manual Trigger al lienzo.
Luego conéctalo al nodo Set Fields.
Ejecuta el flujo de trabajo.
Cuando ejecutes el flujo, Manual Trigger garantiza que se inicie de inmediato; deberías ver que el nodo Set URGENT se ejecuta

---

Observa el último nodo, Set URGENT.

Revisa las entradas, qué valores de campos se establecen y la salida.
Si el flujo se ejecuta correctamente, verás que el campo message en Output ahora incluye "URGENT:" al inicio. Esto confirma que el nodo ha modificado los datos correctamente.

---

Duplica el último nodo Set URGENT usando uno de estos métodos:
Right-click > Duplicate
O selecciona el nodo, haz clic en el elipsis (⋯) y elige Duplicate
Cambia el nombre del duplicado a "Set NOT URGENT".
Conéctalo a la rama False del nodo If Error.
Nota: El nodo If comprueba si una condición es true o false antes de que continúe el flujo. Esto permite que tu automatización tome caminos distintos; por ejemplo, enviar los tickets de alta prioridad por un lado y los normales por otro. Actúa como un punto de decisión simple en tu flujo.

---

Ve al nodo Set Fields.

Edita los Parameters del nodo eliminando la palabra "error" del cuadro message, de modo que ahora ponga "Payment on checkout".
Ejecuta el flujo otra vez y confirma que se activa la rama not urgent. Puedes saber qué nodos se han ejecutado correctamente porque tienen un contorno verde.
Al quitar "error", el mensaje ya no cumple la condición del If Error, así que el flujo tomará la rama false hacia Set NOT URGENT.

Nota: Si no ves el campo message en el nodo Set Fields, haz clic en la pestaña Parameters para mostrar el cuadro de texto del mensaje antes de editar.

---

Ve al nodo Set Fields.

Edita los Parameters del nodo eliminando la palabra "error" del cuadro message, de modo que ahora ponga "Payment on checkout".
Ejecuta el flujo otra vez y confirma que se activa la rama not urgent. Puedes saber qué nodos se han ejecutado correctamente porque tienen un contorno verde.
Al quitar "error", el mensaje ya no cumple la condición del If Error, así que el flujo tomará la rama false hacia Set NOT URGENT.

Nota: Si no ves el campo message en el nodo Set Fields, haz clic en la pestaña Parameters para mostrar el cuadro de texto del mensaje antes de editar.

---

## Captura datos con un formulario
Comprobación inteligente
La división de Eventos de Acme está lanzando una nueva iniciativa de feedback. Te han pedido ayuda para crear un flujo de trabajo que capture automáticamente las respuestas de asistentes usando un Form Trigger de n8n. Recogen comentarios después de cada evento y vas a crear un flujo sencillo que use un Form Trigger para capturar y almacenar las respuestas de forma automática.

### Instrucciones

Abre un nuevo flujo de trabajo.
Si ya estás en un flujo de trabajo activo, puedes hacerlo haciendo clic en el icono + en la barra lateral superior izquierda, luego selecciona Workflow y después Personal.
Esto abre un lienzo en blanco para tu nuevo flujo de trabajo.
Empecemos el nuevo flujo con un trigger n8n Form, específicamente un nodo On new n8n Form event.
Nota: Si tienes problemas para ver algún elemento de la interfaz, puedes cambiar el zoom e incluso redimensionar las cajas de configuración de los nodos para hacerlas más estrechas o más anchas.

---

Dentro de la configuración del nodo trigger:

Añade el title del formulario "Feedback Form" en la sección correspondiente de la pestaña Parameters.
Añade la description del formulario "Collect names and emails" en el cuadro correspondiente

---

En la sección Parameters, añade un nuevo elemento de formulario.
Nombra el Form Element como "First Name" y configúralo como tipo "Text", luego añade un placeholder, por ejemplo "e.g. John".
Márcalo como campo obligatorio para que no se pueda enviar el formulario sin introducir información.

---

Vuelve al lienzo del flujo de trabajo y ejecuta el flujo para abrir el formulario.

Haz clic en el botón Execute Workflow. Esta acción abrirá la ventana emergente del formulario que acabas de crear.
Rellena el formulario con un nombre a tu elección y envíalo.
Cuando veas el mensaje de confirmación, cierra la ventana emergente y abre el nodo On form submission.
Puedes ver la sección Output para consultar los datos que introdujiste.

### Solution
> **Resource:** [ch1_ej3.json](./resources/ch1/ch1_ej3.json)

---

## Elige el trigger perfecto
Ahora que has visto los Manual y Form Triggers, toca decidir cuál encaja en cada situación.

Un Manual Trigger lo inicias tú al probar o ejecutar un flujo durante el desarrollo, haciendo clic en Execute Workflow.
Un Form Trigger empieza cuando un usuario envía datos a través de un formulario.
Lee cada miniescenario y clasifícalo con el trigger correcto. Piensa en quién inicia la ejecución y si se recogen datos de un usuario.

### Instrucciones

Arrastra cada tarjeta de escenario a Manual Trigger o Form Trigger. Cuando termines, envía para comprobar tus respuestas. Decide en función de quién inicia el flujo de trabajo y de dónde viene la entrada.

### Solución
- Manual Trigger
    - Volver a ejecutar la tarea de ayer con entradas fijas
    - Durante una demo en vivo, ejecutar el flujo paso a paso
    - Probar un flujo nuevo una vez con datos de ejemplo
- Form Trigger
    - Una nueva persona voluntaria se registra para un evento
    - Recoger opiniones de clientes (email + comentarios)
    - Un empleado de Acme envía un informe de errores

---

## Convierte datos en HTML
Comprobación inteligente
En este ejercicio, crearás un archivo HTML sencillo con n8n. Añadirás un nodo que genere una salida de texto y después lo guardarás como archivo HTML para usarlo en flujos de trabajo posteriores. Estás generando una página de confirmación que podría enviarse a quienes completen un formulario. Crearás una página de confirmación simple para Acme Events que se pueda enviar a las personas que respondan al formulario.

### Instrucciones

Abre un flujo de trabajo nuevo y añade un Manual Trigger al lienzo del flujo.
Ahora, conecta un nodo Edit Fields (Set) al trigger y abre el nodo Edit Fields (Set) para configurarlo.
Nota: Si tienes problemas para ver algún elemento de la interfaz, puedes cambiar el zoom e incluso redimensionar las cajas de configuración de los nodos para hacerlas más estrechas o más anchas.

---

En el nodo Edit Fields (Set), añade un campo nuevo en la sección Fields to Set.

Para el nombre del campo, añade el texto "data".
Establece el valor en "Welcome to Acme Web Events!" para que el archivo HTML se relacione con tu automatización de formularios de ejercicios anteriores.
Asegúrate de que el tipo de campo se mantiene como String.
Ejecuta el flujo y consulta la sección Output en el nodo Edit Fields (Set).

---

Vuelve al lienzo y añade un nodo Convert to File, seleccionando la opción Convert to HTML.

Abre el nuevo nodo para ver los Parameters.
Deberías ver que el área Input a la izquierda está poblada con la salida del nodo anterior.
Ejecuta el nodo y descarga el File.HTML que aparece en la sección Output del nodo.

---

Vuelve al lienzo del flujo de trabajo. Si el archivo se ha descargado correctamente, podrás hacer clic en el botón de opciones de descarga junto a la barra de direcciones en la parte superior derecha de la ventana.

Si el navegador de tu VM está a pantalla completa, haz clic con el botón derecho cerca de la parte superior de la página, fuera del lienzo de n8n, y selecciona "Exit full screen".
Haz doble clic en la descarga File.html y ve a la nueva pestaña que se ha abierto en el navegador para ver el archivo.
Si quieres volver a pantalla completa, vuelve a la pestaña de n8n y luego haz clic en los tres puntos verticales en la esquina superior derecha del navegador > Zoom > Full-screen.


### Solution
> **Resource:** [ch1_ej4.json](./resources/ch1/ch1_ej4.json)

---

## Enviar mensajes a un modelo
Comprobación inteligente
En este ejercicio, usarás tus credenciales de OpenAI para conectar n8n con una aplicación externa.

Enviarás un mensaje de prueba a través del nodo OpenAI y verás cómo responde el modelo, igual que el asistente de Acme Events que responde automáticamente a preguntas sobre entradas.

### Instrucciones

Crea un flujo de trabajo nuevo y añade un Manual Trigger al lienzo del flujo. Esto te permitirá iniciar tu flujo manualmente.
Haz clic en + de nuevo y busca "OpenAI".
Selecciona “OpenAI” (primer resultado)
Selecciona el nodo "Message a model"
Note: Si tienes problemas para ver algún elemento de la interfaz, puedes cambiar el zoom e incluso redimensionar las cajas de configuración de los nodos para hacerlas más estrechas o anchas.

---

Abre el nodo nuevo para configurar los ajustes.

En la sección Parameters, usa el menú desplegable de Credential to connect with para seleccionar la opción "OpenAI account".
Asegúrate de que Resource está en "Text" y Operation en "Message a Model".
En la sección Model, cambia la opción del desplegable a "By ID".
Luego, en la casilla junto al desplegable, escribe "gpt-4o-mini".

---

En la sección Messages, puedes definir el rol y el prompt para el modelo. Aquí añadirás un prompt con el rol "User"; representa el mensaje real que procesará el modelo.

Establece Role en "User".
En Prompt, escribe o copia y pega lo siguiente: "Where can I download my Acme Web Events ticket?"
Note: Copia con Ctrl + C (o Cmd + C en Mac) y pega con Ctrl + V dentro de la VM. O haz clic derecho y elige Copy y Paste.

---

En la sección Messages, también puedes definir instrucciones del sistema; estas guían cómo debe comportarse y responder el modelo.
Haz clic en Add message.
Establece Role en "System".
En el campo Prompt, escribe o pega lo siguiente: "You are an Acme Events assistant. If asked about tickets, direct the user to their confirmation email and the 'My Tickets' page. Offer to resend the ticket and ask for the email used to register."

---

Ejecuta el nodo.
Revisa la sección Output y examina la respuesta que devuelve el nodo de OpenAI.

### Solution
> **Resource:** [ch1_ej5.json](./resources/ch1/ch1_ej5.json)

---

## Protege tus conexiones
Estás configurando un flujo de trabajo en Acme que se conecta a varias apps. Antes de que un nodo de n8n pueda extraer datos de un servicio como Google Sheets, Slack u OpenAI, ¿qué necesitas configurar para que n8n pueda acceder con seguridad a esas cuentas externas?

### Responder a la pregunta

**Respuestas posibles**
Selecciona una respuesta

- [ ] Renombrar el nodo para cada app
- [x] Crear o adjuntar credenciales para esa app
- [ ] Añadir una llamada API manual dentro del nodo

---

# Chapter 2

##