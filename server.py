from flask import Flask,render_template

app = Flask(__name__)

@app.route('/playground')
def first_round():
    return render_template("index.html",num=3,color="green")

@app.route('/playground/<int:num>')
def second_round(num):
    return render_template("index.html", num=num, color="blue")

@app.route('/playground/<int:num>/<color>')
def third_round(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)
