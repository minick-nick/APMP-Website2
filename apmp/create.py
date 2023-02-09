""" from apmp import db, app
from apmp.models import Client


def go():
    c = Client()

    c.f_name = 'Dominic'
    c.m_name = 'sdfsdf'
    c.l_name = 'sfsdfsfsdf'
    c.number = '10120444'
    c.email = 'ssdfsdfs3dfs'


    app.app_context().push()

    db.session.add(c)
    db.session.commit()
"""