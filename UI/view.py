import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        # row 1
        self._ddCorsi = ft.Dropdown(label = "Selezionare un corso", width=500, hint_text="Selezionare un corso",
            options=[], on_change = self._controller.leggi_corso)
        self._btnCercaiscritti = ft.ElevatedButton(text = "Cerca Iscritti", on_click=self._controller.cercaIscritti)
        row1 = ft.Row([self._ddCorsi, self._btnCercaiscritti], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        # row 2
        self._txtMatricola = ft.TextField(label="Matricola", width=150, hint_text="Inserire una matricola")
        self._txtNome = ft.TextField(label="Nome", width=250, read_only=True)
        self._txtCognome = ft.TextField(label="Cognome", width=250, read_only=True)

        row2 = ft.Row([self._txtMatricola, self._txtNome, self._txtCognome], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        # row 3
        self._btnCercaStudente = ft.ElevatedButton(text = "Cerca Studente", on_click=self._controller.cercaStudente)
        self._btnCercaCorsi = ft.ElevatedButton(text = "Cerca Corsi", on_click=self._controller.cercaCorsi)
        self._btnIscrivi = ft.ElevatedButton(text = "Iscrivi", on_click=self._controller.iscrivi)

        row3 = ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi], spacing=10, alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
