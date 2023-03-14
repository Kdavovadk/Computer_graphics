import sys

from collections.abc import Callable
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import *


class MainMenuWindow(QMainWindow):
    window_size: tuple[int, int]
    labs_count: int = 6
    labs_buttons: list[QPushButton] = []
    labs_runs: list[Callable[[], None]] = []

    def __init__(self, application_name: str, window_size: tuple[int, int]):
        super().__init__()

        self.setWindowTitle(application_name)
        self.window_size = window_size
        self.setFixedSize(QSize(self.window_size[0], self.window_size[1]))

        self.layout = QVBoxLayout()
        self._add_buttons()

        container = QWidget()
        container.setLayout(self.layout)

        self.setCentralWidget(container)

    def _create_button(self, lab_index: int) -> QPushButton:
        push_button = QPushButton()
        push_button.setText(f"Лабораторная работа №{lab_index}")
        push_button.setFixedSize(QSize(self.window_size[0], self.window_size[1] // 6))
        push_button.clicked.connect(self.labs_runs[lab_index - 1])

        return push_button

    def _add_buttons(self):
        self.labs_runs = [
            self._run_lab1,
            self._run_lab2,
            self._run_lab3,
            self._run_lab4,
            self._run_lab5,
            self._run_lab6,
        ]

        for index in range(self.labs_count):
            self.labs_buttons.append(self._create_button(index + 1))
            self.layout.addWidget(self.labs_buttons[index])

    def _run_lab1(self):
        print(self.labs_buttons[0].text())

    def _run_lab2(self):
        print(self.labs_buttons[1].text())

    def _run_lab3(self):
        print(self.labs_buttons[2].text())

    def _run_lab4(self):
        print(self.labs_buttons[3].text())

    def _run_lab5(self):
        print(self.labs_buttons[4].text())

    def _run_lab6(self):
        print(self.labs_buttons[5].text())


def run_application():
    labs_app = QApplication(sys.argv)

    labs_menu_window = MainMenuWindow("Компьютерная графика", (400, 300))
    labs_menu_window.show()

    labs_app.exec()


if __name__ == "__main__":
    run_application()
