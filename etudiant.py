"""Module Etudiant : represente un etudiant."""


class Etudiant:
    """Un etudiant identifie par son matricule."""

    def __init__(self, matricule, nom, prenom):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom

    def __str__(self):
        return f"[{self.matricule}] {self.prenom} {self.nom}"


class GestionEtudiants:
    """Gere la liste des etudiants de l'application."""

    def __init__(self):
        self.etudiants = {}

    def ajouter(self, etudiant):
        """Ajoute un etudiant ; refuse un matricule deja utilise."""
        if etudiant.matricule in self.etudiants:
            raise ValueError(f"Matricule {etudiant.matricule} deja utilise")
        self.etudiants[etudiant.matricule] = etudiant
