from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, report_list: list[dict]) -> str:
        today_date = datetime.today().date()
        manufacturing_dates = []
        expiration_dates = []
        producers = dict()

        for product in report_list:
            manufacturing_date = datetime.strptime(
                product["data_de_fabricacao"], "%Y-%m-%d"
            ).date()
            expiration_date = datetime.strptime(
                product["data_de_validade"], "%Y-%m-%d"
            ).date()

            manufacturing_dates.append(manufacturing_date)

            if expiration_date > today_date:
                expiration_dates.append(expiration_date)

            if product["nome_da_empresa"] in producers:
                producers[product["nome_da_empresa"]] += 1
            else:
                producers[product["nome_da_empresa"]] = 1

        if len(expiration_dates) > 0:
            closest_date = min(expiration_dates)
        else:
            closest_date = ''

        earliest_date = min(manufacturing_dates)
        company_with_more_products = max(producers, key=producers.get)

        return (
            f'Data de fabricação mais antiga: {earliest_date}\n'
            f'Data de validade mais próxima: {closest_date}\n'
            f'Empresa com mais produtos: {company_with_more_products}'
        )
