import json
import os
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self,unique_id,name,marks):
        id_exist = 0
        for i in self.students:
            if i['id'] == unique_id:
                id_exist +=1 
        if id_exist == 0:
            if isinstance(unique_id,int) and not isinstance(unique_id,bool):
                self.unique_id = unique_id
                if isinstance(name,str) and name.strip() != "":
                    self.name = name 
                    if isinstance(marks,int) and not isinstance(marks,bool):
                        if 0 <= marks <= 100:
                            self.marks = marks
                            self.students.append({
                                "id": self.unique_id,
                                "name": self.name,
                                "marks": self.marks
                            })
                            print("Student added successfully")
                        else:
                            print("Marks must be between 0 and 100")
                    else:
                        print("Marks must integer")
                else:
                    print("Name must be non-empty string")
            else:
                print("Id must be integer")
        else:
            print("Student ID already exists")

    def view_all_student(self):
        if self.students != []:
            for i in self.students:
                print(i)
        else:
            print("No students found")

    def search_student(self,id):
        found = 0
        if self.students != []:
            for i in self.students:
                if i['id'] == id:
                    found += 1
                    print(i)
            if found == 0:
                print("No student found with this ID")
        else:
            print("Data is empty")
        
    def update_student(self,unique_id,name,marks):
        found = 0
        if self.students != []:
            for i in self.students:
                if i['id'] == unique_id:
                    found += 1
                    if isinstance(name,str) and name.strip() != "":
                        self.name = name
                        if isinstance(marks,int) and not isinstance(marks,bool):
                            if 0 <= marks <= 100:
                                self.marks = marks
                                i['name'] = self.name 
                                i['marks'] = self.marks
                                print("Student updated successfully")
                            else:
                                print("Marks must be between 0 and 100") 
                        else:
                            print("Marks must be an integer")
                    else:
                        print("Name must be a non-empty string")
            if found == 0:
                print("No student found with this ID")
        else:
            print("Data is empty")
  
    def delete_student(self,stu_id):
        found = 0
        if self.students != []:
            student_to_delete = None
            for i in self.students:
                if i['id'] == stu_id:
                    found += 1
                    student_to_delete = i
            if student_to_delete is not None:
                self.students.remove(student_to_delete)
                print("Student deleted successfully")
            if found == 0:
                print("No student found with this ID")
        else:
            print("No students found")

    def summary(self):
        if self.students != []:
            total_no_of_stu = 0
            total_marks = 0
            for i in self.students:
                total_no_of_stu += 1
                total_marks += i['marks']
            highest_stu = max(
                self.students,
                key= lambda x: x['marks']
                )
            lowest_stu = min(
                self.students,
                key= lambda x: x['marks']
                )
            final_dict = {
                "total_no_of_students": total_no_of_stu,
                "average_marks": total_marks/total_no_of_stu,
                "highest_marks": highest_stu['marks'],
                "lowest_marks": lowest_stu['marks']
            }
            print(final_dict)
        else:
            print("No students found")

    def load_students(self):
        if os.path.exists("projects_topic_24/student management system/students.json"):
            try:
                with open("projects_topic_24/student management system/students.json","r")as f:
                    data = json.load(f)
                    if isinstance(data,list):
                        dict_count = 0
                        for i in data:
                            if isinstance(i,dict):
                                dict_count += 1
                        if len(data) == dict_count:
                            passsed_count = 0
                            seen_ids = []
                            for i in data:
                                if "id" in i and "name" in i and "marks" in i: 
                                    passsed_count += 1
        
                                    if isinstance(i['id'],int) and not isinstance(i['id'],bool):
                                        if isinstance(i['name'],str) and i['name'].strip() != "":
                                            if isinstance(i['marks'],int) and not isinstance(i['marks'],bool):
                                                if 0 <= i['marks'] <= 100:
                                                    if i['id'] not in seen_ids:
                                                        seen_ids.append(i['id'])
                                                    else:
                                                        print("Duplicate student ID")
                                                        return
                                                else:
                                                    print("Marks must be between 0 and 100")
                                                    return
                                            else:
                                                print("Marks must integer")
                                                return
                                        else:
                                            print("Name must be non-empty string")
                                            return
                                    else:
                                        print("Id validation error")
                                        return
                            if len(data) == passsed_count:
                                self.students = data
                            else:
                                print("Key is missing in data")
                                return
                        else:
                            print("Data inside is not in dict")
                            return
                    else:
                        print("Data must be list")
                        return 
            except FileNotFoundError:
                self.students = []
            except json.JSONDecodeError:
                print("Invalid JSON data")
                return
        else:
            self.students = []

    def save_students(self):
        with open("projects_topic_24/student management system/students.json","w")as f:
            json.dump(self.students,f,indent=4)

data = StudentManager()
data.load_students()

while True:
    print('''
    1. add student
    2. view student
    3. search student
    4. update student
    5. delete student
    6. summary
    7. load students
    8. save students
    9. exit
    ''')
    try:
        user_input = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number: ")
        continue
    if user_input == 1:
        try:
            id = int(input("Enter id: "))
            name = input("Enter name: ")
            if name.strip() != "":
                marks = int(input("Enter marks: "))
                if isinstance(marks,int) and not isinstance(marks,bool):
                    if 0 <= marks <= 100:
                        student_count_before = len(data.students)
                        data.add_student(id, name, marks)
                        if len(data.students) > student_count_before:
                            data.save_students()
                    else:
                        print("Marks must be between 0 and 100")
                else:
                    print("marks must be integer") 
            else:
                print("Invalid name")
        except ValueError:
            print("Invalid input")  

    elif user_input == 2:
        data.view_all_student()

    elif user_input == 3:
        try:
            id = int(input("Enter id to search: "))
            data.search_student(id)
        except ValueError:
            print("Invalid input")

    elif user_input == 4:
        try:
            stu_id = int(input("Enter id: "))
            new_name = input("Enter new name: ")
            new_marks = int(input("Enter new marks: "))
            data.update_student(stu_id,new_name,new_marks)
            data.save_students()
        except ValueError:
            print("Invalid input")

    elif user_input == 5:
        try:
            stu_id = int(input("Enter id: "))
            data.delete_student(stu_id)
            data.save_students()
        except ValueError:
            print("Invalid input")

    elif user_input == 6:
        data.summary()

    elif user_input == 7:
        data.load_students()
        data.view_all_student()

    elif user_input == 8:
        data.save_students()
        print("Students saved successfully")

    elif user_input == 9:
        break

    else:
        print("Invalid choice")





