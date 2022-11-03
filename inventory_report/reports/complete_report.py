from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, product):
        count_products = dict()
        for item in product:
            if item["nome_da_empresa"] in count_products.keys():
                count_products[item["nome_da_empresa"]] += 1
            else:
                count_products[item["nome_da_empresa"]] = 1
        phrase_return = ""
        for key, value in count_products.items():
            stock += f"- {key}: {value}\n"
        return (
            f"{super().generate(product)}\n"
            f"Produtos estocados por empresa:\n"
            f"{phrase_return}"
        )
