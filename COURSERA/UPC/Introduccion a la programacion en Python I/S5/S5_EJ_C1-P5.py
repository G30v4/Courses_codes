#Escriba una función que reciba un string como parámetro y retorne el string, pero con cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.

def reemplazo(string):
  res = ""
  mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for s in string:
    if s in mayusculas:
      s = "$"
    res = res + s
  return res # aquí debes retornar el resultado

a = "Viva la Vida"

x = reemplazo(a)
print(x)