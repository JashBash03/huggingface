#TODO Mostrar la respuesta en lenguaje natural, por ejemplo:
#"El sentimiento es mayormente positivo" o "El sentimiento es mayormente negativo"
import requests
import dotenv
import os

dotenv.load_dotenv()
TOKEN = os.getenv("Token")

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": f"Bearer {TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I love gambling",
})

print(output)