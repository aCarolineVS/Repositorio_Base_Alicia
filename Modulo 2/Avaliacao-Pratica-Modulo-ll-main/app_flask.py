from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route("/soma")
def soma():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    resultado = valor1 + valor2

    return {"resultado": resultado}

@app.route("/subtrair")
def subtracao():
     valor1 = float(request.args.get("valor1"))
     valor2 = float(request.args.get("valor2"))
     resultado = valor1 - valor2

     return {"resultado": resultado}

@app.route("/multiplicar")
def multiplicacao():
      valor1 = float(request.args.get("valor1"))
      valor2 = float(request.args.get("valor2"))
      resultado = valor1 * valor2

      return {"resultado": resultado}

@app.route("/dividir")
def divisao():
       valor1 = float(request.args.get("valor1"))
       valor2 = float(request.args.get("valor2"))
       

       if valor2 == 0:
        return {"erro": "Divisao por zero nao e permitida"}
       resultado = valor1 / valor2
            
       return {"resultado": resultado}


if __name__ == "__main__":
    app.run(debug=True)
