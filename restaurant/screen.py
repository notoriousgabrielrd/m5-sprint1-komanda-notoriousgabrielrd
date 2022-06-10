import os

TABLE_TAB = []
from restaurant import management


def add_item_screen() -> None:

    os.system("clear")
    while True:
        product_id = int(input("Digite o id do seu pedido: "))
        product_amount = int(input("Digite q quantidade do seu pedido: "))

        item_adicionado = management.add_item_to_tab(
            TABLE_TAB, product_id, product_amount
        )
        # criar uma copia
        if item_adicionado:
            os.system("clear")
            print(
                f'{item_adicionado[-1]["amount"]} {item_adicionado[-1]["name"]} adicionado(s) a comanda!'
            )
            # item_adicionado.clear() # mesmo espaco de memoria

            break
        else:
            os.system("clear")

            print("Nao e id de item valido!")


def check_out_screen() -> None:

    while True:

        [
            print(
                f'Item {count + 1}: {item["amount"]} {item["name"]} - R${item["price"]}'
            )
            for count, item in enumerate(TABLE_TAB)
        ]
        print("--------------------------------------------------")
        print(f"TOTAL: {management.calculate_tab(TABLE_TAB)}")

        print("Digite F para sair:")

        leave = input().upper()

        if leave == "F":
            os.system("clear")
            break

        # else:
        #     os.system("clear")


def initial_screen() -> None:
    os.system("clear")
    while True:

        print("1. Para adicionar item a comanda")

        print("2. Fechar comanda")

        resultado = input("O que deseja fazer? ")

        if resultado == "1":
            os.system("clear")
            add_item_screen()

        elif resultado == "2":
            os.system("clear")
            check_out_screen()
            break
            # while True:
            #     print("Digite F para sair:")

            #     leave = input().upper()

            #     if leave == "F":
            #         os.system("clear")
            #         break

            #     else:
            #         os.system("clear")
            #         check_out_screen()
            # break

        else:
            os.system("clear")
            print("Escolha uma das opcoes validas!")
