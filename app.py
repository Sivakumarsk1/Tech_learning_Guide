from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("roadmap.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    role_input = ""

    if request.method == "POST":
        role_input = request.form.get("role")

        # Filter data safely
        result = df[df["Role"].str.contains(role_input, case=False, na=False)]

        if not result.empty:
            data = result.to_dict(orient="records")

    return render_template("index.html", data=data, role=role_input)


if __name__ == "__main__":
    app.run(debug=True)