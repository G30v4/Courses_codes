# Chapter 2
- Lógica condicional en los flujos de trabajo
- Transformar y limpiar datos
- El nodo Merge
- Pruebas y validación de flujos de trabajo
- Depuración de errores del flujo de trabajo

---

## If vs. Switch
Tu equipo de soporte está diseñando flujos para enrutar tickets de clientes. Lee cada escenario y decide si debe usar un nodo If (comprobación sí/no) o un nodo Switch (un campo con varios valores posibles).

### Instrucciones

Arrastra cada tarjeta de escenario a IF Node o Switch Node. Decide según si la lógica es binaria (sí/no) o una entre varias (valores distintos múltiples).

### Solucion
- IF Node
    - Comprobar si el pago fue correcto o falló.
    - ¿El texto del mensaje contenía la palabra “error”?
    - ¿El cliente es VIP? Sí → vía rápida; No → normal.
- Switch Node
    - Asignar la consulta por canal: email, chat, teléfono.
    - Elegir el flujo según el estado del ticket: abierto, en progreso, cerrado.
    - Enrutar el ticket según prioridad: baja, media, alta.

---

## Divide flujos con lógica If
Comprobación inteligente
Sigues trabajando con el Acme Support Desk. Algunos tickets son urgentes y hay que gestionarlos rápido. Otros son normales y pueden esperar un poco.

En este ejercicio, vas a crear un flujo de trabajo que enruta los tickets por urgencia; los de alta prioridad van a los managers, mientras que el resto se pone en cola para revisión.

### Instrucciones

En un lienzo de flujo de trabajo nuevo, añade un nodo Manual Trigger y luego conecta un nodo Edit Fields (Set).

Primero añade un campo con "message" en la sección name y "database is not working, need urgent fixing" en la sección value.
Añade un segundo campo con "priority" en la sección name y "high" en la sección value.
Ejecuta el paso y luego vuelve al lienzo del flujo de trabajo.

---

Conecta un nodo If al nodo Edit Fields (Set).
Configura el nodo arrastrando el campo priority desde la sección Input hasta la sección value1 y establece value2 en "high".
Ejecuta el paso y luego vuelve al lienzo del flujo de trabajo.
Nota: Si no ves el campo priority en el panel Input, haz clic en el icono de actualizar o expande el panel para cargar los datos del nodo anterior.

---

Al observar el flujo, verás que el proceso ha pasado por la rama true, ya que priority se estableció en "high" en el nodo Edit Fields. Ahora, sigamos construyendo el flujo.

Conecta la rama true del nodo If a un nuevo nodo Edit Fields (Set) y ponle el nombre "Priority"—rellenarás los campos en un momento.
Ahora conecta un nuevo nodo Edit Fields (Set) a la rama false del nodo If y ponle el nombre "Normal".

---

Ahora debes configurar los dos nuevos nodos Edit Fields (Set).

En el nodo Priority, añade un campo nuevo con el name "status" y el value "Urgent - send to manager".
En el nodo Normal, añade un campo nuevo con el name "status" y el value "Not urgent - add to queue".
Ejecuta ambos nodos para confirmar sus resultados.

---

Vamos a ajustar la configuración de los nodos para ver cuándo se activa la rama false.

Abre tu primer nodo Edit Fields (Set) y cambia priority de "high" a "low".
Vuelve al lienzo del flujo de trabajo y ejecuta el flujo.
Ahora deberías ver que se ha activado la rama false. Abre el nodo Normal y consulta el panel Output.


### Solution
> **Resource:** [ch2_ej1.json](./resources/ch2/ch2_ej1.json)

---

## Gestiona múltiples resultados
Comprobación inteligente
En Acme Support Desk, cada ticket tiene un estado: pending, approved o rejected. En flujos reales, estos valores pueden venir de un formulario o una aplicación externa.

En este ejercicio, vas a simular esa configuración usando un nodo Set Fields para comprobar cómo tu flujo gestiona cada estado. Cuando cada rama funcione como esperas, estarás listo para conectar datos de entrada reales.

Crearás un flujo que comprueba el estado del ticket y lo enruta a la rama correcta, añadiendo un mensaje claro que indique qué camino ha seguido el ticket.

### Instrucciones

En un lienzo de flujo nuevo, añade un nodo Manual Trigger y conecta un nodo Edit Fields (Set) al disparador.

