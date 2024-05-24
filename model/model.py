from database import corso_DAO, iscrizione_DAO, studente_DAO


class Model:
    def get_corsi(self):
        return corso_DAO.get_corso()

    def get_iscritti_corsi(self, corso):
        return iscrizione_DAO.get_studente_corso(corso)

    def get_studente(self, matricola):
        return studente_DAO.get_studente(matricola)

    def get_corsi_matricola(self, matricola):
        corsi_seguiti = iscrizione_DAO.get_corsi_studente(matricola)
        corsi = self.get_corsi()
        result = []
        for cS in corsi_seguiti:
            for c in corsi:
                if cS.codins == c.codins:
                    result.append(c)
        return result

    def iscrivi_corso(self, matricola, codin):
        return iscrizione_DAO.iscrivi_corso(matricola, codin)



