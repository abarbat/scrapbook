# coding: utf-8

from flask import Flask, render_template
from things import THINGS

app = Flask(__name__)

# retrieve all the titles from the dataset and put them into a list
def get_numbers(source):
    numbers = []
    # loop through the source list
    for row in source:
        number = row["number"]
        title = row['title']
        # add the num to the list
        numbers.append([number, title])
    return sorted(numbers)

# find the row that matches the title, retrieve author and year for that title
def get_scrapbook_thing(source, number):
    for row in source:
        if number == row["number"]:
            #this is saying: if input number is the same as the "number" in your row in the data set, do this
            # decode() handles accented characters in foreign names
            title = row["title"].decode('utf-8')
            year = row["year"]
            description = row["description"]

    return number, title, year, description

    # File "/Users/Adriana/Documents/Python/scrapbook_project/index.py", line 39, in base
    # number, title, year, description = get_scrapbook_thing(THINGS, number)
    # File "/Users/Adriana/Documents/Python/scrapbook_project/index.py", line 29, in get_scrapbook_thing
    # return number, title, year, description
    # UnboundLocalError: local variable 'title' referenced before assignment




@app.route('/index')
def index():
    numbers = get_numbers(THINGS)
    return render_template('index.html', numbers=numbers)

@app.route('/index/<number>')
def base(number):
    number, title, year, description = get_scrapbook_thing(THINGS, number)
    print number, title

    return render_template('base.html', number=number, title=title, year=year, description=description)






if __name__ == '__main__':
    app.run(debug=True)
