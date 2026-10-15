from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Buquê Primavera", "price": "R$ 78,90", "description": "Flores coloridas para deixar qualquer momento mais especial.", "image": "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=900&q=80"},
    {"name": "Rosas Encantadas", "price": "R$ 40,90", "description": "Um clássico delicado com rosas selecionadas.", "image": "https://images.unsplash.com/photo-1494972308805-463bc619d34e?auto=format&fit=crop&w=900&q=80"},
    {"name": "Cesta Jardim", "price": "R$ 78,90", "description": "Uma composição charmosa com flores e folhagens.", "image": "https://images.unsplash.com/photo-1523438885200-e635ba2c371e?auto=format&fit=crop&w=900&q=80"},
    {"name": "Girassóis", "price": "R$ 49,90", "description": "Um toque de alegria e luz para presentear.", "image": "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?auto=format&fit=crop&w=900&q=80"},
    {"name": "Orquídea", "price": "R$ 49,90", "description": "Elegância e beleza para decorar ambientes.", "image": "https://alavoura.com.br/colunas/flores-e-jardins/orquideas-beleza-que-fascina/"},
    {"name": "Arranjo Campestre", "price": "R$ 67,90", "description": "Um arranjo leve inspirado na beleza dos jardins.", "image": "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=900&q=80"}
    ]

@app.route("/")
def home():
    return render_template("index.html", products=products[:3])

@app.route("/flores")
def flores():
    return render_template("flores.html", products=products)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/galeria")
def galeria():
    images = [
        ("Nosso jardim", "https://images.unsplash.com/photo-1497250681960-ef046c08a56e?auto=format&fit=crop&w=1200&q=80"),
        ("Flores frescas", "https://images.unsplash.com/photo-1487070183336-b863922373d4?auto=format&fit=crop&w=1200&q=80"),
        ("Arranjos especiais", "https://images.unsplash.com/photo-1527061011665-3652c757a4d4?auto=format&fit=crop&w=1200&q=80"),
        ("Natureza", "https://images.unsplash.com/photo-1512428813834-c702c7702b78?auto=format&fit=crop&w=1200&q=80"),
        ("Detalhes", "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1200&q=80"),
        ("Primavera", "https://images.unsplash.com/photo-1455582916367-25f75bfc6710?auto=format&fit=crop&w=1200&q=80")
        
    ]
    return render_template("galeria.html", images=images)

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(debug=True)
