from flask import Flask, render_template, request
from mysql.connector import Error
from database import get_cities

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index(): # denne funksjonen kan kalles hva man vil, men det er god praksis å navngi den lik html-siden den skal hente
    return render_template(
        "index.html", # render_template er innebygd funksjon i Flask
        heading = "World exploring Jinja"
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

