# ===== app.py =====
from flask import Flask, render_template, request
from utils import sequential_store, indexed_store, direct_store, btree_store

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        org_type = request.form.get("org_type")
        num_records = int(request.form.get("num_records"))

        if org_type == "Sequential":
            df, stats = sequential_store(num_records)
        elif org_type == "Indexed":
            df, stats = indexed_store(num_records)
        elif org_type == "Direct":
            df, stats = direct_store(num_records)
        elif org_type == "B-Tree":
            df, stats = btree_store(num_records)

        data = df.to_dict(orient="records")
        metrics = stats.to_dict(orient="records")
        return render_template("result.html", org_type=org_type, data=data, metrics=metrics)

    return render_template("index.html")

@app.route("/about")
def about():
    authors = ["Mohamed Bahaa", "Rotaj Mohamed"]
    return render_template("about.html", authors=authors)

if __name__ == "__main__":
    app.run(debug=True)
