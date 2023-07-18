from cryptography.fernet import Fernet
import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QFileDialog, QHBoxLayout
from PyQt5 import QtCore

class FileEncryptor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Encryptor")
        self.setGeometry(200, 200, 400, 250)

        self.key = None  # Anahtar

        self.init_ui()

    def init_ui(self):
        self.file_label = QLabel("Emir Byk |  Klasik Bilişim", self)
        self.additional_label = QLabel("ÖNEMLİ", self)
        self.additional_label.setStyleSheet("color: red;")  # Kırmızı renk
        self.another_label = QLabel("|Şifrelenen Bir Dosya Ancak Aynı Anahtar Kullanılarak Çözülebilir|", self)
        self.one_more_label = QLabel("Anahtarınızı Kaydedin, Kaybederseniz Dosyanızı Çözülemez", self)
        self.file_edit = QLineEdit(self)
        self.file_select_button = QPushButton("Dosya Seç", self)
        self.encrypt_button = QPushButton("Şifrele", self)
        self.decrypt_button = QPushButton("Çöz", self)
        self.generate_key_button = QPushButton("Anahtar Oluştur", self)
        self.key_edit = QLineEdit(self)
        self.key_edit.setPlaceholderText("Anahtarınızı buraya girin veya anahtar oluşturun")

        self.file_select_button.clicked.connect(self.select_files)
        self.encrypt_button.clicked.connect(self.encrypt_files)
        self.decrypt_button.clicked.connect(self.decrypt_files)
        self.generate_key_button.clicked.connect(self.generate_key)

        layout = QVBoxLayout()
        
        # Dosya seçimi düzeni
        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_select_button)
        file_layout.addWidget(self.file_edit)
        file_layout.addStretch()
        layout.addLayout(file_layout)

        layout.addWidget(self.file_label, alignment=QtCore.Qt.AlignHCenter)
        layout.addWidget(self.additional_label, alignment=QtCore.Qt.AlignHCenter)
        layout.addWidget(self.another_label, alignment=QtCore.Qt.AlignHCenter)
        layout.addWidget(self.one_more_label, alignment=QtCore.Qt.AlignHCenter)
        
        # Anahtar oluşturma düzeni
        key_layout = QHBoxLayout()
        key_layout.addWidget(self.generate_key_button)
        key_layout.addWidget(self.key_edit)
        key_layout.addStretch()
        layout.addLayout(key_layout)

        # Butonların düzeni
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)
        
        self.encrypt_button.setFixedSize(250, 40)
        self.decrypt_button.setFixedSize(250, 40)
        self.file_select_button.setFixedSize(250, 40)
        self.generate_key_button.setFixedSize(250, 40)

        self.setLayout(layout)

        self.encrypt_button.setStyleSheet("background-color: green; color: white; border-radius: 5px;")
        self.decrypt_button.setStyleSheet("background-color: red; color: white; border-radius: 5px;")
        self.file_select_button.setStyleSheet("background-color: blue; color: white; border-radius: 5px;")
        self.generate_key_button.setStyleSheet("background-color: orange; color: white; border-radius: 5px;")
        self.setStyleSheet("background-color: #eeefed;")

    def select_files(self):
        file_dialog = QFileDialog()
        filenames, _ = file_dialog.getOpenFileNames(self, "Dosyaları Seç", "", "Tüm Dosyalar (*.*)")
        if filenames:
            self.file_edit.setText(", ".join(filenames))

    def encrypt_files(self):
        filenames = self.file_edit.text().split(", ")
        if filenames:
            if self.key or self.key_edit.text():
                self.key = self.key_edit.text() or self.key
                fernet = Fernet(self.key.encode())
                for filename in filenames:
                    try:
                        with open(filename, "rb") as file:
                            data = file.read()
                            encrypted_data = fernet.encrypt(data)
                        with open(filename, "wb") as file:
                            file.write(encrypted_data)
                    except FileNotFoundError:
                        QMessageBox.warning(self, "Hata", "Dosya bulunamadı: " + filename)
                    except Exception as e:
                        QMessageBox.warning(self, "Hata", "Dosya şifrelenirken bir hata oluştu:\n" + str(e))
                QMessageBox.information(self, "Şifreleme Başarılı", "Dosyalar başarıyla şifrelendi.")
            else:
                QMessageBox.warning(self, "Hata", "Lütfen bir anahtar belirleyin veya anahtar girin.")
        else:
            QMessageBox.warning(self, "Hata", "Dosya adlarını girin.")

    def decrypt_files(self):
        filenames = self.file_edit.text().split(", ")
        if filenames:
            if self.key or self.key_edit.text():
                self.key = self.key_edit.text() or self.key
                fernet = Fernet(self.key.encode())
                for filename in filenames:
                    try:
                        with open(filename, "rb") as file:
                            encrypted_data = file.read()
                            decrypted_data = fernet.decrypt(encrypted_data)
                        with open(filename, "wb") as file:
                            file.write(decrypted_data)
                    except FileNotFoundError:
                        QMessageBox.warning(self, "Hata", "Dosya bulunamadı: " + filename)
                    except Exception as e:
                        QMessageBox.warning(self, "Hata", "Dosya çözülürken bir hata oluştu:\n" + str(e))
                QMessageBox.information(self, "Çözme Başarılı", "Dosyalar başarıyla çözüldü.")
            else:
                QMessageBox.warning(self, "Hata", "Lütfen bir anahtar belirleyin veya anahtar girin.")
        else:
            QMessageBox.warning(self, "Hata", "Dosya adlarını girin.")

    def generate_key(self):
        self.key = Fernet.generate_key().decode()
        self.key_edit.setText(self.key)
        self.generate_key_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_encryptor = FileEncryptor()
    file_encryptor.show()
    sys.exit(app.exec_())
