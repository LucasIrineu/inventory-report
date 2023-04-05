from inventory_report.inventory.product import Product


def test_cria_produto():
    product_example = Product(
        1,
        "Gunblade",
        "SquareSoft",
        "20/03/1998",
        "01/01/2010",
        1545,
        "Should be stored in its case",
    )

    assert product_example.id == 1
    assert product_example.nome_do_produto == "Gunblade"
    assert product_example.nome_da_empresa == "SquareSoft"
    assert product_example.data_de_fabricacao == "20/03/1998"
    assert product_example.data_de_validade == "01/01/2010"
    assert product_example.numero_de_serie == 1545
    assert (
        product_example.instrucoes_de_armazenamento
        == "Should be stored in its case"
    )
