import code

from flask import Flask, render_template, request, redirect

from mysql.connector import Error

from database import get_cities
import database

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index(): # denne funksjonen kan kalles hva man vil, men det er god praksis å navngi den lik html-siden den skal hente
    return render_template(
        "index.html", # render_template er innebygd funksjon i Flask
        heading = "Lesson 12: World Exploring"
                           )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        author = "Asbjørn Nordgaard"
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
    return render_template("cities.html", code=code, rows=rows, count = len(rows))


@app.route("/city/<int:city_id>")
def show_city(city_id):
    city = database.get_city(city_id)
    if city is None:
        return "City not found", 404
    return render_template("city_form.html", city_id=city.id, name=city.name, countrycode=city.countryCode, district=city.district, population=city.population)


@app.route("/add", methods=["GET", "POST"])
def add_city():
    if request.method == "GET":
        return render_template("city_form.html", nam="", city_id=None)
    name = request.form.get("name", "").strip()
    if not name or len(name) > 35:
        return "Invalid city name", 400
    database.insert_city(name)
    return redirect("/cities", code=303)