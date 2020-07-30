from app import app
import json
import os


def read_products(category_id=0):
    with open(os.path.join(app.root_path, "data/products.json"), encoding="utf-8") as f:
        products = json.load(f)

        if category_id > 0:
            products = [p for p in products if p["category_id"] == category_id]

        return products


if __name__ == "__main__":
    print(read_products())
