def StudentDetails(name,st_id,n):
    stu = {'Name': name, 'ID': st_id}  

    
    subjects = [] 
    marks = []      
    for i in range(1,n+1):
        
        subject_name = input(f"Enter {i} Subject Name :")
        subject_mark = int(input(f"Enter marks for {subject_name} :"))
        
        subjects.append(subject_name)  
        marks.append(subject_mark)     
        
            
    
    Grade = []
    for a in range(0,n):
        if marks[a] >= 90 :
            grade = "A"
        elif marks[a] < 90 and marks[a] >= 75:
            grade = "B"
        elif marks[a] < 75 and marks[a] >= 60 :
            grade = "C"
        else:
            grade = "D"
        Grade.append(grade)
    
    print("\nStudent Details :")
    print("Student Name:", stu['Name'])
    print("Student ID:", stu['ID'])
    print("Subjects , Marks and Grade:")
    for i in range(n):
            print(f"{i+1}.",f"{subjects[i]} - Marks : {marks[i]}, Grade : {Grade[i]}")
    
    
name = input("Enter your Name :")
id = int(input("Enter your ID Number :"))
n = int(input("Enter number of Subject :"))
StudentDetails(name,id,n)