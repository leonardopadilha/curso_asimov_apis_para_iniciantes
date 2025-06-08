import requests

url = "https://httpbin.org/get"

resposta = requests.get(url)
print(resposta.json())

print()

data = {
    "meus_dados": [1,2,3],
    "pessoa": {
        "nome": "teste da silva",
        "professor": True
    }
}

params = {
  'data_inicio': '2025-01-01',
  'data_fim': '2025-02-01'
}

url_post = "https://httpbin.org/post"
metodo_post = requests.post(url_post, json=data, params=params)
metodo_post.raise_for_status() # para o código se der erro no status_code

try:
  print(metodo_post.request.url)
except requests.HTTPError as e:
  print(f"Erro ao realizar a request desejada: {e}")
else:
  print('Resultado: ')
  print(metodo_post.json())

print()

body_httpbin = metodo_post.json()
print(body_httpbin['data'].meus_dados)