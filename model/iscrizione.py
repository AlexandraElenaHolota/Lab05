from dataclasses import dataclass
@dataclass
class Iscrizione:
    matricola: int
    codins : str

    def __str__(self):
        return f'{self.matricola} - {self.codins}'

    def __hash__(self):
        return hash(self.matricola)