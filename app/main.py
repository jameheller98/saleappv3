from flask import render_template, request, redirect, url_for
from app import app, dao


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def list_products():
    kw = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")

    return render_template("products.html",
                           products=dao.read_products(keyword=kw, from_price=from_price, to_price=to_price))


@app.route("/products/add", methods=["post", "get"])
def add_or_update_products():
    err = ""
    if request.method.lower() == "post":
        name = request.form.get("name")
        price = request.form.get("price", 0)
        images = request.form.get("images")
        description = request.form.get("description")
        category_id = request.form.get("category_id", 0)
        if (dao.add_product(name=name, price=price, images=images,
                            description=description, category_id=category_id)):
            return redirect(url_for("list_products"))


        err = "Something wrong !!! Please back later!!!"

    return render_template("product-add.html", categories=dao.read_categories(), err=err)


@app.route("/products/<int:category_id>")
def product_by_cat_id(category_id):
    return render_template("products.html", products=dao.read_products(category_id))


if __name__ == "__main__":
    app.run(debug=True)
