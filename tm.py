import sys, os
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime, Qt
from PyQt5.QtGui import QFont

class WinForm(QWidget):
    def __init__(self,parent=None):
        print(os.getpid())
        super(WinForm, self).__init__(parent)
        self.setWindowTitle('QTimer demonstration')
        
        self.labelProgramm=QLabel('Programming')
        self.labelProgramm.setStyleSheet("border : 2px solid black")
        self.labelProgramm.setFont(QFont('Times', 15))
        
        self.labelPortug=QLabel('Portugues')
        self.labelPortug.setStyleSheet("border : 2px solid blue")
        self.labelPortug.setFont(QFont('Times', 15))
        
        self.labelPhilo=QLabel('Philosophy')
        self.labelPhilo.setStyleSheet("border : 2px solid yellow")
        self.labelPhilo.setFont(QFont('Times', 15))
        
        self.startBtn=QPushButton('Start coding')
        self.endBtn=QPushButton('Stop coding')
        self.startBtnPortug=QPushButton('Start portugues')
        self.endBtnPortug=QPushButton('Stop portugues')
        self.startBtnPhilo=QPushButton('Start philosophy')
        self.endBtnPhilo=QPushButton('Stop philosophy')
        
        self.countSecCountProgr = 60
        self.countSecCountPortug = 60
        self.countSecCountPhilo = 60

        layout=QGridLayout()

        self.timerProgramm = QTimer()
        self.timerProgramm.timeout.connect(self.showTime)
        self.timerPortug = QTimer()
        self.timerPortug.timeout.connect(self.showTimePortug)
        self.timerPhilo = QTimer()
        self.timerPhilo.timeout.connect(self.showTimePhilo)

        layout.addWidget(self.labelProgramm,0,0,1,2)
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)
        layout.addWidget(self.labelPortug,2,0,1,2)
        layout.addWidget(self.startBtnPortug,3,0)
        layout.addWidget(self.endBtnPortug,3,1)
        layout.addWidget(self.labelPhilo,4,0,1,2)
        layout.addWidget(self.startBtnPhilo,5,0)
        layout.addWidget(self.endBtnPhilo,5,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.startBtnPortug.clicked.connect(self.startTimerPortug)
        self.endBtnPortug.clicked.connect(self.endTimerPortug)
        self.startBtnPhilo.clicked.connect(self.startTimerPhilo)
        self.endBtnPhilo.clicked.connect(self.endTimerPhilo)

        self.setLayout(layout)

    def showTime(self):
        self.countSecCountProgr += 1
        self.countSecProgr = self.countSecCountProgr % 60
        self.countMinCountProgr = (self.countSecCountProgr-60) // 60
        self.countMinProgr = self.countMinCountProgr % 60
        self.countHourProgr = (self.countSecCountProgr-60) // 3600     
        self.labelProgramm.setText('Coding '+str(self.countHourProgr)+":"+str(self.countMinProgr)+":"+str(self.countSecProgr))
        
    def showTimePortug(self):
        self.countSecCountPortug += 1
        self.countSecPortug = self.countSecCountPortug % 60
        self.countMinCountPortug = (self.countSecCountPortug-60) // 60
        self.countMinPortug = self.countMinCountPortug % 60
        self.countHourPortug = (self.countSecCountPortug-60) // 3600	 
        self.labelPortug.setText('Portugues '+str(self.countHourPortug)+":"+str(self.countMinPortug)+":"+str(self.countSecPortug))

    def showTimePhilo(self):
        self.countSecCountPhilo += 1
        self.countSecPhilo = self.countSecCountPhilo % 60
        self.countMinCountPhilo = (self.countSecCountPhilo-60) // 60
        self.countMinPhilo = self.countMinCountPhilo % 60
        self.countHourPhilo = (self.countSecCountPhilo-60) // 3600	 
        self.labelPhilo.setText('Philosophy '+str(self.countHourPhilo)+":"+str(self.countMinPhilo)+":"+str(self.countSecPhilo))

    def startTimer(self):
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
     
    def endTimer(self):
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

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.setWindowFlag(Qt.WindowStaysOnTopHint)
    form.show()
    sys.exit(app.exec_())
    
    
    