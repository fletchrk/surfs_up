from flask import Flask

app = Flask(__name__)

@app.route('/')
def hi_Rachel():
    return 'Hi Rachel'