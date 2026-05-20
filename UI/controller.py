import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._gnrID=None

    def fillDDGenre(self):
        gen = self._model.getGenres()
        l=[ft.dropdown.Option(text=i.Name, key=i.GenreId) for i in gen]
        self._view._ddGenre.options.extend(l)

    def readGenre(self, e):
        try:
            self._gnrID=int(self._view._ddGenre.value)
        except ValueError:
            self._gnrID=None
            print("Errore")

    def handleCreaGrafo(self, e):
        self.readGenre(1)
        if self._gnrID is None:
            return
        nN, nE, art,arc, artList = self._model.creaGrafo(self._gnrID)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Nodi: {nN}"))
        self._view.txt_result.controls.append(ft.Text(f"Archi: {nE}"))
        self._view.txt_result.controls.append(ft.Text(f"Artista piu influente: {art[0].Name}, influenza: {art[1]}"))
        self._view.txt_result.controls.append(ft.Text(f"Top 5 archi"))
        for n,i in enumerate(arc):
            self._view.txt_result.controls.append(
                ft.Text(f"{n+1}: {i[0].Name}->, {i[1].Name}: {i[2]["weight"]}"))
        self._view.update_page()



    def handleCammino(self,e):
        pass