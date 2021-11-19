import sys
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# import resources

BASEDIR = os.path.dirname(__file__)



class MainWindow(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # My code will go here
        self.initial_schedule = {
          'Monday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''},
          'Tuesday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''},
          'Wednesday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''},
          'Thursday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''},
          'Friday': {'07 AM - 08 AM': '', '08 AM - 09 AM': '', '09 AM - 10 AM': '', '10 AM - 11 AM': '', '11 AM - 12 PM': '', '12 PM - 01 PM': '', '01 PM - 02 PM': '', '02 PM - 03 PM': '', '03 PM - 04 PM': '', '04 PM - 05 PM': '', '05 PM - 06 PM': '', '06 PM - 07 PM': '', '07 PM - 08 PM': '', '08 PM - 09 PM': '', '09 PM - 10 PM': ''}
          }
        self.setWindowTitle("My Schedule")
        self.resize(700, 455)
        #create table
        self.tableWidget = qtw.QTableWidget()
        self.tableWidget.setGeometry(qtc.QRect(0, 0, 700, 455))
        # self.tableWidget.resize(1170, 885)
        sizePolicy = qtw.QSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setSizeAdjustPolicy(qtw.QAbstractScrollArea.AdjustToContents)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setMaximumSize(qtc.QSize(1111, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(12)
        
        # populate table
        self.populate_table()

        #add table to Main
        self.setCentralWidget(self.tableWidget)

        
        self.menubar = self.menuBar()
        self.menubar.setGeometry(qtc.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = self.statusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        qtc.QMetaObject.connectSlotsByName(self)

        # My code ends here
        self.show()
    
    def populate_table(self):
         for i, (day, hours) in enumerate(list(self.initial_schedule.items())):
            day_item = qtw.QTableWidgetItem(day)
            font = qtg.QFont()
            font.setPointSize(18)
            day_item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, day_item)

            if i == 0:
                for j, (hour, course) in enumerate(list(hours.items())):
                    hour_item = qtw.QTableWidgetItem(hour)
                    font = qtg.QFont()
                    font.setPointSize(14)
                    hour_item.setFont(font)
                    self.tableWidget.setVerticalHeaderItem(j, hour_item)
                    if j % 2 == 1:
                        hour_item.setBackground(qtg.QColor(114, 159, 207))
            if i % 2 == 0:
                day_item.setBackground(qtg.QColor(136, 138, 133))

    
    def add_course(self, course):
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        hours = ['07 AM - 08 AM', '08 AM - 09 AM', '09 AM - 10 AM', '10 AM - 11 AM', '11 AM - 12 PM', '12 PM - 01 PM',
                 '01 PM - 02 PM', '02 PM - 03 PM', '03 PM - 04 PM', '04 PM - 05 PM', '05 PM - 06 PM', '06 PM - 07 PM',
                  '07 PM - 08 PM', '08 PM - 09 PM', '09 PM - 10 PM']
        course_name = course['name']
        course_schedule = course['schedule']

        for day in course_schedule:
            day_key = list(day.keys())[0]
            day_index = days.index(day_key)
            for hour in day[day_key]:
                hour_index = hours.index(hour)
                self.tableWidget.setItem(hour_index, day_index, qtw.QTableWidgetItem(course_name))


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    math = {'name': 'Math-101', 'schedule': [{'Monday': ['09 AM - 10 AM', '10 AM - 11 AM']}, {'Wednesday': ['12 PM - 01 PM', '01 PM - 02 PM']}]}
    cs = {'name': 'CS-101', 'schedule': [{'Tuesday': ['10 AM - 11 AM', '11 AM - 12 PM']}, {'Thursday': ['11 AM - 12 PM', '12 PM - 01 PM']}]}
    eng = {'name': 'ENG-101', 'schedule': [{'Monday': ['02 PM - 03 PM', '03 PM - 04 PM']}, {'Friday': ['10 AM - 11 AM', '11 AM - 12 PM']}]}
    w.add_course(math)
    w.add_course(cs)
    w.add_course(eng)
    sys.exit(app.exec_())