#Metodo que determine si un número n es pandigital y si al mismo tiempo,
# sus últimos 3 dígitos conforman un número primo
def panprimo(n):
  primo= True # Bandera para saber si es primo
  pandigital = True #Bandera para saber si es pandigital
  
  resto = n%1000 # Obtiene los 3 ultimos digitos de n
  cadena = str(n) #Convierte en cadena a n  
  
  #Verifica si es primo
  for i in range(2,resto):
    if resto%i == 0:
      primo = False

  #Verifica si es pandigital
  for i in ["1","2","3","4","5","6","7","8","9","0"]:
    if i not in cadena:
      pandigital = False 

  return print(primo and pandigital)

panprimo(10123485769)