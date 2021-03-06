from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello(name=None):
    if name:
        return "<p>Hello " + name + "!</p>"
    else:
        return "<p>Hello World!</p>"

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)