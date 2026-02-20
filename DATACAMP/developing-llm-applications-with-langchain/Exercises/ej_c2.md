# Chapter 2

- Sequential chains
- Introduction to LangChain agents
- Custom tools for agents

---

## Creación de prompts para cadenas secuenciales
En los siguientes ejercicios, trabajarás para crear un sistema que ayude a las personas a aprender nuevas habilidades. Este sistema debe construirse de forma secuencial, de modo que los alumnos puedan modificar los planes en función de sus preferencias y limitaciones. Utilizarás tus habilidades en LangChain LCEL para crear una cadena secuencial con la que construir este sistema, y el primer paso será diseñar las plantillas de prompts que utilizará el sistema.

### Instrucciones

Crea una plantilla de prompt llamada «learning_prompt» que tome como entrada «"activity"» y cree un plan de aprendizaje.
Crea una plantilla de prompt llamada «time_prompt» que tome como entrada «"learning_plan"» y la modifique para que quepa en una semana.
Llama al «learning_prompt» con una actividad de tu elección (prueba con «"play golf"» si no se te ocurre nada).


### Solución
```py
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

# Create a prompt template that places a time constraint on the output
time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}."
)

# Invoke the learning_prompt with an activity
print(learning_prompt.invoke({"activity": "learn Quantum Security"}))
```

---


## Cadenas secuenciales con LCEL
Una vez creadas las plantillas de prompts, es hora de unir todo, incluido el LLM, utilizando cadenas y LCEL. Ya se ha definido una interfaz de usuario (llm) que utiliza el modelo gpt-4o-mini de OpenAI.

Para el último paso de llamar a la cadena, siéntete libre de insertar cualquier actividad que desees. Si te cuesta encontrar ideas, prueba a introducir «"play the harmonica"».

### Instrucciones

Crea una cadena secuencial utilizando LCEL que pase learning_prompt al llm y envíe la salida a time_prompt para reenviarla al llm.
Llama a la cadena con la actividad que prefieras.


### Solución
```py
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a concise plan to help me hit this goal: {learning_plan}."
)

# Complete the sequential chain with LCEL
seq_chain = ({"learning_plan": learning_prompt | llm | StrOutputParser()}
    | time_prompt
    | llm
    | StrOutputParser())

# Call the chain
print(seq_chain.invoke({"activity": "create biotech models"}))
```

### result example
```md

**One-Week Plan for Hitting Your Biotech Modeling Goal**

### Day 1: Build a Strong Foundation in Relevant Sciences
- **Morning**: Study key concepts in **Basic Biology**. Focus on cell biology and molecular biology.
  - Resource: "Molecular Biology of the Cell" (Chapters 1-3)
  
- **Afternoon**: Dive into **Biochemistry** fundamentals, focusing on proteins and metabolic pathways.
  - Resource: "Lehninger Principles of Biochemistry" (Chapters 1-2)

- **Evening**: Watch online introductory videos on **genetics** (Khan Academy).

### Day 2: Mathematics and Statistics
- **Morning**: Study basic **Calculus** and **Linear Algebra**.
  - Resource: Khan Academy Calculus sections.
  
- **Afternoon**: Take a course on **Statistics for Data Scientists**.
  - Resource: Read the first few chapters of “Statistics for Scientists” by Pevsner.

- **Evening**: Solve practice problems on statistics and mathematical concepts relevant to biology.

### Day 3: Learn Programming Skills
- **Morning**: Start learning **Python** (a language widely used in biotech).
  - Resource: Codecademy Python Course (complete the introduction and first few modules).

- **Afternoon**: Study **data analysis** using Python libraries like Pandas and NumPy.
  - Resource: Watch tutorials on data analysis with Python.

- **Evening**: Practice coding by manipulating sample biological datasets.

### Day 4: Understanding Bioinformatics and Computational Biology
- **Morning**: Take a concise online course on **Bioinformatics** methods.
  - Resource: Coursera Bioinformatics Specialization (focus on the first module).

- **Afternoon**: Read about modeling biological systems and familiarize yourself with COPASI software.
  - Resource: "Mathematical Models in Biology".

- **Evening**: Download and explore COPASI through sample models.

### Day 5: Specialize in Specific Areas
- **Morning**: Explore **Synthetic Biology** or **Pharmaceutical Modeling** based on your interest.
  - Resource: For Synthetic Biology, read “Synthetic Biology: A Primer”. For Pharma Modeling, read “Molecular Modelling: Principles and Applications”.

- **Afternoon**: Research current projects in synthetic biology or drug design.
  
- **Evening**: Identify and list potential projects or areas you would like to explore further.

### Day 6: Practical Application and Projects
- **Morning**: Plan a small hands-on project using programming skills. 
  - Example: Analyze a dataset from a public bioinformatics repository.

- **Afternoon**: Join an online biotech community or a forum. 
  - Engage with questions on software you’ve learned (e.g., COPASI).

- **Evening**: Participate in a relevant online competition or project (like Kaggle).

### Day 7: Stay Updated, Network, and Reflect
- **Morning**: Read articles from journals like **Nature Biotechnology** or **Bioinformatics**.
  
- **Afternoon**: Identify and join professional organizations related to biotechnology.

- **Evening**: Reflect on the week's learnings, identify strengths and areas to improve, and outline your next steps for further education or project ideas.

### Final Tips
- **Stay Persistent**: Dedicate focused time each day to this learning without distractions.
- **Engage with The Community**: Don’t hesitate to ask questions and share your knowledge.
- **Keep Learning**: This week is just the beginning; use it as a stepping stone for continuous progress. 

By following this week-long structured plan, you'll lay a solid foundation for future deep dives into biotech modeling. Good luck!
```

