from PyQt5.QtWidgets import*

app = QApplication([])

window = QWidget()
window.resize(500, 500)

quest_lbl = QLabel(" якому році перший канал отримав золоту кнопку від ютуб?")

v_2005 = QRadioButton("2005")
v_2010 = QRadioButton("2010")

main_line = QVBoxLayout()
main_line.addWidget(quest_lbl)

horizontal_linia =  QHBoxLayout()
horizontal_linia.addWidget(v_2005)
horizontal_linia.addWidget(v_2010)
main_line.addLayout(horizontal_linia)

def show_win():
    win_msg = QMessageBox()
    win_msg.setText()
    win_msg.exec()

v_2005.clicked.connect(show_win)
window.setLayout(main_line)
window.show()
app.exec()