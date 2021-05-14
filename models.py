from sqlalchemy import Table, Column, Integer, String, ForeignKey, BigInteger, DECIMAL, Text, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'

    id = Column(BigInteger, primary_key=True)
    username = Column(String(50))
    password = Column(String(50))
    nombre = Column(String(100))
    email = Column(String(100))
    admin = Column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}"

class Category(Base):
    __tablename__ = "categoria"

    id = Column(BigInteger, primary_key=True)
    nombre = Column(String(100))

class Article(Base):
    __tablename__= "articulo"

    id = Column(BigInteger, primary_key=True)
    nombre = Column(String(100))
    precio = Column(DECIMAL)
    iva = Column(DECIMAL)
    descripcion = Column(String(100))
    imagen = Column(String(100))
    stock = Column(Integer)
    id_categoria = Column(ForeignKey('categoria.id'), nullable=False)


car_table = Table('carrito', Base.metadata,
Column('id_articulo', ForeignKey('articulo.id'), nullable=False),
Column('id_usuario', ForeignKey('usuario.id'), nullable=False),
Column('cantidad', Integer, nullable=False),
)

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://root:finsocial123@localhost/articulos")
    with engine.connect() as conn:
        Base.metadata.create_all(engine)
        print("Create Tables")

#Example with Simple Constraints

# def migrate():
#     engine = create_engine("mysql+mysqldb://root:finsocial123@localhost/articulos")

#     with engine.connect() as conn:
#         metadata = Metadata()

        # user_table = Table(
        #     "usuario",
        #     metadata,
        #     Column('id', BigInteger, primary_key=True),
        #     Column('username', String(50)),
        #     Column('password', String(50)),
        #     Column('nombre', String(100)),
        #     Column('email', String(100)),
        #     Column('admin', String(100)),
        # )

        # category_table = Table(
        #     "categoria",
        #     metadata,
        #     Column('id', BigInteger, primary_key=True),
        #     Column('nombre', String(100))
        # )

        # article_table = Table(
        #     "articulo",
        #     metadata,
        #     Column('id', BigInteger, primary_key=True),
        #     Column('nombre', String(100)),
        #     Column('precio', DECIMAL),
        #     Column('iva', DECIMAL),
        #     Column('Descripcion', Text),
        #     Column('imagen', String(100)),
        #     Column('stock', Integer),
        #     Column('id_categoria', ForeignKey('categoria.id'), nullable=False),
        # )

        # carrito_table = Table(
        #     "carrito",
        #     metadata,
        #     Column("articulo", ForeignKey('articulo.id'), nullable=False),
        #     Column("id_usuario", ForeignKey('usuario.id'), nullable=False),
        #     Column("cantidad", Integer, nullable=False),
        # )
        # metadata.create_all(engine)
