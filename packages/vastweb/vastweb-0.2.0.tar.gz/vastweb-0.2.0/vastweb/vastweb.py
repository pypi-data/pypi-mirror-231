from flask import Flask, render_template, request

app = Flask(__name__)

def run():
    app.route('/')
    def main():
        return render_template('index.html')
    app.run(host='0.0.0.0')