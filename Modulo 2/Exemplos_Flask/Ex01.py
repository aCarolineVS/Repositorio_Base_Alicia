from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/sobre")
def sobre():
    return "Oieee, sou Alicia."

@app.route("/ola/<nome>")
def ola(nome): 
    return f'Ola {nome}!! Seja Bem Vindo(a)!!'

@app.route("/dobro/<int:numero>")
def dobro(numero):
    return f'O dobro de {numero} é {numero*2}'

if __name__ == "__main__":
    app.run(debug=True)