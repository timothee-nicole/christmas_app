import sys
import os
sys.path.append(os.getcwd())

from app import app, db
from app.models import Users
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': Users}


if __name__ == '__main__':

    app.run()
