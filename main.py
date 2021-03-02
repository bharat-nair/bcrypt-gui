from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QTextEdit, QFormLayout
import bcrypt


def on_button_clicked(password, rounds, textbox):
    textbox.setText(
        (bcrypt.hashpw(password.encode(), bcrypt.gensalt(int(rounds)))).decode())


app = QApplication([])
window = QWidget()
outerLayout = QVBoxLayout()
topLayout = QFormLayout()
bottomLayout = QVBoxLayout()

password_field = QLineEdit('')
rounds_field = QLineEdit('10')
topLayout.addRow('Password: ', password_field)
topLayout.addRow('No. of Rounds: ', rounds_field)

button = QPushButton('Generate Hash')
bottomLayout.addWidget(button)
textbox = QTextEdit('Hash will appear here')
bottomLayout.addWidget(textbox)
outerLayout.addLayout(topLayout)
outerLayout.addLayout(bottomLayout)

button.clicked.connect(lambda: on_button_clicked(
    password_field.text(), rounds_field.text(), textbox))

window.setLayout(outerLayout)
window.setWindowTitle("BCrypt Hash Generator")
window.setFixedHeight(400)
window.setFixedWidth(500)
window.show()

app.exec()
