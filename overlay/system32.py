from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QMenu
)
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtGui import QPixmap
import sys
import os
import subprocess

class PySystemDesktop(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySystem Desktop")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 🖼️ Fond d'écran
        bg_label = QLabel(self)
        bg_label.setAlignment(Qt.AlignCenter)
        bg_path = os.path.join(os.path.dirname(__file__), "BG.png")
        pixmap = QPixmap(bg_path)
        if not pixmap.isNull():
            screen_size = QApplication.primaryScreen().size()
            bg_label.setPixmap(pixmap.scaled(screen_size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        else:
            bg_label.setText("❌ BG.png introuvable")
            bg_label.setStyleSheet("color: red; font-size: 18px;")
        layout.addWidget(bg_label)

        # Barre des tâches
        taskbar = QHBoxLayout()
        taskbar.setContentsMargins(5, 5, 5, 5)

        # Bouton Py (menu démarrer)
        py_button = QPushButton("🟦 Py")
        py_button.setFixedSize(60, 30)
        py_button.setStyleSheet("background-color: #333; color: white;")
        py_button.setMenu(self.create_menu())
        taskbar.addWidget(py_button)

        # Boutons d'apps
        for name, script in [
            ("NotePad", "NotePad.py"),
            ("Fichier", "Fichier.py"),
            ("Calculatrice", "Calculator.py"),
            ("Python", "Python.py"),
            ("Weather", "Weather.py")
        ]:
            btn = QPushButton(name)
            btn.setFixedSize(100, 30)
            btn.setStyleSheet("background-color: #444; color: white;")
            btn.clicked.connect(lambda _, s=script: self.launch_app(s))
            taskbar.addWidget(btn)

        # Spacer
        taskbar.addStretch()

        # Horloge
        self.clock_label = QLabel()
        self.clock_label.setStyleSheet("color: white; font-size: 14px;")
        self.clock_label.setAlignment(Qt.AlignRight)
        self.update_time()
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
        taskbar.addWidget(self.clock_label)

        layout.addLayout(taskbar)

    def update_time(self):
        now = QDateTime.currentDateTime()
        self.clock_label.setText(now.toString("HH:mm:ss — dd/MM/yyyy"))

    def create_menu(self):
        menu = QMenu()
        actions = {
            "NotePad": "NotePad.py",
            "Fichier": "Fichier.py",
            "Calculatrice": "Calculator.py",
            "Python": "Python.py",
            "Paint": "Paint.py",
            "Zip": "Zip.py",
            "Task Manager": "TaskManager.py",
            "Weather": "Weather.py",
            "BackGround": "ChangeBG.py",
            "Éteindre": "shutdown"
        }

        for name, action in actions.items():
            act = menu.addAction(name)
            if action == "shutdown":
                act.triggered.connect(self.shutdown)
            else:
                act.triggered.connect(lambda _, s=action: self.launch_app(s))

        return menu

    def launch_app(self, script_name):
        app_path = os.path.join(os.path.dirname(__file__), "apps", script_name)
        if os.path.exists(app_path):
            subprocess.Popen(["python3", app_path])
        else:
            print(f"❌ App introuvable : {app_path}")

    def shutdown(self):
        print("🛑 Extinction de PySystem...")
        os.system("poweroff")  # Pour Linux embarqué

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PySystemDesktop()
    sys.exit(app.exec_())