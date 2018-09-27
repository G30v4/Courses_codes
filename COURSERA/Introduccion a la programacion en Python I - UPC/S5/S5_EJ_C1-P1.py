#Escribe una función que reciba dos strings (de largo > 2) como parámetros, y retorne un string de largo 4 que consista de las dos primeras letras del primer string y las últimas dos letras del segundo.

def mezclador(string_a, string_b):
  # aquí debes escribir el código de tu programa
  if len(string_a) > 2 and len(string_b) > 2:
    mix = string_a[0:2]+string_b[len(string_b)-2:len(string_b)]
    return mix
  else:
    return "El tamaño de uno de los string no es mayor a 2" # aquí debes retornar el resultado

a = "familia"
b = "abrigarse"

x = mezclador(a,b)
print(x)