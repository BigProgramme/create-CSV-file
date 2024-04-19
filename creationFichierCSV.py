import sqlite3
import csv

bdd = "baseDeDonneesStructuree.db"
connexion = sqlite3.connect(bdd) ## On se connecte à la BDD
curseur = connexion.cursor()                        ## On crée le curseur de requêtes SQL

tables = ["Categorie", "Activite", "Process_Group", "Process", "Tache"] ## Listes des  tables de la base de données

# Récupération des données de la table
## Je vais parcourir toutes les tables pour créer tous les fichiers en une seule fois
for table in tables:
    requete = f"SELECT * FROM {table}" ## Je séléctionne toutes  les lignes et colonnes de ma table
    resultats = curseur.execute(requete).fetchall() ##  J'exécute ma requête et j'attends que je récupère toutes les donnée

# Nom du fichier CSV de sortie
    nom_fichier_csv = f"{table}.csv" ###   J'ajoute ".csv" au nom de mon fichier, je veux que cela soit clair ; 
                                     ### le nom du fichier n'est rien d'autre que le nom de la table

    # Écriture des données dans le fichier CSV avec les en-têtes
    with open(nom_fichier_csv, "w", newline="") as fichier_csv:
        writer = csv.writer(fichier_csv)

    # Récupération des noms des colonnes
        en_tetes = [description[0] for description in curseur.description]  ### curseur.description pour obtenir les informations sur les colonnes de la table (y compris les noms des colonnes)
        writer.writerow(en_tetes)  # Écriture des en-têtes dans le fichier CSV

        writer.writerows(resultats)  # Écriture des données dans le fichier CSV
        

