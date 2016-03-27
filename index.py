from flask import Flask, render_template
app = Flask(__name__)
from things import THINGS
from list_of_dicts import get_numbers, get_scrapbook_thing

@app.route('/index')
def index():
    return render_template('index.html', things=THINGS)

@app.route('/index/<number>')
def base(number):
    # return list_of_dicts(THINGS, number)
    for number in numbers:
        foo = get_scrapbook_thing(THINGS, number)
    return render_template('base.html', number=number, things=THINGS)


if __name__ == '__main__':
    app.run(debug=True)
