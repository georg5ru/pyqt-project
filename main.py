from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # геометрия окна
        self.setWindowTitle("Codeloop - PyQt5 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('icon.png'))

        # инициализация интерфейса
        self.init_ui()
        self.show()

    def init_ui(self):
        # создание плеера
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()

        # кнопки
        open_button = QPushButton('Open Video')
        open_button.setStyleSheet(
            "QPushButton { background-color: #f0f0f0; border: 1px solid #707070; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color: #e0e0e0; }"
        )
        open_button.clicked.connect(self.open_file)

        self.play_button = QPushButton('Play')
        self.play_button.setStyleSheet(
            "QPushButton { background-color: #f0f0f0; border: 1px solid #707070; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color: #e0e0e0; }"
        )
        self.play_button.setEnabled(False)
        self.play_button.clicked.connect(self.play_video)

        self.pause_button = QPushButton('Pause')
        self.pause_button.setStyleSheet(
            "QPushButton { background-color: #f0f0f0; border: 1px solid #707070; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color: #e0e0e0; }"
        )
        self.pause_button.setEnabled(False)
        self.pause_button.clicked.connect(self.pause_video)

        self.stopBtn = QPushButton('Stop')
        self.stopBtn.setStyleSheet(
            "QPushButton { background-color: #f0f0f0; border: 1px solid #707070; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color: #e0e0e0; }"
        )
        self.stopBtn.setEnabled(False)
        self.stopBtn.clicked.connect(self.stop_video)

        # слайдеры звука и момента
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setStyleSheet(
            "QSlider::groove:horizontal { height: 6px; background: #f0f0f0; border: 1px solid #707070; border-radius: 3px; }"
            "QSlider::handle:horizontal { background: #007bff; border: 1px solid #0056b3; width: 14px; margin: -5px 0px; border-radius: 7px; }"
            "QSlider::add-page:horizontal { background: white; }"
            "QSlider::sub-page:horizontal { background: #007bff; }"
        )
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.set_position)

        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setStyleSheet(
            "QSlider::groove:horizontal { height: 6px; background: #f0f0f0; border: 1px solid #707070; border-radius: 3px; }"
            "QSlider::handle:horizontal { background: #007bff; border: 1px solid #0056b3; width: 14px; margin: -5px 0px; border-radius: 7px; }"
            "QSlider::add-page:horizontal { background: white; }"
            "QSlider::sub-page:horizontal { background: #007bff; }"
        )
        self.volumeSlider.setValue(100)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setToolTip("Volume")
        self.volumeSlider.valueChanged.connect(self.change_volume)

        # лейаут горизонтальный
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(open_button)
        hboxLayout.addWidget(self.play_button)
        hboxLayout.addWidget(self.pause_button)
        hboxLayout.addWidget(self.stopBtn)
        hboxLayout.addWidget(self.positionSlider)
        hboxLayout.addWidget(self.volumeSlider)

        # лейаут вертикальный
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)

        # лейаут
        self.setLayout(vboxLayout)
        self.mediaPlayer.setVideoOutput(videowidget)

        # соединение сигналов и действий
        self.mediaPlayer.stateChanged.connect(self.media_state_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        # выбор файла
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.play_button.setEnabled(True)
            self.pause_button.setEnabled(True)
            self.stopBtn.setEnabled(True)

    def play_video(self):
        # старт
        self.mediaPlayer.play()

    def pause_video(self):
        # пауза
        self.mediaPlayer.pause()

    def stop_video(self):
        # стоп
        self.mediaPlayer.stop()

    def media_state_changed(self, state):
        # позиция кнопок
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.play_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.stopBtn.setEnabled(True)
        else:
            self.play_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.stopBtn.setEnabled(False)

    def position_changed(self, position):
        # позиция слайдера
        self.positionSlider.setValue(position)

    def duration_changed(self, duration):
        # длина слайдера
        self.positionSlider.setRange(0, duration)

    def set_position(self, position):
        # позиция видео от слайдера
        self.mediaPlayer.setPosition(position)

    def change_volume(self, volume):
        # звук от слайдера
        self.mediaPlayer.setVolume(volume)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())