# Student_Management_System

The aim of this project is to understand the working of a system that manages the information of the students studying in schools and colleges. This information can the be name of student, roll number, library subsciptions, extra curricular activities, overall marks obtained, etc. This information can be used to track the overall performance and development of student.

![image](https://user-images.githubusercontent.com/88525549/188596327-04bf1d8b-fb49-4a0b-a9d4-504d408af712.png)

This also reduces the effort and time of the teachers in their assessment of a particular student. The system is designed to give an overall idea of a student and present it to the teachers and parents in an easy fashion.

![image](https://user-images.githubusercontent.com/88525549/188597332-a5aba628-d2ea-46a6-9304-a92b18f125b7.png)


This project has been developed using python3x and its various libraries such as:

- tkinter for GUI
- PDBC using SQLite3
- Pandas
- Matplotlib
- Requests
- bs4
- sqlalchemy

For managing the student data, I have used Data Science features such as Data Exraction, Analysis and Visualization.

This project also consists of features such as 

- Data Authentications and Data Connectivity
- Adding a student record
- Viewing the student records
- Updating the student record
- Deleting a student record
- Comparing the Student data with help of bar plot charts
- Real-Time data 

With the help of tkinter,  a local application has been developed that is further divided into 5 windows:

1. The S.M.S window consists of windows such as Add, View, Update, Delete, Charts. The window also has some real-time features such as Location and Temperature.

![1](https://user-images.githubusercontent.com/88525549/188590695-7affd983-87a4-48f7-8bfb-7c92bf91efb4.png)

2. The Add Student window is to add a student by filling the fields such as Rno., Name, Marks, etc, along with Add and Back Buttons.

![2](https://user-images.githubusercontent.com/88525549/188591699-1c0ea461-0ede-41b9-8873-05649cab6ca4.png)

3. The View Student Record window shows the data entered by the user in the add window.

![3](https://user-images.githubusercontent.com/88525549/188592144-63279090-bf67-410d-a139-fd23f7fd4c0f.png)

4. The Update Student Record window is to update a student record which consists of the same fields as that of the add student window.

![4](https://user-images.githubusercontent.com/88525549/188592576-6bd86097-e86d-4dea-8b46-3d80e6b0547a.png)

5. The Delete Student Record window is to delete a particular student record.

![5](https://user-images.githubusercontent.com/88525549/188595246-553a1772-0242-42e3-95d3-fee6b31c9e68.png)

6. All the data entries and student details are saved on a database which can be accessed by using SQLite3. To view this data, the charts option is provided.
    On-clicking the Charts button, a window opens with bar-plot representation of the data. This data can also be viewed in the command prompt.
    
![7](https://user-images.githubusercontent.com/88525549/188595904-426578ed-853d-4813-b6a5-5f0ff0eee6ee.jpg)

