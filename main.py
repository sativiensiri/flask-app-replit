from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route("/")
def index():
  name = "Sati Viensiri"
  print(f"Hello Mr.{name}")
  return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
  if request.method == 'POST':
      email = request.form.get('email')
      password = request.form.get('password')
      if email != "" and password != "":
        print(f"We have {email} and {password}")
        return render_template("home.html")
      else:
        return redirect(url_for('index'))
      

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
