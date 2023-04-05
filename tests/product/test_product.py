from inventory_report.inventory.product import Product


expected = (
    'O produto D '
    'fabricado em 2002-05-12 '
    'por AZ com validade '
    'até 2019-05-12 '
    'precisa ser armazenado air.'
)


def test_cria_produto():
    product = Product(1, "D", "AZ", "2002-05-12", "2019-05-12", 122, "air")
    assert isinstance(product.id, int)
    assert isinstance(product.nome_do_produto, str)
    assert isinstance(product.nome_da_empresa, str)
    assert isinstance(product.data_de_fabricacao, str)
    assert isinstance(product.data_de_validade, str)
    assert isinstance(product.numero_de_serie, int)
    assert isinstance(product.instrucoes_de_armazenamento, str)
    assert repr(product) == expected
