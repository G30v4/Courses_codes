#Escribe una funci�n que reciba dos strings (de largo > 2) como par�metros, y retorne un string de largo 4 que consista de las dos primeras letras del primer string y las �ltimas dos letras del segundo.

def mezclador(string_a, string_b):
  # aqu� debes escribir el c�digo de tu programa
  if len(string_a) > 2 and len(string_b) > 2:
    mix = string_a[0:2]+string_b[len(string_b)-2:len(string_b)]
    return mix
  else:
    return "El tama�o de uno de los string no es mayor a 2" # aqu� debes retornar el resultado

a = "familia"
b = "abrigarse"

x = mezclador(a,b)
print(x)