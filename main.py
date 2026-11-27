"""Point d'entree de l'application de gestion des etudiants."""
from etudiant import Etudiant
from note import Note


def afficher_message():
    """Affiche le message d'accueil de l'application."""
    print("Bienvenue dans la gestion des notes")


def main():
    """Cree quelques objets et affiche leurs informations."""
    afficher_message()
    etudiant = Etudiant(1, "Ben Ali", "Sami")
    note = Note(1, "DevOps", 15.5)
    print(etudiant)
    print(note)


if __name__ == "__main__":
    main()
