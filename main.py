from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, \
    QSizePolicy
import sys
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Media Player for SH')
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('images/icon_of_app.jpg'))
        palet = self.palette()
        palet.setColor(QPalette.Window, Qt.black)
        self.setPalette(palet)
        self.show()
        self.init_ui()

    def init_ui(self):
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # видео виджет
        videowidget = QVideoWidget()

        # кнопка
        open_button = QPushButton('Open Video')
        self.play_button = QPushButton('')
        self.play_button.setEnabled(False)
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))


        # слайдер
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)


        # лейбл
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)


        #hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # виджеты для хбокс ейаута
        hboxLayout.addWidget(open_button)
        hboxLayout.addWidget(self.play_button)
        hboxLayout.addWidget(self.slider)


        #vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)




        self.setLayout(vboxLayout)
app = QApplication(sys.argv)
window = Window() #помогите меня держат в заложниках
sys.exit(app.exec_())