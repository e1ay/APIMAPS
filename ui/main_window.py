from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QKeyEvent
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication

from app_services.map_app_service import MapAppService
from domain.request import Request
from services.ya_map_service import YaMapService


class MainWindow(QWidget):
    def __init__(self, app_service:MapAppService, parent=None):
        super().__init__(parent)
        self.initUI()
        self.app_service = app_service
        self.request = Request()
        self.show_map()

    def initUI(self):
        self.setGeometry(100, 100, 1000, 800)
        self.map_label = QLabel(self)

        layout = QVBoxLayout(self)
        layout.addWidget(self.map_label)

        self.setLayout(layout)

    def show_map(self):
        map = self.app_service.execute(self.request)

        pixmap = QPixmap()
        pixmap.loadFromData(map, 'PNG')
        self.map_label.setPixmap(pixmap)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()
        if key == Qt.Key_PageUp:
            self.request.up_zoom()
        elif key == Qt.Key_PageDown:
            self.request.down_zoom()
        self.show_map()
if __name__ == '__main__':
    app = QApplication([])

    map_service = YaMapService()
    app_map_service = MapAppService(map_service)

    window = MainWindow(app_map_service)
    window.show()

    app.exec()
