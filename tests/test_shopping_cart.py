from typing import Callable  
from hypothesis import given, strategies as st  
from hypothesis.strategies import SearchStrategy  
from src.shopping_cart import ShoppingCart, Item  
  
  
# Create a strategy for items  
@st.composite  
def items_strategy(draw: Callable[[SearchStrategy[Item]], Item]):  
    return draw(st.sampled_from(list(Item)))  
  
  
# Create a strategy for price  
@st.composite  
def price_strategy(draw: Callable[[SearchStrategy[int]], int]):  
    return draw(st.integers(min_value=1, max_value=100))
  
  
# Create a strategy for quantity  
@st.composite  
def qty_strategy(draw: Callable[[SearchStrategy[int]], int]):  
    return draw(st.integers(min_value=1, max_value=10))  
  
  
@given(items_strategy(), price_strategy(), qty_strategy())  
def test_add_item_hypothesis(item, price, quantity):  
    cart = ShoppingCart()  
  
    # Add items to cart  
    cart.add_item(item=item, price=price, quantity=quantity)  
  
    # Assert that the quantity of items in the cart is equal to the number of items added  
    assert item.name in cart.items  
    assert cart.items[item.name]["quantity"] == quantity  
  
  
@given(items_strategy(), price_strategy(), qty_strategy())  
def test_remove_item_hypothesis(item, price, quantity):  
    cart = ShoppingCart()  
  
    print("Adding Items")  
    # Add items to cart  
    cart.add_item(item=item, price=price, quantity=quantity)  
    cart.add_item(item=item, price=price, quantity=quantity)  
    print(cart.items)  
  
    # Remove item from cart  
    print(f"Removing Item {item}")  
    quantity_before = cart.items[item.name]["quantity"]  
    cart.remove_item(item=item)  
    quantity_after = cart.items[item.name]["quantity"]  
  
    # Assert that if we remove an item, the quantity of items in the cart is equal to the number of items added - 1   
    assert quantity_before == quantity_after + 1  
  
  
@given(items_strategy(), price_strategy(), qty_strategy())  
def test_calculate_total_hypothesis(item, price, quantity):  
    cart = ShoppingCart()  
  
    # Add items to cart  
    cart.add_item(item=item, price=price, quantity=quantity)  
    cart.add_item(item=item, price=price, quantity=quantity)  
  
    # Remove item from cart  
    cart.remove_item(item=item)  
  
    # Calculate total  
    total = cart.get_total_price()  
    assert total == cart.items[item.name]["price"] * cart.items[item.name]["quantity"]
