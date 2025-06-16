import os
import requests
from pprint import pprint
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

# Essa classe está fazendo a conversão do base64 igual na aula07
auth = HTTPBasicAuth(username=client_id, password=client_secret)

url = 'https://accounts.spotify.com/api/token'
body = {
  'grant_type': 'client_credentials'
}

resposta = requests.post(url=url, data=body, auth=auth)

try:
  resposta.raise_for_status()
except requests.HTTPError as e:
  print(f"Erro no request: {e}")
  resultado = None
else:
  resultado = resposta.json()

token = resultado['access_token']
# pprint(token)


id_artista = "6iAY2AyUZLSX3PWLIAfFZY"
url = f"https://api.spotify.com/v1/artists/{id_artista}"
headers = {
  'Authorization': f"Bearer {token}"
}

resposta = requests.get(url=url, headers=headers)

try:
  resposta.raise_for_status()
except requests.HTTPError as e:
  print(f"Erro no request: {e}")
  resultado = None
else:
  resultado = resposta.json()

pprint(resultado)

