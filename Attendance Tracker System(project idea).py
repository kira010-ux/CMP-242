import csv
import datetime

class AttendanceTracker:
    def __init__(self):
        self.students = []
        self.attendance = {}  # date: {student: "P"/"A"}
        self.load_data()

    # ----------------------------
    # STUDENT MANAGEMENT
    # ----------------------------
    def add_student(self, name):
        if name not in self.students:
            self.students.append(name)
            print(f"✅ {name} added successfully.")
        else:
            print("⚠️ Student already exists!")

    # ----------------------------
    # ATTENDANCE MARKING
    # ----------------------------
    def mark_attendance(self):
        if not self.students:
            print("⚠️ No students registered yet!")
            return

