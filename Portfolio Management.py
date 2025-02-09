from flask import Flask, render_template
from empyrial import empyrial, Engine

app = Flask(__name__)

@app.route('/')
def portfolio_analysis():
    portfolio = Engine(
        start_date="2020-06-09",
        portfolio=["NHPC.NS", "GAILF", "ATGL.NS", "IDFCFIRSTB.NS", "IDFCFIRSTB.NS"],
        weights=[0.2, 0.2, 0.2, 0.2, 0.2],
        benchmark=["SPY"]
    )
    results = empyrial(portfolio)
    return render_template('portfolio.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
