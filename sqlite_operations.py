import sqlite3


def create_film(titre, description, annee, acteurs, realisation, producteur, image):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO films (titre, description, annee, acteurs, realisation, producteur, image) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (titre, description, annee, acteurs, realisation, producteur, image))

    conn.commit()
    conn.close()


# Les autres fonctions du fichier restent inchangées

def get_all_films():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM films")
    data = cursor.fetchall()

    conn.close()

    films = []
    for film_data in data:
        film = {
            'id': film_data[0],
            'titre': film_data[1],
            'description': film_data[2],
            'annee': film_data[3],
            'acteurs': film_data[4],
            'realisation': film_data[5],
            'producteur': film_data[6],
            'image': film_data[7]
        }
        films.append(film)

    return films


def get_film_id(film_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM films WHERE id = ?", (film_id,))
    data = cursor.fetchall()

    conn.close()

    if data:
        film_data = data[0]
        film = {
            'id': film_data[0],
            'titre': film_data[1],
            'description': film_data[2],
            'annee': film_data[3],
            'acteurs': film_data[4],
            'realisation': film_data[5],
            'producteur': film_data[6],
            'image': film_data[7]
        }
        return film
    else:
        return None


def update_film(film_id, titre, description, annee, acteurs, realisation, producteur, image):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE films SET titre=?, description=?, annee=?, acteurs=?, realisation=?, producteur=?, image=? WHERE id=?',
        (titre, description, annee, acteurs, realisation, producteur, image, film_id))

    conn.commit()
    conn.close()


def delete_film_id(film_id):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM films WHERE id=?', (film_id,))

    conn.commit()
    conn.close()


def delete_all_films():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM films")

    conn.commit()
    conn.close()
