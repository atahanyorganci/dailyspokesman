from newsapp import app, db
from newsapp.models import Article


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Article': Article}


if __name__ == "__main__":
    app.run()
