# Chapter 1

- The LangChain ecosystem
- Prompt templates
- Few-shot prompting

---

## Modelos OpenAI en LangChain
Los modelos de la serie GPT de OpenAI son algunos de los LLM con mejor rendimiento que existen. Están disponibles a través de la API de OpenAI, con la que puedes interactuar fácilmente utilizando LangChain.

Normalmente, el uso de los modelos de OpenAI requeriría una clave API personal que se utiliza para facturar el coste de los modelos. En este curso, no hace falta crear ni proporcionar una clave API de OpenAI. El marcador de posición "<OPENAI_API_TOKEN>" enviará solicitudes válidas a la API. Si realizas un gran número de solicitudes en un breve periodo de tiempo, es posible que se produzca el error «RateLimitError». Si lo ves, haz una pausa por un momento y vuelve a intentarlo.

La clase ChatOpenAI ya se ha importado.

### Instrucciones
Define un modelo de chat OpenAI utilizando una clase LangChain; deja el marcador de posición de la clave API tal y como está.
Invoca el LLM que has definido para responder a la pregunta «prompt» (aquí puedes probar otros prompts).

### Solución
```py
# Define the LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>")

# Predict the words following the text in question
prompt = 'Three reasons for using LangChain for LLM application development.'
response = llm.invoke(prompt)

print(response.content)
```

---

## Modelos Hugging Face en LangChain
Hay miles de modelos disponibles para descargar y utilizar gratuitamente en Hugging Face. Hugging Face se integra muy bien en LangChain a través de su biblioteca asociada, langchain-huggingface, que está disponible para su uso.

En este ejercicio, cargarás y llamarás al modelo «crumb/nano-mistral» de Hugging Face. Se trata de un LLM ultraligero diseñado para ajustarse con precisión y ofrecer un mayor rendimiento.

### Instrucciones

Importa la clase para definir las canalizaciones de Hugging Face en LangChain.
Define un LLM de generación de texto utilizando el ID de modelo 'crumb/nano-mistral' de Hugging Face.
Utiliza llm para predecir las siguientes palabras después del texto en prompt

### Solución
```py
# Import the class for defining Hugging Face pipelines
from langchain_huggingface import HuggingFacePipeline

# Define the LLM from the Hugging Face model ID
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20}
)

prompt = "Hugging Face is"

# Invoke the model
response = llm.invoke(prompt)
print(response)
```

---

## Plantillas de prompt y cadenas
En este ejercicio, comenzarás a utilizar dos de los componentes básicos de LangChain: las plantillas de prompts y las cadenas.

Las clases necesarias para completar este ejercicio, incluida ChatOpenAI, ya se han cargado previamente para ti.

### Instrucciones

Convierte el texto «template» proporcionado en una plantilla de prompt estándar (que no sea de chat).
Crea una cadena para pasar la plantilla de prompt al LLM.
Invoca la cadena en la variable question proporcionada.


### Solución
```py
# Create a prompt template from the template string
template = "You are an artificial intelligence assistant, answer the question. {question}"
prompt = PromptTemplate.from_template(
    template=template
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')	

# Create a chain to integrate the prompt template and LLM
llm_chain = prompt | llm

# Invoke the chain on the question
question = "How does LangChain make LLM application development easier?"
print(llm_chain.invoke({"question": question}))
```

---


## Plantillas de prompts de chat
Dada la importancia de los modelos de chat en muchas aplicaciones LLM, LangChain proporciona funcionalidad para crear plantillas de prompts rápidos con el fin de estructurar mensajes para diferentes roles de chat.

La clase ChatPromptTemplate ya se ha importado y ya se ha definido un LLM.

### Instrucciones

Asigna las funciones adecuadas a los mensajes proporcionados y conviértelos en una plantilla de prompts de chat.
Crea una cadena LCEL y llámala con la entrada proporcionada.

### Solución
```py
llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

# Create a chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a geography expert that returns the colors present in a country's flag."),
        ("human", "France"),
        ("ai", "blue, white, red"),
        ("human", "{country}")
    ]
)

# Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm

country = "Japan"
response = llm_chain.invoke({"country": country})
print(response.content)
```

---


## Creación del conjunto de ejemplos con pocos disparos
PromptTemplate ChatPromptTemplate son excelentes para integrar variables, pero tienen dificultades para integrar conjuntos de datos que contienen muchos ejemplos. Aquí es donde entra en juego FewShotPromptTemplate. En este ejercicio, crearás un conjunto de datos, en forma de lista de diccionarios, que contendrá los siguientes pares de preguntas y respuestas.

Pregunta: How many DataCamp courses has Jack completed?
Respuesta: 36
Pregunta: How much XP does Jack have on DataCamp?
Respuesta: 284,320XP
Pregunta: What technology does Jack learn about most on DataCamp?
Respuesta: Python
En el siguiente ejercicio, convertirás esta información en una plantilla de prompt de pocos disparos.

### Instrucciones

Crea una lista de diccionarios para las preguntas y respuestas proporcionadas, con las claves "question" y "answer".


### Solución
```py
# Create the examples list of dicts
examples = [
  {
    "question": "How many DataCamp courses has Jack completed?",
    "answer": "36"
  },
  {
    "question": "How much XP does Jack have on DataCamp?",
    "answer": "284,320XP"
  },
  {
    "question": "What technology does Jack learn about most on DataCamp?",
    "answer": "Python"
  }
]
```

---


## Creación de la plantilla de prompt de pocos disparos
Con tus ejemplos en un formato estructurado, ya es hora de crear la plantilla de prompt de pocos ejemplos. Crearás una plantilla que convierta los pares pregunta-respuesta al siguiente formato:

Question: Example question
Example Answer
Todas las clases de LangChain necesarias para completar este ejercicio ya están precargadas.

### Instrucciones

Completa el prompt para dar formato a las respuestas de modo que incluyan las claves question y answer.
Crea el prompt de pocos disparos utilizando examples y example_prompt; completa la lista de variables de entrada según el sufijo proporcionado.


### Solución
```py
# Complete the prompt for formatting answers
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

# Create the few-shot prompt
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

prompt = prompt_template.invoke({"input": "What is Jack's favorite technology on DataCamp?"})
print(prompt.text)
```

---


## Implementación de prompts de pocos disparos
Es hora de combinar tus componentes en una cadena. El prompt de pocos disparos que creaste en el ejercicio anterior sigue estando disponible para que lo utilices, junto con examples y example_prompt.

Todas las clases de LangChain necesarias para completar este ejercicio ya están precargadas.

### Instrucciones

Instancia un LLM de chat de OpenAI.
Crea una cadena a partir del LLM y la plantilla de prompt, y ejecútala en la entrada proporcionada.


### Solución
```py
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

# Create an OpenAI chat LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

# Create and invoke the chain
llm_chain = prompt_template | llm
print(llm_chain.invoke({"input": "What is Jack's favorite technology on DataCamp?"}))
```