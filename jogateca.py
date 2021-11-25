from flask import Flask, render_template, request, redirect
from classe_jogo import Jogo
app = Flask(__name__)

tetris = Jogo('Tetris', 'diversao', 'pc')
domino = Jogo('Dominó', 'mesa', 'Play 1')
cartas = Jogo('Cartas', 'mesa', 'Xbox')
lista = [tetris,domino,cartas]

@app.route('/')
def ola():
    return render_template('lista.html', titulo = 'Jogos',jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo = 'Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    #vamos atribuir a variável nome o campo do input de novo.html com o name = nome
    nome = request.form['nome']

    #faremos o mesmo pra categoria e console
    categoria = request.form['categoria']

    console = request.form['console']

    #criamos e instanciamos um objeto com os dados recebidos
    jogo = Jogo(nome,categoria,console)

    #e depois adicionamos o objeto a nossa lista de jogos
    lista.append(jogo)

    #agora precisamos retornar algo pra informar ao usuário que a ação funcionou, nesse caso mostraremos a nova lista
    return redirect('/')

#passando o Parâmetro debug=True, não precisamos a tod'o' momento restartar o server
app.run(debug=True)

#Para definir a porta como 8080 e o host como 0.0.0.0 devemos chamar o run da seguinte maneira.
# trecho da app , neste caso pessoas que tiverem na mesma rede consegue ver aplicação
#app.run(host='0.0.0.0', port=8080)