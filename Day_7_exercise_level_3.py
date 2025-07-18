age = [22, 19, 24, 25, 26, 24, 25, 24]
#ejercicio 1
edades_conjunto=set(age)
longitud_age=len(age)
longitud_conjunto=len(edades_conjunto)
print(f"Longitud de la lista: {longitud_age}")
print(f"Longitud del conjunto: {longitud_conjunto}")

if longitud_age > longitud_conjunto:
    print("La lista tiene más elementos que el conjunto.")
elif longitud_age < longitud_conjunto:
    print("El conjunto tiene más elementos que la lista.")
else:
    print("La lista y el conjunto tienen la misma cantidad de elementos.")

#ejercicio 2
cadena = age
print(cadena[0])

lista = age
lista.append(4) 
lista[0] = 0     
print(lista)

tupla = age
print(tupla[0])  

#ejercicio 3
oracion = "Soy profesor y me encanta inspirar y enseñar."

# Dividir la oración en palabras y eliminar puntuación
palabras = oracion.replace(".", "").split()
# Crear un conjunto para obtener palabras únicas
palabras_unicas = set(palabras)
# Contar las palabras únicas
cantidad_palabras_unicas = len(palabras_unicas)
# Mostrar el resultado
print(f"Palabras únicas: {palabras_unicas}")
print(f"Cantidad de palabras únicas: {cantidad_palabras_unicas}")