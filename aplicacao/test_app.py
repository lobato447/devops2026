import pytest
from app import APP

import pytest
from app import APP

@pytest.fixture()
def client():
    app = APP
    app.config.update({
        "TESTING": True
    })

    yield app.test_client()

def test_index(client):
    resposta = client.get("/")
    conteudo_da_resposta = resposta.text

    assert """<h1>Mauricio Lobato</h1>
<h1>Mauricio Lobato</h1>""" == conteudo_da_resposta
