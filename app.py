from flask import Flask, render_template

app Flask (name_)

@app.route("/")

def home():

return render_template(r"index.html")

if name__ == "main":

app.run (debug=False, port=8000)