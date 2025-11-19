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
        today = str(datetime.date.today())
        self.attendance[today] = {}

        print(f"/n📅 mark attendance for {today}")
        for name in self.students:
            while True:
                status = input(f"{name} (P/A): ").upper()
                if status in ["P", "A"]:
                    self.attendance[today][name] = status
                    break
                else:
                    print("❌ Invalid input! Enter 'P' for Present or 'A' for Absent.")

        print("✅ Attendance marked successfully!")
