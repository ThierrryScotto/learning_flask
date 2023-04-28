from flask import Flask, render_template

app = Flask(__name__)


# decorator - atribui uma 
@app.route("/")
def homepage():
  # return "This is my first web site using Flask"
  return render_template("homepage.html")

@app.route('/test')
def test():
  return "this is a test"

@app.route('/contatos')
def contatos():
  return render_template('contatos.html')

@app.route('/html')
def html():
  return "<h1>Using  HTML</h1>"

@app.route('/usuarios/<user_name>')
def usuarios(user_name):
  # return f"You are {user_name}"
  return render_template('usuarios.html', user_name = user_name)

if __name__ == "__main__":
  # Rodando a aplicação
  app.run(debug=True)