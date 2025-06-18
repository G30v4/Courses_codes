fun main(args: Array<String>) {

    /*** WHEN ***/
    println("Ingresa año de nnacimiento")
    val año = readLine()!!.toInt()

    val generacion = when {
        año >= 1946 && año <= 1964 -> "Baby Boomer"
        año >= 1965 && año <= 1980 -> "Generación X"
        else -> "Sin generación"
    }
    println(generacion)

    // alternative
    val generacion2 = when(año) {
        1946,1964 -> "Baby Boomer" // solo esos dos años
        in 1965..1980 -> "Generación X"
        in 1981..1996 -> "Generación X"
        else -> "Sin generación"
    }

    println(generacion2)

    /*** FOR ***/
    for(i in 1.rangeTo(10)) {println("Hello!! $i")} // rango
    for(i in 1 until 10) {println("Hello!! $i")} // hasta el 9
    for(i in 2..10 step 2) println("Hello!! $i") // con saltos
    for(i in 10 downTo 1 step 2) {println("Hello!! $i")} // reverso
        

    // con Listas
    val diasSemana: List<String> = listOf("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
    for(i in 0..6) {println(diasSemana[i])}
    for(i in 6 downTo 0) {println(diasSemana[i])}

    val calificaciones: List<Int> = listOf(10,8,9,5,8)
    var suma = 0
    for(i in 0..4){suma += calificaciones[i]}
    val promedio = suma/calificaciones.size
    println(promedio)
    
    // alternativa
    suma = 0
    for(c in calificaciones) {suma += c}
    val promedio = suma/calificaciones.size
    println(promedio)

    /*** CONTROL DE FLUJO ***/
    val numeros = listOf(1,5,7,10,8,9,5,8,4,6,2,5)
    var s = 0
    for(n in numeros){
        if(n %2 == 0) {break}
        s += n
    }
    println(s)

    /*** EXCEPCIONES ***/
    do {
        try{
            var numero1: Int
            var numero2: Int
            println("Ingresa un numero: ")
            numero1 = readLine()!!.toInt()
            println("Ingresa otro numero: ")
            numero2 = readLine()!!.toInt()
            val res = numero1 / numero2
            print(res)
            break
        }catch(e: NumberFormatException){
            println("Coloca un valor numerico")
        }catch(e: ArithmeticException){
            println("No se puede dividir por cero")
        }
    } while (true)
    
}