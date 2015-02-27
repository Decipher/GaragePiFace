#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask('garagepiface')
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

class Server():
	def run(self):
		app.run(host='0.0.0.0', port=80)

if __name__ == "__main__":
	garagepiface = Server()
	garagepiface.run()