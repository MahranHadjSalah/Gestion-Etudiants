"""Point d'entree de l'application de gestion des etudiants."""
from etudiant import Etudiant, GestionEtudiants
from note import Note, GestionNotes


def afficher_message():
    """Affiche le message d'accueil de l'application."""
    print("Bienvenue dans la gestion des étudiants et des notes")


def main():
    """Demontre les fonctionnalites des deux branches fusionnees."""
    afficher_message()

    etudiants = GestionEtudiants()
    etudiants.ajouter(Etudiant(1, "Ben Ali", "Sami"))
    etudiants.ajouter(Etudiant(2, "Trabelsi", "Amira"))
    etudiants.ajouter(Etudiant(3, "Gharbi", "Youssef"))
    etudiants.supprimer(3)
    print("
-- Etudiants --")
    etudiants.afficher()

    notes = GestionNotes()
    notes.ajouter(Note(1, "DevOps", 15.5))
    notes.ajouter(Note(1, "Python", 13))
    notes.ajouter(Note(2, "DevOps", 17))
    print("
-- Notes --")
    notes.afficher()
    print("
-- Moyennes --")
    for matricule in etudiants.etudiants:
        print(f"Etudiant {matricule} : {notes.moyenne(matricule)}/20")


if __name__ == "__main__":
    main()
