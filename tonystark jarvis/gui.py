import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class JarvisGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("J.A.R.V.I.S")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #1c1e26; color: #ffffff;")

        # Title Label
        title_label = QtWidgets.QLabel("Welcome to J.A.R.V.I.S", self)
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        title_label.setFont(QtGui.QFont("Roboto", 28, QtGui.QFont.Bold))
        title_label.setGeometry(0, 50, 800, 50)

        # Command Input
        self.command_input = QtWidgets.QLineEdit(self)
        self.command_input.setPlaceholderText("Enter your command...")
        self.command_input.setGeometry(150, 150, 500, 40)
        self.command_input.setStyleSheet("""
            padding: 10px; 
            border: 2px solid #61afef; 
            border-radius: 10px; 
            background-color: #2b2d36;
            color: #ffffff;
        """)

        # Speak Button
        speak_button = QtWidgets.QPushButton("Speak", self)
        speak_button.setGeometry(320, 220, 160, 50)
        speak_button.setStyleSheet("""
            background-color: #61afef; 
            font-size: 18px; 
            border-radius: 10px;
            color: white;
            font-weight: bold;
        """)
        speak_button.clicked.connect(self.speak_command)

        # Output Display
        self.output_display = QtWidgets.QTextBrowser(self)
        self.output_display.setGeometry(50, 300, 700, 250)
        self.output_display.setStyleSheet("""
            background-color: #2b2d36; 
            color: #ffffff; 
            border-radius: 10px; 
            padding: 10px;
        """)

        self.show()

    def speak_command(self):
        command = self.command_input.text()
        self.output_display.append(f"Command: {command}")
        # Here you would add the code to process the command with Jarvis
        self.command_input.clear()  # Clear the input field

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # Use Fusion style for a modern look
    window = JarvisGUI()
    sys.exit(app.exec_())
