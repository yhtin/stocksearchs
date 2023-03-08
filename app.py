from flask import Flask, render_template, request
from nsetools import Nse

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    nse = Nse()
    options = nse.get_stock_codes()
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        try:
            stocks = nse.get_quote(stock_name)
            current_price = stocks['lastPrice']
            low52 = stocks['low52']
            high52 = stocks['high52']
            return render_template('home.html', options=options, current_price=current_price, low52=low52, high52=high52, selected=stock_name)
        except IndexError:
            error = f"Stock not found: {stock_name}"
            return render_template('home.html', options=options, error=error)
    return render_template('home.html', options=options)


if __name__ == '__main__':
    app.run(debug=True)
