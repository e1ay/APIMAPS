from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QKeyEvent
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QPushButton

from app_services.map_app_service import MapAppService
from domain.request import Request
from services.ya_map_service import YaMapService


class MainWindow(QWidget):
    def __init__(self, app_service: MapAppService, parent=None):
        super().__init__(parent)
        self.initUI()
        self.app_service = app_service
        self.request = Request()
        self.show_map()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 800)
        self.map_label = QLabel(self)

        self.label1 = QLabel(self)
        self.label1.setText('Нажмите "S" чтобы поменять на спутник')
        self.label1.resize(210, 30)
        self.label1.move(0, 0)

        self.label2 = QLabel(self)
        self.label2.setText('Нажмите "M" чтобы поменять на схему')
        self.label2.move(0, 30)
        self.label2.resize(210, 30)

        self.label3 = QLabel(self)
        self.label3.setText('Нажмите "G" чтобы поменять на гибрид')
        self.label3.resize(210, 30)
        self.label3.move(0, 60)

        layout = QVBoxLayout(self)
        layout.addWidget(self.map_label)

        self.setLayout(layout)

    def show_map(self):
        map = self.app_service.execute(self.request)

        pixmap = QPixmap()
        pixmap.loadFromData(map, self.request.type)
        self.map_label.setPixmap(pixmap)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == Qt.Key_PageUp:
            self.request.up_zoom()
        elif key == Qt.Key_PageDown:
            self.request.down_zoom()
        elif key == Qt.Key_Left:
            self.request.left()
        elif key == Qt.Key_Right:
            self.request.right()
        elif key == Qt.Key_Up:
            self.request.up()
        elif key == Qt.Key_Down:
            self.request.down()
        elif key == Qt.Key_S:
            self.request.l = 'sat'
            self.request.type = 'JPG'
        elif key == Qt.Key_M:
            self.request.l = 'map'
            self.request.type = 'PNG'
        elif key == Qt.Key_G:
            self.request.l = 'sat,skl'
            self.request.type = 'JPG'

        self.show_map()


if __name__ == '__main__':
    app = QApplication([])

    map_service = YaMapService()
    app_map_service = MapAppService(map_service)

    window = MainWindow(app_map_service)
    window.show()

    app.exec()
