from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome to Docker with EC2</h1>"

@app.route("/deploy")
def deploy_cmd():
    return "<p>Deploy check</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)    