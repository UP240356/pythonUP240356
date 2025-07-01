#ejercicio 1
empty_dog={}

#ejercicio 2
dct={'nombre':'luka', 'color':'cafe', 'raza':'chihuahua', 'patas':'pequeñas', 'edad':'2 años'}
empty_dog=dct

#ejercicio 3
estudiante={'nombre':'carlos', 'apellido':'mata', 'sexo':'masculino', 'edad':'19', 'estado civil':'soltero', 'habilidades':'python', 'país':'mexico', 'ciudad':'aguascalientes','dirección':'24003'}

#ejercicio 4
print(len(estudiante))

#ejercicio 5
print(estudiante.get('nombre'))
print(estudiante.get('apellido'))
print(estudiante.get('sexo'))
print(estudiante.get('edad'))
print(estudiante['estado civil'])
print(estudiante['habilidades'])
print(estudiante['país'])
print(estudiante['ciudad'])
print(estudiante['dirección'])

#ejercicio 6
estudiante['habilidades']=['java','excel']
print(estudiante['habilidades'])

#ejercicio 7
claves=list(estudiante.keys())
print(claves)

#ejercicio 8
valores=list(estudiante.values())
print(valores)

#ejercicio 9
lista_de_tuplas=list(estudiante.items())
print(lista_de_tuplas)

#ejercicio 10
elemento_eliminado =estudiante.pop("edad")

print("Elemento eliminado:", elemento_eliminado)
print("Diccionario actualizado:", estudiante)

#ejercicio 11
print(empty_dog.clear())