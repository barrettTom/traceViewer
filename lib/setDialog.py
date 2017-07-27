from PyQt5.QtWidgets import QGridLayout, QDialog, QDialogButtonBox, QLabel, QLineEdit

class setDialog(QDialog):
    def __init__(self):
        super(setDialog, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel("X:",self), 0, 0)
        layout.addWidget(QLabel("Y:",self), 1, 0)

        self.x0 = QLineEdit("0",self)
        layout.addWidget(self.x0, 0, 1)
        self.x1 = QLineEdit("1",self)
        layout.addWidget(self.x1, 0, 2)

        self.y0 = QLineEdit("0",self)
        layout.addWidget(self.y0, 1, 1)
        self.y1 = QLineEdit("1",self)
        layout.addWidget(self.y1, 1, 2)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.accept)
        buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)

        layout.addWidget(buttonBox, 2, 0, 1, 3)

    @staticmethod
    def getInfo():
        dialog = setDialog()
        result = dialog.exec_()
        if result:
            result = [dialog.x0.text(), dialog.x1.text(), dialog.y0.text(), dialog.y1.text()]
            result = list(map(float, result))
            return result
        else:
            return False
