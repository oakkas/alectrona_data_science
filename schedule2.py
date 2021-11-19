import sys
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# import resources

BASEDIR = os.path.dirname(__file__)

class ScheduleTable(qtw.QTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.hours = ['07 AM - 08 AM', '08 AM - 09 AM', '09 AM - 10 AM', '10 AM - 11 AM', '11 AM - 12 PM',
                      '12 PM - 01 PM', '01 PM - 02 PM', '02 PM - 03 PM', '03 PM - 04 PM', '04 PM - 05 PM', '05PM - 06 PM', '06 PM - 07 PM', '07 PM - 08 PM', '08 PM - 09 PM', '09 PM - 10 PM']
        self.setWindowTitle("My Schedule")
        # create table
        self.setGeometry(qtc.QRect(0, 0, 700, 455))
        sizePolicy = qtw.QSizePolicy(
            qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setSizeAdjustPolicy(
            qtw.QAbstractScrollArea.AdjustToContents)

        self.resizeColumnsToContents()
        self.setMaximumSize(qtc.QSize(1111, 16777215))
        self.setObjectName("tableWidget")
        self.setColumnCount(5)
        self.setRowCount(12)

        # populate table
        self.populate_table()

    def populate_table(self):
        for i, day in enumerate(self.days):
            day_item = qtw.QTableWidgetItem(day)
            font = qtg.QFont()
            font.setPointSize(18)
            day_item.setFont(font)
            self.setHorizontalHeaderItem(i, day_item)
            if i % 2 == 0:
                day_item.setBackground(qtg.QColor(136, 138, 133))

        for j, hour in enumerate(self.hours):
            hour_item = qtw.QTableWidgetItem(hour)
            font = qtg.QFont()
            font.setPointSize(14)
            hour_item.setFont(font)
            self.setVerticalHeaderItem(j, hour_item)
            if j % 2 == 1:
                hour_item.setBackground(qtg.QColor(114, 159, 207))

    def add_course(self, course):

        course_name = course['name']
        course_schedule = course['schedule']

        for day in course_schedule:
            day_key = list(day.keys())[0]
            day_index = self.days.index(day_key)
            for hour in day[day_key]:
                hour_index = self.hours.index(hour)
                self.setItem(
                    hour_index, day_index, qtw.QTableWidgetItem(course_name))

class LoginForm(qtw.QWidget):

    #custom signals
    authenticated = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(qtw.QLineEdit.Password)

        self.cancel_button = qtw.QPushButton('Cancel')
        self.login_button = qtw.QPushButton('Login')

        layout = qtw.QFormLayout()
        layout.addRow('Username:', self.username_input)
        layout.addRow('Password:', self.password_input)

        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.login_button)
        layout.addRow('', button_widget)
        self.setLayout(layout)

        self.cancel_button.clicked.connect(self.close)
        self.login_button.clicked.connect(self.authenticate)

        self.username_input.textChanged.connect(self.set_button_text)
        # self.authenticated.connect(self.user_logged_in)
        # My code ends here
        self.show()
    
    def set_button_text(self, text):
        if text:
            self.login_button.setText(f'Log In {text}')
        else:
            self.login_button.setText('Log In')

    def authenticate(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == 'user' and password == 'pass':
            # qtw.QMessageBox.information(self, 'Sucess', 'You are logged in')
            self.authenticated.emit(username)
        else:
            qtw.QMessageBox.critical(self, 'Failed', 'Please enter corect credentials!')

class CourseDisplay(qtw.QWidget):

    submitted = qtc.pyqtSignal(str)

    def __init__(self, course, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course = course
        self.setLayout(qtw.QFormLayout())
        self.course_name = qtw.QLabel(f"Course Name: {course['name']}")
        self.course_instructor = qtw.QLabel(f"Course Instructor: {course['instructor']}")
        self.course_credits = qtw.QLabel(f"Course Credits: {course['credits']}")
        schedule_text = "\n"
        for day in course['schedule']:
            day_key = list(day.keys())[0]
            schedule_text += f"{day_key}: "
            for i, hour in enumerate(day[day_key]):
                if i == len(day[day_key]) - 1:
                    schedule_text += f"{hour}\n"
                else:
                    schedule_text += f"{hour}, "

                
        self.course_schedule = qtw.QLabel(f"Course Schedule: {schedule_text}")

        self.submit_button = qtw.QPushButton('Take COurse', clicked = self.on_submit)


        self.layout().addRow('', self.course_name)
        self.layout().addRow('', self.course_instructor)
        self.layout().addRow('', self.course_credits)
        self.layout().addRow('', self.course_schedule)
        self.layout().addRow('', self.submit_button)
    
    def on_submit(self):
        self.submitted.emit(self.course['name'])

class SearchWidget(qtw.QWidget):

    submitted = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLayout(qtw.QFormLayout())
        self.term_input = qtw.QLineEdit()
        # self.case_checkbox = qtw.QCheckBox('Case Sensitive')
        search_image = qtg.QPixmap(':/search.svg')
        self.submit_button = qtw.QPushButton('Search', clicked = self.on_submit, icon = qtg.QIcon(search_image))

        
        # self.layout().addRow(qtw.QLabel(pixmap = search_image))

        self.layout().addRow('Enter course name:', self.term_input)
        # self.layout().addRow('', self.case_checkbox)
        self.layout().addRow('', self.submit_button)
    
    def on_submit(self):
        term = self.term_input.text()
        # case_sensitive = (self.case_checkbox.checkState() == qtc.Qt.Checked)
        # self.submitted.emit(term, case_sensitive)
        self.submitted.emit(term)

    

class Schedule(qtw.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # My code will go here
        
        self.courses = []
        self.table_widget = ScheduleTable()
        
        self.login_widget = LoginForm()
        self.login_widget.authenticated.connect(self.user_logged_in)
        self.setCentralWidget(self.login_widget)

        self.menubar = self.menuBar()
        self.menubar.setGeometry(qtc.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        self.statusbar = self.statusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        qtc.QMetaObject.connectSlotsByName(self)

        # Dockwidget
        self.serach_dock = qtw.QDockWidget()
        self.search_widget = SearchWidget()
        self.serach_dock.setWidget(self.search_widget)

        self.search_widget.submitted.connect(self.search_course)
        self.current_course_widget = None
    
        self.show()
    
    def add_course(self, course):
        self.courses.append(course)
    
    def take_course(self, course_name):
        for course in self.courses:
            if course['name'] == course_name:
                self.table_widget.add_course(course)

    
    def user_logged_in(self, username):
        self.login_widget.close()
        self.setCentralWidget(self.table_widget)
        self.resize(1000, 455)

        self.addDockWidget(qtc.Qt.RightDockWidgetArea, self.serach_dock)

        self.show()
        
    def search_course(self, term): 
        for course in self.courses:
            if course['name'] == term:
                course_widget = CourseDisplay(course)
                course_widget.submitted.connect(self.take_course)
                if self.current_course_widget:
                    self.current_course_widget.close()
                self.current_course_widget = course_widget
                self.search_widget.layout().addRow(course_widget)
                
                # qtw.QMessageBox.information(self, 'Sucess', f'{course["name"]} found')
            else:
                self.statusBar().showMessage('No matches found', 3000)




if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = Schedule()
    math = {'name': 'Math-101', 'schedule': [{'Monday': ['09 AM - 10 AM', '10 AM - 11 AM']}, {'Wednesday': ['12 PM - 01 PM', '01 PM - 02 PM']}],
          "credits": 3, "instructor": "Jhon Snow", "exam_schedule": []}
    cs = {'name': 'CS-101', 'schedule': [{'Tuesday': ['10 AM - 11 AM', '11 AM - 12 PM']}, {'Thursday': ['11 AM - 12 PM', '12 PM - 01 PM']}],
        "credits": 3, "instructor": "Julia Hu", "exam_schedule": []}
    eng = {'name': 'ENG-101', 'schedule': [{'Monday': ['02 PM - 03 PM', '03 PM - 04 PM']}, {'Friday': ['10 AM - 11 AM', '11 AM - 12 PM']}],
         "credits": 3, "instructor": "Jhon Snow", "exam_schedule": []}

    w.add_course(math)
    w.add_course(cs)
    w.add_course(eng)
    sys.exit(app.exec_())
