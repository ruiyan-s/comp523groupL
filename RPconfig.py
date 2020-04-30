# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RPconfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os


class Ui_MainWindow(object):
    def __init__(self):
        self.controller = ""
        self.plant = ""
        self.intermediate_node = ""
        self.value_type = ""
        self.initial_value = ""
        self.controller_formula = ""
        self.loss_rule = ""
        self.timeout_threshold = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 514)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(
            650, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.setItemText(0, "")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_6)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_4)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.setItemText(0, "")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.verticalLayout_7.addWidget(self.comboBox_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_5.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Controller"))
        self.label_2.setText(_translate("MainWindow", "Plant"))
        self.label_3.setText(_translate("MainWindow", "Intermediate Node"))

        self.lineEdit_3.setPlaceholderText(_translate(
            "MainWindow", "Please enter MAC address"))
        self.lineEdit_4.setPlaceholderText(_translate(
            "MainWindow", "Please enter MAC address"))
        self.lineEdit_5.setPlaceholderText(_translate(
            "MainWindow", "Please enter MAC address"))

        self.lineEdit_3.editingFinished.connect(self.handleController)
        self.lineEdit_4.editingFinished.connect(self.handleIntermediateNode)
        self.lineEdit_5.editingFinished.connect(self.handlePlant)

        self.label_4.setText(_translate("MainWindow", "Value Type"))
        self.label_5.setText(_translate("MainWindow", "Value"))
        self.label_6.setText(_translate("MainWindow", "Controller Formula"))

        self.comboBox_6.setItemText(1, _translate("MainWindow", "Integer"))
        # self.comboBox_6.setItemText(2, _translate("MainWindow", "Matrix"))
        self.comboBox_6.activated.connect(self.handleValueType)

        self.lineEdit.setPlaceholderText(
            _translate("MainWindow", "Initial Input"))
        self.lineEdit_2.setPlaceholderText(
            _translate("MainWindow", "e.g. y=2*x^2"))

        self.lineEdit.editingFinished.connect(self.handleValue)
        self.lineEdit_2.editingFinished.connect(self.handleFormula)

        self.label_7.setText(_translate("MainWindow", "How to deal with loss"))
        self.label_8.setText(_translate("MainWindow", "Time-out threshold"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Re-transmit"))
        # self.comboBox_4.setItemText(
        #     2, _translate("MainWindow", "Switch route"))
        # self.comboBox_4.setItemText(
        #     3, _translate("MainWindow", "Take a guess"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "1 s"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "2 s"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "3 s"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "4 s"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "5 s"))

        self.comboBox_4.activated.connect(self.handleLoss)
        self.comboBox_5.activated.connect(self.handleTime)

        self.pushButton_2.setText(_translate("MainWindow", "Reset"))
        self.pushButton.setText(_translate("MainWindow", "Done"))

        self.pushButton_2.clicked.connect(self.triggerReset)
        self.pushButton.clicked.connect(self.triggerInterface)

        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def handleController(self):
        self.controller = self.lineEdit_3.text()

    def handlePlant(self):
        self.plant = self.lineEdit_5.text()

    def handleIntermediateNode(self):
        self.intermediate_node = self.lineEdit_4.text()
        print(self.intermediate_node)

    def handleValueType(self, index):
        self.value_type = self.comboBox_6.itemText(index)

    def handleValue(self):
        self.initial_value = self.lineEdit.text()

    def handleFormula(self):
        self.controller_formula = self.lineEdit_2.text()

    def handleLoss(self, index):
        self.loss_rule = self.comboBox_4.itemText(index)

    def handleTime(self, index):
        self.timeout_threshold = self.comboBox_5.itemText(index)

    def triggerReset(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def triggerInterface(self):
        last = str(int(self.intermediate_node[-2:])+1)
        print(last)
        self.intermediate_node = self.intermediate_node[:-2]
        self.intermediate_node += last
        with open ("code_source/controller.py", "r") as controllerCode:
            controllerCode=controllerCode.readlines()
        with open ("code_source/hop.py", "r") as hopCode:
            hopCode=hopCode.readlines()
        with open ("code_source/plant.py", "r") as plantCode:
            plantCode=plantCode.readlines()

        if os.path.exists("controllerArgs.txt"):
            os.remove("controllerArgs.txt")
        with open("controllerArgs.txt", "a+") as controllerArgs:
            controllerArgs.write(self.intermediate_node + "\n")
            controllerArgs.write(self.controller_formula + "\n")
            controllerArgs.write(self.timeout_threshold + "\n")
        controllerArgs.close()
        if os.path.exists("plantArgs.txt"):
            os.remove("plantArgs.txt")
        with open("plantArgs.txt", "a+") as plantArgs:
            plantArgs.write(self.intermediate_node+"\n")
            plantArgs.write(self.initial_value+"\n")
        plantArgs.close()
        print(self.intermediate_node)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
