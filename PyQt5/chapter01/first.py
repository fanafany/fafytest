# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-20 16:14 '

from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox


class Stats():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 310)
        self.window.setWindowTitle('统计')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入薪资")
        self.textEdit.move(25, 25)
        self.textEdit.resize(300, 350)

        self. button = QPushButton("统计", self.window)
        self.button.move(370, 50)
        self.button.clicked.connect(self.handle)

    def handle(self):
        info = self.textEdit.toPlainText()

        salarya_20 = ''
        salaryb_20 = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')
            parts = [p for p in parts if p]
            name,salary,age = parts
            if int(salary) >= 20000:
                salarya_20 += name +'\n'
            else:
                salaryb_20 += name +'\n'

        QMessageBox.about(self.window,
                          '统计结果',
                          f'''薪资20000以上的：\n{salarya_20}
                          \n薪资20000以下的：\n{salaryb_20}
                          ''')

app = QApplication([])
stats = Stats()
stats.window.show()
app.exec_()
