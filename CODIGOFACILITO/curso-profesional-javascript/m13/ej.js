/* 
STRING o CADENAS
*/
let nombre = 'G30v4' // primitivo
console.log(nombre.length)
let nombre2 = new String("G30v4") // objeto
console.log(typeof nombre);
console.log(typeof nombre2);


/* 
Caracteres especiales (Escaping)
*/
console.log("Ejemplo de \"Printing\"");
console.log("Ejemplo de \n\t \\Barra invertida\\");


/* 
Concatenación e interpolación
*/
let c1 = "Hola";
let c2 = "Mundo!"
console.log(c1.concat(c2));

// tmeplate literal => template Strings
let template = `${c1} ${nombre}, como estas?`;
console.log(template)

// ej1: imprimir mes con digito 0 : i => 01, 02 .. 12 
// G30v4 Solution:
let mes = 1;
console.log(`Mes es: ${(mes < 10? '0':'') + mes}`)
// Profe solution:
let mes2 = "3";
console.log(mes2.padStart(2,"0"));
console.log(mes2.padEnd(2,"0"));


/* 
Comparación de cadenas
*/
console.log("A" > "B");
console.log("a" > "B");
console.log("A" == "a");

// local compare
// 0 : iguales
// -1: A,B
// 1: B,A
console.log("A".localeCompare("z"));
console.log("B".localeCompare("a"));
console.log("A".localeCompare("a"));
console.log("a".localeCompare("B"));
console.log("A".localeCompare("A"));
console.log("B".toLowerCase().localeCompare("B".toLowerCase()));

// inmutabilidad
let c3 = c1.toUpperCase();
console.log(c1)
console.log(c3)


/* 
Subcadenas y caracteres
*/
console.log(c3[0])
for (const c of c3) {
    console.log(c);
}

// substring
let cadena = "Ejemplo de texto";
console.log(cadena.substring(-1,7)); // empieza en 0
console.log(cadena.substring(0,7));
console.log(cadena.substring(7,2)); // se intercambia posicion
console.log(cadena.slice(0,7)); 
console.log(cadena.slice(7,2)); // no se ejecuta
console.log(cadena.slice(-5));


/* 
Búsqueda
*/
