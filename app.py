from flask import Flask, render_template, request, send_file
from mkpdf import PDF
from datetime import datetime
import tempfile
from os.path import join

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        with tempfile.TemporaryDirectory() as tmpdirname:
            title = request.form["title"]
            data = (
                ("Name", request.form["name"]),
                ("Scholar ID", request.form["schid"]),
                ("Course", request.form["course"]),
                ("Department", request.form["dept"]),
                ("Submitted to", request.form["subto"]),
                ("Date", request.form["date"]),
            )
            pdf = PDF()
            pdf.alias_nb_pages()
            pdf.add_page()
            pdf.chapter_body(title)
            pdf.info(data)
            filename = str(datetime.now())+".pdf"
            pdf.output(join(tmpdirname, filename))
            return send_file(join(tmpdirname, filename), as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
