from things import THINGS
# the data file above follows this file in this gist

# retrieve all the titles from the dataset and put them into a list
def get_numbers(source):
    numbers = []
    # loop through the source list
    for row in source:
        number = row["number"]
        # add the title to the list
        numbers.append(number)
    return sorted(numbers)

# find the row that matches the title, retrieve author and year for that title
def get_scrapbook_thing(source, number):
    for row in source:
        if number == row["number"]:
            # decode() handles accented characters in foreign names
            title = row["title"].decode('utf-8')
            year = row["year"]
            description = row["description"]

    return number#, title, year, description
    # UnboundLocalError: local variable 'title' referenced before assignment

# run the functions and use variables to hold what they return
numbers = get_numbers(THINGS)


for number in numbers:
    foo = []
    foo.append(get_scrapbook_thing(THINGS, number))
# this doesnt do anything