Añade un campo nuevo con esta configuración:
Nombre del campo: "status"
Valor del campo: "pending"
Cambia el nombre del nodo Edit Fields (Set) a Set Status
Ejecuta el flujo.

---

De vuelta en el lienzo del flujo, añade un nodo Switch al final del flujo actual. Abre el nodo nuevo.

En la sección Parameters, verás que hay una regla de enrutamiento lista para configurar. Añade dos reglas más para que haya tres en total.
En cada regla de enrutamiento, establece el marcador value1 como status, arrastrando el campo status desde la sección Input hasta la casilla correspondiente.
Para el marcador value2, añade los siguientes valores:
Regla de enrutamiento 1: "pending"
Regla de enrutamiento 2: "approved"
Regla de enrutamiento 3: "rejected"
Ejecuta el flujo.

---

Vuelve al lienzo del flujo y observa qué rama y columna de salida aparece resaltada en verde. Esa fue la que se ejecutó correctamente.

Conecta un nuevo nodo Edit Fields (Set) a la rama que está resaltada en verde.
Como era la rama de "pending", cambia el nombre del nuevo nodo Set a Set Pending.
Abre el nodo nuevo y configura un campo con los siguientes ajustes:
Nombre del campo: "message"
Valor del campo "ticket is still pending review"

---

En el lienzo del flujo, repite el paso anterior para las otras dos ramas restantes del nodo Switch. Configura los nodos Edit Fields (Set) como sigue:

Rama intermedia ("approved")
Cambia el nombre del nodo a Set Approved y configura el campo así:
Nombre del campo: "message"
Valor del campo "ticket is approved"
Rama inferior ("rejected")
Cambia el nombre del nodo a Set Rejected y configura el campo así:
Nombre del campo: "message"
Valor del campo "ticket is rejected"

---

Vuelve al lienzo.

Ejecuta el flujo con el valor "pending" de Set Status con el que empezaste.
Cambia el estado del nodo Set Status a "approved" y ejecuta el flujo. Confirma que se activó la rama correcta.
Repite el proceso, pero esta vez cambia el estado a "rejected".

### Solution
> **Resource:** [ch2_ej2.json](./resources/ch2/ch2_ej2.json)

---

## Tareas de limpieza
El equipo de Acme Events está preparando un conjunto de datos para analizarlo y necesita tu ayuda para limpiarlo. Cada escenario describe una tarea común de limpieza de datos; decide si se resuelve mejor con un nodo Set o con un nodo Code.

### Instrucciones

Arrastra cada tarjeta de escenario a la categoría correcta: nodo Set o nodo Code.

### SOlución
- Node Set
    - Reformatear la fecha de registro a yyyy-MM-dd.
    - Recortar espacios y poner en minúsculas el email de un asistente antes de guardarlo.
- Node Code
    - Calcular la elegibilidad de descuento usando campos como earlyBird, loyaltyPoints y referral.
    - Limpiar los campos de nombre y email, y añadir un valor por defecto "ticketType = standard" si falta.

---

## Arregla datos de entrada desordenados
Comprobación inteligente
El equipo de Acme Events recopila datos de asistentes mediante formularios en línea, pero a menudo llegan con mayúsculas o espacios incoherentes. Vas a crear un flujo de trabajo que estandarice y limpie estos campos automáticamente.

### Instrucciones

Crea un nuevo flujo de trabajo y añade el nodo n8n Form al lienzo. Asegúrate de elegir la opción On new n8n Form event.

Abre el nodo y establece el Form Title en "Contact Us"
Añade la siguiente descripción del formulario: "Please enter your name and email"

---

Ahora toca añadir dos elementos nuevos al formulario en el nodo n8n Form.

Para el primer elemento usa esta información:
Field name: "Name"
Element Type: "Text"
Placeholder: "e.g. alice"
Para el segundo elemento usa esta información:
Field name: "Email"
Element Type: "Email"
Placeholder: "e.g. alice@example.com"
Asegúrate de marcar ambos elementos como Required Fields.

---

Vuelve al lienzo del flujo de trabajo y guarda el flujo.
Ejecuta el flujo y asegúrate de que aparece la ventana emergente del formulario.
Usando el texto de ejemplo del placeholder, introduce valores en los campos Name y Email que combinen mayúsculas y minúsculas. Por ejemplo:
Name: "ALice"
Email: "AliCE@EXample.com"
Envía tus entradas.

