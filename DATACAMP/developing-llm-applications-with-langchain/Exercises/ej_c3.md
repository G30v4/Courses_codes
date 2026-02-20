# Chapter 3

- Integración de cargadores de documentos
- División de datos externos para su recuperación
- Almacenamiento y recuperación RAG mediante bases de datos vectoriales

---

## Cargadores de documentos PDF
Para empezar a implementar la generación aumentada por recuperación (RAG), primero tendrás que cargar los documentos a los que accederá el modelo. Estos documentos pueden provenir de diversas fuentes, y LangChain admite cargadores de documentos para muchas de ellas.

En este ejercicio, utilizarás un cargador de documentos para cargar un documento PDF que contiene el artículo RAG VS Fine-Tuning: Pipelines, Tradeoffs, and a Case Study on Agriculture de Balaguer et al. (2024).

Nota: pypdf, una dependencia para cargar documentos PDF en LangChain, ya se ha instalado por ti.

### Instrucciones

Importa la clase adecuada para cargar documentos PDF en LangChain.
Crea un cargador de documentos para el documento 'rag_vs_fine_tuning.pdf', que está disponible en el directorio actual.
Carga el documento en la memoria para ver el contenido del primer documento o página.


### Solución
```py
# Import library
from langchain_community.document_loaders import PyPDFLoader

# Create a document loader for rag_vs_fine_tuning.pdf
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')

# Load the document
data = loader.load()
print(data[0])
```

---


## Cargadores de documentos CSV
Los archivos de valores separados por comas (CSV) son un formato de archivo muy común, especialmente en campos relacionados con los datos. Afortunadamente, LangChain proporciona diferentes cargadores de documentos para diferentes formatos, y con casi toda la sintaxis igual.

En este ejercicio, utilizarás un cargador de documentos para cargar un archivo CSV que contiene datos sobre la audiencia internacional de la Copa Mundial de la FIFA. Si te interesa el análisis completo de estos datos, consulta Cómo romper la FIFA.

### Instrucciones

Importa la clase adecuada para cargar documentos CSV en LangChain.
Crea un cargador de documentos para el documento 'fifa_countries_audience.csv', que está disponible en el directorio actual.
Carga los documentos en la memoria para ver el contenido del primer documento.


### Solución
```py
# Import library
from langchain_community.document_loaders.csv_loader import CSVLoader

# Create a document loader for fifa_countries_audience.csv
loader = CSVLoader('fifa_countries_audience.csv')

# Load the document
data = loader.load()
print(data[0])
```

---


## Cargadores de documentos HTML
Es posible cargar documentos de muchos formatos diferentes, incluidos formatos complejos como HTML.

En este ejercicio, cargarás un archivo HTML que contiene una orden ejecutiva de la Casa Blanca.

### Instrucciones

Utiliza la clase UnstructuredHTMLLoader para cargar el archivo white_house_executive_order_nov_2023.html en el directorio actual.
Carga los documentos en la memoria.
Imprime el primer documento.
Imprime los metadatos del primer documento.


### Solución
```py
from langchain_community.document_loaders import UnstructuredHTMLLoader

# Create a document loader for unstructured HTML
loader = UnstructuredHTMLLoader('white_house_executive_order_nov_2023.html')

# Load the document
data = loader.load()

# Print the first document
print(data[0])

# Print the first document's metadata
print(data[0].metadata)
```

---


## División por caracteres
Un proceso clave en la implementación de la generación aumentada por recuperación (RAG) es dividir los documentos en fragmentos para almacenarlos en una base de datos vectorial.

Hay varias estrategias de división disponibles en LangChain, algunas con rutinas más complejas que otras. En este ejercicio, implementarás un divisor de texto por caracteres, que divide los documentos en función de los caracteres y mide la longitud de los fragmentos por el número de caracteres.

Recuerda que no existe una estrategia de división ideal, es posible que tengas que probar varias hasta encontrar la más adecuada para tu caso concreto.

### Instrucciones

Importa la clase LangChain adecuada para dividir un documento por caracteres.
Define un separador de caracteres que divida en "\n" con un chunk_size de 24 y chunk_overlap de 10.
Divide quote e imprime los fragmentos y sus longitudes.


### Solución
```py
# Import the character splitter
from langchain_text_splitters import CharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

# Split the string and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])
```

---


## División recursiva por caracteres
Muchos programadores utilizan un divisor de caracteres recursivo para dividir documentos basándose en una lista específica de caracteres. Estos caracteres son párrafos, saltos de línea, espacios y cadenas vacías, por defecto: ["\n\n", "\n", " ", ""].

En la práctica, el divisor intenta dividir por párrafos, comprueba si se cumplen los valores chunk_size y chunk_overlap y, si no es así, divide por frases, luego por palabras y, por último, por caracteres individuales.

A menudo, tendrás que probar diferentes valores de chunk_size y chunk_overlap para encontrar los que mejor se adapten a tus documentos.

### Instrucciones

Importa la clase LangChain adecuada para dividir un documento de forma recursiva por caracteres.
Define un divisor de caracteres recursivo para dividir los caracteres "\n", " " y "" (en ese orden) con un chunk_size de 24 y un chunk_overlap de 10.
Divide quote e imprime los fragmentos y sus longitudes.


