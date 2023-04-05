from inventory_report.inventory.product import Product


def test_relatorio_produto():
    pr_example = Product(
        1,
        "Gunblade",
        "SquareSoft",
        "20/03/1998",
        "01/01/2010",
        1545,
        "Should be stored in its case",
    )

    assert pr_example.__repr__() == (
        f"O produto {pr_example.nome_do_produto}"
        f" fabricado em {pr_example.data_de_fabricacao}"
        f" por {pr_example.nome_da_empresa} com validade"
        f" até {pr_example.data_de_validade}"
        f" precisa ser armazenado {pr_example.instrucoes_de_armazenamento}."
    )
