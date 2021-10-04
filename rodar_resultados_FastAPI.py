from requests import post, get
from json import dump, dumps, load, loads

fastapi = post("http://127.0.0.1:8000/outrarota", json = {"valor1": 10, "valor2": 5, "operação": "divisão"})

resultados = loads(fastapi.text)
if resultados["operação"] == "adição":
    print(resultados["valor1"] + resultados["valor2"])
elif resultados["operação"] == "subtração":
    print(resultados["valor1"] - resultados["valor2"])
elif resultados["operação"] == "multiplicação":
    print(resultados["valor1"] * resultados["valor2"])
elif resultados["operação"] == "divisão":
    print(resultados["valor1"] / resultados["valor2"])
else:
    print("""Operação deve ser 'adição', 'subtração', 'multiplicação' e 'divisão', escritos dessa forma!""")
