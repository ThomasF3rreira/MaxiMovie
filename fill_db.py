from sqlite_operations import create_film, delete_all_films

# Exemples de films
films = [
    {
        'titre': 'Film 1',
        'description': 'Description du film 1',
        'annee': '2021',
        'acteurs': 'Acteur 1, Acteur 2',
        'realisation': 'Réalisateur 1',
        'producteur': 'Producteur 1',
        'image': 'film1.jpg'
    },
    {
        'titre': 'Film 2',
        'description': 'Description du film 2',
        'annee': '2022',
        'acteurs': 'Acteur 3, Acteur 4',
        'realisation': 'Réalisateur 2',
        'producteur': 'Producteur 2',
        'image': 'film2.jpg'
    },
    {
        'titre': 'Film 3',
        'description': 'Description du film 3',
        'annee': '2023',
        'acteurs': 'Acteur 5, Acteur 6',
        'realisation': 'Réalisateur 3',
        'producteur': 'Producteur 3',
        'image': 'film3.jpg'
    }
]

delete_all_films()

# Insertion des films dans la base de données
for film in films:
    create_film(
        film['titre'],
        film['description'],
        film['annee'],
        film['acteurs'],
        film['realisation'],
        film['producteur'],
        film['image']
    )

print("Base de données remplie avec succès !")

