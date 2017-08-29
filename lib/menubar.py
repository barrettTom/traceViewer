from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QAction

class menubar():
    def __init__(self, view):
        menu = view.menuBar()
        fileMenu = menu.addMenu('&File')
        openButton = QAction('&Open', view)
        openButton.triggered.connect(view.open)
        fileMenu.addAction(openButton)

        view.timer = QTimer()
        view.timer.timeout.connect(view.update)
        view.timer.start(100)

        view.status = view.statusBar()

        viewMenu = menu.addMenu('&View')
        autoButton = QAction('&Auto Axis', view)
        autoButton.triggered.connect(view.auto)
        viewMenu.addAction(autoButton)

        view.splitButton = QAction('&Split Axis', view)
        view.splitButton.triggered.connect(view.split)
        view.splitButton.setCheckable(True)
        viewMenu.addAction(view.splitButton)

        view.syncButton = QAction('&Sync Split X Axis', view)
        view.syncButton.triggered.connect(view.syncToggle)
        view.syncButton.setCheckable(True)
        view.syncButton.setEnabled(False)
        viewMenu.addAction(view.syncButton)
        view.sync = False

        view.regionButton = QAction('&Toggle Region', view)
        view.regionButton.triggered.connect(view.region)
        view.regionButton.setCheckable(True)
        viewMenu.addAction(view.regionButton)
