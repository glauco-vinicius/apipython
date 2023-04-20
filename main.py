from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    if request.method == 'GET':
        return 'pong'
    elif request.method == 'POST':
        return 'Received ping'

@app.route('/pong', methods=['GET', 'POST'])
def pong():
    if request.method == 'GET':
        return 'ping'
    elif request.method == 'POST':
        return 'Received pong'

if __name__ == '__main__':
    app.run()
