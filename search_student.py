student_id = input("Talaba ID sini kiriting: ")

with open("student.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

found = False

for i in range(len(lines)):
    if lines[i].startswith("Ism:"):
        ism = lines[i].replace("Ism:", "").strip()
        id_raqam = lines[i + 1].replace("Id:", "").strip()

        if id_raqam == student_id:
            print("Ism:", ism)
            print("Id:", id_raqam)
            found = True
            break

if not found:
    print("Talaba topilmadi")