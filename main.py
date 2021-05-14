from flask import Flask
from sqlalchemy import create_engine, text

app = Flask(__name__)

@app.route('/')
def index():
    

    
        result = conn.execute(text("select 'Hello world!'"))
        return result.all()[0][0]

if __name__ == '__main__':
    app.run(port=80, debug=True)