class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, qty=1):
        self.items.append({"name": name, "price": price, "qty": qty})

    def total(self):
        return sum(i["price"] * i["qty"] for i in self.items)

    def total_with_discount(self, percent):
        return self.total() * percent / 100
