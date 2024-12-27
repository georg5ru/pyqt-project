from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt, QUrl
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SH mediaplayer")
        self.setGeometry(350, 100, 700, 500)
        self.init_ui()
        self.show()

    def init_ui(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videowidget = QVideoWidget()
        open_button = QPushButton('Open Video')
        open_button.clicked.connect(self.open_file)
        self.play_button = QPushButton('Play')
        self.play_button.setEnabled(False)
        self.play_button.clicked.connect(self.play_video)
        self.pause_button = QPushButton('Pause')
        self.pause_button.setEnabled(False)
        self.pause_button.clicked.connect(self.pause_video)
        self.stop_button = QPushButton('Stop')
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_video)
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.set_position)
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setToolTip("Volume")
        self.volumeSlider.valueChanged.connect(self.change_volume)
        hbox = QHBoxLayout()
        hbox.addWidget(open_button)
        hbox.addWidget(self.play_button)
        hbox.addWidget(self.pause_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.positionSlider)
        hbox.addWidget(self.volumeSlider)
        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.mediaPlayer.setVideoOutput(videowidget)
        self.mediaPlayer.stateChanged.connect(self.media_state_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.play_button.setEnabled(True)
            self.pause_button.setEnabled(True)
            self.stop_button.setEnabled(True)

    def play_video(self):
        self.mediaPlayer.play()

    def pause_video(self):
        self.mediaPlayer.pause()

    def stop_video(self):
        self.mediaPlayer.stop()

    def media_state_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.play_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.stop_button.setEnabled(True)
        else:
            self.play_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.stop_button.setEnabled(False)

    def position_changed(self, position):
        self.positionSlider.setValue(position)

    def duration_changed(self, duration):
        self.positionSlider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def change_volume(self, volume):
        self.mediaPlayer.setVolume(volume)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
