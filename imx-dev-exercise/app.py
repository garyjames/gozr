from flask import Flask, render_template
import number_cruncher.app as nc

app = Flask(__name__)

def pageresults(results):
    viewlist = []
    columns = list(map(lambda x: x[0], results.description))
    for result in results:
        record = list(zip(columns,result))
        for elem in record:
            column, value = elem
            viewlist.append(f'{column} = {value}')
    return viewlist


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/avg_ev_range')
def avg_ev_range():
    query = nc.avg_ev_range()
    results = nc.db_cursor.execute(query)
    return render_template('/renderview.html', results=pageresults(results))

@app.route('/make_highest_avg_ev_range')
def make_highest_avg_ev_range():
    query = nc.make_highest_avg_ev_range()
    results = nc.db_cursor.execute(query)
    return render_template('/renderview.html', results=pageresults(results))

@app.route('/most_common_year')
def most_common_year():
    query = nc.most_common_year()
    results = nc.db_cursor.execute(query)
    return render_template('/renderview.html', results=pageresults(results))

@app.route('/hybrid_market_share')
def hybrid_market_share():
    query = nc.hybrid_market_share()
    results = nc.db_cursor.execute(query)
    return render_template('/renderview.html', results=pageresults(results))

@app.route('/most_common_car')
def most_common_car():
    query = nc.most_common_car()
    results = nc.db_cursor.execute(query)
    return render_template('/renderview.html', results=pageresults(results))

@app.route('/most_prolific_make')
def most_prolific_make():
    query = nc.most_prolific_make()
    results = nc.db_cursor.execute(query)
    return render_template('/renderview.html', results=pageresults(results))

@app.route('/newest_postal_code')
def newest_postal_code():
    query = nc.newest_postal_code()
    results = nc.db_cursor.execute(query)
    return render_template('/renderview.html', results=pageresults(results))

@app.route('/range_growth')
def range_growth():
    query = nc.range_growth()
    results = nc.db_cursor.execute(query)
    return render_template('/renderview.html', results=pageresults(results))
