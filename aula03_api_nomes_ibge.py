import requests
from pprint import pprint # Como se fosse fazer o print bonito

nome = input("Digite um nome a ser pesquisado: ")
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

resposta = requests.get(url)

try:
  resposta.raise_for_status()
except requests.HTTPError as e:
  print(f"Erro no request: {e}")
  resultado = None
else:
  resultado = resposta.json()
  pprint(resultado[0]['res'])
