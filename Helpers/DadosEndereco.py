import requests

def get_codigo(nome_municipio: str, uf: str) -> int | None:

    uf = uf.upper().strip()
    nome = nome_municipio.strip()
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    resp = requests.get(url)
    if resp.status_code != 200:
        print("Erro ao consultar IBGE:", resp.status_code)
        return None
    municipios = resp.json()
    for m in municipios:
        # o campo pode se chamar "nome"
        if m.get("nome").lower() == nome.lower():
            return m.get("id")  # o ID é o código IBGE
    return None


def get_municipio(codigo: int) -> str | None:
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{codigo}"
    resp = requests.get(url)
    if resp.status_code != 200:
        print("Erro ao consultar IBGE:", resp.status_code)
        return None
    municipio = resp.json()
    if not municipio:
        return None
    nome = municipio.get("nome")
    uf = municipio.get("microrregiao", {}).get("mesorregiao", {}).get("UF", {}).get("sigla")
    if nome and uf:
        return f"{nome}/{uf}"
    return None