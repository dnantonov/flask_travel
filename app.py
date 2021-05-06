import data
import random

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    random_tours = sorted(data.tours.items(), key=lambda x: random.random())[:6]

    return render_template('index.html', tours=random_tours)


@app.route('/departures/<departure>/')
def departure(departure):
    current_departure = data.departures[departure]
    departure_tours = {}
    for key, tour in data.tours.items():
        if tour['departure'] == departure:
            departure_tours[key] = tour
    prices = [x['price'] for x in departure_tours.values()]
    min_price = min(prices)
    max_price = max(prices)
    nights = [x['nights'] for x in departure_tours.values()]
    min_nights = min(nights)
    max_nights = max(nights)
    return render_template('departure.html',
                            tours=departure_tours.items(),
                            departure=current_departure,
                            min_price=min_price,
                            max_price=max_price,
                            min_nights=min_nights,
                            max_nights=max_nights)


@app.route('/tours/<int:id>/')
def tour(id):
    tour = data.tours[id]
    departure = data.departures[tour["departure"]]
    stars = "★ " * int(tour["stars"])
    return render_template('tour.html',
                            tour=tour,
                            departure=departure,
                            stars=stars)


if __name__ == '__main__':
    app.run(host='localhost')