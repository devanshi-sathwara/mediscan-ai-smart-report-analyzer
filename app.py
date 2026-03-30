from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("report")

        if not file:
            return render_template("index.html", error="No file uploaded")

        try:
            report = file.read().decode("utf-8")

            final_diagnosis = "Processed Report:\n" + report

            final_diagnosis_text = "### Final Diagnosis:\n\n" + final_diagnosis

            return render_template("index.html", diagnosis=final_diagnosis_text)

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)