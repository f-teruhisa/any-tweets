from flask import Flask, render_template, request, logging, Response, redirect, flash

app = Flask(__name__)

@app.route('/', methods = ["GET" , "POST"])
def index():
   if request.method == 'POST':
       return render_template('index.html')
   else:
       return render_template('index.html')

app.run(host="localhost")