from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hero():
    return render_template("hero.html")

@app.route("/profile")
def pofile():
    members = [
        {
            "name": "ANGELICA MARI S. VICTORINO",
            "course_section": "BSCPE 2-2",
            "quote": "I don’t chase, I attract",
            "image": "assets/member-1.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "HANNAH NYTRISHA D. CASABUENA",
            "course_section": "BSCPE 2-2",
            "quote": "Dream boldly, act fearlessly, and live with purpose.",
            "image": "assets/member-2.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "JANNINA ALEXA I. TABOR",
            "course_section": "BSCPE 2-2",
            "quote": "Let go and be unhurried",
            "image": "assets/member-3.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "CASEY E. DE VERA",
            "course_section": "BSCPE 2-2",
            "quote": "When the pain penetrates, code resonates.",
            "image": "assets/member-4.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "MIGUEL DOMINIC DG. PAYUMO",
            "course_section": "BSCPE 2-2",
            "quote": "Carpe diem, seize the day.",
            "image": "assets/member-5.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "JOSEPH S. ELULA",
            "course_section": "BSCPE 2-2",
            "quote": "When life gives you lemons, make lemonade.",
            "image": "assets/member-6.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link1"},
                {"image": "assets/victorino-project-1.png", "link": "link2"},
                {"image": "assets/victorino-project-1.png", "link": "link3"},
            ]
        },
        {
            "name": "JOHN LUIS GEPILA",
            "course_section": "BSCPE 2-3",
            "quote": "Success is earned through effort, not given by chance.",
            "image": "assets/member-7.png",
            "projects": [
                {"image": "assets/victorino-project-1.png", "link": "link4"},
                {"image": "assets/victorino-project-1.png", "link": "link5"},
                {"image": "assets/victorino-project-1.png", "link": "link6"},
            ]
        },
    ]
    return render_template('profile.html', members=members)

@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)

