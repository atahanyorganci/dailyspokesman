from newsapp import create_app
from newsapp import tasks

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
