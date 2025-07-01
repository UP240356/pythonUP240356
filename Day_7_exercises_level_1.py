
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# ejercicico 1 
print('la longitud de it_companes es :',len(it_companies))
print('')

#ejercicio 2
it_companies.add('twitter')
print(it_companies)
print('')

#ejercicio 3
new_companies={'meta','samsung'}
it_companies.update(new_companies)
print(it_companies)
print('')

#ejercicio 4 
it_companies.discard('meta')
print(it_companies)

#ejercicio 5
mi_conjunto = {1, 2, 3, 4, 5}
try:
    mi_conjunto.remove(3)  
    print("Después de remove(3):", mi_conjunto)
    mi_conjunto.remove(10)  
except KeyError as e:
    print(f"Error con remove: {e}")

mi_conjunto.discard(4) 
print("Después de discard(4):", mi_conjunto)