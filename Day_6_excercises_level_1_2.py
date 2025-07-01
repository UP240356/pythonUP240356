#excercises level 1
#ejercicio 1
tuple_vacia=()
tuple_vacia= tuple()
print('')

#ejercicio 2
hermanos=('eduardo','viviano','ricardo','moices')
hermanas=('lola','karla')
print('')

#ejercicio 3
todos_hermanos=hermanos+hermanas
print(todos_hermanos)
numero_de_hermanos=len(todos_hermanos)
print(numero_de_hermanos)
print('')

#ejercicio 4
family_members=todos_hermanos+('maricela','rafael')
print(family_members)
print('')

### exercises level 2
#ejercicio 1
print(family_members[0:6])
print('')

#ejercicio 2
frutas=('manzana', 'platano', 'mango', 'uva')
vegetales=('chayote','zanahoria', 'calabaza')
origen_animal=('huevo','leche', 'carne')
food_stuff_tp=frutas+vegetales+origen_animal
print(food_stuff_tp)
print('')

#ejercicio 3
food_stuff_lt=food_stuff_tp
print(food_stuff_tp)
print('')

#ejercicio 4
print(food_stuff_lt[4:6])
print('')

#ejrcicios 5
print(food_stuff_lt[0:3],food_stuff_lt[-10:-7])
print('')

#ejercicios 6
food_stuff_tp=frutas+vegetales+origen_animal
del food_stuff_tp

#ejercicio 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)