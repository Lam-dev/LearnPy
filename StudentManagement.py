import random
import os
class Student:
    def __init__(self, csvLine):
        self.name = None
        self.registerCode = None
        self.birthDay = None
        self.literatureScore = None
        self.mathScore = None
        self.englishScore = None
        self.__ParseTextLine(csvLine)

    def ScoreAverage(self):
        sum = self.literatureScore + self.mathScore + self.englishScore
        average = round(sum/3, 1)
        return average

    def __ParseTextLine(self, line):
        parts = line.split(',')
        self.registerCode = parts[0]
        self.name = parts[1]
        self.birthDay = parts[2]
        self.literatureScore = float(parts[3])
        self.mathScore = float(parts[4])
        self.englishScore = float(parts[5])

class UserInterface:
    def __init__(self, listStudents):
        self.__listStudents = listStudents

    def ShowMainMenu(self):
        print("1: Tìm kiếm học viên")
        print("2: Lọc")
        print("3: Thống kê")
        selected = int(input("Chọn: "))
        match selected:
            case 1:
                self.__FindStudent()

    def __FindStudent(self):
        os.system('cls||clear')
        studentName = input("Nhập tên học viên: ")
        for st in self.__listStudents:
            if(st.name.upper().__contains__(studentName.upper())):
                self.__ShowStudent(st)
        input("Nhấn enter để quay lại.")
        
    def ShowStudents(self, listStudent):
        for st in listStudent:
            self.__ShowStudent(st)

    def __ShowStudent(self, studentInfo):
        print(f'{studentInfo.registerCode}, {studentInfo.name}, {studentInfo.birthDay}, {studentInfo.mathScore}, {studentInfo.literatureScore}, {studentInfo.englishScore}')

    def FiltMenu(self):
        print("1: Các học viên có điểm ")
        print("2: Lọc")
        print("3: Thống kê")

def ReadListStudentFromFile():
    listStudentInfo = []
    with open("DiemThi.txt", 'rb') as f:
        while True:
            line = f.readline()
            if(line == b''):
                return listStudentInfo
            listStudentInfo.append(Student(line.decode('utf-8')))

listStudentInfo = ReadListStudentFromFile()
ui = UserInterface(listStudentInfo)
selected = ui.ShowMainMenu()
os.system('cls||clear')
ui.FiltMenu()
input("Press Enter to continue...")

            


