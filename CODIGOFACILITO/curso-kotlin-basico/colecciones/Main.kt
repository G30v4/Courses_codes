fun main(args: Array<String>) {


    /*** Arreglos ***/
    val alumnos = arrayOf<String>("Maria", "Jose", "Laura", "pedro")
    println("Hola " + alumnos[0]) // index

    //Remplazar
    alumnos[1] = "David"
    println(alumnos[1])

    /*** Listas ***/
    // lista inmutable
    val frutas = listOf("Manzanas", "Bananas", "Limones")
    println(frutas[1])
    //frutas[1] = "Mangos" // No permitido, genera error

    val profesores = mutableListOf<String>("Miarines", "Eduardo", "Uriel", "Carlos")
    val calificaciones = mutableListOf<Int>(1,3,5,6,8,10,9)
    
    // Ordenamiento
    val ascendente = profesores.sorted()
    val descendente = calificaciones.sortedDescending()
    println(ascendente)
    println(descendente)

    // filtrado
    val filtrado = calificaciones.filter {x -> x > 5}
    println(filtrado)


    /*** Sets ***/
    val setA = setOf(3,8,1,6,10,6,18,20,3)
    val setB = setOf(12,8,1,6,7,16,34,3)
    println(setA.elementAt(6))

    // interseccion
    val interseccion = setA.intersect(setB)
    println(interseccion)

    // union
    val union = setA.union(setB)
    println(union)

    // Set Mutable
    val setC = mutableSetOf(12,4,67,3,6,7,9)
    setC.add(40)
    setC.remove(7)

    // sustracción
    val sustraer = setA.subtract(setB)
    println(sustraer)

    // otros metodos
    println(sustraer.count())
    println(sustraer.sum())
    println(sustraer.average())

    /*** Maps ***/
    val datos = mapOf(
        "Nombre" to "Maria",
        "Apellido" to "Mendez"
        )
    println(datos["Apellido"])

    // Mutable Map
    val datos2 = mutableMapOf(
        "Nombre" to "Jhon",
        "Apellido" to "Jones"
    )

    // Acciones
    datos2["Nombre"] = "Juan" //Actualizar
    println(datos2)
    datos2.remove("Nombre") // Eliminar
    println(datos2)
    datos2["Edad"] = "20" // Agregar, solo string
    println(datos2)

    // alterntiva
    val datos3 = mutableMapOf(
        Pair("uno", 1),
        Pair("dos", 2)
    )
    println(datos3["dos"])

}