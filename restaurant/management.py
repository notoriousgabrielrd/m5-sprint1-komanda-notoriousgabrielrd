from .menu import AVAILABLE_MENU


def get_item(item_id):

    for item in AVAILABLE_MENU:
        if item["id"] == item_id:

            return item
    return None  # existe outra forma de declarar que a func retorna none?


def add_item_to_tab(table_tab: list, item_id: int, amount: int):
    item_required = get_item(item_id)
    if item_required:
        table_tab.append(
            {
                "id": item_required["id"],
                "name": item_required["name"],
                "price": item_required["price"],
                "amount": amount,
            }
        )
        # from copy import deepcopy
        # deepcopy(table_tab)
        return table_tab
    return False


def calculate_tab(table_tab):
    treated_price = 0
    total_price = [item["price"] * item["amount"] for item in table_tab]
    for numb in total_price:
        treated_price += numb

    return "{:.2f}".format(treated_price)
