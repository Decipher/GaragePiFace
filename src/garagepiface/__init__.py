#!/usr/bin/env python

from flask import Flask, render_template, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import SubmitField
from time import sleep
import pifacedigitalio

pifacedigital = pifacedigitalio.PiFaceDigital()

app = Flask('garagepiface')
Bootstrap(app)


class ButtonsForm(Form):
	submit_button = SubmitField('Submit Form')


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		pifacedigital.output_pins[0].toggle()
		sleep(0.5)
		pifacedigital.output_pins[0].toggle()

	form = ButtonsForm()
	return render_template('index.html', form=form)


def main():
	app.config['SECRET_KEY'] = 'devkey'
	app.run(host='0.0.0.0', port=80)


if __name__ == "__main__":
	main()
