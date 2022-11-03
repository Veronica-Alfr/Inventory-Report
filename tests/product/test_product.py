from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    produto = 'Café Zen'
    empresa = 'Espresso'
    fab = '2022-10-31'
    val = '2024-10-31'
    serie = '1234'
    instruction = 'em ambiente fresco'

    product = Product(id, produto, empresa, fab, val, serie, instruction)

    assert product.id == id
    assert product.nome_do_produto == produto
    assert product.nome_da_empresa == empresa
    assert product.data_de_fabricacao == fab
    assert product.data_de_validade == val
    assert product.numero_de_serie == serie
    assert product.instrucoes_de_armazenamento == instruction
