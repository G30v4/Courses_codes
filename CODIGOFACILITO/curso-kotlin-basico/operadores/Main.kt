fun main(args: Array<String>) {

    // operadores null safe
    var nombre: String = "Marines"

    var apellido: String? = null
    println(apellido)
    apellido = apellido ?: "Default value" // evitar nulos
    println(apellido)

    var title: String? = "My title" // try with null
    // var tamaño: Int? = title!!.length // si o si requiere un valor
    var tamaño: Int? = title?.length // evitar el nulo de lengh si es nulo
    println(tamaño)

}