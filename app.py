import os
from flask import Flask, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
from sqlite_operations import *

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Dossier où les images seront enregistrées

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    films = get_all_films()
    return render_template("index.html", films=films)


# Route pour obtenir photos
@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/add_film", methods=['GET', 'POST'])
def add_film():
    if request.method == 'GET':
        return render_template("add_film.html")
    elif request.method == 'POST':
        titre = request.form.get('titre')
        description = request.form.get('description')
        annee = request.form.get('annee')
        acteurs = request.form.get('acteurs')
        realisation = request.form.get('realisation')
        producteur = request.form.get('producteur')
        image_uploaded = request.files['image_upload']

        if image_uploaded:
            # L'utilisateur a téléchargé une image avec une extension autorisée
            filename = secure_filename(image_uploaded.filename)
            image_uploaded.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            image = filename
        else:
            # Aucune image n'a été téléchargée ou l'extension du fichier n'est pas autorisée
            image = None

        create_film(titre, description, annee, acteurs, realisation, producteur, image)

        # Redirection vers la page d'accueil après l'ajout du film
        return redirect('/')


@app.route("/details_film/<film_id>")
def details_film(film_id):
    film = get_film_id(film_id)  # Passer l'ID du film à la fonction get_film_id()
    return render_template("details_film.html", film=film)


# Route pour supprimer un film
@app.route('/delete_film/<int:film_id>', methods=['GET', 'POST'])
def delete_film(film_id):
    film = get_film_id(film_id)
    if request.method == 'POST':
        delete_film_id(film_id)
        return redirect(url_for('index'))
    else:
        return render_template('details_film.html', film=film)


@app.route('/edit_film/<int:film_id>', methods=['GET', 'POST'])
def edit_film(film_id):
    film = get_film_id(film_id)

    if request.method == 'POST':
        titre = request.form.get('titre')
        description = request.form.get('description')
        annee = request.form.get('annee')
        acteurs = request.form.get('acteurs')
        realisation = request.form.get('realisation')
        producteur = request.form.get('producteur')

        # Vérification et mise à jour de l'image
        if 'image' in request.files:
            fichier_image = request.files['image']
            if fichier_image.filename != '':
                nom_fichier = secure_filename(fichier_image.filename)
                fichier_image.save(os.path.join(UPLOAD_FOLDER, nom_fichier))
                chemin_image = os.path.join(UPLOAD_FOLDER, nom_fichier)
                update_film(film_id, titre, description, annee, acteurs, realisation, producteur, chemin_image)
            else:
                update_film(film_id, titre, description, annee, acteurs, realisation, producteur, film['image'])
        else:
            update_film(film_id, titre, description, annee, acteurs, realisation, producteur, film['image'])

        return redirect(url_for('details_film', film_id=film_id))

    return render_template('edit_film.html', film=film)



if __name__ == '__main__':
    app.run()
