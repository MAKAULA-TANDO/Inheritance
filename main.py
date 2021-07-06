from tkinter import *

screen = Tk()
screen.geometry("400x400")
screen.title("Phd App")


class Person:

    def __init__(self, name, surname, id_no, dob):
        self.name = name
        self.surname = surname
        self.identity = id_no
        self.dob = dob

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_surname(self, surname):
        self.surname = surname

    def get_surname(self):
        return self.surname

    def set_identity(self, id_no):
        self.identity = id_no

    def get_identity(self):
        return self.identity

    def set_dob(self, dob):
        self.dob = dob

    def get_dob(self):
        return self.dob

    def __str__(self):
        string = ""
        string = string + "Your Name Is: " + self.name
        string = string + "\n" + "Your Surname Is: " + self.surname
        string = string + "\n" + "Your ID NO. Is: " + self.identity
        string = string + "\n" + "Your Date Of Birth Is: " + self.dob
        return string


class Student(Person):

    def __init__(self, name, surname, id_no, dob, student_no, int_mark, ext_mark):
        super().__init__(name, surname, id_no, dob)
        self.student_no = student_no
        self.int_mark = int_mark
        self.ext_mark = ext_mark

    # super().__init__(self, name, surname, id)

    def set_student_no(self, student_no):
        self.student_no = student_no

    def get_student_no(self):
        return self.student_no

    def set_int_mark(self, int_mark):
        self.int_mark = int_mark

    def get_int_mark(self):
        return self.int_mark

    def set_ext_mark(self, ext_mark):
        self.ext_mark = ext_mark

    def get_ext_mark(self):
        return self.ext_mark

    def output(self):
        print("PERSON DETAILS ")
        print(super().__str__())
        print("Your PhD Student details: ")
        print("\n" + "Your Student Number Is: " + self.student_no + "\n" + "Your External Mark Is: ", self.ext_mark)
        print("\n" + "Your Internal Mark Is: ", self.int_mark, "\n" + "Your Average Mark Is: ", ((self.ext_mark + self.int_mark)/2))

    def put(self):
        Label(screen, text=("\n" + "Your Student Number Is: ", self.student_no, "\n", "Your External Mark Is: ", self.ext_mark, "\n", "Your Internal Mark Is: ", self.int_mark, "\n", "Your Average Mark Is: ", ((self.ext_mark + self.int_mark)/2)), font=('Calibri', 12)).grid(row=6, column=2, sticky=W)


class Examiner(Person):
    def __init__(self, name, surname, id_no, dob, staff_no, no_hours, hourly_rate):
        super().__init__(name, surname, id_no, dob)
        self.ext_mark = None
        self.student_no = None
        self.int_mark = None
        self.staff_no = staff_no
        self.no_hours = no_hours
        self.hourly_rate = hourly_rate
        # super().__init__(self, name, surname, id_no)

    def get_staff_no(self):
        return self.staff_no

    def get_hourly_rate(self):
        return self.hourly_rate

    def get_no_hours(self):
        return self.no_hours

    def tot(self):
        return self.no_hours * self.hourly_rate

    def output(self):
        print("\n")
        print("\n")
        print("Your PhD Examiner details: ")
        print("\n")
        print("Your Staff Number Is: " + self.staff_no)
        print("Your Hourly Rate Is: ", self.hourly_rate)
        print("Your Number Of Hours Is: ", self.no_hours)
        print("Your Salary Is: ", self.tot())

    def put(self):
        Label(screen, text=("\n" + "Your Staff Number Is: " + self.staff_no + "\n" + "Your Hourly Rate Is: ", self.hourly_rate, "\n" + "Your Number Of Hours Is: ", self.no_hours, "\n" + "Your Salary Is: ", self.tot()), font=('Calibri', 12)).grid(row=9, column=12, sticky=W)


temp_name = Entry(bd=3)
temp_surname = Entry()
temp_id_no = Entry()
temp_dob = Entry()
temp_student_no = Entry()
temp_int_mark = Entry()
temp_ext_mark = Entry()


def student():

    Label(screen, text="Enter student NO", font=('Calibri', 12)).grid(row=6, column=6, sticky=W)
    Label(screen, text="Enter internal mark", font=('Calibri', 12)).grid(row=7, column=6, sticky=W)
    Label(screen, text="Enter external mark", font=('Calibri', 12)).grid(row=8, column=6, sticky=W)
    Entry(screen, textvariable=temp_student_no).grid(row=6, column=7)
    Entry(screen, textvariable=temp_int_mark).grid(row=7, column=7)
    Entry(screen, textvariable=temp_ext_mark).grid(row=8, column=7)


Label(screen, text="name", font=('Calibri', 12)).grid(row=1, sticky=W)
Label(screen, text="Enter Surname", font=('Calibri', 12)).grid(row=2, sticky=W)
Label(screen, text="Enter ID NO", font=('Calibri', 12)).grid(row=3, sticky=W)
Label(screen, text="Enter D.O.B", font=('Calibri', 12)).grid(row=4, sticky=W)
Entry(screen, textvariable=temp_name).grid(row=1, column=1)
Entry(screen, textvariable=temp_surname).grid(row=2, column=1)
Entry(screen, textvariable=temp_id_no).grid(row=3, column=1)
Entry(screen, textvariable=temp_dob).grid(row=4, column=1)
tname = str(temp_name.get())
tsurname = str(temp_surname.get())
tid_no = str(temp_id_no.get())
tdob = str(temp_dob.get())
tstudent_no = str(temp_student_no.get())
tint_mark = int(temp_int_mark.get())
text_mark = int(temp_ext_mark.get())
r1 = Student(tname, tsurname, tid_no, tdob, tstudent_no, tint_mark, text_mark)
r = Examiner("AMkle", "jampethu", "2717273", "2021-21-09", "263736", 2, 45)
v0 = IntVar()
v0.set(1)
Radiobutton(screen, text="Phd Student", variable=v0, value=1, command=student, font=('Calibri', 12)).grid(row=1, column=6, sticky=N, pady=10)
Radiobutton(screen, text="Examiner", value=2, command=r.put(), font=('Calibri', 12)).grid(row=1, column=10, sticky=N, pady=10)
Button(screen, text="ok", command=r1.put(), font=('Calibri', 18)).grid(row=14, column=6, sticky=N, pady=10)
r1.put()
screen.mainloop()
