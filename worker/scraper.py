import requests
from .config import Environment
from .parser_html import Html_Parser
import json


class Scraper(Html_Parser):

    def __init__(self, in_cnpj):
        self._in_cnpj = in_cnpj
        super().__init__()

    def _set_headers(self):
        self._headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=ISO-8859-1",
            "Cookie": "ASPSESSIONIDSSBRQCCC=NEPGBHACCBODIPCMBDHOFMBD; BIGipServer~Apps~pool_appasp-sefaz-go=rd3o00000000000000000000ffff0a0793fao80; ASPSESSIONIDQSCQTDCC=HGBEOCNCBHAFBOEIHJOOJBFL; ASPSESSIONIDSQATQDDD=LDNGNOJDHDPPICLADKLABOHC; ASPSESSIONIDSQDTQDCD=BJBGICACHDGNAGLLIEDEOPNO; TS01ebb0c0=01c51a2261bb7bba85ea4dabc4b88d54cc6527a134ecba4b810941daaf4d54a3faaa45c2e3202850b95f0e6885b48d3195df3413ce5246f49cd0a8ee41caa3737d0e55e67b5a243365783539f0d65747eea02ca55a8c4fbfd1a506dce058fea4e0d5afece1d6552879b4493e61a2a9b6e0cd70503ccea1e105ef97c3275c6c85f736c1737b; TSdf1ea11b027=08b9c2a2deab20008127380eb0f94e93c4b505e2f85f4e00ef56c2c4192ce6788515cbda8c1bc04508ede62cd8113000692514fae068a5ee1f115cd46566cad7ba17bb21b30d47fb11b84e0a30f2ff2d01c96536de5fe5f6a6bc8fccdf7f78a4",
            "Host": "appasp.sefaz.go.gov.br",
            "Origin": "http://appasp.sefaz.go.gov.br",
            "Referer": "http://appasp.sefaz.go.gov.br/Sintegra/Consulta/default.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "charset": "ISO-8859-1"
        }

    def _set_payload_cnpj(self, in_cnpj):
        self._payload_cnpj = {
            "rTipoDoc": 2,
            "tDoc": in_cnpj,
            "tCCE": "",
            "tCNPJ": in_cnpj,
            "tCPF": "",
            "btCGC": "Consultar",
            "zion.SystemAction": "consultarSintegra()",
            "zion.OnSubmited": "",
            "zion.FormElementPosted": "zionFormID_1",
            "zionPostMethod": "",
            "zionRichValidator": True,
        }

    def _ini_section(self):
        url_ini_section = Environment().URL_SEFAZ_GO
        response = requests.get(url_ini_section, headers=self._headers)
        if response.status_code == 200:
            self._section_cookies = response.cookies

    def _post_data(self):
        url_post_data = Environment().URL_SEFAZ_GO.replace(
            "default.html", "consultar.asp")
        response = requests.post(url_post_data, cookies=self._section_cookies,
                                 data=self._payload_cnpj, headers=self._headers)
        if response.status_code == 200:
            self._html_data = response.text

    def main(self):
        self._set_headers()
        self._set_payload_cnpj(self._in_cnpj)
        self._ini_section()
        self._post_data()
        if not super().has_cpnj_tag(self._html_data):
            return json.dumps({'message': f"não foi encontrado nenhum contribuinte para o CNPJ {self._in_cnpj}"})
        self._rjson = super().parse_html_to_json(self._html_data)
        return self._rjson
