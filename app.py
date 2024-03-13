from flask import Flask
from flask_restful import Api
from resources.Funcionario import Funcionario


app = Flask(__name__)
api = Api(app)


api.add_resource(Funcionario,'/funcionario', endpoint='buscar', methods=["GET"])
api.add_resource(Funcionario,'/funcionario', endpoint='incluir', methods=["POST"])
api.add_resource(Funcionario,'/funcionario/<int:id>', endpoint='alterar', methods=["PUT"])
api.add_resource(Funcionario,'/funcionario/<int:id>', endpoint='excluir', methods=["DELETE"])

if __name__ == '__main__':
    app.run(debug=True)

