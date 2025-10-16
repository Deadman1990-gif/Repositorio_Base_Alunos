class ItemDoPedido:
    def __init__(self, Produto: str, Quantidade: int, Preço_unitário: float):
        self.Produto=Produto
        self.Quantidade=Quantidade
        self.Preço_unitário=Preço_unitário
    def calcular_subtotal(self) -> float:
        return self.quantidade * self.Preço_unitário
class Pedido:
    def __init__(self, id_cliente: int):
        self.id_cliente=id_cliente
        self.items=[]
        print(f"\n Pedido Criado para o cliente{self.id_cliente}.")
    def adicionar_item(self, Produto:str, Quantidade: int, Preço_unitário: float):
        novo_item= ItemDoPedido(Produto, Quantidade, Preço_unitário)
        self.itens.append(novo_item)
        print(f" - Item'{Produto}' adicionado ao pedido.")
    def calcular_total(self):
        total=sum(item.calcular_subtotal() for item in self._itens)
        print(f"Total do Pedido: R$ {total:.2f}")
pedido_123=Pedido(957)

pedido_123.adicionar_item("Notebook Gamer", 1, 5000.00)
pedido_123.adicionar_item("Mouse sem Fio", 2, 150.00)
pedido_123.adicionar_item("Monitor", 3, 200.00)
pedido_123.adicionar_item("Placa_mãe", 4, 5078.00)
pedido_123.adicionar_item("Placa de Video", 5, 4000.00)
pedido_123()