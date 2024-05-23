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
        self._view.update()



    def cercaCorsi(self, e):
        pass

    def iscrivi(self, e):
        pass

