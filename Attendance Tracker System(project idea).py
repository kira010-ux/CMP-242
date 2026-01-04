import csv
import datetime

class AttendanceTracker:
    def __init__(self):
        self.students = []
        self.attendance = {}  # date: {student: "P"/"A"}
        self.load_data()

    # STUDENT MANAGEMENT
    def add_student(self, name):
        if name not in self.students:
            self.students.append(name)
            print(f"✅ {name} added successfully.")
        else:
            print("⚠️ Student already exists!")

    # ATTENDANCE MARKING
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

    # VIEW REPORTS
    def view_report(self):
        if not self.attendance:
            print("⚠️ No attendance records yet.")
            return

        print("\n===== Attendance Report =====")
        for date, records in self.attendance.items():
            print(f"\n📅 Date: {date}")
            for name, status in records.items():
                print(f" - {name}: {status}")

    # VIEW ATTENDANCE PERCENTAGE
    def attendance_summary(self):
        if not self.attendance:
            print("⚠️ No attendance data available.")
            return

        total_days = len(self.attendance)
        print("\n===== Attendance Summary =====")
        for student in self.students:
            present_days = sum(
                1 for date in self.attendance if self.attendance[date].get(student) == "P"
            )
            percentage = (present_days / total_days) * 100
            print(f"{student}: {present_days}/{total_days} days present ({percentage:.1f}%)")

    # FILE HANDLING (SAVE/LOAD)
    def save_data(self):
        with open("attendance_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Student", "Status"])
            for date, records in self.attendance.items():
                for name, status in records.items():
                    writer.writerow([date, name, status])
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for s in self.students:
                writer.writerow([s])
        print("💾 Data saved successfully!")

    def load_data(self):
        try:
            with open("students.csv", "r") as file:
                reader = csv.reader(file)
                self.students = [row[0] for row in reader if row]
        except FileNotFoundError:
            self.students = []

        try:
            with open("attendance_data.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    date, name, status = row["Date"], row["Student"], row["Status"]
                    if date not in self.attendance:
                        self.attendance[date] = {}
                    self.attendance[date][name] = status
        except FileNotFoundError:
            self.attendance = {}
# MAIN MENU
def run(self):
        while True:
            print("\n===== Attendance Tracker Menu =====")
            print("1. Add Student")
            print("2. Mark Attendance")
            print("3. View Attendance Report")
            print("4. View Attendance Summary")
            print("5. Save & Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter student name: ").strip().title()
                self.add_student(name)
            elif choice == "2":
                self.mark_attendance()
            elif choice == "3":
                self.view_report()
            elif choice == "4":
                self.attendance_summary()
            elif choice == "5":
                self.save_data()
                print("👋 Exiting program. Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please select between 1–5.")
                
# Run the program
if __name__ == "__main__":
    system = AttendanceTracker()
    system.run()
