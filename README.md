# 🎓 Student Management System (Python CLI)

A simple command-line based Student Management System built using Python.
This project allows users to manage student records such as adding, viewing, searching, and deleting students. Data is stored persistently using a JSON file.

---

## 🚀 Features

* ➕ Add Student (Name & Marks)
* 📋 View All Students
* 🔍 Search Student by Name
* ❌ Delete Student
* 💾 Save Data to File (`students.json`)
* 📂 Load Existing Data Automatically

---

## 🛠️ Technologies Used

* Python 3
* JSON (for data storage)

---

## 📁 Project Structure

```
student_management.py
students.json   (auto-created after saving)
README.md
```

---

## ▶️ How to Run

1. Install Python (if not already installed)
2. Save the code in a file:

   ```
   student_management.py
   ```
3. Run the program:

   ```
   python student_management.py
   ```

---

## 🧑‍💻 Usage

After running, you will see a menu:

```
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
```

* Enter the corresponding number to perform actions
* Data is automatically saved when you exit

---

## 💡 Example

```
Enter Name : Gokul
Enter Mark : 85
Student Added...✔️
```

---

## ⚠️ Notes

* Data is stored in `students.json`
* If the file does not exist, it will be created automatically
* Ensure valid numeric input for marks

---

## 📌 Future Improvements

* ✏️ Update student details
* 📊 Sort students by marks
* 🏆 Display top performers
* GUI version using Tkinter

---

## 👨‍🎓 Author

* Gokul Giri

---

## 📜 License

This project is open-source and free to use.
