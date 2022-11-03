import datetime


class SimpleReport:

    @classmethod
    def generate(cls, product):
        date = cls.oldest_date(product)
        val = cls.validity(product)
        highest_products = cls.count_products(product)

        return (
            f"Data de fabricação mais antiga: {date}\n"
            f"Data de validade mais próxima: {val}\n"
            f"Empresa com mais produtos: {highest_products}"
        )

    @classmethod
    def oldest_date(cls, product):
        return min([item["data_de_fabricacao"] for item in product])

    @classmethod
    def validity(cls, product):
        date_time = datetime.datetime.now()
        return min([item["data_de_validade"] for item in product if (
                        item["data_de_validade"] > str(date_time.date())
                )]
            )

    @classmethod
    def count_products(cls, product):
        count_products = dict()
        for item in product:
            if item["nome_da_empresa"] in count_products.keys():
                count_products[item["nome_da_empresa"]] += 1
            else:
                count_products[item["nome_da_empresa"]] = 1
        return max(count_products, key=count_products.get)
