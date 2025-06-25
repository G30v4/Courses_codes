# Notes

## Commands utils
```bash
# Try code in console
java -cp . fileName
```

# Exercises

## Project 1
```java
/*
Mostrar un menu con tres opciones:
- Agregar tarea
- Ver tareas (placeholder)
- Salir

Req:
- Leer la opcion del usuario con Scanner
- Verificar que la opción ingresada sea valida
- Solicitar el nombre de la tarea y su prioridad
- Hacer una operación con esa prioridad
*/
```

> Solution: [TaskManagerEj1.java](./src/TaskManagerEj1.java)

> Execute: ```java -cp . TaskManagerEj1.java```


## Project 2
```java
/*
- Repetir el menú mientras el usuario no elija salir
- Usar condicionales y ciclos para manjero opciones del menu

Req:
- Validar prioridad
- Elegir opción segun opción del menu
- Repetir el menú hasta que se elija salir
*/
```

> Solution: [TaskManagerEj2.java](./src/TaskManagerEj2.java)

> Execute: ```java -cp . TaskManagerEj2.java```


## Project 3
```java
/*
- Separar las acciones del menú en métodos reutilizables
- Aplicar conceptos sobre parámetros, retorno y scope

Req:
- Métodos simples
- Parámetros y retorno
- Scope de variables
*/
```

> Solution: [TaskManagerEj3.java](./src/TaskManagerEj3.java)

> Execute: ```java -cp . TaskManagerEj3.java```


## Project 4
```java
/*
- Transformar un programa estructurado en un de POO
- Aplicar los pilares de la POO

Req:
- Encapsulamiento de atributos privados, uso de getters/setters
- Tarea hereda de Actividad
- Aplicar polimorfirmo en el metodo ejecutar()
- Crear constructor personalizado
- Mantenr la logica y estructura del código
*/
```

> Solution: [TaskManager.java](./src/ej4/TaskManager.java)

> Execute: ```javac *.java && java TaskManager && rm -rf *.class```


## Project 5
```java
/*
- Gestion de tareas con ArrayList
- Acceso por ID usando HashMap

Req:
- Uso de herencia, encapsulamiento y polimorfismo
- Realizar operaciones con for-each, get(), remove()
*/
```

> Solution: [TaskManager.java](./src/ej5/TaskManager.java)

> Execute: ```javac *.java && java TaskManager && rm -rf *.class```


## Project 6
```java
/*
- Mejoras modernas con tipos de datos inferidos
- Uso de lambda para listarr tareas
- COdigo limpio aplicando buenas practicas y metodos reutilizables

Req:
- Usar var para tipos inferidos
- Hacer uso de .forEach() con lambdas
- Añadir comentarios
*/
```

> Solution: [TaskManager.java](./src/ej6/TaskManager.java)

> Execute: ```javac *.java && java TaskManagerAdvance && rm -rf *.class```