from bs4 import BeautifulSoup
import json


class Html_Parser:

    def parse_html_to_json(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')

        cnpj = soup.find('span', string="CNPJ").find_next_sibling(
            'span').string.strip()
        inscricao_estadual = soup.find(
            'span', string="Inscrição Estadual").find_next_sibling('span').string.strip()
        cadastro_atualizado = soup.find(
            'span', string="Cadastro Atualizado em").find_next_sibling('span').string.strip()
        nome_empresarial = soup.find(
            'span', string="Nome Empresarial").find_next_sibling('span').string.strip()
        contribuinte = soup.find(
            'span', string="Contribuinte?").find_next_sibling('span').string.strip()
        nome_propriedade = soup.find('span', string="Nome da Propriedade:")
        nome_fantasia = soup.find('span', string="Nome Fantasia")
        if nome_fantasia != None:
            nome_fantasia.find_next_sibling('span').string.strip()
            nome_propriedade = ""
        else:
            nome_propriedade.find_next_sibling('span').string.strip()
            nome_fantasia = ""
        endereco = soup.find('div', string="Endereço Estabelecimento ").find_next_sibling(
            'span').string.strip()
        atividade_principal = soup.find(
            'span', string="Atividade Principal").find_next('span').string.strip()
        regime_apuracao = soup.find(
            'span', string="Regime de Apuração:").find_next_sibling('span').string.strip()
        situacao_cadastral = soup.find(
            'span', string="Situação Cadastral Vigente:").find_next_sibling('span').string.strip()
        data_situacao_cadastral = soup.find(
            'span', string="Data desta Situação Cadastral:").find_next_sibling('span').string.strip()
        data_cadastramento = soup.find(
            'span', string="Data de Cadastramento:").find_next_sibling('span').string.strip()
        operacoes_nfe = soup.find(
            'span', string="Operações com NF-E:").find_next_sibling('span').string.strip()
        data_consulta = soup.find(
            'span', string="Data da Consulta").find_next_sibling('span').string.strip()

        data = {
            "cnpj": cnpj,
            "inscricao_estadual": inscricao_estadual,
            "cadastro_atualizado": cadastro_atualizado,
            "nome_empresarial": nome_empresarial,
            "contribuinte": contribuinte,
            "nome_fantasia": nome_fantasia,
            "nome_propriedade": nome_propriedade,
            "endereco_estabelecimento": endereco,
            "atividade_principal": atividade_principal,
            "regime_de_apuracao": regime_apuracao,
            "situacao_cadastral_vigente": situacao_cadastral,
            "data_situacao_cadastral": data_situacao_cadastral,
            "data_cadastramento": data_cadastramento,
            "operacoes_com_nfe": operacoes_nfe,
            "data_consulta": data_consulta
        }
        return json.dumps(data, ensure_ascii=False)

    def has_cpnj_tag(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')
        if soup.find('span', string="CNPJ") != None:
            return True
        return False
