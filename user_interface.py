# Form implementation generated from reading ui file 'ui_interface.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(547, 731)
        MainWindow.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(parent=self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(20, 10, 511, 641))
        self.toolBox.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"background-color: rgb(122, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.toolBox.setObjectName("toolBox")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 511, 491))
        self.widget.setObjectName("widget")
        self.pushButton_Show_All = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_Show_All.setGeometry(QtCore.QRect(310, 20, 141, 24))
        self.pushButton_Show_All.setStyleSheet("background-color: rgb(76, 70, 64);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Show_All.setObjectName("pushButton_Show_All")
        self.pushButton_Connect = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_Connect.setGeometry(QtCore.QRect(40, 20, 141, 24))
        self.pushButton_Connect.setStyleSheet("background-color: rgb(76, 70, 64);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Connect.setObjectName("pushButton_Connect")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.widget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 421, 391))
        self.tableWidget.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.toolBox.addItem(self.widget, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_4.setObjectName("page_4")
        self.lineEdit_Added_name = QtWidgets.QLineEdit(parent=self.page_4)
        self.lineEdit_Added_name.setGeometry(QtCore.QRect(110, 40, 271, 22))
        self.lineEdit_Added_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Added_name.setObjectName("lineEdit_Added_name")
        self.label_3 = QtWidgets.QLabel(parent=self.page_4)
        self.label_3.setGeometry(QtCore.QRect(170, 20, 151, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_Added_number = QtWidgets.QLineEdit(parent=self.page_4)
        self.lineEdit_Added_number.setGeometry(QtCore.QRect(110, 100, 271, 22))
        self.lineEdit_Added_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Added_number.setObjectName("lineEdit_Added_number")
        self.label_4 = QtWidgets.QLabel(parent=self.page_4)
        self.label_4.setGeometry(QtCore.QRect(170, 70, 151, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_Added_comment = QtWidgets.QLineEdit(parent=self.page_4)
        self.lineEdit_Added_comment.setGeometry(QtCore.QRect(110, 160, 271, 22))
        self.lineEdit_Added_comment.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_Added_comment.setObjectName("lineEdit_Added_comment")
        self.label_5 = QtWidgets.QLabel(parent=self.page_4)
        self.label_5.setGeometry(QtCore.QRect(170, 130, 151, 20))
        self.label_5.setObjectName("label_5")
        self.pushButton_Added = QtWidgets.QPushButton(parent=self.page_4)
        self.pushButton_Added.setGeometry(QtCore.QRect(170, 200, 141, 24))
        self.pushButton_Added.setStyleSheet("background-color: rgb(76, 70, 64);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Added.setObjectName("pushButton_Added")
        self.toolBox.addItem(self.page_4, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 511, 491))
        self.page.setObjectName("page")
        self.lineEdit_found_name = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit_found_name.setGeometry(QtCore.QRect(120, 20, 271, 22))
        self.lineEdit_found_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_found_name.setObjectName("lineEdit_found_name")
        self.label_6 = QtWidgets.QLabel(parent=self.page)
        self.label_6.setGeometry(QtCore.QRect(180, 0, 151, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit_found_number = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit_found_number.setGeometry(QtCore.QRect(120, 80, 271, 22))
        self.lineEdit_found_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_found_number.setObjectName("lineEdit_found_number")
        self.label_8 = QtWidgets.QLabel(parent=self.page)
        self.label_8.setGeometry(QtCore.QRect(180, 50, 151, 20))
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(parent=self.page)
        self.label_11.setGeometry(QtCore.QRect(-10, 150, 521, 20))
        self.label_11.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.lineEdit_update_name = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit_update_name.setGeometry(QtCore.QRect(120, 210, 271, 22))
        self.lineEdit_update_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_update_name.setObjectName("lineEdit_update_name")
        self.lineEdit_update_number = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit_update_number.setGeometry(QtCore.QRect(120, 270, 271, 22))
        self.lineEdit_update_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_update_number.setObjectName("lineEdit_update_number")
        self.lineEdit_update_comment = QtWidgets.QLineEdit(parent=self.page)
        self.lineEdit_update_comment.setGeometry(QtCore.QRect(120, 320, 271, 22))
        self.lineEdit_update_comment.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_update_comment.setObjectName("lineEdit_update_comment")
        self.label_12 = QtWidgets.QLabel(parent=self.page)
        self.label_12.setGeometry(QtCore.QRect(180, 190, 151, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.page)
        self.label_13.setGeometry(QtCore.QRect(180, 240, 151, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.page)
        self.label_14.setGeometry(QtCore.QRect(180, 290, 151, 20))
        self.label_14.setObjectName("label_14")
        self.pushButton_Update = QtWidgets.QPushButton(parent=self.page)
        self.pushButton_Update.setGeometry(QtCore.QRect(190, 350, 141, 24))
        self.pushButton_Update.setStyleSheet("background-color: rgb(76, 70, 64);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Update.setObjectName("pushButton_Update")
        self.toolBox.addItem(self.page, "")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_7.setObjectName("page_7")
        self.lineEdit_del_nume = QtWidgets.QLineEdit(parent=self.page_7)
        self.lineEdit_del_nume.setGeometry(QtCore.QRect(100, 90, 271, 22))
        self.lineEdit_del_nume.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_del_nume.setObjectName("lineEdit_del_nume")
        self.label_15 = QtWidgets.QLabel(parent=self.page_7)
        self.label_15.setGeometry(QtCore.QRect(170, 20, 151, 20))
        self.label_15.setObjectName("label_15")
        self.lineEdit_del_number = QtWidgets.QLineEdit(parent=self.page_7)
        self.lineEdit_del_number.setGeometry(QtCore.QRect(100, 40, 271, 22))
        self.lineEdit_del_number.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_del_number.setObjectName("lineEdit_del_number")
        self.label_16 = QtWidgets.QLabel(parent=self.page_7)
        self.label_16.setGeometry(QtCore.QRect(170, 70, 151, 20))
        self.label_16.setObjectName("label_16")
        self.pushButton_dell = QtWidgets.QPushButton(parent=self.page_7)
        self.pushButton_dell.setGeometry(QtCore.QRect(180, 120, 141, 24))
        self.pushButton_dell.setStyleSheet("background-color: rgb(76, 70, 64);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_dell.setObjectName("pushButton_dell")
        self.toolBox.addItem(self.page_7, "")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_8.setObjectName("page_8")
        self.pushButton_claer = QtWidgets.QPushButton(parent=self.page_8)
        self.pushButton_claer.setGeometry(QtCore.QRect(310, 20, 141, 24))
        self.pushButton_claer.setStyleSheet("background-color: rgb(76, 70, 64);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_claer.setObjectName("pushButton_claer")
        self.lineEdit_found_many_name = QtWidgets.QLineEdit(parent=self.page_8)
        self.lineEdit_found_many_name.setGeometry(QtCore.QRect(100, 70, 271, 22))
        self.lineEdit_found_many_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_found_many_name.setObjectName("lineEdit_found_many_name")
        self.label_17 = QtWidgets.QLabel(parent=self.page_8)
        self.label_17.setGeometry(QtCore.QRect(150, 50, 151, 20))
        self.label_17.setObjectName("label_17")
        self.listWidget = QtWidgets.QListWidget(parent=self.page_8)
        self.listWidget.setGeometry(QtCore.QRect(100, 100, 271, 321))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        self.pushButton_Found = QtWidgets.QPushButton(parent=self.page_8)
        self.pushButton_Found.setGeometry(QtCore.QRect(30, 20, 141, 24))
        self.pushButton_Found.setStyleSheet("background-color: rgb(76, 70, 64);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_Found.setObjectName("pushButton_Found")
        self.toolBox.addItem(self.page_8, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Show_All.setText(_translate("MainWindow", "Показать"))
        self.pushButton_Connect.setText(_translate("MainWindow", "Подключить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ИМЯ"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ТЕЛЕФОН"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "КОММЕНТАРИЙ"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.widget), _translate("MainWindow", "Показать номера"))
        self.label_3.setText(_translate("MainWindow", "                    Имя"))
        self.label_4.setText(_translate("MainWindow", "                Телефон"))
        self.label_5.setText(_translate("MainWindow", "            Комментарий"))
        self.pushButton_Added.setText(_translate("MainWindow", "Добавить"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Добавить номер"))
        self.label_6.setText(_translate("MainWindow", "                    Имя"))
        self.label_8.setText(_translate("MainWindow", "                Телефон"))
        self.label_11.setText(_translate("MainWindow", "                                                                           Новые данные"))
        self.label_12.setText(_translate("MainWindow", "                    Имя"))
        self.label_13.setText(_translate("MainWindow", "                Телефон"))
        self.label_14.setText(_translate("MainWindow", "            Комментарий"))
        self.pushButton_Update.setText(_translate("MainWindow", "Обновить"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Изменить номер"))
        self.label_15.setText(_translate("MainWindow", "                    Имя"))
        self.label_16.setText(_translate("MainWindow", "                Телефон"))
        self.pushButton_dell.setText(_translate("MainWindow", "Удалить"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_7), _translate("MainWindow", "Удалить номер"))
        self.pushButton_claer.setText(_translate("MainWindow", "Очистить"))
        self.label_17.setText(_translate("MainWindow", "                    Имя"))
        self.pushButton_Found.setText(_translate("MainWindow", "Найти"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_8), _translate("MainWindow", "Найти номера"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())