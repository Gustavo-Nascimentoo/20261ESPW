# catalogo = [
#     ["Camiseta Azul", 59.90, 120, [38, 40, 42, 44]],
#     ["Tênis Runner", 199,90, 40],
# ]
# print(f"Produto: {catalogo[0][0]}")
# print(f"Estoque: {catalogo[0][2]} Unidades")
# print(f"Tamanho: {catalogo[0][3][2]} Cm")

def cadastrarProduto(catalogo, nome, preco, estoque):
    produto = [nome, preco, estoque]
    catalogo.append(produto)
    return catalogo

if __name__ =="__main__":
    novosProdutos = []
    novosProdutos = cadastrarProduto(novosProdutos,
                "Jaqueta Preta",
                    189.99,
                    50)
    novosProdutos = cadastrarProduto(novosProdutos,
                    "Camisa listrada",
                    60.90,
                    120)
    novosProdutos = cadastrarProduto(novosProdutos,
                    "Calça rosa",
                    99.99,
                    85)

    def exibirCatalogo(catalogo):
        for produto in catalogo:
            print(f"{produto[0]}, R$ {produto[1]:.2f}, (Estoque: {produto[2]})")

    exibirCatalogo(novosProdutos)

