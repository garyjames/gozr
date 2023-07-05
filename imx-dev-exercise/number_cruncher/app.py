"""
Impliment the methods below as documented in the comment. Feel free to change the parameters as
you see fit. The data for all these queries can be found in the database in this repo. Be aware
that not all data is correct and some fields may be None or 0...
"""

import sqlite3
import sys


db_connection = sqlite3.connect('data.db', check_same_thread=False)
db_connection.row_factory = sqlite3.Row
db_cursor = db_connection.cursor()


def printrows(results):
    """https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.description
    To remain compatible with the Python DB API, it returns a 7-tuple for each
    column where the last six items of each tuple are None.
    """

    columns = list(map(lambda x: x[0], results.description))
    for result in results:
        record = list(zip(columns,result))
        for elem in record:
            column, value = elem
            print(f'{column} = {value}')
        print('\n\n')


def avg_ev_range():
    """Calculate the average range of the electric vehicles in the database
    Find the average range of the vehicles in the data base where that data exists.
    """

    query = """
    select avg(electric_range) as avg_range
    from electric_vehicles
    where electric_range > 0
    """

    return query


def make_highest_avg_ev_range():
    """Of all the makes in the database, which has the highest overall average range
    """

    query = """
    with make_avg_range as (
        select make, avg(electric_range) avg_range
        from electric_vehicles
        where electric_range > 0
        group by make
    )
    select make, max(avg_range) as avg_range from make_avg_range
    """

    return query


def most_common_year():
    """Find the most common model year of cars in the database
    """

    query = """
    select model_year, max(models_per_year) models_per_year
    from (
        select model_year, count(*) as models_per_year
        from electric_vehicles
        group by model_year
        )
    """

    return query


def hybrid_market_share():
    """Find the market share of hybrid vehicles in the dataset
    Of all the vehicles in the dataset, what percentage are hybrid vehicles.
    """

    query = """
    with hybrid_count as (
        select count(1) as h_count
        from electric_vehicles
        where ev_type = 'Plug-in Hybrid Electric Vehicle'
    ),
    electric_count as (
        select count(1) as e_count
        from electric_vehicles
        where ev_type = 'Battery Electric Vehicle'
    )
    select 100*cast(h_count as real)/cast(e_count as real) hybrid_pct
    from hybrid_count, electric_count
    """

    return query


def most_common_car():
    """of all the cars in the database, what car (Make, model, and year) is the
    most common
    """

    query = """
    with model_counts as (
        select make, model, model_year, count(1) model_count
        from electric_vehicles
        group by make, model, model_year
    )
    select make, model, model_year, max(model_count) as model_count
    from model_counts
    """

    return query


def most_prolific_make():
    """Of all the Makes in the database, which has the most unique cars(Model, year)
    """

    query = """
    with models as (
        select make, model, model_year
        from electric_vehicles
        group by make, model, model_year
    ),
    make_unique_models as (
        select make, count(1) make_unique_models
        from models
        group by make
    )

    select make, max(make_unique_models) as most_unique_models
    from make_unique_models
    """

    return query


def newest_postal_code():
    """On average, what postal code has the most recent model year
    """

    query = """
    with postal_code_avg as (
        select postal_code, avg(model_year) avg_model_year
        from electric_vehicles
        group by postal_code
    )
    select postal_code, avg_model_year from postal_code_avg
    where avg_model_year = (select max(avg_model_year) from postal_code_avg)
    """

    return query


def range_growth():
    """How much higher is the averge ev range between cars of a model year on or before
    before 2010 and cars of a model year on or after 2020
    """

    query = """
    with
    new_avg_range as (
    select distinct make, model, model_year, avg_range
    from (
        select make, model, model_year, electric_range,
        avg(electric_range) over (partition by make, model) as avg_range
        from electric_vehicles
        where electric_range > 0 and
            model_year >= 2020
            group by make, model, model_year
        )
    ),
    old_avg_range as (
    select distinct make, model, model_year, avg_range
    from (
        select make, model, model_year, electric_range,
        avg(electric_range) over (partition by make, model) as avg_range
        from electric_vehicles
        where electric_range > 0 and
            model_year <= 2010
            group by make, model, model_year
        )
    )

    select make, model, avg_range from new_avg_range
    group by make, model
    """

    return query


def main():
    print("hello foo")
    func_list = [
        avg_ev_range,
        make_highest_avg_ev_range,
        most_common_year,
        hybrid_market_share,
        most_common_car,
        most_prolific_make,
        newest_postal_code,
        #range_growth
        ]

    for func in func_list:
        print('\nQuestion: ', func.__doc__)
        query = func()
        ret = db_cursor.execute(query)
        printrows(ret)



# Call your completed functions and output the results below...

if __name__ == "__main__":
    sys.exit(main())
