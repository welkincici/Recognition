# A simple GUI to test and display the function of MobileNet

import sys
import PyQt5.QtWidgets as Qwd
import PyQt5.QtGui as Qg
import Mobilenet as mbn


class Entrance(Qwd.QWidget):

    def __init__(self):
        super(Entrance, self).__init__()

        self.setGeometry(1000, 300, 400, 400)
        self.setWindowTitle('Neo Light Lab')

        self.picture = Qwd.QLabel()
        self.picture.setFixedSize(224, 224)

        self.result = Qwd.QLabel()
        self.result.setFixedSize(224, 224)

        self.file_name = ''

        choose_btn = Qwd.QPushButton('Choose')
        choose_btn.clicked.connect(self.choose)

        identify_btn = Qwd.QPushButton('Identify')
        identify_btn.clicked.connect(self.identify)

        h_box1 = Qwd.QHBoxLayout()
        h_box1.addWidget(self.picture)
        h_box1.addWidget(self.result)

        h_box2 = Qwd.QHBoxLayout()
        h_box2.addWidget(choose_btn)
        h_box2.addWidget(identify_btn)

        v_box = Qwd.QVBoxLayout(self)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)

        self.show()

    def choose(self):
        options = Qwd.QFileDialog.Options()
        options |= Qwd.QFileDialog.DontUseNativeDialog
        self.file_name, _ = Qwd.QFileDialog.getOpenFileName(self, "Choose a picture", "",
                                                   "All Files (*);;JPG Files (*.jpg , *.jpeg)",
                                                   options=options)

        pic = Qg.QPixmap(self.file_name)
        self.picture.setPixmap(pic)
        self.picture.setScaledContents(True)

    def identify(self):
        if self.file_name == '':
            print('please choose a picture!')
        else:
            self.result.setText(mbn.identify(self.file_name))

if __name__ == '__main__':
    app = Qwd.QApplication(sys.argv)
    start = Entrance()
    sys.exit(app.exec_())

