import requests

url = "https://www.google.com.br"

resposta = requests.get(url)
print(resposta)
# print(resposta.text)

with open('pagina_google_requests.html', 'w') as arquivo:
  arquivo.write(resposta.text)
