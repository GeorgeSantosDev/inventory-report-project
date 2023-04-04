from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report_list: list[dict]) -> str:
        response = super().generate(report_list)
        producers = dict()

        for product in report_list:
            if product["nome_da_empresa"] in producers:
                producers[product["nome_da_empresa"]] += 1
            else:
                producers[product["nome_da_empresa"]] = 1

        response += "\nProdutos estocados por empresa:\n"

        for key, value in producers.items():
            response += f"- {key}: {value}\n"
        print(response)
        return response
