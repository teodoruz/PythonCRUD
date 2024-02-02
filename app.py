from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo':'o senhor dos da aneis',
        'autor': 'j.r.r tolkien'
    },
    {
        'id':2,
        'título':'harry potter',
        'autor':'J.K.HOWLING'
    }
]
#retornando todos os livros
@app.route('/livros')
def obter_livros():
    return jsonify(livros)

#buscando por id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#alterando um livro passando um corpo Json
@app.route('/livros/alter/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro[indice] == id:
            return jsonify(livros[indice])


#cadastrando um novo livro
@app.route('/livros', methods=['POST'])
def incluir_livros():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


#deletando um livro por ID
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros.remove(livro)
    return jsonify(livros)



app.run(port=5000, host='localhost', debug=True)
