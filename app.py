
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



from flask  import Flask, render_template #primeiro sempre chamar flask com letra minuscula e depois Flask com letra maiuscula

app = Flask("Hello") # criou serviço

@app.route('/hello') # criou um link/url, por enquanto só uma segunda parte de uma URL normal
def hello():   # funçao que será chamada
    return render_template ("hello.html") # sera mostrada na página

#@app.route('/tchau') # criou um link/url, por enquanto só uma segunda parte de uma URL normal
#def tchau():   # funçao que será chamada
#return "Tchauuuuu!!!!" # sera mostrada na página