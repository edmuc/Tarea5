#Arreglos


#1 Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

def promedio(arreglo):
    suma = 0
    for x in arreglo:
        suma += x        
    return suma / len(arreglo)

n = int(input("¿Cuántos números tiene el arreglo? "))
arreglo = []

for i in range(n):
    valor = float(input(f"Ingrese el número {i+1}: "))
    arreglo.append(valor)

print("Promedio:", promedio(arreglo))


#2 Desarrollar un algoritmo que calcule el producto punto de dos arreglos de n ́umeros enteros (reales) de igual tama ̃no. Sean
#v = [v0, v1, . . . , vn−1] y w = [w0,w1, . . . ,wn−1] dos arreglos, el
#producto de v y w (notado v · w) es el n ́umero:
#v0 ∗ w0 + v1 ∗ w1 + · · · + vn−1 ∗ wn−1.

def producto_punto(v, w):
    if len(v) != len(w):
        raise ValueError("Los arreglos deben tener el mismo tamaño")
    resultado = 0
    for i in range(len(v)):
        resultado += v[i] * w[i]
    return resultado

n = int(input("¿Cuántos elementos tienen los arreglos? "))

v = []
w = []

print("Ingrese los elementos del primer arreglo:")
for i in range(n):
    v.append(float(input(f"v[{i}]: ")))

print("Ingrese los elementos del segundo arreglo:")
for i in range(n):
    w.append(float(input(f"w[{i}]: ")))


print("Producto punto:", producto_punto(v, w))


#3 Desarrollar un algoritmo que calcule el producto directo de dos
#arreglos de n ́umeros reales de igual tama ̃no. Sean
#v = [v0, v1, . . . , vn−1] y w = [w0,w1, . . . ,wn−1] dos arreglos, el
#producto directo de v y w (notado v ∗ w) es el vector:
#[v0 ∗ w0, v1 ∗ w1, . . . , vn−1 ∗ wn−1].

def producto_directo(v, w):
    if len(v) != len(w):
        raise ValueError("Los arreglos deben tener el mismo tamaño")
    resultado = []
    for i in range(len(v)):
        resultado.append(v[i] * w[i])
    return resultado

n = int(input("¿Cuántos elementos tienen los arreglos? "))

v = []
w = []

print("Ingrese los elementos del primer arreglo:")
for i in range(n):
    v.append(float(input(f"v[{i}]: ")))

print("Ingrese los elementos del segundo arreglo:")
for i in range(n):
    w.append(float(input(f"w[{i}]: ")))


print("Producto directo:", producto_directo(v, w))



#4 Desarrollar un algoritmo que determine la mediana de un arreglo de
#enteros. La mediana es el n ́umero que queda en la mitad del arreglo
#despues de ser ordenado.


def mediana(arreglo):
    arreglo_ordenado = sorted(arreglo)
    n = len(arreglo_ordenado)
    mitad = n // 2

    if n % 2 == 0:
        
        return (arreglo_ordenado[mitad - 1] + arreglo_ordenado[mitad]) / 2
    else:
        
        return arreglo_ordenado[mitad]

n = int(input("¿Cuántos números tiene el arreglo? "))
arreglo = []

for i in range(n):
    valor = int(input(f"Ingrese el número {i+1}: "))
    arreglo.append(valor)


print("Arreglo ordenado:", sorted(arreglo))
print("Mediana:", mediana(arreglo))



#5 Hacer un algoritmo que deje al final de un arreglo de n ́umeros todos
#los ceros que aparezcan en dicho arreglo.


def mover_ceros(arreglo):
    resultado = []
    ceros = 0

    for num in arreglo:
        if num == 0:
            ceros += 1
        else:
            resultado.append(num)

   
    resultado.extend([0] * ceros)
    return resultado


n = int(input("¿Cuántos números tiene el arreglo? "))
arreglo = []

for i in range(n):
    valor = int(input(f"Ingrese el número {i+1}: "))
    arreglo.append(valor)

print("Arreglo original:", arreglo)
print("Arreglo con ceros al final:", mover_ceros(arreglo))





#Diccionario


#1 Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.

Lista1= {12:"Juan", 23:"Joe", 80:"Pedro", 3306:"Kevin"}

ordenados_por_clave = sorted(Lista1.items(), key=lambda item: item[0])
for clave, valor in ordenados_por_clave:
    print(f"{clave}: {valor}")




#2 Desarrollar un algoritmo que verifique si todas las clave:valor de un diccionario se encuentran en otro diccionario.

Lista1= {12:"Juan", 23:"Joe", 80:"Pedro", 3306:"Kevin"}
Lista2= {15:"SS", 23:"Joe", 31:"ZZ", 3307:"KK"}
def verificar_claves_valores(Lista1, Lista2):
    for clave, valor in Lista1.items():
        if Lista2.get(clave) != valor:
            return False
    return True
    print (verificar_claves_valores(Lista1, Lista2))

#3 Desarrollar una funci ́on que reciba dos diccionarios como par ́ametros
#y los mezcle, es decir, que se construya un nuevo diccionario con las
#llaves de los dos diccionarios; si hay una clave repetida en ambos
#diccionarios, se debe asignar el valor que tenga la clave en el
#primer diccionario.


def mezclar_diccionarios(dic1, dic2):
    
    resultado = dic1.copy()

    for clave, valor in dic2.items():
        if clave not in resultado:
            resultado[clave] = valor

    return resultado


n1 = int(input("¿Cuántos elementos tendrá el primer diccionario? "))
dic1 = {}

for i in range(n1):
    clave = input(f"Ingrese la clave {i+1} del primer diccionario: ")
    valor = input(f"Ingrese el valor para '{clave}': ")
    dic1[clave] = valor

n2 = int(input("\n¿Cuántos elementos tendrá el segundo diccionario? "))
dic2 = {}

for i in range(n2):
    clave = input(f"Ingrese la clave {i+1} del segundo diccionario: ")
    valor = input(f"Ingrese el valor para '{clave}': ")
    dic2[clave] = valor

print("\nDiccionario 1:", dic1)
print("Diccionario 2:", dic2)

mezclado = mezclar_diccionarios(dic1, dic2)
print("\nDiccionario mezclado:", mezclado)



#4 Desarrollar un programa que dada una listas de personas, cada
#persona representada como el siguiente ejemplo:
#{"nombres":"Pedro Julio", "apellidos":"Trist ́an Merch ́an",
#"edad":101}, imprima los nombres y apellidos de las personas que
#est ́an en un rango de edades.

def personas_en_rango(personas, edad_min, edad_max):
    print(f"\nPersonas entre {edad_min} y {edad_max} años:")
    encontrado = False

    for persona in personas:
        if edad_min <= persona["edad"] <= edad_max:
            print(f"- {persona['nombres']} {persona['apellidos']} ({persona['edad']} años)")
            encontrado = True

    if not encontrado:
        print("No hay personas en ese rango de edad.")


n = int(input("¿Cuántas personas desea ingresar? "))
personas = []

for i in range(n):
    print(f"\nPersona #{i+1}:")
    nombres = input("Ingrese los nombres: ")
    apellidos = input("Ingrese los apellidos: ")
    edad = int(input("Ingrese la edad: "))

    persona = {"nombres": nombres, "apellidos": apellidos, "edad": edad}
    personas.append(persona)

edad_min = int(input("\nIngrese la edad mínima del rango: "))
edad_max = int(input("Ingrese la edad máxima del rango: "))

personas_en_rango(personas, edad_min, edad_max)
