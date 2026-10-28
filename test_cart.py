from cart import Cart


def make_cart():
    cart = Cart()
    cart.add("Хліб", 25, 2)
    cart.add("Молоко", 40)
    return cart


def test_total():
    assert make_cart().total() == 90


def test_empty_cart():
    assert Cart().total() == 0


def test_discount():
    assert make_cart().total_with_discount(10) == 81