### Solución
```py
# Import the recursive character splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = RecursiveCharacterTextSplitter(
    separators=["\n", " ", ""],
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

# Split the document and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])
```

---


## Dividir HTML
En este ejercicio, dividirás un archivo HTML que contiene una orden ejecutiva sobre IA creada por la Casa Blanca de Estados Unidos en octubre de 2023. Para conservar el máximo contexto posible en los fragmentos, dividirás utilizando valores más grandes para chunk_size y chunk_overlap.

Todas las clases de LangChain necesarias para completar este ejercicio ya están precargadas.

### Instrucciones

Crea un cargador de documentos para white_house_executive_order_nov_2023.html y cárgalo en la memoria.
Establece un chunk_size de 300 y un chunk_overlap de 100.
Define el divisor, divide por el carácter «'.'» y utilízalo para dividir «data» e imprimir los fragmentos.


### Solución
```py
# Load the HTML document into memory
loader = UnstructuredHTMLLoader('white_house_executive_order_nov_2023.html')
data = loader.load()

# Define variables
chunk_size = 300
chunk_overlap = 100

# Split the HTML
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators=['.'])

docs = splitter.split_documents(data)
print(docs)
```

---


## Preparación de los documentos y la base de datos vectorial
En los siguientes ejercicios, crearás un flujo de trabajo RAG completo para mantener una conversación con un documento PDF que contiene el artículo RAG VS Fine-Tuning: Pipelines, Tradeoffs, and a Case Study on Agriculture_ de Balaguer et al. (2024). Esto funciona dividiendo los documentos en fragmentos, almacenándolos en una base de datos vectorial, definiendo un prompt para conectar los documentos recuperados y la entrada del usuario y creando una cadena de recuperación para que el LLM acceda a estos datos externos.

En este ejercicio, prepararás el documento para su almacenamiento y lo incorporarás a una base de datos vectorial Chroma. Utilizarás un RecursiveCharacterTextSplitter para dividir el PDF en fragmentos y los incorporarás a una base de datos vectorial Chroma utilizando una función de incrustaciones de OpenAI. Al igual que con el resto del curso, no es necesario que proporciones tu propia clave API de OpenAI.

Las siguientes clases ya se han importado por ti: RecursiveCharacterTextSplitter, Chroma y OpenAIEmbeddings.

### Instrucciones

Divide los documentos en data utilizando un divisor de caracteres recursivo con un chunk_size de 300 y chunk_overlap de 50; omite el argumento separators, ya que el valor predeterminado es ["\n\n", "\n", " ", ""].
Define un modelo de incrustaciones de OpenAI utilizando el marcador de posición <OPENAI_API_TOKEN> proporcionado y utilízalo para incrustar e incorporar los documentos en una base de datos Chroma.
Configura vectorstore como un objeto recuperador que devuelve los tres documentos principales para su uso en la cadena RAG final.


### Solución
```py
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

# Split the document using RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=300,
    chunk_overlap=50
)
docs = splitter.split_documents(data) 

# Embed the documents in a persistent Chroma vector database
embedding_function = OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small')
vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding_function,
    persist_directory=os.getcwd()
)

# Configure the vector store as a retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)
```

---


## Creación de una plantilla de prompt de recuperación
Ahora que tus documentos se han incorporado a la base de datos vectorial y están listos para su recuperación, deberás diseñar una plantilla de prompts de chat para combinar los fragmentos de documentos recuperados con la pregunta introducida por el usuario.

Ya se ha proporcionado la estructura general del prompt; tu objetivo es insertar los marcadores de posición de las variables de entrada correctas en la cadena «message» y convertir la cadena en una plantilla de prompt de chat.

### Instrucciones

Completa la cadena de mensaje para añadir un marcador de posición para la inserción dinámica de los documentos recuperados, denominado «context», y la pregunta que debe responder el usuario, «question».
Crea una plantilla de prompt de chat desde message.


### Solución
```py
# Add placeholders to the message string
message = """
Answer the following question using the context provided:

Context:
{context}

Question:
{question}

Answer:
"""

# Create a chat prompt template from the message string
prompt_template = ChatPromptTemplate.from_messages([("human", message)])
```

---


## Creación de una cadena RAG
Ahora vamos a reunir todos los componentes en tu flujo de trabajo RAG. Has preparado los documentos y los has introducido en una base de datos Chroma para su recuperación. Has creado una plantilla de prompt para incluir los fragmentos extraídos del artículo académico y responder a las preguntas.

La plantilla de prompt que creaste en el ejercicio anterior está disponible como prompt_template, se ha inicializado un modelo OpenAI como llm y se ha incluido en el script el código para recrear tu retriever.

### Instrucciones

Crea una cadena LCEL para vincular retriever, prompt_template y llm de modo que el modelo pueda recuperar los documentos.
Invoca la cadena en el 'question' proporcionado.


### Solución
```py
vectorstore = Chroma.from_documents(
    docs,
    embedding=OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small'),
    persist_directory=os.getcwd()
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Create a chain to link retriever, prompt_template, and llm
rag_chain = ({"context": retriever, "question": RunnablePassthrough()}
            | prompt_template
            | llm)

# Invoke the chain
response = rag_chain.invoke("Which popular LLMs were considered in the paper?")
print(response.content)
```