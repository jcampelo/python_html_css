
# instalar o flask - pip install flask
# flask --version
# para rodar o codigo flask usar o comando no terminal "flask run"
# pra rodar as alterações realizadas tem que derrubar com ctrl+c 
# pip freeze --- para saber o que o python tem instalado
# pip freeze > requirements.txt    ---- para criar pacote do pip
# pip install -r requirements.txt
# pip install python-dotenv  --- > comando para rodar modo debug
# https://developer.mozilla.org/en-US/docs/Web/HTML/Element - para referencia de html
# https://www.w3schools.com/ - para referencia html
# git add .
# git commit -m "aula 1"
# git push

from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"
SECRET_KEY = "chave"

app = Flask("Hello")
app.config.from_object(__name__)

def conecta_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.bd = conecta_bd()

@app.teardown_request
def depois_requisicao(e):
    g.bd.close()

@app.route("/")
def exibir_entradas():
    sql = "SELECT titulo, texto, criado_em FROM entradas ORDER BY id DESC"
    cur = g.bd.execute(sql)
    entradas = []
    for titulo, texto, criado_em in cur.fetchall():
        entradas.append({"titulo": titulo, "texto": texto, "criado_em": criado_em})
    return render_template("layout.html", entradas=entradas)

#@app.route('/tchau') # criou um link/url, por enquanto só uma segunda parte de uma URL normal
#def tchau():   # funçao que será chamada
#return "Tchauuuuu!!!!" # sera mostrada na página
# sqlite3 banco.bd < esquema.sql  --- comando para criar o arquivo banco.bd