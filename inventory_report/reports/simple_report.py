from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products):

        data_fabricacao_velha = cls.get_data_fabricacao_velha(products)

        data_validade_proxima = cls.get_data_validade_proxima(products)

        empresa_com_mais_produto = cls.get_empresa_com_mais_produto(products)

        return (
            f"Data de fabricação mais antiga: {data_fabricacao_velha}\n"
            f"Data de validade mais próxima: {data_validade_proxima}\n"
            f"Empresa com mais produtos: {empresa_com_mais_produto}"
        )

    @classmethod
    def get_data_fabricacao_velha(cls, products):
        result = min([product["data_de_fabricacao"] for product in products])
        return result

    @classmethod
    def get_data_validade_proxima(cls, products):
        result = min(
            [
                product["data_de_validade"]
                for product in products
                if product["data_de_validade"] > str(datetime.today().date())
            ]
        )
        return result

    @classmethod
    def quantos_produtos_por_empresa(cls, products):
        empresas_com_produtos = dict()
        for product in products:
            if product["nome_da_empresa"] in empresas_com_produtos.keys():
                empresas_com_produtos[product["nome_da_empresa"]] += 1
            else:
                empresas_com_produtos[product["nome_da_empresa"]] = 1
        return empresas_com_produtos

    @classmethod
    def get_empresa_com_mais_produto(cls, products):
        empresas_com_produtos = cls.quantos_produtos_por_empresa(products)
        return max(empresas_com_produtos, key=empresas_com_produtos.get)
