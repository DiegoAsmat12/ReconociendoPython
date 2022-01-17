num1 = 42 #entero
num2 = 2.3 #flotante
boolean = True #booleano
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #arreglo
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #diccionario
fruit = ('blueberry', 'strawberry', 'banana') #tupla
print(type(fruit)) #imprime en consola el tipo tupla
print(pizza_toppings[1]) #imprime segundo elemento de arreglo
pizza_toppings.append('Mushrooms') #Agrega elemento al final del arreglo
print(person['name']) #Imprime valor con llave name del diccionario
person['name'] = 'George' #asigna valor a la llave name 
person['eye_color'] = 'blue' #asigna valor a la llave eye_color y como no existe la crea
print(fruit[2]) #imprime el tercer elemento de la tupla fruit

if num1 > 45: #condicion if 
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #condicion if con la longitud de la cadena 
    print("It's a short word!")
elif len(string) > 15: #condicion else if con la longitud de la cadena
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #imprime de 0 a 4
    print(x)
for x in range(2,5): #imprime de 2 a 4
    print(x)
for x in range(2,10,3): #imprime de 2 a 9 saltando de 3 en 3
    print(x)
x = 0 #redefine el iterador
while(x < 5): #iterador en bucle while 
    print(x)
    x += 1 #incremento de 1 en 1

pizza_toppings.pop() #elimina el ultimo elemento
pizza_toppings.pop(1) #elimina elemento en el index 1

print(person)
person.pop('eye_color') #elimina el elemento con llave eye_color del diccionario
print(person)

for topping in pizza_toppings: #iteración de elemento equivalente a forEach ( item =>{})
    if topping == 'Pepperoni': 
        continue #se salta al siguiente elemento ignorando lo demás si topping es Pepperoni
    print('After 1st if statement') #Escribirá esta linea con cada iteración menos cuando el topping es Pepperoni
    if topping == 'Olives':
        break #Termina el bucle independientemente de si hay más elementos

def print_hello_ten_times(): #declaracion de funcion sin parametros
    for num in range(10): #num itera de 0 a 9
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #declaracion de funcion con parametro x
    for num in range(x): #num itera de 0 a x
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #declara la funcion con parametro x y en caso de x no ser asignada la iguala a 10
    for num in range(x): #num itera de 0 a x
        print('Hello')

print_hello_x_or_ten_times() #x obtiene el valor 10 por default
print_hello_x_or_ten_times(4) #x obtiene el valor de 4


"""
Bonus section
"""

# print(num3) #el valor num3 no está definido aún, botará error (NameError)
# num3 = 72 #se asigna num3 pero el orden es importante por lo que la linea anterior seguirá botando error
# fruit[0] = 'cranberry' #error porque la tupla es inalterable (TypeError)
# print(person['favorite_team']) #error porque la llave no existe (KeyError)
# print(pizza_toppings[7]) #error porque está fuera del rango (IndexError)
#   print(boolean) #error de indentación (IndentationError)
# fruit.append('raspberry') #la tupla no tiene la función append (AttributeError)
# fruit.pop(1) #la tupla no tiene la función pop (AttributeError)