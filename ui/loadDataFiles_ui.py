# Form implementation generated from reading ui file 'c:\perso\trading\anaconda3\backtrader-ichimoku\ui\loadDataFiles.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(488, 458)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dataFilesListWidget = QtWidgets.QListWidget(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataFilesListWidget.sizePolicy().hasHeightForWidth())
        self.dataFilesListWidget.setSizePolicy(sizePolicy)
        self.dataFilesListWidget.setObjectName("dataFilesListWidget")
        self.gridLayout_2.addWidget(self.dataFilesListWidget, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.importPB = QtWidgets.QPushButton(parent=Form)
        self.importPB.setMinimumSize(QtCore.QSize(0, 40))
        self.importPB.setObjectName("importPB")
        self.gridLayout_2.addWidget(self.importPB, 5, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2.addLayout(self.verticalLayout, 3, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.semicolonRB = QtWidgets.QRadioButton(parent=self.groupBox)
        self.semicolonRB.setObjectName("semicolonRB")
        self.gridLayout.addWidget(self.semicolonRB, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.tabRB = QtWidgets.QRadioButton(parent=self.groupBox)
        self.tabRB.setChecked(True)
        self.tabRB.setObjectName("tabRB")
        self.gridLayout.addWidget(self.tabRB, 3, 1, 1, 1)
        self.commaRB = QtWidgets.QRadioButton(parent=self.groupBox)
        self.commaRB.setObjectName("commaRB")
        self.gridLayout.addWidget(self.commaRB, 3, 2, 1, 1)
        self.filePathLE = QtWidgets.QLineEdit(parent=self.groupBox)
        self.filePathLE.setObjectName("filePathLE")
        self.gridLayout.addWidget(self.filePathLE, 0, 1, 1, 3)
        self.openFilePB = QtWidgets.QToolButton(parent=self.groupBox)
        self.openFilePB.setObjectName("openFilePB")
        self.gridLayout.addWidget(self.openFilePB, 0, 4, 1, 1)
        self.loadFilePB = QtWidgets.QPushButton(parent=self.groupBox)
        self.loadFilePB.setMinimumSize(QtCore.QSize(0, 40))
        self.loadFilePB.setObjectName("loadFilePB")
        self.gridLayout.addWidget(self.loadFilePB, 4, 1, 1, 4)
        self.errorLabel = QtWidgets.QLabel(parent=self.groupBox)
        self.errorLabel.setStyleSheet("color: red")
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout.addWidget(self.errorLabel, 5, 0, 1, 5)
        self.datetimeFormatLE = QtWidgets.QLineEdit(parent=self.groupBox)
        self.datetimeFormatLE.setObjectName("datetimeFormatLE")
        self.gridLayout.addWidget(self.datetimeFormatLE, 1, 1, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setStyleSheet("font-style: italic")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Import one or multiple data files"))
        self.label_4.setText(_translate("Form", "List of all files to import in cerebro"))
        self.importPB.setText(_translate("Form", "Import all data files"))
        self.groupBox.setTitle(_translate("Form", "Loading a new data file"))
        self.semicolonRB.setText(_translate("Form", "semicolon"))
        self.label.setText(_translate("Form", "Import a new data file"))
        self.label_3.setText(_translate("Form", "Date time format"))
        self.label_2.setText(_translate("Form", "Separator"))
        self.tabRB.setText(_translate("Form", "tab"))
        self.commaRB.setText(_translate("Form", "comma"))
        self.openFilePB.setText(_translate("Form", "..."))
        self.loadFilePB.setText(_translate("Form", "Load .CSV file"))
        self.label_5.setText(_translate("Form", "Files should be ordered from lower (on top) to higher timeframe (at bottom)."))
