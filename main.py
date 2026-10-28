from cart import Cart

cart = Cart()
cart.add("Хліб", 25, 2)
cart.add("Молоко", 40)

print("Сума:", cart.total())
print("Зі знижкою 10%:", cart.total_with_discount(10))
