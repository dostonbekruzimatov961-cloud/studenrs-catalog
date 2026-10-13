# Ali

print("Salom bolajonlar!")

with open("student.txt", 'a') as file:
    ism = input("Ismni kiriting: ").title()
    id = input("Id ni kiriting: ")
    file.write(f"Talaba: {ism}\n")
    file.write(f"Id: {id}\n")