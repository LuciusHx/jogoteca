import os

SECRET_KEY = 'ADMIN'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql',
        usuario='root',
        senha='admin',
        servidor='localhost',
        database='jogoteca'
    )
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/jogoteca'


UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'

#pra fazer igual o caboco falou
#+mysqlconnector