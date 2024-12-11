from data import Student
from view.view_functions import display_students, find_student_index
from view.input_functions import input_student_data

def display_menu():
    print("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]: ", end=' ')

def main():
    students = []
    while True:
        display_menu()
        choice = input().lower()
        if choice == 't':
            nim, nama, tugas, uts, uas = input_student_data()
            students.append(Student(nim, nama, tugas, uts, uas))
        elif choice == 'l':
            display_students(students)
        elif choice == 'u':
            display_students(students)
            nama = input("\nMasukkan nama mahasiswa yang akan diubah: ")
            index = find_student_index(students, nama)
            if index is not None:
                print("Data baru:")
                nama = input("Nama: ")
                tugas = int(input("Nilai Tugas: "))
                uts = int(input("Nilai UTS: "))
                uas = int(input("Nilai UAS: "))
                students[index] = Student(nim, nama, tugas, uts, uas)
            else:
                print("Mahasiswa dengan nama tersebut tidak ditemukan.")
        elif choice == 'h':
            display_students(students)
            nama = input("\nMasukkan nama mahasiswa yang akan dihapus: ")
            index = find_student_index(students, nama)
            if index is not None:
                del students[index]
                print("Data mahasiswa berhasil dihapus.")
            else:
                print("Mahasiswa dengan nama tersebut tidak ditemukan.")
        elif choice == 'k':
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
