import random  
from enum import Enum, auto  
  
  
class Item(Enum):  
    """Item type"""  
  
    LUNIX_CAMERA = auto()  
    IMAC = auto()  
    HTC_TOUCH = auto()  
    CANNON_EOS = auto()  
    IPOD_TOUCH = auto()  
    APPLE_VISION_PRO = auto()  
    COFMACBOOKFEE = auto()  
    GALAXY_S24 = auto()  
     
  
    def __str__(self):  
        return self.name.upper()  
  
  
class ShoppingCart:  
    def __init__(self):  
        """  
        Creates a shopping cart object with an empty dictionary of items  
        """  
        self.items = {}  
  
    def add_item(self, item: Item, price: int | float, quantity: int = 1) -> None:  
        """  
        Adds an item to the shopping cart  
        :param quantity: Quantity of the item  
        :param item: Item to add  
        :param price: Price of the item  
        :return: None  
        """  
        if item.name in self.items:  
            self.items[item.name]["quantity"] += quantity  
        else:  
            self.items[item.name] = {"price": price, "quantity": quantity}  
  
    def remove_item(self, item: Item, quantity: int = 1) -> None:  
        """  
        Removes an item from the shopping cart  
        :param quantity: Quantity of the item  
        :param item: Item to remove  
        :return: None  
        """  
        if item.name in self.items:  
            if self.items[item.name]["quantity"] <= quantity:  
                del self.items[item.name]  
            else:  
                self.items[item.name]["quantity"] -= quantity  
  
    def get_total_price(self):  
        total_price = 0  
        for item in self.items.values():  
            total_price += item["price"] * item["quantity"]  
        return total_price

