with open("students.txt",'r') as file:
    qatorlar = file.readlines()
    for qator in qatorlar:
        print(qator)
