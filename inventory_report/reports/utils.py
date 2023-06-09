import datetime as dt
from typing import List, Dict


def getDate(str):
    return dt.datetime.strptime(str, "%Y-%M-%d")


def getTodayDate():
    return dt.datetime.today().strftime("%Y-%m-%d")


def sort_companies_count(companies: List[str]):
    sorted_companies_list = []

    for company in companies:
        company_count = companies.count(company)
        sorted_company = {
            "name": company["name"],
            "products_count": company_count,
        }

        if sorted_company not in sorted_companies_list:
            sorted_companies_list.append(sorted_company)

    return sorted_companies_list


def most_products_report(companies: List[Dict]):
    company_with_most_products = companies[0]

    for company in companies:
        if (
            company["products_count"]
            >= company_with_most_products["products_count"]
        ):
            company_with_most_products = company

    return company_with_most_products


def sort_companies_stock(companies_list: List[Dict]):
    sorted_stock = []
    result_string = ""
    companies = sorted(
        companies_list, key=lambda x: x["products_count"], reverse=True
    )

    for company in companies:
        sorted_stock.append(
            f"- {company['name']}: {company['products_count']}\n"
        )

    for str in sorted_stock:
        result_string += str

    return result_string
