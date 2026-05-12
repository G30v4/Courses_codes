/* 
ITERADORES
Tempalte:
let iterador = {
    next(){
        return {
            value: null,
            done: true
        }
    }
};
*/
let iterador = {
    currentValue: 1,
    next(){
        let res = {value: null, done: false};
        if(this.currentValue > 0 && this.currentValue <=5){
            res = {value: this.currentValue, done: false};
            this.currentValue += 1;
        } else {
            res = {done: true};
        }
        return res;
    }
};

//console.log(iterador.next());
//console.log(iterador.next());
//console.log(iterador.next());
//console.log(iterador.next());
//setTimeout(() => console.log(iterador.next()), 5000);
//console.log(iterador.next());
//console.log(iterador.next());
//console.log(iterador.next());

let item = iterador.next();
while(!item.done){
    console.log(item.value);
    item = iterador.next();
}

/* 
GENERADORES
template:
function* counter(){
    console.log("Estoy aqui");
    yield 1;
    console.log("ahora estoy aqui");
    yield 2;
}
*/
function* counter(){
    for (var i = 1; i <= 5; i++){
        yield i;
    }    
}

let generator = counter();
console.log(generator.next());
console.log(generator.next());
console.log(generator.next());
console.log(generator.next());
console.log(generator.next());
console.log(generator.next());


/* 
Return en funciones generadoras
*/
function* retornador(){
    return 3;
    yield 5; // no se llamará
}
let g = retornador();
console.log(g.next());
console.log(g.next());

/* 
Delegar generadores
*/
function* counter2(){
    for (var i = 1; i <= 5; i++){
        yield i;
    }
}
function* retornador2(){
    yield* counter2();
    console.log("regrese!!");
    yield 3;
}
let g2 = retornador2();
console.log(g2.next());

while(!g2.done){ 
    console.log(g2.next());
}


/* 
SIMBOLOS
*/
let simbolo = Symbol('mi-simbolo');
//let simbolo2 = Symbol('mi-simbolo'); // es distinto

let obj = {};
obj[simbolo] = function(){
    console.log("Mi nombre es un simbolo");
}

obj[simbolo](); // con el nombre de la variable


/* 
Iterables con iteradores
*/
function* counter3() {
    for(var i = 1; i<=5; i++){
        yield i;
    }
}
let generador3 = counter3();
let numeros = [2,5,10];
for (numero of generador3){
    console.log(numero);
}
// @@iterator
// SYynbol.iterator
// ej1
let contador = {
    [Symbol.iterator](){
        return {
            currentValue: 1,
            next(){
                let res = {value: null, done: false};
                if(this.currentValue > 0 && this.currentValue <=5){
                    res = {value: this.currentValue, done: false};
                    this.currentValue += 1;
                } else {
                    res = {done: true};
                }
                return res;
            }
        }
    }
}

for(num of contador){
    console.log(num)
}

// ej2
let rango = {
    min: null,
    max: null,
    currentValue: null,
    [Symbol.iterator](){return this;},
    next(){
        if(this.currentValue == null)
            this.currentValue = this.min;
        let res = {}
        if(this.currentValue >= this.min && this.currentValue <= this.max){
            res = {value: this.currentValue, done: false};
            this.currentValue += 1;
        } else {
            res = {done: true};
        }
        return res;
    }
}
rango.min = 1;
rango.max = 10;
for(n of rango){
    console.log(n)
}

/* 
Iterables y generadores
*/
let rango2 = {
    min: null,
    max: null,
    [Symbol.iterator](){return this.generator();},
    generator: function* (){
        for(var i=this.min; i<=this.max; i++){
            yield i;
        }
    }
}
rango2.min = 1;
rango2.max = 10;
for(n of rango2){
    console.log(n)
}