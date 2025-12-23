import sys, os
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime, Qt
from PyQt5.QtGui import QFont, QColor

class WinForm(QWidget):
    def __init__(self, parent=None):
        print(os.getpid())
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('Time Tracker')
        
        # Initialize counters (starting from 0 instead of 60)
        self.countSecCountProgr = 0
        self.countSecCountPortug = 0
        self.countSecCountPhilo = 0
        
        # Create labels with initial time display
        self.labelProgramm = QLabel('Programming 0:00:00')
        self.labelProgramm.setStyleSheet("border: 2px solid black; padding: 5px; background-color: #f0f0f0;")
        self.labelProgramm.setFont(QFont('Times', 15))
        
        self.labelPortug = QLabel('Portugues 0:00:00')
        self.labelPortug.setStyleSheet("border: 2px solid blue; padding: 5px; background-color: #e0f7fa;")
        self.labelPortug.setFont(QFont('Times', 15))
        
        self.labelPhilo = QLabel('Philosophy 0:00:00')
        self.labelPhilo.setStyleSheet("border: 2px solid yellow; padding: 5px; background-color: #fffde7;")
        self.labelPhilo.setFont(QFont('Times', 15))
        
        # Create buttons
        self.startBtn = QPushButton('Start coding')
        self.endBtn = QPushButton('Stop coding')
        self.endBtn.setEnabled(False)
        
        self.startBtnPortug = QPushButton('Start portugues')
        self.endBtnPortug = QPushButton('Stop portugues')
        self.endBtnPortug.setEnabled(False)
        
        self.startBtnPhilo = QPushButton('Start philosophy')
        self.endBtnPhilo = QPushButton('Stop philosophy')
        self.endBtnPhilo.setEnabled(False)
        
        # NEW: Reset button
        self.resetBtn = QPushButton('Reset All Timers')
        self.resetBtn.setStyleSheet("background-color: #ff6b6b; color: white; font-weight: bold; padding: 10px; border-radius: 5px;")
        
        layout = QGridLayout()

        # Setup timers
        self.timerProgramm = QTimer()
        self.timerProgramm.timeout.connect(self.showTimeProgr)
        
        self.timerPortug = QTimer()
        self.timerPortug.timeout.connect(self.showTimePortug)
        
        self.timerPhilo = QTimer()
        self.timerPhilo.timeout.connect(self.showTimePhilo)

        # Add widgets to layout
        layout.addWidget(self.labelProgramm, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)
        
        layout.addWidget(self.labelPortug, 2, 0, 1, 2)
        layout.addWidget(self.startBtnPortug, 3, 0)
        layout.addWidget(self.endBtnPortug, 3, 1)
        
        layout.addWidget(self.labelPhilo, 4, 0, 1, 2)
        layout.addWidget(self.startBtnPhilo, 5, 0)
        layout.addWidget(self.endBtnPhilo, 5, 1)
        
        # NEW: Add reset button spanning two columns
        layout.addWidget(self.resetBtn, 6, 0, 1, 2)

        # Connect signals
        self.startBtn.clicked.connect(self.startTimerProgr)
        self.endBtn.clicked.connect(self.endTimerProgr)
        
        self.startBtnPortug.clicked.connect(self.startTimerPortug)
        self.endBtnPortug.clicked.connect(self.endTimerPortug)
        
        self.startBtnPhilo.clicked.connect(self.startTimerPhilo)
        self.endBtnPhilo.clicked.connect(self.endTimerPhilo)
        
        # NEW: Connect reset button
        self.resetBtn.clicked.connect(self.resetAllTimers)

        self.setLayout(layout)
    
    # Simplified time formatting function
    def format_time(self, total_seconds):
        """Convert total seconds to HH:MM:SS format"""
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    
    def showTimeProgr(self):
        self.countSecCountProgr += 1
        self.labelProgramm.setText(f'Programming {self.format_time(self.countSecCountProgr)}')
        
    def showTimePortug(self):
        self.countSecCountPortug += 1
        self.labelPortug.setText(f'Portugues {self.format_time(self.countSecCountPortug)}')

    def showTimePhilo(self):
        self.countSecCountPhilo += 1
        self.labelPhilo.setText(f'Philosophy {self.format_time(self.countSecCountPhilo)}')

    def startTimerProgr(self):
        self.timerProgramm.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)
        
    def startTimerPortug(self):
        self.timerPortug.start(1000)
        self.startBtnPortug.setEnabled(False)
        self.endBtnPortug.setEnabled(True)  
        
    def startTimerPhilo(self):
        self.timerPhilo.start(1000)
        self.startBtnPhilo.setEnabled(False)
        self.endBtnPhilo.setEnabled(True)   
     
    def endTimerProgr(self):
        self.timerProgramm.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)
        
    def endTimerPortug(self):
        self.timerPortug.stop()
        self.startBtnPortug.setEnabled(True)
        self.endBtnPortug.setEnabled(False)
        
    def endTimerPhilo(self):
        self.timerPhilo.stop()
        self.startBtnPhilo.setEnabled(True)
        self.endBtnPhilo.setEnabled(False)
    
    # NEW: Reset all timers function
    def resetAllTimers(self):
        """Reset all timers to zero and update displays"""
        # Stop all timers first
        self.timerProgramm.stop()
        self.timerPortug.stop()
        self.timerPhilo.stop()
        
        # Reset counters to zero
        self.countSecCountProgr = 0
        self.countSecCountPortug = 0
        self.countSecCountPhilo = 0
        
        # Update labels
        self.labelProgramm.setText('Programming 0:00:00')
        self.labelPortug.setText('Portugues 0:00:00')
        self.labelPhilo.setText('Philosophy 0:00:00')
        
        # Reset button states
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)
        
        self.startBtnPortug.setEnabled(True)
        self.endBtnPortug.setEnabled(False)
        
        self.startBtnPhilo.setEnabled(True)
        self.endBtnPhilo.setEnabled(False)
        
        print("All timers have been reset to zero.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.setWindowFlag(Qt.WindowStaysOnTopHint)
    form.show()
    sys.exit(app.exec_())