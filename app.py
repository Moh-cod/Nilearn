
import sqlite3
import os
from flask import Flask, render_template, send_from_directory, request, redirect


app = Flask(__name__)

resource_type_names = {
    "Past Paper": "امتحان سابق",
    "Book": "كتاب",
    "Notes": "مذكرة",
    "Study Guide": "دليل دراسي",
}

subject_names = {
    "Physics": "الفيزياء",
    "English": "اللغة الإنجليزية",
    "History": "التاريخ",
    "Geography": "الجغرافيا",
    "Chemistry": "الكيمياء",
    "Arabic": "اللغة العربية",
    "Islamic Studies": "دراسات اسلامية",
    "Islamic Education": "تربية اسلامية",
    "Engineering Sciences": "علوم هندسية",
    "Biology": "احياء",
    "Computer Science": "حاسوب",
    "Additional Mathematics": "رياضيات متخصصة",
    "Basic Mathematics": "رياضيات الاساسية",
}

def get_db():
    connection = sqlite3.connect("nilearn.db")
    connection.row_factory = sqlite3.Row
    return connection



def format_file_size(size):
    if size < 1024:
        return f"{size} B"

    if size <1024 * 1024:
        return f"{size / 1024:.1f} KB"

    if size < 1024 * 1024 * 1024:
        return f"{size / (1024 * 1024):.1f} MB"

    return f"{size / (1024 * 1024 * 1024):.1f} GB"

@app.route("/")
def index():
    return render_template("index.html")




@app.route("/resources")
def resources():
    search = request.args.get("search")
    subject = request.args.get("subject")
    connection = get_db()

    subjects = connection.execute(
        "SELECT DISTINCT subject FROM resources"
    ).fetchall()

    query = "SELECT * FROM resources"
    parameter = []

    if search:
        query += " WHERE title LIKE ? OR subject LIKE ?"
        parameter.extend([f"%{search}%", f"%{search}%"])

    if subject:
        if search:
            query += " AND subject = ?"
            parameter.append(subject)
        else:
            query += " WHERE subject = ?"
            parameter.append(subject)

    resources = connection.execute(
        query, parameter
        ).fetchall()

    connection.close()

    return render_template("resources.html",
                           resources=resources, subjects=subjects, subject_names=subject_names, resource_type_names=resource_type_names)




@app.route("/resources/<int:resource_id>")
def resource_detail(resource_id):
    connection = get_db()

    resource = connection.execute(
        "SELECT * FROM  resources WHERE id = ?", (resource_id,)
    ).fetchone()

    if resource ["file_size"]:
        file_size = format_file_size(resource["file_size"])

    else:
        file_size = "Unknown"

    connection.close()

    return render_template("resource_detail.html",
                            resource=resource, file_size=file_size,
                            subject_names=subject_names, resource_type_names=resource_type_names)




@app.route("/download/<filename>")
def download(filename):
    return send_from_directory ("uploads", filename)





@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        connection = get_db()
        title = request.form["title"]
        subject = request.form["subject"]
        resource_type = request.form["resource_type"]
        year = request.form["year"]
        description = request.form["description"]
        pdf = request.files["pdf"]

        file_path = "uploads/" + pdf.filename
        pdf.save(file_path)

        file_size = os.path.getsize(file_path)

        connection.execute(
            """
            INSERT INTO resources
            (title, subject, resource_type, year, description, file_path, file_size)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (title, subject, resource_type, year, description, pdf.filename, file_size)
        )

        connection.commit()
        connection.close()

        return redirect("/resources")

    return render_template("admin.html")


@app.route("/reset-library")
def reset_library():
    connection = sqlite3.connect("nilearn.db")

    connection.execute("DELETE FROM resources")
    connection.commit()
    connection.close()

    for filename in os.listdir("uploads"):
        file_path = os.path.join("uploads", filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    return "Nilearn library has been reset."
