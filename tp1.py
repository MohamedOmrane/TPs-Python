import csv

menu_options = {
    1: 'Afficher la liste de toutes les personnes enregistrées',
    2: 'Ajouter une nouvelle personne',
    3: 'Modifier les informations d\'une personne',
    4: 'Supprimer une personne ',
    5: 'Exit'
}

def print_menu():
    for key, value in menu_options.items():
        print (key, '--', value)

def lecture_csv():
    """
    Cette fonction lit le fichier .csv 
    retourne une liste de toutes les personnes sous forme d'un dioctionnaires
    """

    with open('donnees.csv', 'r', newline='') as f:
        csv_reader = csv.reader(f)
        # Initialisation d'une liste vide pour garder le contenu du fichier
        data = []
    
        for row in csv_reader:
            row_dict = {}
            # Assigner les données au dictionnaire
            row_dict['nom'] = row[0]
            row_dict['prénom'] = row[1]
            row_dict['âge ans'] = row[2]
            row_dict['ville'] = row[3]
            # Add the dictionary to the list
            data.append(row_dict)
    #Affichage des données
    return(data)


def affichage():
    """
    Cette fonction affiche toutes les ligne du fichier
    """

    print('Toutes les personnes présents dans le documents: ')
    data = lecture_csv()
    for dictionnaire in data:
        personne = ", ".join(dictionnaire.values())
        print(personne)   
    print("""-----------------------------------
------------------------------------
------------------------------------
------------------------------------""")

def ajout():
    """
    Cette fonction ajoute une ligne dans le fichier
    """
    nom = input('Donner le nom: ')
    prenom = input('Donner le prénom: ')
    age = input('Donner l\'age en ans: ')
    ville = input('Donner la ville: ') 
  
    with open('donnees.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        # Ecriture de la nouvelle personne dans le fichier 
        writer.writerow([nom, prenom, age, ville])
    print("Nouvelle personne ajoutée")

    print("""-----------------------------------
------------------------------------
------------------------------------
------------------------------------""")

def modification():
    """
    Cette fonction modifie les informations d'une personne du fichier
    """

    # Ouverture du csv en mode lecture
    with open('donnees.csv', 'r') as f:
        reader = csv.reader(f)
        # Mettre toutes les ligne dans une liste
        lignes = list(reader)

    nom = input('Donner le nom de la personne à modifier: ')
    #Verifier si la personne existe
    if any(nom in ligne for ligne in lignes):
        prenom = input('Donner le nouveau prénom: ')
        age = input('Donner le nouvel age en ans: ')
        ville = input('Donner la nouvelle ville: ')
        # Ouverture du csv en mode écriture
        with open('donnees.csv', 'w') as f:
            writer = csv.writer(f)
            for ligne in lignes:
                # Modification des informations de la personne souhaitée
                if nom in lignes:
                    ligne = [nom, prenom, age, ville]
                writer.writerow(ligne)
        print('Les information de cette personne ont été modifié')
    else:
        print('Cette personne n\'existe pas')
    print("""-----------------------------------
------------------------------------
------------------------------------
------------------------------------""")
    
def suppression():
    """
    Cette fonction supprime les information d'une personne du fichier
    """
    nom = input('Donner le nom de la personne à supprimer: ')
    # ouverture du csv en mode lecture
    with open('donnees.csv', 'r') as f:
        reader = csv.reader(f)
        # Mettre toutes les ligne dans une liste
        lignes = list(reader)

    #Verifier si la personne existe
    if any(nom in ligne for ligne in lignes):
        # Ouverture du csv en mode écriture
        with open('donnees.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for ligne in lignes:
                if nom not in lignes:
                    # Ecrire la ligne dans le fichier si elle ne contient pas le nom
                    writer.writerow(ligne)
        print('Cette personne a été supprimé du ficher')
    else:
        print('Cette personne n\'existe pas')
    print("""-----------------------------------
------------------------------------
------------------------------------
------------------------------------""")

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Faites votre choix: '))
        except:
            print('Enrée érronée. Entrez un nombre entier ...')
            
        if option == 1:
           affichage()
        elif option == 2:
            ajout()
        elif option == 3:
            modification()
        elif option == 4:
            suppression()
        elif option == 5:
            print('Merci! Sortie de progamme.')
            exit()
        else:
            print('Option invalide. Entrer une valeur entre 1 et 5') 
