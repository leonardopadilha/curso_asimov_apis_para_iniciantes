import requests
from pprint import pprint # Como se fosse fazer o print bonito

def pegar_ids_estados():
  url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
  params = {
    "view": "nivelado"
  }
  dados_estados = fazer_request(url=url, params=params)
  dict_estado = {}
  for dados in dados_estados:
    id_estado = dados['UF-id']
    nome_estado = dados['UF-nome']
    dict_estado[id_estado] = nome_estado
  return dict_estado


def pegar_frequencia_nome_por_estado(nome):
  url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
  params = {
  'groupBy': 'UF'
  }

  dados_frequencia = fazer_request(url=url, params=params)
  dict_frequencia = {}
  for dados in dados_frequencia:
    id_estado  = int(dados['localidade'])
    frequencia = dados['res'][0]['proporcao']
    dict_frequencia[id_estado] = frequencia
  return dict_frequencia

  
def fazer_request(url, params=None):
  resposta = requests.get(url, params=params)

  try:
    resposta.raise_for_status()
  except requests.HTTPError as e:
    print(f"Erro no request: {e}")
    resultado = None
  else:
    resultado = resposta.json()
  return resultado

def main(nome):
  dict_estados = pegar_ids_estados()
  dict_frequencia = pegar_frequencia_nome_por_estado(nome)
  print(f'Frequência do nome {nome} por Estados (por 100.000 habitantes)')
  for id_estado, nome_estado in dict_estados.items():
    frequencia_estado = dict_frequencia[id_estado]
    print(f"-> {nome_estado} -> {frequencia_estado}")

if __name__ == '__main__':
  nome = input("Informe um nome: ")
  main(nome)
