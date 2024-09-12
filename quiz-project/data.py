import requests

parmas = {
    "amount": 10,
    "type": "boolean",
    "difficulty": "easy"
}

connection = requests.get("https://opentdb.com/api.php", params=parmas )
connection.raise_for_status()
question_data = connection.json()["results"]