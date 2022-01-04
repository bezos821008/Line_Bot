from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return('首頁')

@app.route('/response/<string:name>')
def response(name):
    return("{}".format(name))

@app.route('/get_test/',methods=['GET'])
def get_test():
    get_test_name = request.args.get('get_test_name')
    return("{}".format(get_test_name))

if __name__ == '__main__':
    app.run()