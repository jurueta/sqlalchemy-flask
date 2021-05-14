from flask import Flask, make_response, jsonify
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Article, Category, User

app = Flask(__name__)

@app.route('/api/v1/category', methods=['GET'])
def category():
    engine = create_engine("mysql+mysqldb://root:finsocial123@localhost/articulos")
    with engine.connect() as conn:
        session = Session(engine)
        result = session.execute(select(Category)).all()
        categories = list()
        print(result)
        for i in result:
            categories.append({'nombre': i[0].nombre})
        
        data = {
            'category': categories
        }

        return make_response(jsonify(data), 200)



@app.route('/api/v1/user', methods=['GET'])
def user():
    engine = create_engine("mysql+mysqldb://root:finsocial123@localhost/articulos")
    with engine.connect() as conn:
        session = Session(engine)
        result = session.execute(select(User)).all()
        users = list()
        print(result)
        for i in result:
            users.append({
                'nombre': i[0].nombre,
                'username': i[0].username,
                'email': i[0].email,
                'admin': i[0].admin
                })
        
        data = {
            'users': users
        }

        return make_response(jsonify(data), 200)

@app.route('/api/v1/article', methods=['GET'])
def article():
    engine = create_engine("mysql+mysqldb://root:finsocial123@localhost/articulos")
    with engine.connect() as conn:
        session = Session(engine)
        result = session.execute(select(Article)).all()
        articles = list()
        print(result)
        for i in result:
            articles.append({
                'nombre': i[0].nombre,
                'precio': str(i[0].precio),
                'iva': str(i[0].iva),
                'descripcion': i[0].descripcion,
                'imagen': i[0].imagen,
                'stock': i[0].stock,
                'id_categoria': i[0].id_categoria,
                })
        
        data = {
            'articles': articles
        }

        return make_response(jsonify(data), 200)

if __name__ == '__main__':
    app.run(port=80, debug=True)