---

Los datos que introdujiste se han guardado correctamente y el flujo se ha ejecutado. Ahora, vamos a añadir un nodo para tratar entradas desordenadas del formulario.

Conecta un nodo Edit Fields (Set) al flujo.
En la sección Fields to Set, añade dos campos nuevos.
Para el primer campo, establece Field Name como "name_clean"; para el segundo, usa "email_clean".
En Values, arrastra el campo Name desde la sección Input al valor de "name_clean", y arrastra el campo Email al valor de "email_clean".
Quédate en el nodo Set Fields. Lo usarás de nuevo en el siguiente paso.

---

Al añadir nombres de campo, vemos que el valor es una expresión JSON. Podemos editar estos valores añadiendo a la expresión.

Dentro del valor del campo "name_clean", y después de la parte $json.Name, añade .toLowerCase().
El valor final de este campo debe ser {{ $json.Name.toLowerCase() }}
Haz lo mismo para el valor del campo "email_clean".
Si aparece un error, confirma que ambos campos (Name y Email) se capturaron correctamente en la sección Input antes de aplicar transformaciones.
Ejecuta el paso y comprueba en la sección Output si han cambiado las entradas del formulario.

### Solution
> **Resource:** [ch2_ej3.json](./resources/ch2/ch2_ej3.json)

---

## Fusiona conjuntos de datos sin complicaciones
Comprobación inteligente
El equipo de datos de Acme te ha pedido que fusiones los datos de registro con las confirmaciones de pago. Combinarás ambos conjuntos de datos usando el campo compartido userId para reconciliar los registros de asistentes.

### Instrucciones

En un flujo de trabajo nuevo, importa el archivo 2.2.4_merging.json desde la carpeta Resources/CH2 en el escritorio de la VM.

Ejecuta el flujo de trabajo e inspecciona la salida en tabla de ambos nodos Code.
Los nodos de código se usan para crear dos elementos cada uno, que representan dos registros de usuario y dos registros de pago, ambos con un campo userID en común.

> **Resource:** [2.2.4_merging.json](./resources/ch2/2.2.4_merging.json)

---

¡Hora de fusionar los conjuntos de datos!

Añade un nodo Merge al lienzo y conecta los dos nodos Code al nuevo nodo.
Asegúrate de que el nodo Create Two User Records esté conectado a Input 1 del nodo Merge, y el otro nodo Code esté conectado a Input 2.
Abre el nodo Merge para empezar la configuración.

---

En el nodo Merge, cambia la vista de la sección Input a Table para poder ver correctamente ambos nodos entrantes.
En Parameters, cambia Mode a "Combine" y asegúrate de que la opción Combine By esté en "Matching Fields".
Introduce userId en la sección Fields to Match. Distingue mayúsculas y minúsculas, así que asegúrate de que coincide con los datos vistos en la sección Input.
Ejecuta el flujo de trabajo.

---

Inspecciona la salida del nodo Merge después de ejecutar el flujo de trabajo.

Asegúrate de estar en modo Table para ver los dos elementos en formato de filas.
Deberías ver una tabla con cuatro columnas y dos filas.


### Solution
> **Resource:** [2.2.4_merging_solved](./resources/ch2/2.2.4_merging_solved.json)

---

## Pruebas vs. validación
El equipo de Soporte de Acme quiere asegurarse de que sus flujos de trabajo se ejecuten de forma fiable. Te han pedido que revises su proceso y decidas si cada acción es un paso de prueba o un paso de validación.

### Instrucciones

Arrastra cada enunciado al grupo correcto: Pruebas o Validación.

### Solución
- Pruebas
    - Prueba el paso de Slack para ver si se entrega un mensaje.
    - Detecta errores pronto aislando dónde se rompe el flujo de trabajo.
    - Ejecuta un único nodo con el botón Execute Node para inspeccionar su resultado.
- Validaciones
    - Comprueba que un campo de email contiene “@” antes de guardarlo.
    - Asegúrate de que el estado del pago coincide con el formato esperado.
    - Confirma que un campo de fecha sigue el formato YYYY-MM-DD.

---

