#1
cadena_concatenada='treinta' +' '+ 'dias' + ' '+'de'+' ' + 'python'
print(cadena_concatenada)
#2
cadena_conc= 'codificacion'+' '+ 'para'+' '+ 'todos'
print(cadena_conc)
#3
empresa= 'Codificación para todos'
#4
print(empresa)
#5
print(len(empresa))
#6
print(empresa.upper())
#7
print(empresa.lower())
#8
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())
#9
primera_palabra=empresa.split()[0]
print(primera_palabra)
#10
palabra='Codificación'

if palabra in empresa:
    print(f'[palabra]', 'ésta en la cadena')
else:
    print(f'[palabra]','no esta en la cadena')
#11
cadena_modificada=cadena_conc.replace('codificacion','Python')
print(cadena_modificada)
#12
cadena_modificada2=cadena_modificada.replace('todos', 'siempre')
print(cadena_modificada2)
#13
print(empresa.split())
resultado=cadena_concatenada.split(' ')
print(resultado)
#14
cadena1='Facebook  Google  Microsoft  Apple  IBM  Oracle  Amazon'
resultado1=cadena1.split()
print(resultado1)
#15
cadena='codificacion para todos'
caracter=cadena[0]
print(caracter)
#16
ultimo_indice=len(cadena)-1
print('el untimo indice es :',ultimo_indice)
#17
caracter1=cadena[10]
print(caracter1)
#18
acronimo='python para todos'
print(acronimo[0],acronimo[7],acronimo[12])
#19
print(empresa[0],empresa[13],empresa[18])
#20
posicion=cadena.find('c')
print(posicion)
#21
posicion=cadena.find('f')
print(posicion)
#22
variable='codigo para toda la gente'
posicion1=variable.find('l')
print(posicion1)
#23
frase='No se puede terminar una oración con "because" porque es una conjunción'
posicion2=frase.find('because')
print(posicion2)
#24
posicion2=frase.rindex('because')
print(posicion2)
#25
frase1=frase.replace('"because" porque es una conjunción', " ")
print(frase1)
#26
falla='No puedes terminar una oración con porque porque porque es una conjunción'
encontrada=falla.find('porque')
print(encontrada)
#27
falla2=falla.replace('porque porque porque','')
print(falla2)
#28
resultado=cadena.startswith('codificacion')
print(resultado)
#29
resultado=cadena.endswith('codificacion')
print(resultado)
#30
frase3='    codificacion para todos     '
resultado=frase3.strip()
print(resultado)
#31
print('30DaysOfPython'.isidentifier())
print('thirteen_days_of_python'.isidentifier())
#32
bibliotecas=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado2=' # '.join(bibliotecas)
print(resultado2)
#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("nombre\t\tedad\tpais\t\tciudad")
print("Marina\t        19\tMexico\t\taguascalientes")
#35
radio = 10
area = 3.14 * radio ** 2
mensaje = "El area de un circulo con radio de {} es {} metros cuadrados.".format(radio, int(area))
print(mensaje)
#36
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} * {b} = {a * b}")


