from apmp import db, app
from apmp.models import Client


def create_client():
    c = Client()

    c.f_name = 'Dominic'
    c.m_name = 'sdfsdf'
    c.l_name = 'sfsdfsfsdf'
    c.number = '1012044444444'
    c.email = 'ssdfsdfs3dfs444'


    app.app_context().push()

    db.session.add(c)
    db.session.commit()

    print("Hello")