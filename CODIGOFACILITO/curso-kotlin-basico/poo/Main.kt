fun main(args: Array<String>) {
    // val persona1 = Persona("Jose", 20)
    val persona1 = Persona(15)
    persona1.apellido = "Lopez"
    println(persona1.nombre)
    persona1.hablar("deportes")

    
    val persona2 = Persona("1234567")
    persona2.nombre = "Sofia"
    persona2.apellido = "Garcia"
    println(persona2.nombre)
    persona2.hablar("historias")

    // Getters & Setters
    val persona3 = Persona()
    persona3.nombre = "Pepito"
    persona3.apellido = "LOPEZ"
    persona3.edad = 15
    println(persona3.nombre)
    println(persona3.apellido)
    println(persona3.esMayor())

    // Herencia
    val cliente = Cliente()
    cliente.nombre = "Marines"
    println(cliente.nombre)
    cliente.comer()

    // Abstracción
    val proveedor = Proveedor4()
    proveedor.eliminar()

    // Polimorfismo
    val cliente4 = Cliente4()
    cliente4.iniciarSesion(123455)
    cliente4.iniciarSesion("my@mail.com", "my-pass")

    // Companion object Factory
    val  instanciaUsuario = Usuario.crear("Marines")
    println(instanciaUsuario.nombre)

    // data class
    data class Texto(val mensaje: String, val alerta: String)
    val texto = Texto(mensaje = "Hola!!", alerta ="Cuidado!")
    println(texto.toString())
    val texto2 = texto.copy(mensaje= "Bienvenido!")
    println(texto2.toString())
    println(texto2.hashCode() == texto.hashCode())

    // inner class
    Externa().Interna().saludo()

    // Sealed class
    val circulo = Forma.Circulo(54.8)

    // Enums
    val pago = Pagos.DECLINADO
    when(pago) {
        Pagos.ACEPTADO -> println("Pago exitoso")
        Pagos.CANCELADO -> println("Pago cancelado")
        Pagos.DECLINADO -> println("Pago declinado")
    }

    Pagos2.DECLINADO.transaccion()
    
}

// class Persona constructor(_nombre: String, _edad: Int)  // con constructor primario
class Persona {    
    var nombre: String = ""
    var apellido: String = ""
    var edad: Int = 0
    var telefono: String = ""

    // Constructores secundarios
    constructor(_edad: Int) {
        if(_edad >= 18) {
            println("Eres mayor de edad")
        }
    }

    // Constructores secundarios
    constructor(_telefono: String) {
        if(_telefono.length > 5) {
            println("Número valido")
        }
    }

    //Constructor Init - primario
    init{
        it(_edad >= 18) {
            println("Hola $_nombre, eres mayor de edad")
            nombre = _nombre
            edad = _edad
        }
    }

    fun hablar(hablar: String) {
        println("Soy $nombre y hablo de $hablar")
    }

    fun ver() {
        println("Soy y veo")
    }

    fun cantar() {
        println("Soy y canto")
    }
}

/*** Getters & Setters - Encapsulamiento ***/
class Persona2 {
    var nombre: String = ""
    get() = field
    set(value) {
        field = value.uppercase()
    }

    var apellido: String = ""
    get() = field
    set(value) {
        field = value.lowercase()
    }

    var edad: Int = 0
    private var telefono: String = "" // parametro privado

    fun hablar(hablar: String) {
        println("Soy $nombre y hablo de $hablar")
    }

    fun ver() {
        println("Soy y veo")
    }

    fun cantar() {
        println("Soy y canto")
    }

    // Metodo Publico
    fun esMayor() {
        verificarSiEsMayor()
    }

    // Metodos privados
    private fun verificarSiEsMayor() {
        if(edad >= 18) {
            println("Es mayor de edad")
        } else {
            println("No es mayor de edad")
        }
    }
}

/*** HENRENCIA ***/
open class Persona3 {  
    var nombre: String = ""
    protect var apellido: String = ""
    var edad: Int = 0
    var telefono: String = ""

    fun hablar(hablar: String) {
        println("Soy $nombre y hablo de $hablar")
    }

    fun ver() {
        println("Soy y veo")
    }

    fun cantar() {
        println("Soy y canto")
    }
}


class Cliente: Persona3 {
    var esFrecuente: Boolean
    var correo: String = ""
    fun comer(){
        apellido = "Millar"
        println("$nombre $apellido come espagueti!!")
    }
}

class Empleado: Persona3 {
    var cargo: String = ""
    var horario: String = ""
    fun cocinar(){}
}

class Proveedor: Persona3 {
    var cuenta: String = ""
    var banco: String = ""
    fun productos(){}
}

/*** ABSTRACCIÓN & POLIMORFISMO***/
abstract class Persona4 {  
    var nombre: String = ""
    protect var apellido: String = ""
    var edad: Int = 0
    var telefono: String = ""

    abstract fun eliminar()

    // Polimorfismo
    open fun iniciarSesion(idFacebook: Long)

    fun hablar(hablar: String) {
        println("Soy $nombre y hablo de $hablar")
    }

    fun ver() {
        println("Soy y veo")
    }

    fun cantar() {
        println("Soy y canto")
    }
}

// Interfaces
interface Acciones {
    fun agregar()
    fun actualizar()
}

class Cliente4: Persona4 {
    var esFrecuente: Boolean
    var correo: String = ""
    fun comer(){
        apellido = "Millar"
        println("$nombre $apellido come espagueti!!")
    }

    override fun eliminar(){}

    // Polimorfismo
    fun iniciarSesion(email: String, contraseña: String) {
        println("Inicio session con email: $email")
    }

    override fun iniciarSesion(idFacebook: Long) {
        println("Iicio session con id de Facebook: $idFacebook")
    }
}

class Empleado4: Acciones {
    var cargo: String = ""
    var horario: String = ""
    fun cocinar(){}
    override fun eliminar(){}
    override fun agregar(){}
    override fun actualizar(){}
}

class Proveedor4: Persona4, Acciones {
    var cuenta: String = ""
    var banco: String = ""
    fun productos(){}
    override fun eliminar(){
        println("Eliminar proveedor")
    }
    override fun agregar(){}
    override fun actualizar(){}
}

/*** COMPANION OBJECT FACTORY ***/
class Usuario constructor(val nombre: String) {
    companion object Factory {
        fun crear(nombre: String): Usuaario = Usuario(nombre)
    }
}

/*** INNER CLASS ***/
class Externa {
    private val nombre: String = "Marines"
    inner class Interna {
        fun saludo() {
            println("Hola $nombre")
        }
    }
}

/*** SEALED CLASS ***/
sealed class Forma {

    class Circulo(var radio: Double): Forma() {

    }
    
    class Rectangulo(var largo: Int, var ancho: Int): Forma() {
        
    }

}


/*** ENUM CLASS ***/
interface Acciones {
    fun transaccion()
}

enum class Pagos: Acciones {
    ACEPTADO,
    CANCELADO,
    DECLINADO
}

enum class Pagos2: Acciones { // with interfaces
    ACEPTADO {override fun transaccion() {println("Pago exitoso")} },
    CANCELADO {override fun transaccion() {println("Pago cancelado")} },
    DECLINADO {override fun transaccion() {println("Pago declinado")} }
}
