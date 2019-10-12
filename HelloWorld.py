import sys

print("Hola %s, Dios te ama desde el script" % ("Nestor"))

##asignacion de variables
#asignacion simple
a = 1
b = 2
#asignacion mulitple
a,b = 1,2

#impresion con formateo
print("Hola %s, Dios te ama, Desde la funcion" % ("Nestor"))
#pruede imprimir print (" %s, %s, ....%s")%("1","2", ...,"n")

#manipulacion de strings
"""
Las cadenas se cuentan desde la posicion 0 hasta la n-1
"""
cadena = "1234567890"
print(cadena[0:5])
print(cadena[5:])

#ciclo for
arr = [1,2,3,4,5,6,7,8,9]
for x in arr:
    print(x)
#for rangos
for x in range(5,51,5):
    print(x)

#eliminar un elemento de un array
#elimina el elmento 0
del arr[0]
#tamaño de un arreglo
print(len(arr))

#diccionarios son arreglos tipo clave valor y se inicializan por {}
dictionary = {"a":1, "b":2, "c":3}

#acceso
print(dictionary["c"])
#eliminar indice
del dictionary["c"]

#duplas son contenidos inmutables
tupl = ("a", 2, "B", "C")
"""
Las tuplas no se pueden modificar ni cambiar 
su acceso es similar a los arreglos desde la posicion 0 hasta n-1
"""


##conditional stament
a=1
if (a >1):
    print("Es mayor a 1")
else:
    print("%s Es menor o igual a 1"%(a))

try:
    print(""+2)
except:
    print("Error Sitax")

### function
def Saludar():
    print("Hola %s, Dios te ama, Desde la funcion" % ("Nestor"))


Saludar()


### function whit parameters
def sumar(a, b):
    return a + b

c = sumar(1, 10)
print("La suma es %s"%(c))

### Math Functions
print(abs(-15))
print(bool(1))
print(bool(16))
print(bool(0))

'''
Busqueda de funciones desde la consola de python se hace
obj = ""
help(obj.function)
ejemplo
help(obj.upper)
print 
Help on built-in function upper:
upper(...) method of builtins.str instance
    S.upper() -> str
    
    Return a copy of S converted to uppercase.
'''

#Ejecucion de codigo desde Strings
sent = 'print("Evaluacion desde cadenas: Hello from String")'
eval(sent)

#castear variables
a = int("1")
string = str(2546)
b = float(a)

print("CASTEO DE DATOS")
print(a)
print(string)
print(b)

## Clases
#void class
"""
Las funciones de las clases necesitan 
el parametro self para poderse llamar a si mismas
"""
class Person:
    pass

p = Person()

##Clase con paramentros
class Car:
    def __init__(self, brand):
        self.brand = brand

    def getBrand(self):
        print("Clase con paramentros BRAND:" + self.brand)

car = Car("BMW")
car.getBrand()

#inherence Herencia
class Animal:
    def __init__(self):
        print("Class Animal")
    def voces(self):
        print("No se que Animal soy")

animal = Animal()
print(animal.voces())

print("Herencia")
class Perro(Animal):
    def __init__(self):
        print("Soy un perro")
    def voces(self):
        #super().voces()
        print("El perro Ladra")

perro = Perro()
print(perro.voces())

print("End")


##lectura de archivos
archivo = open("texto.txt", "w")
print(archivo.read());
#en donde esta el puntero
print("position in file %s"%(archivo.tell()))
#cambiar la posicion del puntero
archivo.seek(0,0)
print("position in file %s"%(archivo.tell()))

#mover archivos
"""
import os;
os.rename("texto.txt", "texto_destino.txt")

"""


