# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QMessageBox, QVBoxLayout, QComboBox, QLabel, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QGuiApplication
import sqlite3
import json


class Ui_Form(object):
    def setupUi(self, Form, mvid):

        Form.setObjectName("Покупка билетов в кино")
        Form.resize(604, 330)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 601, 331))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 271))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(f'{mvid[4]}'))
        self.label.setObjectName("label")
        self.text1 = QtWidgets.QLabel(self.widget)
        self.text1.setGeometry(QtCore.QRect(218, 13, 221, 21))
        self.text1.setMinimumSize(QtCore.QSize(5, 0))
        self.text1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.text1.setFont(font)
        self.text1.setMouseTracking(True)
        self.text1.setTabletTracking(False)
        self.text1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text1.setAutoFillBackground(False)
        self.text1.setTextFormat(QtCore.Qt.AutoText)
        self.text1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text1.setWordWrap(True)
        self.text1.setObjectName("text1")
        self.text1_2 = QtWidgets.QLabel(self.widget)
        self.text1_2.setGeometry(QtCore.QRect(218, 40, 341, 21))
        self.text1_2.setMinimumSize(QtCore.QSize(5, 0))
        self.text1_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text1_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.text1_2.setFont(font)
        self.text1_2.setMouseTracking(True)
        self.text1_2.setTabletTracking(False)
        self.text1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text1_2.setAutoFillBackground(False)
        self.text1_2.setTextFormat(QtCore.Qt.AutoText)
        self.text1_2.setWordWrap(True)
        self.text1_2.setObjectName("text1_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(220, 90, 161, 20))
        self.comboBox.setObjectName("comboBox")

        for i in range(int(max(json.loads(mvid[2]).keys())) + 1):
            self.comboBox.addItem("")

        self.text1_3 = QtWidgets.QLabel(self.widget)
        self.text1_3.setGeometry(QtCore.QRect(216, 70, 70, 21))
        self.text1_3.setMinimumSize(QtCore.QSize(5, 0))
        self.text1_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text1_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.text1_3.setFont(font)
        self.text1_3.setMouseTracking(True)
        self.text1_3.setTabletTracking(False)
        self.text1_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text1_3.setAutoFillBackground(False)
        self.text1_3.setTextFormat(QtCore.Qt.AutoText)
        self.text1_3.setWordWrap(True)
        self.text1_3.setObjectName("text1_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 140, 161, 20))
        self.comboBox_2.setObjectName("comboBox_2")

        for i in json.loads(mvid[2])["0"].keys():
            if json.loads(mvid[2])['0'][str(i)]:
                self.comboBox_2.addItem(i)

        self.comboBox.currentIndexChanged.connect(self.update_read_variable)
        self.text1_4 = QtWidgets.QLabel(self.widget)
        self.text1_4.setGeometry(QtCore.QRect(217, 120, 70, 21))
        self.text1_4.setMinimumSize(QtCore.QSize(5, 0))
        self.text1_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text1_4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.text1_4 = QtWidgets.QLabel(self.widget)
        self.text1_4.setGeometry(QtCore.QRect(217, 120, 81, 21))
        self.text1_4.setMinimumSize(QtCore.QSize(5, 0))
        self.text1_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text1_4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.text1_4.setFont(font)
        self.text1_4.setMouseTracking(True)
        self.text1_4.setTabletTracking(False)
        self.text1_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text1_4.setAutoFillBackground(False)
        self.text1_4.setTextFormat(QtCore.Qt.AutoText)
        self.text1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.text1_4.setWordWrap(True)
        self.text1_4.setObjectName("text1_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(220, 180, 341, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(lambda: self.on_buy_button_clicked(mvid))

        self.parent_form = Form

        self.retranslateUi(Form, mvid)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def on_buy_button_clicked(self, mvid):
        selected_row = self.comboBox.currentText()
        selected_seat = self.comboBox_2.currentText()

        success_dialog = SuccessDialog(mvid, selected_row, selected_seat, self.parent_form)
        success_dialog.exec_()

        self.parent_form.close()

    def retranslateUi(self, Form, mvid):

        conk = sqlite3.connect('films_db.sqlite')
        curk = conk.cursor()
        resk = curk.execute(f"SELECT * FROM films WHERE id = {int(mvid[0])}")

        datak = json.loads(resk.fetchone()[2])
        self.mvid = mvid

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", f'{mvid[1]}'))
        self.text1.setText(_translate("Form", f'{mvid[1]}'))
        self.text1_2.setText(_translate("Form", f'{mvid[3]}'))

        for i in datak.keys():
            self.comboBox.setItemText(int(i), _translate("Form", f'{int(i) + 1}'))

        self.text1_3.setText(_translate("Form", f"Выберите ряд:"))

        self.text1_4.setText(_translate("Form", "Выберите место:"))
        self.pushButton.setText(_translate("Form", "Купить"))

        curk.close()

    def update_read_variable(self, index):
        self.read = str(index)
        self.update_second_combobox()

    def update_second_combobox(self):
        datak = json.loads(self.mvid[2])

        for j in range(10):
            if datak[self.read][str(j)]:
                self.comboBox_2.setItemText(j, QGuiApplication.translate("Form", f"{j + 1}"))

        self.comboBox_2.clear()

        for j in range(10):
            if datak[self.read][str(j)]:
                self.comboBox_2.addItem(QGuiApplication.translate("Form", f"{j + 1}"))

    def on_form_closed(self):
        print("Ui_Form is closed")


class SuccessDialog(QDialog):
    def __init__(self, mvid, selected_row, selected_seat, parent=None):
        super(SuccessDialog, self).__init__(parent)
        self.mvid = mvid

        self.selected_row = selected_row
        self.selected_seat = selected_seat

        conkp = sqlite3.connect('films_db.sqlite')
        curkp = conkp.cursor()
        reskp = curkp.execute(f"SELECT * FROM films WHERE id = {self.mvid[0]}")

        json_data = json.loads(reskp.fetchone()[2])

        json_data[str(int(self.selected_row) - 1)][str(int(self.selected_seat) - 1)] = False
        reskp.close()

        conp = sqlite3.connect('films_db.sqlite')
        curp = conp.cursor()
        curp.execute("UPDATE films SET data = ? WHERE id = ?", (str(json_data).replace("'", "\"").lower(), self.mvid[0]))
        conp.commit()
        conp.close()

        self.setWindowTitle("Успешная покупка")
        self.setGeometry(100, 100, 300, 100)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

        self.purchase_ticket()

    def purchase_ticket(self):
        try:
            success_message = f"Билет на фильм {self.mvid[1]} успешно куплен!\nРяд: {self.selected_row}, Место: {self.selected_seat}\nСпасибо за покупку!"
            self.label.setText(success_message)
            print(self.mvid[2])
            print(f"Покупка билета для фильма {self.mvid[1]}")
            print(f"Выбранный ряд: {self.selected_row}, Выбранное место: {self.selected_seat}")
        except Exception as e:
            print(f"Error during ticket purchase: {e}")


class BuyDialog(QDialog):
    def __init__(self, mvid, parent=None):
        super(BuyDialog, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self, mvid)

    def closeEvent(self, event):
        self.ui.on_form_closed()
        event.accept()


class Ui_MovieUI(object):
    def setupUi(self, MovieUI):
        MovieUI.setObjectName("MovieUI")
        MovieUI.resize(435, 290)
        MovieUI.setMinimumSize(QtCore.QSize(435, 290))
        MovieUI.setMaximumSize(QtCore.QSize(435, 290))
        self.verticalLayout = QtWidgets.QVBoxLayout(MovieUI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(MovieUI)
        self.frame.setMinimumSize(QtCore.QSize(435, 290))
        self.frame.setMaximumSize(QtCore.QSize(435, 290))
        self.frame.setStyleSheet("margin-left: 10px;\n"
                                 "margin-top: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM films""").fetchall()

        for i in result:
            movie_frame = QtWidgets.QFrame(self.frame)
            movie_frame.setGeometry(QtCore.QRect(int(i[5]), 10, 120, 271))
            movie_frame.setStyleSheet("")
            movie_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            movie_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            movie_frame.setObjectName("movie_frame")

            img_label = QtWidgets.QLabel(movie_frame)
            img_label.setGeometry(QtCore.QRect(0, 0, 121, 171))
            img_label.setStyleSheet("border-radius: 10px;")
            img_label.setText("")
            img_label.setPixmap(QtGui.QPixmap(i[4]))
            img_label.setScaledContents(True)
            img_label.setObjectName("img_label")

            text_label = QtWidgets.QLabel(movie_frame)
            text_label.setGeometry(QtCore.QRect(10, 160, 111, 61))
            text_label.setMaximumSize(QtCore.QSize(100, 16777215))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            text_label.setFont(font)
            text_label.setMouseTracking(True)
            text_label.setTabletTracking(False)
            text_label.setLayoutDirection(QtCore.Qt.LeftToRight)
            text_label.setAutoFillBackground(False)
            text_label.setAlignment(QtCore.Qt.AlignCenter)
            text_label.setWordWrap(True)
            text_label.setObjectName("text_label")
            text_label.setText(i[1])

            buy_button = QtWidgets.QPushButton(movie_frame)
            buy_button.setGeometry(QtCore.QRect(0, 216, 111, 41))
            buy_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            buy_button.setStyleSheet("")
            buy_button.setCheckable(False)
            buy_button.setAutoRepeat(False)
            buy_button.setAutoExclusive(False)
            buy_button.setObjectName("buy_button")
            buy_button.setText("Купить билет")
            buy_button.clicked.connect(lambda _, mvid=i: self.show_buy_dialog(mvid))

            self.verticalLayout.addWidget(movie_frame)
        self.retranslateUi(MovieUI)
        QtCore.QMetaObject.connectSlotsByName(MovieUI)
        con.close()

    def retranslateUi(self, MovieUI):
        _translate = QtCore.QCoreApplication.translate
        MovieUI.setWindowTitle(_translate("MovieUI", "Покупка билетов в кино"))
    def show_buy_dialog(self, movie_id):
        buy_dialog = BuyDialog(movie_id)
        buy_dialog.exec_()

    def on_buy_ticket_clicked(self, movie_id):
        print(f"Покупка билета на фильм с ID: {movie_id}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MovieUI = QtWidgets.QMainWindow()
    ui = Ui_MovieUI()
    ui.setupUi(MovieUI)

    MovieUI.show()
    sys.exit(app.exec_())
