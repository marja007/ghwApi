from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_ghw():
    return"<p>Hello You gorgeous<p>"

if __name__=="__main_2":
    app.run(debug=True)