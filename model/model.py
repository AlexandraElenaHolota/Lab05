from database import corso_DAO, iscrizione_DAO, studente_DAO


class Model:
    def get_corsi(self):
        return corso_DAO.get_corso()

    def get_iscritti_corsi(self, corso):
        return iscrizione_DAO.get_studente_corso(corso)

    def get_studente(self, matricola):
        return studente_DAO.get_studente(matricola)


