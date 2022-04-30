import os
from domains.Order import Order

class Order_Manager:
    def __init__(self):
        self.__orders = []

    def get_orders(self):
        return self.__orders

    def add_order(self, table_id, dish_manager):
        print(f'\nOrdering for table {table_id}')
        dish_manager.select_dishes()
        