## Prueba paso a paso
Comprobación inteligente
Gestionas un servicio interno de soporte IT. Se creó un flujo de trabajo para clasificar los tickets como urgentes o no según su prioridad. Si está marcado como "high", debe escalarse a un responsable. En caso contrario, se añade a la cola de soporte normal. Pero algo no funciona como debería. En el segundo nodo, la prioridad del mensaje es claramente alta, y aun así el flujo lo clasifica como normal. Tu tarea es probar y depurar el flujo paso a paso para averiguar por qué.

### Instrucciones

En un flujo de trabajo nuevo, importa el archivo 2.3.3_testing.json desde la carpeta Resources/CH2 en el escritorio de la VM.

Abre el nodo Set Message and Priority y ejecuta solo este paso.
Inspecciona la sección Output y los campos creados, confirmando que el campo priority está establecido en "high". Esto confirma la entrada del flujo antes de probar la condición If.

> **Resource:** [2.3.3_testing.json](./resources/ch2/2.3.3_testing.json)

---

Vuelve al lienzo del flujo de trabajo.

Abre el nodo If, ejecútalo y observa que la rama Normal (false) se activa, aunque el valor de entrada priority sea "high".

---

Parece que la rama del nodo Normal se activa continuamente en lugar de la rama del nodo Priority.

Revisa la configuración de los nodos del flujo e identifica dónde ocurre el error.
Cuando encuentres el problema, escribe tu explicación en la nota adhesiva verde de la derecha.
Haz clic en Save antes de Enviar tu respuesta.
Nota: Haz doble clic en la nota adhesiva verde para abrirla y editarla.

### Solution
> **Resource:** [2.3.3_testing_solved](./resources/ch2/2.3.3_testing_solved.json)

---

## Comprobar la exactitud de los datos
Comprobación inteligente
Estás creando un pequeño workflow para procesar nuevos registros de usuarios. El workflow genera varios registros, cada uno con nombre y dirección de email. Sin embargo, no todos los emails son válidos; a algunos les falta el símbolo "@".

Antes de enviar estos registros a otras partes del sistema, necesitas separar los emails válidos de los inválidos para no acabar creando cuentas defectuosas ni enviando mensajes al lugar equivocado. Vas a crear un flujo de validación que filtre las direcciones de email no válidas.

### Instrucciones

En un workflow nuevo, importa el archivo 2.3.4_validating.json desde la carpeta Resources/CH2 del escritorio de la VM.

Ejecuta el workflow para que se ejecuten el primer y el segundo nodo.
Revisa la salida del nodo Generate User Records y observa que ha generado ocho registros de usuario de ejemplo, con nombres y sus respectivos emails.

> **Resource:** [2.3.4_validating.json](./resources/ch2/2.3.4_validating.json)

---

Conecta el nodo Generate User Records con el nodo If y ábrelo para configurarlo.
Configura la condición para que solo los emails con un formato válido continúen hacia delante.
Piensa en qué debería incluir todo email. No cambies la regla condicional, es decir, contains, que ya está configurada.

---

Una vez que hayas añadido la lógica en el nodo If, ejecuta el nodo.
Observa los resultados en la sección Output y anota cuántos registros de email pasaron por cada salida de la rama.

---

De vuelta en la vista del lienzo del workflow, conecta la rama True al nodo Valid Records y la rama False al nodo Invalid Records.

Ejecuta todo el workflow e inspecciona los resultados.
Los nodos Edit Field (Set) que conectaste añadieron un campo de estado a las salidas. Comprueba que esos estados sean correctos.

### Solution
> **Resource:** [2.3.4_validating_solved](./resources/ch2/2.3.4_validating_solved.json)

---

## Gestión de errores
Has creado un flujo de trabajo que procesa pedidos de clientes desde Google Sheets y envía correos de confirmación. A veces faltan los correos en algunas filas, a veces falla el servicio de email y, en otras ocasiones, un flujo falla sin que te des cuenta. ¿Qué función de gestión de errores usarías en cada caso?

### Responder a la pregunta

**Respuestas posibles**
Selecciona una respuesta

- [x] Nodo Stop y Error
- [ ] Workflow con Error Trigger
- [ ] Continue on Fail
- [ ] Ninguna de las anteriores

---

## Generar mensajes de error personalizados
Comprobación inteligente
Acme Events procesa solicitudes de campaña con un campo budget. Datos no válidos, como presupuestos negativos o ausentes, pueden romper las automatizaciones y corromper el CRM de Acme.

