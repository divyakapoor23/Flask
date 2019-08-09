from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def Dojo():
    return 'Dojo!'

@app.route('/say/michael')
def hello(michael):
    print(name)
    return "Hello Michael!"

@app.route('/say/flask')
def flask():
    return "Hello Flask!"

@app.route('/say/john')
def john():
    return "Hello John!"

@app.route("/repeat/<num>/hello")
def crazy(num):
    hoho = int(num)
    return f" hellos "* hoho


@app.route("/repeat/<x>/bye")
def crazy1(x):
    lulu = int(x)
    return f" hello "* lulu


@app.route("/repeat/<num>/dogs")
def crazy2(y):
    lemon = int(y)
    return f" hellos "* lemon

if __name__ =="__main__":
    app.run(debug=True)