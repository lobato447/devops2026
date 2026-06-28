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

    conteudo_esperado = """<h1>Integrantes</h1>
<br>
Mauricio Lobato Moraes"""

    assert conteudo_esperado == conteudo_da_resposta

def test_livros(client):
    resposta = client.get("/livros")
    conteudo_da_resposta = resposta.text

    assert resposta.status_code == 200
    assert "<h1>Livros</h1>" in conteudo_da_resposta


def test_livros_titulo(client):
    resposta = client.get("/livros")
    assert "Título:</strong> 1984" in resposta.text


def test_livros_autor(client):
    resposta = client.get("/livros")
    assert "Autor:</strong> George Orwell" in resposta.text


def test_livros_issn(client):
    resposta = client.get("/livros")
    assert "ISSN:</strong> 1234" in resposta.text


def test_livros_data_publicacao(client):
    resposta = client.get("/livros")
    assert "Data de Publicação:</strong>" in resposta.text


def test_livros_qtde_paginas(client):
    resposta = client.get("/livros")
    assert "Quantidade de Páginas:</strong> 350" in resposta.text

