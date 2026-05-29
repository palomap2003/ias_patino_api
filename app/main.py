import os

from flask import Flask, render_template, request, redirect
from app.models import db, Usuario

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgres://",
        "postgresql://",
        1
    )
DEBUG_MODE = os.environ.get("DEBUG", "false").lower() in ["true", "1", "t"]

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = DEBUG_MODE

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    usuarios = Usuario.query.all()
    return render_template("index.html", usuarios=usuarios)
@app.route("/health")
def health():
    return {"status": "ok"}, 200

@app.route("/crear", methods=["POST"])
def crear():
    nombre = request.form["nombre"]
    email = request.form["email"]

    usuario = Usuario(nombre=nombre, email=email)

    db.session.add(usuario)
    db.session.commit()

    return redirect("/")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    usuario = Usuario.query.get(id)

    db.session.delete(usuario)
    db.session.commit()

    return redirect("/")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    usuario = Usuario.query.get(id)

    if request.method == "POST":
        usuario.nombre = request.form["nombre"]
        usuario.email = request.form["email"]

        db.session.commit()

        return redirect("/")

    return render_template("edit.html", usuario=usuario)