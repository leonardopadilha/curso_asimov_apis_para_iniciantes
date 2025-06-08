import requests
from pprint import pprint # Como se fosse fazer o print bonito

nome = input("Digite um nome a ser pesquisado: ")
url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

parms = {
  'sexo': 'M',
  #'localidade': 33,
  'groupBy': 'UF'
}

resposta = requests.get(url, params=parms)

try:
  resposta.raise_for_status()
except requests.HTTPError as e:
  print(f"Erro no request: {e}")
  resultado = None
else:
  resultado = resposta.json()
  pprint(resultado)

# Exibindo o endpoint
print("url: " , resposta.request.url)
