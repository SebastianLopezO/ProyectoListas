import webbrowser

class Html:
    def __init__(self):
        # Head estandar
        self.Head = '<head><title>Proyecto de Listas</title><link rel="stylesheet" type="text/css" href="style.css"></head>'
        self.Body = '<body></body>'

    def AddBody(self, html):
        self.Body += html

    def Export(self, FileName):
        try:
            # Crear archivo HTML
            archivo = open("src/frame/" + FileName + ".html", "w")
            archivo.write(self.Head + self.Body)
            archivo.close()

            # Abrir el archivo HTML en el navegador predeterminado
            webbrowser.open("src/frame/" + FileName + ".html")
        except Exception as e:
            print("Error al Exportar resultado: ", e)
