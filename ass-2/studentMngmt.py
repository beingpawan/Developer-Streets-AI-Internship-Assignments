class StudentManagementSystem:
    def __init__(self):
        self.students={}
    def add_student(self,student_id,first_name,last_name,subject_list,grades_list):
        if student_id in self.students:
            print(f"student ID {student_id} already exist !!")
            return
        
        name_tuple=(first_name,last_name)

        subjects_set=set(subject_list)
        
        grades = list(grades_list)

        self.students[student_id]= {
            "name" :  name_tuple ,
            "subjects": subjects_set ,
            "grades": grades  
         }

        print(f"Added student: {first_name}{last_name}")

    def calculate_average(self,grades):
        if not grades:
                return 0
        return sum(grades)/len(grades)
    def display_all_students(self):
        print("\n---Student Recordd---")
        for student_id, info in self.students.items():
                name=f"{info['name'][0]} {info['name'][1]}"
                subjects = ", ".join(info['subjects'])
                avg_grade = self.calculate_average(info['grades'])
                print(f"ID: {student_id} | name:{name} | subjects: {subjects} | Avg Grade: {avg_grade:.2f}")

    def get_honor_roll(self, min_average):
        honor_roll = [
                f"{info['name'][0]} {info['name'][1]}"
                for student_id, info in self.students.items()
                if self.calculate_average(info['grades'])>= min_average
            ]
        return honor_roll
        
    def get_all_unique_subjects_offered(self):
        all_subjects=set()
        for info in self.students.values():
                all_subjects=all_subjects.union(info['subjects'])
        return all_subjects
        

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.add_student(101,"Alice","Smith",["Math","Physics","Math"], [88,92,95])
    sms.add_student(102,"Bob","Jones",["English","History"], [75,80,78])
    sms.add_student(103, "Charlie","Brown",["Math","Computer Science"], [95,98,99])

    sms.display_all_students()

    print("\n--Honor Roll (Avg>=90)--")
    top_students = sms.get_honor_roll(90.0)
    print(top_students)

    print("\n--- All Unique Subjects taken bhy students ---")
    unique_subjects=sms.get_all_unique_subjects_offered()
    print(unique_subjects)