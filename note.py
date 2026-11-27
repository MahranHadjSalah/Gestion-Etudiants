"""Module Note : represente la note d'un etudiant dans une matiere."""


class Note:
    """Une note sur 20 obtenue par un etudiant dans une matiere."""

    def __init__(self, matricule, matiere, valeur):
        self.matricule = matricule
        self.matiere = matiere
        self.valeur = valeur

    def __str__(self):
        return f"{self.matricule} - {self.matiere} : {self.valeur}/20"


class GestionNotes:
    """Gere les notes des etudiants."""

    def __init__(self):
        self.notes = []

    def ajouter(self, note):
        """Ajoute une note ; elle doit etre comprise entre 0 et 20."""
        if not 0 <= note.valeur <= 20:
            raise ValueError("La note doit etre comprise entre 0 et 20")
        self.notes.append(note)

    def afficher(self, matricule=None):
        """Affiche les notes (toutes, ou celles d'un etudiant)."""
        for note in self.notes:
            if matricule is None or note.matricule == matricule:
                print(note)
