from flask import Flask, render_template, request, logging, Response, redirect, flash

app = Flask(__name__)

@app.route('/', methods = ["GET" , "POST"])
def index():
   if request.method == 'POST':
       # Get name = "user_id" on form
       user_id = request.form['user_id']
       return render_template('index.html', user_id = user_id)
   else:
       return render_template('index.html')


app.run(host="localhost")