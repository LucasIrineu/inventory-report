from typing import List, Dict
from inventory_report.reports.utils import (
    getDate,
    getTodayDate,
    most_products_report,
    sort_companies_count,
)


class SimpleReport:
    def generate(products: List[Dict]):
        oldest_manufacture = products[0]["data_de_fabricacao"]
        nearest_expiration_date = products[0]["data_de_validade"]
        present_date = getTodayDate()
        companies = []

        for product in products:
            if getDate(product["data_de_fabricacao"]) < getDate(
                oldest_manufacture
            ):
                oldest_manufacture = product["data_de_fabricacao"]

            days1 = abs(
                getDate(product["data_de_validade"]).day
                - getDate(present_date).day
            )
            days2 = abs(
                getDate(nearest_expiration_date).day
                - getDate(present_date).day
            )

            if days1 <= days2:
                nearest_expiration_date = product["data_de_validade"]

            companies.append(
                {"name": product["nome_da_empresa"], "products_count": 1}
            )

        sorted_companies = sort_companies_count(companies)
        company_with_most_products = most_products_report(sorted_companies)

        result = (
            f"Data de fabricação mais antiga: {oldest_manufacture}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_most_products['name']}"
        )

        return result
