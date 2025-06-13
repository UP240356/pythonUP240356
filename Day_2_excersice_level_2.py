print('')
#1
print(type([1,2]))
print((type('a,b')))
print(type([1,2,3,4]))
print('')

#2
lista=[5]
longitud_lista=len(lista)
print(longitud_lista)
tupla=1,2,3
longitud_tupla=len(tupla)
print(longitud_tupla)
print('')

#3
print(bool('marina'>'macias'))
#4
num_one=5
num_two=4
#5
print((num_one)+(num_two))
print(type([(num_one)+(num_two)]))
#6
diff=num_two-num_one
print(diff)
#7
product=num_one*num_two
print(product)
#8
divicion=num_one/num_two
print(divicion)
#9
remainder=num_one % num_two
print(remainder)
#10
exp=num_one**num_two
print(exp)
#11
floor_division=num_one//num_two
print(floor_division)
#12
radius=30
area_of_circle=3.1416*(radius)**2
print(area_of_circle)

circulum_of_circule=2*3.1416*(radius)
print(circulum_of_circule)

#solicitud de radio el radio
radius=float(input('introduce el radio de el circulo: '))
#calcular el area
area=3.1416*(radius**2)
print(f'el area de el circulum con', [radius] ,'es:',[area])

#13
#obtener el nombre, apellido, país y edad de un usuario
fist_name=input('dame tu nombre :')
last_name=input('dame tu apollido :')
country=input('dame tu país')
age=input('dame tu edad :')
#acumulacion de datos
print(f'el nombre es',[fist_name],'el apellido es',[last_name],'el país es',[country],'la edad',[age])
print('')

#14

