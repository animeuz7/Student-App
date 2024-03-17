from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QRadioButton, QFormLayout, QComboBox, QSpinBox
import sys

class MyWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Students App")
        
        self.setStyleSheet("Font-size: 25px")
        self.init_ui()
        
    def init_ui(self):
        self.ism_input = QLineEdit(self)
        self.Sharif_input = QLineEdit(self)
        self.yoshi_spinbox = QSpinBox(self)
        self.yoshi_spinbox.setMinimum(17)
        self.yoshi_spinbox.setMaximum(35) 
          
        self.Jins_radio_erkak = QRadioButton("Erkak", self)
        self.Jins_radio_Ayol = QRadioButton("Ayol", self)
        
        
        
        self.country_combobox = QComboBox(self)
        self.country_combobox.addItem("Samarqand")
        self.country_combobox.addItem("Toshkent")
        self.country_combobox.addItem("Andijon")
        self.country_combobox.addItem("Buxoro")
        self.country_combobox.addItem("Farg'ona")
        self.country_combobox.addItem("Jizzax")
        self.country_combobox.addItem("Namangan")
        self.country_combobox.addItem("Navoiy")
        self.country_combobox.addItem("Qashqadaryo")
        self.country_combobox.addItem("Qoraqalpog'iston")
        self.country_combobox.addItem("Sirdaryo")
        self.country_combobox.addItem("Surxondaryo")
        self.country_combobox.addItem("Xorazm")
        
        self.Telefon_input = QLineEdit(self)
        self.Fakultet1_input = QLineEdit(self)
        self.kurs_input = QComboBox()
        self.kurs_input.addItem("1")
        self.kurs_input.addItem("2")
        self.kurs_input.addItem("3")
        self.kurs_input.addItem("4")


    
        
        self.save_btn = QPushButton("Ma'lumotlarni Faylga Yozish", self)
        self.save_btn.clicked.connect(self.save_data)
        
        layout = QFormLayout()
        layout.addRow("Ism", self.ism_input)
        layout.addRow("Sharif", self.Sharif_input)
        layout.addRow("Yosh", self.yoshi_spinbox)
        layout.addRow("Jins", self.Jins_radio_erkak)
        layout.addRow("", self.Jins_radio_Ayol)
        layout.addRow("Manzili", self.country_combobox)
        layout.addRow("Telefon", self.Telefon_input)
        layout.addRow("Fakultet", self.Fakultet1_input)
        layout.addRow("Kurs",self.kurs_input)
        layout.addRow("", self.save_btn)
        
        self.setLayout(layout)
        
    def save_data(self):
       Ism = self.ism_input.text()
       Sharif = self.Sharif_input.text()
       Jins = "Erkak" if self.Jins_radio_erkak.isChecked() else "Ayol"
       Yosh = self.yoshi_spinbox.value()
       Mamlakat = self.country_combobox.currentText()
       Telefon_raqami = self.Telefon_input.text()
       Fakultet1 = self.Fakultet1_input.text()
       kurs = self.kurs_input.currentText()
       
       
       fayl_nomi = "Ma'lumotlar.txt"
       with open(fayl_nomi, "w") as fayl:
           fayl.write(f"Ism: {Ism}\n")
           fayl.write(f"Sharif: {Sharif}\n")
           fayl.write(f"Yosh: {Yosh}\n")
           fayl.write(f"Jins: {Jins}\n")
           fayl.write(f"Mamlakat: {Mamlakat}\n")
           fayl.write(f"Telefon raqami: {Telefon_raqami}\n")
           fayl.write(f"Fakultet: {Fakultet1}\n")
           fayl.write(f"Kurs: {kurs}\n ")

       

app = QApplication(sys.argv)
oyna = MyWindow()
oyna.show()
sys.exit(app.exec_())
