fun main(args: Array<String>) {
    fun obtenerEdad() {
        val edad = 2024 - 1994
        println("Mi edad es: $edad")
    }

    fun suma() {
        val resultado = 100 + 200
        println("EL resultado de la suma es $resultado")
    }

    obtenerEdad()
    suma()

    /*** PARAMETROS Y ARGUMENTOS ***/
    
    fun obtenerDescuento(descuento:Double, total:Double) {
        val cantidadDescuento = total * (descuento/100)
        val totalConDescuento = total - cantidadDescuento
        println("Tienes $descuento% de descuento!!")
        println("Total a pagar: $totalConDescuento")
    }

    println("Ingresa el descuento")
    val descuento = readLine()!!.toDouble()
    println("Ingresa el total")
    val total = readLine()!!.toDouble()
    obtenerDescuento(descuento, total)

    fun obtenerEdad2(añoNacimiento: Int, añoActual: Int = 2025) {
        val edad = añoActual - añoNacimiento
        println("Mi edad es: $edad")
    }
    obtenerEdad2(1994, 2025)
    obtenerEdad2(añoNacimiento=1994, añoActual=2025)
    obtenerEdad2(añoActual=2025, añoNacimiento=1994)
    obtenerEdad2(añoNacimiento=1994)
    

    /*** RETURN ***/

    fun obtenerDescuento2(descuento:Double, total:Double): Double {
        val cantidadDescuento = total * (descuento / 100)
        val totalConDescuento = total - cantidadDescuento
        return totalConDescuento
    }

    fun obtenrIva(totalConDescuento: Double): Double {
        val cantidadIva = totalConDescuento * 0.16
        val totalIva = cantidadIva + totalConDescuento
        return totalIva
    }

    println("Ingresa el descuento")
    val descuento = readLine()!!.toDouble()
    println("Ingresa el total")
    val total = readLine()!!.toDouble()
    val totalConDescuento = obtenerDescuento2(descuento, total= total)
    val totalConIva = obtenrIva(totalConDescuento)
    println("El total con descuento es: $totalConDescuento")
    println("El total con IVA es: $totalConIva")

    /*** FUNCIONES ANONIMAS Y LAMBDAS ***/

    val sumaAnonima = fun(a: Int,  b: Int): Int {
        return a + b
    }
    val resultado = sumaAnonima(30,50)
    println(resultado)

    val sumaLambda = {a: Int, b: Int -> a + b}
    val resultado = sumaLambda(30,50)
    println(resultado)


    val numeros3 = listOf(4,3,5,6,2,6,7,8,2,10)
    val filtrado2 = numeros3.filter {x -> x % 2 == 0}
    println(filtrado2)
}