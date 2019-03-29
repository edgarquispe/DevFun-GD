
class StyleApp:
    def __init__(self):
        self._style = ""

    def get_style_app(self):
        """
        Este metodo se encarga de cargar los estilos para los componentes de UI
        que se usan en las vistas.
        :return:
        """
        self._style = """
                        QMainWindow{background-image: url(view/imgs/bg-2.png); background-size: 100%;}
                        QLineEdit {border-radius: 10px; min-height: 20px; min-width: 20px; padding: 5px;}
                        QComboBox {border-radius: 10px; min-height: 20px; min-width: 20px; padding: 5px;}
                        QGroupBox {background-color: rgba(255, 255, 255, 60); border-radius: 5px; padding: 20px;}                               
                        QPushButton {
                            background-color: palegoldenrod;
                            border-width: 1px;
                            border-color: darkkhaki;
                            border-style: solid;
                            border-radius: 5;
                            padding: 3px;
                            min-width: 10ex;
                            min-height: 5.5ex;
                            font-family: 'Roboto';
                        }
                        QPushButton:hover{
                            background-color: #ff7043;
                        }
                        QStatusBar{color: yellow;}
                        QToolTip {
                            border: 1px solid darkkhaki;
                            padding: 5px;
                            border-radius: 10px;
                            opacity: 60;
                        }
                        QLabel{
                            font-family: 'Roboto';
                            color: black;
                            font-size: 15px;
                        }
                        QTableView {
                            alternate-background-color: #f2f2f2; background-color: white;
                        }
                        QDialog{

                            padding: 5px;
                            color: white;
                        }
                      """
        return self._style