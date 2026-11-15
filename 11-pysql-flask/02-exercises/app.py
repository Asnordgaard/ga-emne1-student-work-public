from flask import Flask, render_template, request, appcontext_popped
from mysql.connector import Error
from database import get_cities, get_countries, get_regions

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return render_template(
        "index.html",
        title = "Exercise 11",
        heading = "This heading comes from the app route in app.py"
    )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        author = "Asbjørn Nordgaard"
    )

@app.route("/greet")
def greet():
    name = request.args.get("name", "guest").strip()
    if name == "":
        return render_template("greet.html", name = "Nameless person")
    return render_template(
            "greet.html", name = name
        )

@app.route("/cities")
def cities():
    code = request.args.get("country", "NOR").strip().upper() # "NOR" blir standardverdi dersom det ikke blir sendt inn et parameter
    if (len(code) != 3 or not code.isascii() or not code.isalpha()):
        return "Invalid code", 400
    try:
        rows = get_cities(code)
    except Error:
        app.logger.exception(
            "Database query failed"
        )
        return "Database unavailable", 503
    return render_template("cities.html", code = code, rows = rows, count = len(rows))

@app.route("/countries")
def countries():
    region = request.args.get("region", "Antartica")
    region_rows = get_regions()
    countries = get_countries(region)
    return render_template("countries.html", regions_rows = region_rows, region = region, countries = countries)