import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QTextEdit,QLineEdit,QCompleter
from PyQt5.QtGui import QStandardItem , QStandardItemModel,QFont
from PyQt5.Qt import Qt

from tries import AutoCompleteTrie


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.autocomplete = AutoCompleteTrie('*')

        self.resize(1200,800)
        fnt=QFont('Open Sans',22)

        mainLayout=QVBoxLayout()

        #input fields
        self.input=QLineEdit()
        self.input.setFixedHeight(50)
        self.input.setFont(fnt)
        self.input.textChanged.connect(self.printText)
        self.input.editingFinished.connect(self.addEntry)
        mainLayout.addWidget(self.input)
        self.suggestion=[]
        # self.model=QStandardItemModel()


        # completer=QCompleter(self.model,self)
        # completer=QCompleter(self.suggestion)
        self.input.setCompleter(QCompleter(self.suggestion))
        # self.input.setCompleter(completer)

        self.console=QTextEdit()
        self.console.setFont(fnt)
        mainLayout.addWidget(self.console)


        self.setLayout(mainLayout)

    def addEntry(self):
        entryItem=self.input.text()
        self.autocomplete.insert(entryItem)
        # print(self.autocomplete)
        self.input.clear()
        # self.input.setCompleter(QCompleter(["hi","bye"]))
        self.console.append(entryItem)
        # print(entryItem)
        # if not self.model.findItems(entryItem):
        #     self.model.appendRow(QStandardItem(entryItem))
    def printText(self):

        self.suggestion=self.autocomplete.nSuggestions(self.input.text(),9)

        print(self.suggestion)
        # print(self.autocomplete.nSuggestions("hi",3))
        # self.input.setCompleter(QCompleter(self.suggestion))




app=QApplication(sys.argv)
demo=AppDemo()
demo.show()
sys.exit(app.exec_())