---


## Agentes ReAct
Es hora de intentar crear tu propio agente ReAct. Recordemos que ReAct significa «razonar y actuar», lo que describe cómo toman las decisiones. En este ejercicio, cargarás la herramienta integrada «wikipedia» para integrar datos externos de Wikipedia con tu LLM. Ya se ha definido una interfaz de usuario (llm) que utiliza el modelo gpt-4o-mini de OpenAI.

Nota: La herramienta wikipedia requiere que la biblioteca Python wikipedia esté instalada como dependencia, lo cual ya se ha hecho por ti en este caso.

### Instrucciones

Carga la herramienta «"wikipedia"».
Define un agente ReAct y pásale el llm y las herramientas que se van a utilizar.
Ejecuta el agente en la entrada proporcionada e imprime el contenido del mensaje final en response.



### Solución
```py
# Define the tools
tools = load_tools(["wikipedia"])

# Define the agent
agent = create_react_agent(llm, tools)

# Invoke the agent
response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})
print(response)
```

---


## Definición de una función para el uso de herramientas
Trabajas para una empresa de SaaS (software como servicio) con grandes objetivos para implementar herramientas que ayuden a los empleados de todos los niveles de la organización a tomar decisiones basadas en datos. Estás creando una prueba de concepto para una aplicación que permite a los gestores de éxito de clientes interactuar con los datos de la empresa utilizando lenguaje natural para recuperar datos importantes de los clientes.

Se te ha proporcionado un DataFrame de pandas llamado «customers» que contiene una pequeña muestra de datos de clientes. Tu primer paso en este proyecto es definir una función Python para extraer información de esta tabla dado el nombre de un cliente. pandas ya se ha importado como pd.

### Instrucciones

Define una función retrieve_customer_info() que tome un argumento de cadena, name.
Filtra el DataFrame «customers» para devolver las filas con «"name"» igual al argumento de entrada, «name».
Llama a la función con el nombre del cliente, "Peak Performance Co.".


### Solución
```py
# Define a function to retrieve customer info by-name
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    # Filter customers for the customer's name
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Call the function on Peak Performance Co.
print(retrieve_customer_info("Peak Performance Co."))
```

---


## Creación de herramientas personalizadas
Ahora que ya tienes una función para extraer datos de clientes del DataFrame «customers», es hora de convertir esta función en una herramienta compatible con los agentes LangChain.

### Instrucciones

Modifica la función proporcionada para que pueda utilizarse como herramienta.
Imprime los argumentos de la herramienta utilizando un atributo de herramienta.


### Solución
```py
# Convert the retrieve_customer_info function into a tool
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Print the tool's arguments
print(retrieve_customer_info.args)
```

---


## Integración de herramientas personalizadas con agentes
Ahora que ya tienes tus herramientas a mano, ¡es hora de configurar tu flujo de trabajo de agente! Volverás a utilizar un agente ReAct, que, como recordarás, razona sobre los pasos que debe seguir y selecciona las herramientas utilizando este contexto y las descripciones de las herramientas. Ya se ha definido una interfaz de usuario (llm) que utiliza el modelo gpt-4o-mini de OpenAI.

### Instrucciones

Crea un agente ReAct utilizando tu herramienta retrieve_customer_info y el archivo llm proporcionado.
Invoca el agente en la entrada proporcionada e imprime el contenido del mensaje final en messages.


### Solución
```py
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()

# Create a ReAct agent
agent = create_react_agent(llm, [retrieve_customer_info])

# Invoke the agent on the input
messages = agent.invoke({"messages": [("human", "Create a summary of our customer: Peak Performance Co.")]})
print(messages['messages'][-1].content)
```