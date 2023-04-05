from inventory_report.inventory.product import Product


expected = (
    "O produto farinha "
    "fabricado em 2021-05-01 "
    "por Farinini com validade "
    "até 2023-06-02 "
    "precisa ser armazenado ao abrigo de luz."
)


def test_relatorio_produto():
    product = Product(
        1,
        "farinha",
        "Farinini",
        "2021-05-01",
        "2023-06-02",
        122,
        "ao abrigo de luz"
    )
    assert repr(product) == expected
