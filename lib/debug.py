from customer import Customer
from coffee import Coffee
from order import Order


benjie = Customer('Benjie')
aston = Customer('Aston')

mocha = Coffee('Mocha')
latte = Coffee('Latte')
espresso = Coffee('Espresso')

order1 = Order(benjie,latte,4.0)
order2 = Order(benjie,espresso,3.5)
order3 = Order(aston,latte,4.5)

print(benjie.coffees()) 
print(latte.average_price())  
print(Customer.most_aficionado(latte).name)  