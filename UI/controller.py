import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # self dizionario corsi
        self._id_map_corsi = {}
        # il corso selezionato nel menu a tendina
        self.corso_selezionato = None


    def populated_ddCorsi(self):
        for corso in self._model.get_corsi():
            self._id_map_corsi[corso.codins] = corso
            self._view._ddCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()


    def cercaIscritti(self, e):
        if self.corso_selezionato == None:
            self._view.create_alert("Selezionare un corso!")
            return
        iscritti = self._model.get_iscritti_corsi(self.corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione!")
            return
        self._view.txt_result.controls.clear()
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti al corso"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))
            self._view.update_page()

    def leggi_corso(self, e):
        self.corso_selezionato = self._view._ddCorsi.value


    def cercaStudente(self, e):
        matricola = self._view._txtMatricola.value
        if matricola == "":
            self._view.create_alert("Selezionare una matricola!")
            return
        studente = self._model.get_studente(matricola)
        if studente is None:
            self._view.create_alert("Problema nella connessione!")
            return
        else:
            self._view._txtCognome.value = f"{studente.cognome}"
            self._view._txtNome.value = f"{studente.nome}"

        self._view.update_page()

    def cercaCorsi(self, e):
        matricola = self._view._txtMatricola.value
        if matricola == "":
            self._view.create_alert("Selezionare una matricola!")
            return
        result = self._model.get_corsi_matricola(matricola)
        if len(result) == 0:
            self._view.create_alert("Matricola non presente!")
            return
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(result)} corsi seguiti:"))
            for c in result:
                self._view.txt_result.controls.append(ft.Text(f"{c}"))
        self._view.update_page()


    def iscrivi(self, e):
        matricola = self._view._txtMatricola.value
        if matricola == "":
            self._view.create_alert("inserire una matricola")
            return
        studente = self._model.get_studente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non presente nel database")
            return
        codice_corso = self._view._ddCorsi.value
        if codice_corso is None:
            self._view.create_alert("Selezionare un corso!")
            return
        if self.corsoGiaSeguito(matricola, codice_corso)==True:
            self._view.create_alert("Corso già seguito!")
            return
        result = self._model.iscrivi_corso(matricola, codice_corso)
        self._view.txt_result.controls.clear()
        if result:
            self._view.txt_result.controls.append(ft.Text("Iscrizione avvenuta con successo"))
        else:
            self._view.txt_result.controls.append(ft.Text("Iscrizione fallita"))
        self._view.update_page()

    def corsoGiaSeguito(self, matricola, corso):
        corsi_già_seguiti = self._model.get_corsi_matricola(matricola)
        for c in corsi_già_seguiti:
            if c.codins == corso:
                return True
        return False


