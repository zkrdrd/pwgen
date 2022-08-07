from PyQt5.QtWidgets import QLabel, QRadioButton, QDialog, QWidget, QLineEdit, QButtonGroup, QPushButton, QGridLayout, QApplication
import sys, secrets, string, pyperclip
class QLabelBuddy(QDialog, QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setFixedWidth(250)

        # lovercase
        lowercaseLabel = QLabel('Lowercase',self)
        self.lowercaseyes = QRadioButton("Yes")
        self.lowercaseyes.lovercase = "1"
        self.lowercaseno = QRadioButton("No")
        self.lowercaseno.lovercase = "0"
        self.lowercaseyes.setChecked(True)
        
        # uppercase
        self.uppercaseLabel = QLabel('Uppercase',self)
        self.uppercaseyes = QRadioButton("Yes")
        self.uppercaseyes.uppercase = "1"
        self.uppercaseno = QRadioButton("No")
        self.uppercaseno.uppercase = "0"
        self.uppercaseyes.setChecked(True)

        # digits
        self.digitsLabel = QLabel('Digits',self)
        self.digitsyes = QRadioButton("Yes")
        self.digitsyes.digits = "1"
        self.digitsno = QRadioButton("No")
        self.digitsno.digits = "0"
        self.digitsyes.setChecked(True)

        # punctuation
        self.punctuationLabel = QLabel('Punctuation',self)
        self.punctuationyes = QRadioButton("Yes")
        self.punctuationyes.punctuation = "1"
        self.punctuationno = QRadioButton("No")
        self.punctuationno.punctuation = "0"
        self.punctuationyes.setChecked(True)

        # Line edit length password
        self.countLabel = QLabel('Length',self)
        self.countLineEdit = QLineEdit(self)
        self.countLabel.setBuddy(self.countLineEdit)
        self.countLineEdit.setText("8")

        self.BtnGroupLowercase = QButtonGroup()
        self.BtnGroupLowercase.addButton(self.lowercaseyes)
        self.BtnGroupLowercase.addButton(self.lowercaseno)

        self.BtnGroupUppercase = QButtonGroup()
        self.BtnGroupUppercase.addButton(self.uppercaseyes)
        self.BtnGroupUppercase.addButton(self.uppercaseno)

        self.BtnGroupDigits = QButtonGroup()
        self.BtnGroupDigits.addButton(self.digitsyes)
        self.BtnGroupDigits.addButton(self.digitsno)

        self.BtnGroupPunctuation = QButtonGroup()
        self.BtnGroupPunctuation.addButton(self.punctuationyes)
        self.BtnGroupPunctuation.addButton(self.punctuationno)

        mainLayout = QGridLayout(self)
        self.lowercaseyes.setEnabled(True)

        # lowercase add to window
        mainLayout.addWidget(lowercaseLabel, 0, 1)
        mainLayout.addWidget(self.lowercaseyes, 0, 2)
        mainLayout.addWidget(self.lowercaseno, 0, 3)

        # lowercase add to window
        mainLayout.addWidget(self.uppercaseLabel, 1, 1)
        mainLayout.addWidget(self.uppercaseyes, 1, 2)
        mainLayout.addWidget(self.uppercaseno, 1, 3)

        # digits add to window
        mainLayout.addWidget(self.digitsLabel, 2, 1)
        mainLayout.addWidget(self.digitsyes, 2, 2)
        mainLayout.addWidget(self.digitsno, 2, 3)

        # digits add to window
        mainLayout.addWidget(self.punctuationLabel, 3, 1)
        mainLayout.addWidget(self.punctuationyes, 3, 2)
        mainLayout.addWidget(self.punctuationno, 3, 3)

        # line edit
        mainLayout.addWidget(self.countLabel,4,1)
        mainLayout.addWidget(self.countLineEdit,4,2,1,2)

        # generate Button
        self.generate = QPushButton('Generate', self)
        mainLayout.addWidget(self.generate, 5, 2)

        # pwd label
        self.pwd = QLabel("")
        mainLayout.addWidget(self.pwd, 6, 0, 1,0)

        # button copy
        self.copy = QPushButton('Copy', self)
        mainLayout.addWidget(self.copy, 7, 2)

        self.countLineEdit.textChanged.connect(self.textChanged)
        self.generate.clicked.connect(self.GeneratePwd)
        self.copy.clicked.connect(self.onClickCopy)

        #diactivate button
        self.copy.setEnabled(False)
        #self.generate.setEnabled(False)


    def textChanged(self, s):
        if s:
            self.generate.setEnabled(True)
        else:
            self.generate.setEnabled(False)

    def onClickCopy(self):
        pyperclip.copy(self.pwd.text())
        

    def GeneratePwd(self):
        all = ""
        count = int(self.countLineEdit.text())
        if self.lowercaseyes.isChecked() == True:
            all = all + string.ascii_lowercase
        else: all = all
        if self.uppercaseyes.isChecked() == True:
            all = all + string.ascii_uppercase
        else: all = all
        if self.digitsyes.isChecked() == True:
            all = all + string.digits
        else: all = all
        if self.punctuationyes.isChecked() == True:
            all = all + string.punctuation
        else: all = all
        if (all == ""):
            self.pwd.setText("Error: all parameters is empty")
        else:
            length = count
            password = "".join(secrets.choice(all) for i in range(length)) 
            self.pwd.setText(password)
            if len(self.pwd.text()) > 0:
                self.copy.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())
