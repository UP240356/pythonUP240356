#ECERSICE LEVEL2


# PARTE 2
print('addition','3+4=',3+4)
print('subtration','4-2=',4-2)
print('multiplication','3*2=',3*2)
print('modulus','3%2=',3%2)
print('divicion','3/2=',3-2)
print('exponential','3**2=',3**2)
print('floor divicion operator','3///2',3//2)
print('')
# PARTE 3
print('my name is Marina')
print('my family name is Macias Rodriguez')
print('aguascalientes')
print('')

# ECERSICE LEVEl 3 PART 1
print('lau es',type(12))
print('')

print(float('1.1666'))
print('')
#literal de nuemero coplejo
z1 = 1+3j
print(z1) # output(1+3j)
print('')
#funcion complex
z2 = complex(2,-1)
print(z2) #output (2-1j)
print(z2.real) #output : 2.0
print(z2.imag) #putput -1.0
print(z2.conjugate()) #output : (2-1j)
#operaciones
z3=z1+z2
print(z3) #output (3+2j)
z4= z1 * z2
print(z4) # output(5+1j)
print('')

#nuemero en cadena 
numero=123
cadena= 'el numero es: '+str(numero)
print(cadena)
print('')

numero=123
cadena=f'el numero es:[numero]'
print(cadena) # salida de el numero es 144
print('')
numero=123
cadena='numero es:[]'.format(numero)
print(cadena) #salida del numero es 123
print('')
#boleanos
X1=5
Y1=10
print(X1 <Y1) #output :true
print(X1 >Y1) #output :false
print(X1 == X1)#output :true
print('')
#list
print(type([1,2,3,4]))
#diccionary
print(type['name':'abdul'])
#set
print(type([9.8, 3.14, 2.7]))
#true
print(type((9.8, 3.14, 2.7)))

#EXCERCISE: LEVEL 3 PART 2
X1=2
X2=10
Y1=3
Y2=8
d=((((X2-X1)**2)+((Y2-Y1)**2))**0.5)
print(d)