from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')
    return 'Hello,Jassea !!!'

if __name__ == 'main':
    app.run(debug=True,port=2000)