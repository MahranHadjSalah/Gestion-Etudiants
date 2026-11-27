"""Module Note : represente la note d'un etudiant dans une matiere."""


class Note:
    """Une note sur 20 obtenue par un etudiant dans une matiere."""

    def __init__(self, matricule, matiere, valeur):
        self.matricule = matricule
        self.matiere = matiere
        self.valeur = valeur

    def __str__(self):
        return f"{self.matricule} - {self.matiere} : {self.valeur}/20"
