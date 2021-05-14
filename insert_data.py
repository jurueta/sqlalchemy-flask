from models import Article, Category, User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def insert(session):
    user_urueta = User(username="urueta01", password="21121999", nombre="Jesus Urueta", email="sistemas22@red5g.co", admin=1)
    user_shannon = User(username="shannon", password="78945623", nombre="Shannon Villa", email="sistemas23@red5g.co", admin=0)
    user_danny = User(username="danny", password="785154", nombre="Danny Ospino", email="sistemas24@red5g.co", admin=1)
    user_nacha = User(username="nacha", password="78945622", nombre="Ignacia Cantillo", email="sistemas25@red5g.co", admin=0)

    session.add(user_urueta)
    session.add(user_shannon)
    session.add(user_danny)
    session.add(user_nacha)

    session.flush()
    session.commit()

    category_vegetables = Category(nombre='vegetales')
    category_meat = Category(nombre='Carnes')
    category_cleanliness = Category(nombre='Aseo')

    session.add(category_vegetables)
    session.add(category_meat)
    session.add(category_cleanliness)

    session.flush()
    session.commit()

    article_corn = Article(nombre="Maiz", precio=5000, iva=500, descripcion="Maiz tierno crudo", imagen="https://s1.eestatic.com/2020/01/10/ciencia/nutricion/maiz-cereales-salud_458715971_142137584_1706x960.jpg", stock=5, id_categoria=1)
    article_onion = Article(nombre="Cebolla", precio=300, iva=90, descripcion="Cebolla morada", imagen="https://www.lavanguardia.com/files/article_main_microformat/uploads/2018/07/13/5e99856f0b685.jpeg", stock=10, id_categoria=1)
    article_res = Article(nombre="Espaldilla", precio=6000, iva=100, descripcion="carne Espaldilla de res", imagen="https://cdn.shopify.com/s/files/1/0469/4966/2885/products/ESPALDILLA.jpg?v=1601131736", stock=50, id_categoria=2)
    article_soap = Article(nombre="Jabon", precio=7500, iva=320, descripcion="Jabon de cocina", imagen="https://www.cocinavital.mx/wp-content/uploads/2017/08/como-hacer-jabon-liquido-lavatrastes-casero-y-ecologico-00.jpg", stock=20, id_categoria=3)

    session.add(article_corn)
    session.add(article_onion)
    session.add(article_res)
    session.add(article_soap)

    session.flush()
    session.commit()
    session.close()


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://root:finsocial123@localhost/articulos")
    with engine.connect() as conn:
        session = Session(engine)
        insert(session)
        print("Data Inserted")