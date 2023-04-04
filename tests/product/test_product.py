from tests.factories.product_factory import ProductFactory


def test_cria_produto():
    product = ProductFactory()
    assert isinstance(product.id, int)
    assert isinstance(product.nome_do_produto, str)
    assert isinstance(product.nome_da_empresa, str)
    assert isinstance(product.data_de_fabricacao, str)
    assert isinstance(product.data_de_validade, str)
    assert isinstance(product.numero_de_serie, int)
    assert isinstance(product.instrucoes_de_armazenamento, str)
