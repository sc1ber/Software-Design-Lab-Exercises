"""
Samuel II C. Imperial
Group03
GUI version of temperature converter
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(300, 300)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(20, 40, 111, 41))
		font = QtGui.QFont()
		font.setFamily("URW Gothic L")
		font.setPointSize(15)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(160, 40, 111, 41))
		font = QtGui.QFont()
		font.setFamily("URW Gothic L")
		font.setPointSize(15)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.fah = QtWidgets.QLineEdit(self.centralwidget)
		self.fah.setGeometry(QtCore.QRect(20, 80, 101, 33))
		self.fah.setObjectName("fah")
		self.cel = QtWidgets.QLineEdit(self.centralwidget)
		self.cel.setGeometry(QtCore.QRect(150, 80, 113, 33))
		self.cel.setObjectName("cel")
		self.ftoc = QtWidgets.QPushButton(self.centralwidget)
		self.ftoc.setGeometry(QtCore.QRect(90, 130, 98, 31))
		self.ftoc.setObjectName("ftoc")
		self.ctof = QtWidgets.QPushButton(self.centralwidget)
		self.ctof.setGeometry(QtCore.QRect(90, 170, 98, 31))
		self.ctof.setObjectName("ctof")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 25))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		self.ftoc.clicked.connect(self.fftocc)
		self.ctof.clicked.connect(self.cctoff)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Temperature Converter"))
		self.label.setText(_translate("MainWindow", "Fahrenheit"))
		self.label_2.setText(_translate("MainWindow", "Celcius"))
		self.fah.setText(_translate("MainWindow", "32.0"))
		self.cel.setText(_translate("MainWindow", "0.0"))
		self.ftoc.setText(_translate("MainWindow", ">>>>"))
		self.ctof.setText(_translate("MainWindow", "<<<<"))

	def fftocc(self):
		cels = (float(self.fah.text()) - 32) * 5/9
		celss = round(cels, 2)
		self.cel.setText(str(celss))

	def cctoff(self):
		fahs = (float(self.cel.text()) * 9/5) + 32
		fahss = round(fahs, 2)
		self.fah.setText(str(fahss))

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
