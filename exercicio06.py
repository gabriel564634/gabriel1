class BurgerKingSimples:
    def __init__(self):
        self.menu = {
            'Hamburguer Simples': 9.99,
            'Batata Frita Pequena': 4.99,
            'Refri Pequeno': 3.99
        }
        self.pedido = []

    def mostrar_menu(self):
        print("\nBurger Kingdom - Menu Simples:")
        for item, preco in self.menu.items():
            print(f"{item}: R${preco:.2f}")

    def fazer_pedido(self):
        print("\nFaça seu pedido:")
        for item in self.menu.keys():
            quantidade = int(input(f"Quantidade de {item}: "))
            self.pedido.append({'item': item, 'quantidade': quantidade})

    def calcular_total(self):
        total = sum(item['quantidade'] * self.menu[item['item']] for item in self.pedido)
        return total

    def imprimir_pedido(self):
        print("\nResumo do Pedido:")
        for pedido_item in self.pedido:
            item = pedido_item['item']
            quantidade = pedido_item['quantidade']
            print(f"{item} x{quantidade}")
        total = self.calcular_total()
        print(f"\nTotal a pagar: R${total:.2f}")
        print("Obrigado por escolher o Burger Kingdom Simples!")

if __name__ == "__main__":
    bks = BurgerKingSimples()
    bks.mostrar_menu()
    bks.fazer_pedido()
    bks.imprimir_pedido()