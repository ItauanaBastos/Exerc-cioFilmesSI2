from flask import Flask, render_template, request

app = Flask(__name__)

# Conjunto de dados de filmes
filmes = [
    {"nome": "Mad Max", "genero": "Ação"},
    {"nome": "Tropa de Elite", "genero": "Ação"},
    {"nome": "As Branquelas", "genero": "Comédia"},
    {"nome": "Tô Rica", "genero": "Comédia"},
    {"nome": "Corra", "genero": "Terror"},
    {"nome": "Invocação do Mal", "genero": "Terror"},
    {"nome": "Moana", "genero": "Animação"},
    {"nome": "Enrolados", "genero": "Animação"},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    sugestoes = []
    if request.method == 'POST':
        genero_preferido = request.form['genero'].capitalize()
        # Filtra os filmes com o gênero escolhido
        sugestoes = [f['nome'] for f in filmes if f['genero'] == genero_preferido]
    return render_template('index.html', sugestoes=sugestoes)

if __name__ == '__main__':
    app.run(debug=True)
