from flask import Flask
app = Flask(__name__)

@app.route("/sum/<x>/<y>")
def sum():
    sum = x+y
    return {"Result":sum}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)
    