from flask import render_template
from app import app, dao


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def list_products():
    return render_template("products.html", products=dao.read_products())


@app.route("/products/<int:category_id>")
def product_by_cat_id(category_id):
    return render_template("products.html", products=dao.read_products(category_id))


if __name__ == "__main__":
    app.run(debug=True)
