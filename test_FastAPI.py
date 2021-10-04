import pytest
from requests import get, post
from json import loads

class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok

    def test_APIresponse(self):
        resp = get(self.url)
        message = loads(resp.text)
        assert message["message"] == "Mentorama"

    def test_POSTmethod(self):
        resp = post(self.url + "/outrarota",
                    json = {"valor1" : 10, "valor2" : 5, "operação" : "adição"})
        message = loads(resp.text)
        resposta_final = {
                            "valor1" : 10,
                            "valor2" : 5,
                            "operação" : "adição"
        }
        assert message == resposta_final
