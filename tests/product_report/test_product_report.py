from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    produto = 'Café Zen'
    empresa = 'Espresso'
    fab = '2022-10-31'
    val = '2024-10-31'
    serie = '1234'
    instruction = 'em ambiente fresco'

    product = Product(id, produto, empresa, fab, val, serie, instruction)

    retorno_de_product = (
            f"O produto {produto}"
            f" fabricado em {fab}"
            f" por {empresa} com validade"
            f" até {val}"
            f" precisa ser armazenado {instruction}."
        )

    assert product.__repr__() == retorno_de_product
