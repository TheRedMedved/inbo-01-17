from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/trm')
def hello_world_trm():
    return 'Hello, my name is Alexandr'

@app.route('/v2')
def another_text():
    return 'Another Text'

<<<<<<< HEAD
@app.route('/trm')
def hello_world_trm():
    return 'Hello, my name is Alexandr'

@app.route('/trm')
def hello_world_test():
    return 'test complite!'
=======
@app.route('/capchik')
def capchik():
    return 'Макущенко Максим'

@app.route('/danilkashtan')
def danilkashtan():
    return 'Асоян Данила'
>>>>>>> master
