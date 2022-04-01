import json
import random
from flask import render_template, redirect, url_for, request

from app import app
from app.forms import InputForm

with open('quotes.json') as f:
    quotes = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    quote_arr = []
    form = InputForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            goal = form.goal.data
            keyword = form.keyword.data
            quotekey = " " + keyword + " "
            for i in range(len(quotes)):
                if quotekey in quotes[i]['quoteText']:
                    quote_arr.append(quotes[i]['quoteText'])
            quote = quote_arr[random.randint(0, len(quote_arr))]
                
        return redirect(url_for('quote', quote=quote, goal=goal))
                
    return render_template('index.html', title='Home', form=form)

@app.route('/quote', methods=['GET', 'POST'])
def quote():
    goal = request.args.get('goal')
    quote = request.args.get('quote')
    quotePresent = quote != None
    if not quotePresent:
        quote = quotes[random.randint(0, len(quotes))]['quoteText']
        return render_template('quote.html', title='Your Quote', quote=quote, goal=goal)
    return render_template('quote.html', title='Your Quote', goal=goal, quote=quote)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/help')
def help():
    return render_template('help.html', title='Help')

@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 500