from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Dictionary import Dictionary
from Countdown import Countdown
from threading import Thread


class Ui_MainWindow(QtWidgets.QMainWindow):
        def setupUi(self, MainWindow):
                self.new_dictionary = Dictionary()
                self.new_countdown = Countdown()
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(800, 600)
                MainWindow.setStyleSheet("background-color: #00af91;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.title = QtWidgets.QLabel(self.centralwidget)
                self.title.setGeometry(QtCore.QRect(10, 0, 781, 71))
                font = QtGui.QFont()
                font.setFamily("Hachi Maru Pop")
                font.setPointSize(40)
                font.setBold(False)
                font.setWeight(50)
                self.title.setFont(font)
                self.title.setStyleSheet("color: #ffffff;\n"
        "")
                self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.title.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
                self.title.setObjectName("title")
                self.timerTitle = QtWidgets.QLabel(self.centralwidget)
                self.timerTitle.setGeometry(QtCore.QRect(30, 100, 101, 31))
                font = QtGui.QFont()
                font.setFamily("Orbitron")
                font.setPointSize(22)
                font.setItalic(False)
                self.timerTitle.setFont(font)
                self.timerTitle.setStyleSheet("color: rgb(238, 238, 236);")
                self.timerTitle.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
                self.timerTitle.setObjectName("timerTitle")
                self.TimerNumber = QtWidgets.QLCDNumber(self.centralwidget)
                self.TimerNumber.setGeometry(QtCore.QRect(20, 140, 121, 31))
                self.TimerNumber.setStyleSheet("background-color: #007965;\n"
        "")
                self.TimerNumber.setSmallDecimalPoint(False)
                self.TimerNumber.setDigitCount(5)
                self.TimerNumber.setProperty("value", 60.0)
                self.TimerNumber.setProperty("intValue", 60)
                self.TimerNumber.setObjectName("TimerNumber")
                self.WordsTitle = QtWidgets.QLabel(self.centralwidget)
                self.WordsTitle.setGeometry(QtCore.QRect(150, 100, 121, 31))
                font = QtGui.QFont()
                font.setPointSize(22)
                self.WordsTitle.setFont(font)
                self.WordsTitle.setStyleSheet("color: rgb(238, 238, 236);")
                self.WordsTitle.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
                self.WordsTitle.setObjectName("WordsTitle")
                self.textContainer = QtWidgets.QTextBrowser(self.centralwidget)
                self.textContainer.setGeometry(QtCore.QRect(150, 140, 591, 221))
                self.textContainer.setStyleSheet("background-color: rgb(238, 238, 236);\n"
        "border: 1px solid black;")
                self.textContainer.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
                self.textContainer.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
                self.textContainer.setObjectName("textContainer")
                self.ActiveWord = QtWidgets.QLabel(self.centralwidget)
                self.ActiveWord.setGeometry(QtCore.QRect(550, 110, 191, 21))
                self.ActiveWord.setStyleSheet("background-color: rgb(238, 238, 236);\n"
        "color: rgb(0, 0, 0);\n"
        "border: 1px solid black;")
                self.ActiveWord.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.ActiveWord.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
                self.ActiveWord.setObjectName("ActiveWord")
                self.SecondTItle = QtWidgets.QLabel(self.centralwidget)
                self.SecondTItle.setGeometry(QtCore.QRect(150, 370, 591, 71))
                font = QtGui.QFont()
                font.setFamily("Hachi Maru Pop")
                font.setPointSize(25)
                self.SecondTItle.setFont(font)
                self.SecondTItle.setStyleSheet("color: rgb(238, 238, 236);")
                self.SecondTItle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.SecondTItle.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
                self.SecondTItle.setObjectName("SecondTItle")
                self.UserInput = QtWidgets.QLineEdit(self.centralwidget)
                self.UserInput.setGeometry(QtCore.QRect(152, 470, 591, 51))
                self.UserInput.setStyleSheet("background-color: rgb(238, 238, 236);\n"
        "color: rgb(0, 0, 0);\n"
        "border: 1px solid black;")
                self.UserInput.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.UserInput.setObjectName("UserInput")
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.UserInput.keyPressEvent = self.write
                self.changeActiveWord(self.new_dictionary.word_active)
                text_cont = self.new_dictionary.create_text()
                self.changeWords(text_cont)
                self.UserInput.installEventFilter(self)


        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Speed Word Test"))
                self.title.setText(_translate("MainWindow", "SPEED WORD TEST"))
                self.timerTitle.setText(_translate("MainWindow", "TIMER"))
                self.WordsTitle.setText(_translate("MainWindow", "WORDS"))
                self.textContainer.setPlaceholderText(_translate("MainWindow", "Loading words..."))
                self.ActiveWord.setText(_translate("MainWindow", "ActiveWord"))
                self.SecondTItle.setText(_translate("MainWindow", "WRITE BELOW"))
                self.UserInput.setPlaceholderText(_translate("MainWindow", "Write Here"))

        def write(self, e):
                original_text = self.UserInput.text()
                if e.key() == QtCore.Qt.Key.Key_Space or e.key() == QtCore.Qt.Key.Key_Backspace:
                        self.new_dictionary.check_word(original_text)
                        self.changeActiveWord(self.new_dictionary.word_active)
                        self.UserInput.setText('')
                        if self.new_dictionary.end:
                                self.messageBox()
                else:
                        key = e.text()
                        self.UserInput.setText(self.UserInput.text() + key)

        def eventFilter(self, source, event):
                if event.type() == QtCore.QEvent.Type.FocusIn:
                        if not self.new_countdown.start:
                                countodwn_thread = Thread(target=self.new_countdown.starterd)
                                self.time_up(countodwn_thread)
                                return True
                return False

        def changeWords(self, words):
                self.textContainer.setPlainText(words)

        def changeActiveWord(self, word):
                self.ActiveWord.setText(word)


        def messageBox(self):
                msg = QMessageBox()
                text = f'Words per minute: {self.new_dictionary.word_guess}'
                msg.setText(text)
                msg.setWindowTitle("Final Score")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
                self.start_again()

        def start_again(self):
                self.UserInput.clearFocus()
                self.TimerNumber.setProperty("value", 60.0)
                self.TimerNumber.setProperty("intValue", 60)
                QtWidgets.QApplication.processEvents()
                self.TimerNumber.display(60)
                self.new_dictionary.reset()
                self.changeActiveWord(self.new_dictionary.word_active)
                self.new_countdown = Countdown()

        
        def time_up(self, count):
                count.start()
                while self.new_countdown.my_timer > 0 and self.new_countdown.start: 
                        QtWidgets.QApplication.processEvents()
                        self.TimerNumber.display(self.new_countdown.my_timer)
                self.messageBox()
                