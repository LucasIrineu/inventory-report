from inventory_report.inventory.product import Product


def test_cria_produto():
    product_example = Product(
        1,
        "Gunblade",
        "SquareSoft",
        "20/03/1998",
        "01/01/2010",
        '456',
        "Should be store in its case",
    )

    assert product_example.id == 'Gunblade'
