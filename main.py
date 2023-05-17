from flask import Flask,request,jsonify

main = Flask(__name__)

@main.route('/')
def index():
    return "Hello world"

if __name__ == '__main__':
    main.run(debug=True)
