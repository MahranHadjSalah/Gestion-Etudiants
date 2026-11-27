"""Module Etudiant : represente un etudiant."""


class Etudiant:
    """Un etudiant identifie par son matricule."""

    def __init__(self, matricule, nom, prenom):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"[{self.matricule}] {self.prenom} {self.nom}"
