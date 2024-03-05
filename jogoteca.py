from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt


#iniciar Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')

#Banco de Dados
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)


from views_games import *
from views_user import *

#rodar
if __name__ == '__main__':
    app.run(debug=True)



