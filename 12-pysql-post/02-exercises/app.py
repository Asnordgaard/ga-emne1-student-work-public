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
        heading = "Exercise 12: World Exploring"
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
        country_name = database.get_country_name(code)
        code_rows = database.get_country_code()
        rows = get_cities(code)
    except Error:
        app.logger.exception(
            "Database query failed"
        )
        return "Database unavailable", 503
    return render_template(
        "cities.html",
        code=code,
        rows=rows,
        code_rows=code_rows,
        country_name=country_name,
        count = len(rows))


@app.route("/city/<int:city_id>")
def show_city(city_id):
    city = database.get_city(city_id)
    heading = "Edit city"
    if city is None:
        return "City not found", 404
    return render_template("city_form.html", city_id=city.id, name=city.name, countrycode=city.countryCode, district=city.district, population=city.population, code_rows=database.get_country_code(), heading=heading)


@app.route("/add", methods=["GET", "POST"])
def add_city():
    if request.method == "GET":
        return render_template(
            "city_form.html",
            name="",
            city_id=None,
            countrycode="",
            code_rows=database.get_country_code(),
            heading = "Add a new city",
        )

    name = request.form.get("name", "").strip()
    if not name or len(name) > 35:
        return "Invalid city name", 400
    countrycode = request.form.get("countrycode")
    district = request.form.get("district")
    population = request.form.get("population")
    database.insert_city(name, countrycode, district, population)
    return redirect("/cities", code=303)


@app.route("/edit/<int:city_id>", methods=["GET", "POST"])
def edit_city(city_id):
    if request.method == "GET":
        return show_city(city_id)

    name = request.form.get("name", "").strip()
    if not name or len(name) > 35:
        return "Invalid city name", 400
    countrycode = request.form.get("countrycode")
    district = request.form.get("district")
    try:
        population = int(request.form.get("population", ""))
    except ValueError:
        return "Population must be a number", 400
    if population < 0:
        return "Population must be 0 or more", 400
    database.update_city(city_id, name, countrycode, district, population)
    return redirect("/cities", code=303)


# Delete is only invoked for loaded cities.
# Thus, no need to support the GET method.
@app.route("/delete/<int:city_id>", methods=["GET", "POST"])
def delete_city(city_id):
    if request.method == "GET":
        return show_city(city_id)

    database.delete_city(city_id)
    return redirect("/cities", code=303)