En este ejercicio, validarás el campo budget para detectar datos erróneos cuanto antes. Después del nodo Code, añade un nodo If para comprobar si budget es menor que 0 O está vacío. Encamina los registros no válidos (rama false) a un nodo Stop and Error con un mensaje personalizado, garantizando que el flujo se detiene cuando los presupuestos no cumplen los criterios de Acme.

### Instrucciones

En un lienzo de flujo nuevo, importa el flujo 2.4.3_customer_errors desde la carpeta Resources/CH2 en el escritorio de la VM y ejecuta el flujo.

Conecta un nodo If al nodo Code y crea una regla condicional que diga:
si budget es menor que cero O está vacío
Ejecuta el paso y vuelve al lienzo del flujo.

> **Resource:** [2.4.3_customer_errors.json](./resources/ch2/2.4.3_customer_errors.json)

---

Deberías ver tres registros identificados por la rama false.

Conecta un nodo Stop and Error a la rama false del nodo If.
Edita el nodo para que el mensaje de error que aparezca sea:
"Invalid record - budget doesn't meet criteria"
Vuelve al lienzo del flujo y ejecuta el flujo.

---

Verás que aparece un mensaje de error.
Pero el mensaje de error está previsto, ya que muestra el texto que has añadido en el nodo Stop and Error.

### Solution
> **Resource:** [2.4.3_customer_errors_solved](./resources/ch2/2.4.3_customer_errors_solved.json)

---

## Crea un vigilante de flujos de trabajo
Comprobación inteligente
Acme Events depende de flujos de trabajo para la venta de entradas, confirmaciones y recordatorios. Si alguno falla, tienen que saberlo al momento para que las personas asistentes no se pierdan correos importantes.

Ahora vas a crear un flujo de trabajo global con Error Trigger para capturar y registrar cualquier error de flujo.

### Instrucciones

Crea un flujo de trabajo nuevo y renómbralo «Error Logger - Acme Events».

Ahora añade un nodo Error Trigger al lienzo. Este nodo se activará siempre que fallen los flujos vinculados a este flujo de trabajo.
Ejecuta el nodo recuperando un evento de prueba o ejecutando el flujo.
Observa el esquema de salida del nodo y luego vuelve al lienzo del flujo de trabajo.

---

Conecta el nodo Error Trigger a un nodo Edit Fields (Set).
Añade tres campos nuevos y configura los nombres así:
Campo 1: «Workflow Name»
Campo 2: «Execution URL»
Campo 3: «Error Message»
Para los valores de los campos, consulta la información del esquema en Input y arrastra los valores correspondientes según los nombres anteriores.
Ejecuta el nodo y revisa el Output de cada campo.

---

Ahora vamos a imprimir los errores como registros.

Conecta un nodo Convert to File al final del flujo y elige la opción Convert to HTML.
Elimina cualquier contenido ya presente en la sección Put Output File in Field y arrastra los campos desde el nodo Edit Fields (Set) en la sección Input hacia la sección Put Output File in Field.
Pon cada expresión en una línea nueva dentro de la sección Put Output File in Field.
Ejecuta el nodo y descarga el archivo de salida desde la sección Output.
Ahora puedes abrir el archivo HTML en una nueva pestaña del navegador y ver el resultado.

---

Para que tu flujo Error Logger capture realmente los fallos, tienes que vincularlo al flujo que quieras monitorizar.

Guarda el flujo y vuelve a la página general.
Crea un flujo de trabajo nuevo y renómbralo «SAMPLE WORKFLOW».
Vamos a crear una plantilla de flujo añadiendo un disparador manual, un nodo Edit Fields (Set) y un nodo de error.

---

Ve a los Settings del flujo usando el menú de tres puntos en la esquina superior derecha.
En la sección Error Workflow, selecciona la opción Error Logger - Acme Events y guarda los cambios de la configuración.
Guarda el flujo.
A partir de ahora, cuando este flujo encuentre un error, los detalles se enviarán al flujo Error Logger- Acme Events.

### Solution
> **Resources:** 
- [ch2_ej8_p1.json](./resources/ch2/ch2_ej8_p1.json)
- [ch2_ej8_p2.json](./resources/ch2/ch2_ej8_p2.json)
