from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QComboBox, QGridLayout, QWidget
import sys


class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance: ")
        self.distance_input = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Metric (km)', 'Imperial (miles)'])

        time_label = QLabel("Time (hours)")
        self.time_input = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())
        speed = distance/time

        if self.combo.currentText() == 'Metric (km)':
            speed = round(speed, 2)
            self.output_label.setText(f"Average Speed: {speed} km/h")
        if self.combo.currentText() == 'Imperial (miles)':
            speed = round(speed * 0.621371, 2)
            self.output_label.setText(f"Average Speed: {speed} mph")


app = QApplication(sys.argv)
average_speed_calculator = AverageSpeedCalculator()
average_speed_calculator.show()
sys.exit(app.exec())


