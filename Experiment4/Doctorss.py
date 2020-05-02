"""
Samuel Imperial
Group03
GUI version of Doctor class
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import os.path
from os import path

class Ui_Doctor(object):
	history = []
	hedges = ("Please tell me more.","Many of my patients tell me the same thing.","Please coninue.")
	qualifiers = ("Why do you say that ",
                  "You seem to think that ",
                  "Can you explain why ")
	replacements = {"I": "you", "me": "you", "my": "your",
                    "we": "you", "us": "you", "mine": "yours",
                    "you": "I", "your": "my", "yours": "mine", "am" : "are",
							"i": "you"}

	def __init__(self, patientn):
		self.patientn = patientn

	def reply(self):
		self.patientn = open(self.searchpatient.text(), "a")
		probability = random.randint(1, 5)
		if probability in (1, 2):
			answer = random.choice(Ui_Doctor.hedges)
		elif probability == 3 and len(Ui_Doctor.history) > 3:
			answer = "Earlier you said that " + \
				self.changePerson(random.choice(Ui_Doctor.history))
		else:
			answer = random.choice(Ui_Doctor.qualifiers) + \
				self.changePerson(self.replyyou.text())
		Ui_Doctor.history.append(self.replyyou.text())
		self.patientn.write(self.replyyou.text())
		self.patientn.write("\n")
		self.patientn.close()
		textread = open(self.searchpatient.text(), "r+")
		self.history.setPlainText(textread.read())
		self.doc.setText(answer)
		if self.replyyou.text() == "bye" or self.replyyou.text() == "Bye":
			self.doc.setText("Have a nice day!")
		self.replyyou.clear()

	def changePerson(self, sentence):
		words = sentence.split()
		replyWords = []
		for word in words:
			replyWords.append(Ui_Doctor.replacements.get(word, word))
		return " ".join(replyWords)

	def searchpatientname(self):
		if path.exists(self.searchpatient.text()):
			self.patientn = open(self.searchpatient.text(), "a")
			self.nopatient.setText("Patient found!")
			self.createpatient.clear()
		else:
			self.nopatient.setText("Patient does not exist!")
			self.createpatient.setText("Create new patient?")
			self.yess.show()
			self.noo.show()

	def createnewpatient(self):
		self.patientn = open(self.searchpatient.text(), "w+")
		self.nopatient.setText("")
		self.createpatient.setText("Created successfuly!")
		self.yess.hide()
		self.noo.hide()

	def dontcreate(self):
		self.nopatient.setText("")
		self.createpatient.setText("")
		self.yess.hide()
		self.noo.hide()

	def setupUi(self, Doctor):
		Doctor.setObjectName("Doctor")
		Doctor.resize(489, 410)
		self.centralwidget = QtWidgets.QWidget(Doctor)
		self.centralwidget.setObjectName("centralwidget")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(30, 30, 141, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.searchpatient = QtWidgets.QLineEdit(self.centralwidget)
		self.searchpatient.setGeometry(QtCore.QRect(170, 32, 211, 31))
		self.searchpatient.setObjectName("searchpatient")
		self.searchbtn = QtWidgets.QPushButton(self.centralwidget)
		self.searchbtn.setGeometry(QtCore.QRect(390, 30, 71, 31))
		self.searchbtn.setObjectName("searchbtn")
		self.nopatient = QtWidgets.QLabel(self.centralwidget)
		self.nopatient.setGeometry(QtCore.QRect(170, 0, 211, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.nopatient.setFont(font)
		self.nopatient.setAlignment(QtCore.Qt.AlignCenter)
		self.nopatient.setObjectName("nopatient")
		self.createpatient = QtWidgets.QLabel(self.centralwidget)
		self.createpatient.setGeometry(QtCore.QRect(170, 70, 211, 31))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.createpatient.setFont(font)
		self.createpatient.setAlignment(QtCore.Qt.AlignCenter)
		self.createpatient.setObjectName("createpatient")
		self.yess = QtWidgets.QPushButton(self.centralwidget)
		self.yess.setGeometry(QtCore.QRect(380, 70, 41, 31))
		self.yess.setObjectName("yess")
		self.yess.hide()
		self.noo = QtWidgets.QPushButton(self.centralwidget)
		self.noo.setGeometry(QtCore.QRect(420, 70, 41, 31))
		self.noo.setObjectName("noo")
		self.noo.hide()
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(30, 110, 71, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.doc = QtWidgets.QLabel(self.centralwidget)
		self.doc.setGeometry(QtCore.QRect(100, 110, 381, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.doc.setFont(font)
		self.doc.setObjectName("doc")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(30, 150, 71, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_4.setFont(font)
		self.label_4.setObjectName("label_4")
		self.replyyou = QtWidgets.QLineEdit(self.centralwidget)
		self.replyyou.setGeometry(QtCore.QRect(100, 150, 361, 31))
		self.replyyou.setObjectName("replyyou")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(30, 190, 151, 31))
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.history = QtWidgets.QPlainTextEdit(self.centralwidget)
		self.history.setGeometry(QtCore.QRect(30, 220, 261, 131))
		font = QtGui.QFont()
		font.setPointSize(9)
		font.setItalic(True)
		self.history.setFont(font)
		self.history.setObjectName("history")
		Doctor.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(Doctor)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 25))
		self.menubar.setObjectName("menubar")
		Doctor.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(Doctor)
		self.statusbar.setObjectName("statusbar")
		Doctor.setStatusBar(self.statusbar)

		self.retranslateUi(Doctor)
		self.searchbtn.clicked.connect(self.searchpatientname)
		self.yess.clicked.connect(self.createnewpatient)
		self.noo.clicked.connect(self.dontcreate)
		self.replyyou.returnPressed.connect(self.reply)
		QtCore.QMetaObject.connectSlotsByName(Doctor)

	def retranslateUi(self, Doctor):
		_translate = QtCore.QCoreApplication.translate
		Doctor.setWindowTitle(_translate("Doctor", "Doctors"))
		self.label_2.setText(_translate("Doctor", "Patient\'s name:"))
		self.searchbtn.setText(_translate("Doctor", "Search"))
		self.nopatient.setText(_translate("Doctor", "."))
		self.createpatient.setText(_translate("Doctor", "."))
		self.yess.setText(_translate("Doctor", "yes"))
		self.noo.setText(_translate("Doctor", "no"))
		self.label_3.setText(_translate("Doctor", "Doctor:"))
		self.doc.setText(_translate("Doctor", "Good morning, I hope you are well today"))
		self.label_4.setText(_translate("Doctor", "You:"))
		self.label_5.setText(_translate("Doctor", "Patient\'s history: "))


if __name__ == "__main__":
	import sys
	patient = open("dump", "w")
	app = QtWidgets.QApplication(sys.argv)
	Doctor = QtWidgets.QMainWindow()
	ui = Ui_Doctor(patients)
	ui.setupUi(Doctor)
	Doctor.show()
	sys.exit(app.exec_())
