from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


mock_list = [
    {
        "data_de_fabricacao": "2022-05-23",
        "data_de_validade": "2023-08-29",
        "nome_da_empresa": "ABC",
    },
    {
        "data_de_fabricacao": "2022-05-19",
        "data_de_validade": "2024-04-01",
        "nome_da_empresa": "ABC",
    },
]

green_phrases = [
    "Data de fabricação mais antiga:",
    "Data de validade mais próxima:",
    "Empresa com mais produtos:",
]

phrases = [f"\033[32m{phrase}\033[0m" for phrase in green_phrases]


expect = (
    f"{phrases[0]} \033[36m2022-05-19\033[0m\n"
    f"{phrases[1]} \033[36m2023-08-29\033[0m\n"
    f"{phrases[2]} \033[31mABC\033[0m"
)


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport)
    report = colored_report.generate(mock_list)
    assert expect == report
