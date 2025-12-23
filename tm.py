import sys, os
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel, QInputDialog
from PyQt5.QtCore import QTimer,QDateTime, Qt
from PyQt5.QtGui import QFont, QColor
from functools import partial

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
        
        # NEW: Add Task button (to create custom timers)
        self.addTaskBtn = QPushButton('Add Task')
        self.addTaskBtn.setStyleSheet("background-color: #1976D2; color: white; padding: 8px; border-radius: 5px;")
        
        layout = QGridLayout()

        # Setup timers
        self.timerProgramm = QTimer()
        self.timerProgramm.timeout.connect(self.showTimeProgr)
        
        self.timerPortug = QTimer()
        self.timerPortug.timeout.connect(self.showTimePortug)
        
        self.timerPhilo = QTimer()
        self.timerPhilo.timeout.connect(self.showTimePhilo)

        # Add widgets to layout (existing default blocks)
        layout.addWidget(self.labelProgramm, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)
        
        layout.addWidget(self.labelPortug, 2, 0, 1, 2)
        layout.addWidget(self.startBtnPortug, 3, 0)
        layout.addWidget(self.endBtnPortug, 3, 1)
        
        layout.addWidget(self.labelPhilo, 4, 0, 1, 2)
        layout.addWidget(self.startBtnPhilo, 5, 0)
        layout.addWidget(self.endBtnPhilo, 5, 1)
        
        # NEW: Add "Add Task" button and place Reset below it
        layout.addWidget(self.addTaskBtn, 6, 0)
        layout.addWidget(self.resetBtn, 6, 1)

        # Connect signals
        self.startBtn.clicked.connect(self.startTimerProgr)
        self.endBtn.clicked.connect(self.endTimerProgr)
        
        self.startBtnPortug.clicked.connect(self.startTimerPortug)
        self.endBtnPortug.clicked.connect(self.endTimerPortug)
        
        self.startBtnPhilo.clicked.connect(self.startTimerPhilo)
        self.endBtnPhilo.clicked.connect(self.endTimerPhilo)
        
        # NEW: Connect addTask button
        self.addTaskBtn.clicked.connect(self.addTask)
        # NEW: Connect reset button
        self.resetBtn.clicked.connect(self.resetAllTimers)

        # Keep references for dynamic tasks
        self.dynamic_tasks = []  # list of dicts: {'name','label','start','stop','timer','counter'}
        # Next available row to insert a new task (rows 0..6 used by defaults + buttons)
        self.next_dynamic_row = 7

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
    
    # NEW helper to update a dynamic task's label (bound to its timer)
    def _update_dynamic_label(self, task):
        task['counter'] += 1
        task['label'].setText(f"{task['name']} {self.format_time(task['counter'])}")

    # NEW: Add task dialog and widget creation
    def addTask(self):
        name, ok = QInputDialog.getText(self, "Add Task", "Task name:")
        if not ok:
            return
        name = name.strip()
        if not name:
            return

        # Create widgets for the new task
        label = QLabel(f"{name} 0:00:00")
        label.setStyleSheet("border: 2px solid #9e9e9e; padding: 5px; background-color: #f9f9f9;")
        label.setFont(QFont('Times', 14))

        startBtn = QPushButton(f"Start {name}")
        stopBtn = QPushButton(f"Stop {name}")
        stopBtn.setEnabled(False)

        timer = QTimer()
        task = {'name': name, 'label': label, 'start': startBtn, 'stop': stopBtn, 'timer': timer, 'counter': 0}

        # Connect timer to update function (capture task dict)
        timer.timeout.connect(partial(self._update_dynamic_label, task))

        # Connect start/stop buttons
        startBtn.clicked.connect(partial(self._start_dynamic_task, task))
        stopBtn.clicked.connect(partial(self._stop_dynamic_task, task))

        # Insert widgets into layout
        # place label in full-width row, buttons on next row
        self.layout().addWidget(label, self.next_dynamic_row, 0, 1, 2)
        self.layout().addWidget(startBtn, self.next_dynamic_row + 1, 0)
        self.layout().addWidget(stopBtn, self.next_dynamic_row + 1, 1)

        self.next_dynamic_row += 2

        # Move Reset and AddTask buttons to always sit after dynamic tasks
        # remove existing and re-add in new position
        try:
            self.layout().removeWidget(self.addTaskBtn)
            self.layout().removeWidget(self.resetBtn)
        except Exception:
            pass
        self.layout().addWidget(self.addTaskBtn, self.next_dynamic_row, 0)
        self.layout().addWidget(self.resetBtn, self.next_dynamic_row, 1)
        self.next_dynamic_row += 1  # keep the row for further tasks

        # store task
        self.dynamic_tasks.append(task)

    # NEW: start/stop for dynamic tasks
    def _start_dynamic_task(self, task):
        task['timer'].start(1000)
        task['start'].setEnabled(False)
        task['stop'].setEnabled(True)

    def _stop_dynamic_task(self, task):
        task['timer'].stop()
        task['start'].setEnabled(True)
        task['stop'].setEnabled(False)

    # Update resetAllTimers to include dynamic tasks
    def resetAllTimers(self):
        """Reset all timers to zero and update displays"""
        # Stop default timers first
        try:
            self.timerProgramm.stop()
            self.timerPortug.stop()
            self.timerPhilo.stop()
        except Exception:
            pass
        
        # Reset default counters to zero
        self.countSecCountProgr = 0
        self.countSecCountPortug = 0
        self.countSecCountPhilo = 0
        
        # Update default labels
        self.labelProgramm.setText('Programming 0:00:00')
        self.labelPortug.setText('Portugues 0:00:00')
        self.labelPhilo.setText('Philosophy 0:00:00')
        
        # Reset default button states
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)
        
        self.startBtnPortug.setEnabled(True)
        self.endBtnPortug.setEnabled(False)
        
        self.startBtnPhilo.setEnabled(True)
        self.endBtnPhilo.setEnabled(False)
        
        # NEW: stop and reset all dynamic tasks
        for task in self.dynamic_tasks:
            try:
                task['timer'].stop()
            except Exception:
                pass
            task['counter'] = 0
            task['label'].setText(f"{task['name']} 0:00:00")
            task['start'].setEnabled(True)
            task['stop'].setEnabled(False)
        
        print("All timers have been reset to zero.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.setWindowFlag(Qt.WindowStaysOnTopHint)
    form.show()
    sys.exit(app.exec_())