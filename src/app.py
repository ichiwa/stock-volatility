import datetime
from flask import Flask, render_template, request
from stocks import get_stock_info

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', title='Japanese Stock Info')

@app.route('/', methods=['POST'])
def showv():
  if request.method == 'POST':
    code = request.form['company_code']
  else:
    code = request.args.get('company_code')
  volatilities = {'last_one_year': {}, 'last_three_year': {}}
  now = datetime.datetime.now()
  start_date = datetime.date(now.year - 1, now.month, 1)
  end_date = datetime.date(now.year, now.month, 1)
  volatilities['last_one_year'] = get_stock_info(code, start_date, end_date)
  start_date = datetime.date(now.year - 3, now.month, 1)
  volatilities['last_three_year'] = get_stock_info(code, start_date, end_date)
  title = 'Stock Informatoion {}'.format(code)
  return render_template('stocks.html', title=title, volatilities=volatilities)
