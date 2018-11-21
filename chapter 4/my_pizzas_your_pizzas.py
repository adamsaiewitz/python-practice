pizzas = ['cheese', 'pepperoni', 'white']

for pizza in pizzas:
    print("I like " + pizza + " pizzas the best!")

print("Boy I sure love pizza!")

friend_pizzas = pizzas[:]

pizzas.append('sausage')
friend_pizzas.append('margherita')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
