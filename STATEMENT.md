==================================================
        PROBLEM STATEMENT / PROJECT REQUIREMENT
==================================================

Project Title: 
--------------
Student Marks and Attendance Management System


Objective:
----------
To build a simple, menu-driven Python application that helps teachers or school 
administrators store student details, calculate their academic performance, and 
save the data to a text file for future use.


Problem Description:
--------------------
Managing student records manually on paper is time-consuming and can lead to errors 
in calculating marks, percentages, and grades. Additionally, paper records can easily 
get lost or damaged. 

To solve this problem, we need a small computer program that can:
1. Store student details like Roll Number, Name, Marks for 3 subjects, and Attendance %.
2. Automatically calculate Total Marks, Percentage, and assign a Grade based on score.
3. Save all the student records permanently into a local file ("students_data.txt") 
   so the data is not lost when the program closes.
4. Load existing records automatically whenever the program starts up.
5. Provide a simple text menu so the user can easily choose options to add records, 
   view records, or search for a student using their Roll Number.


Functional Requirements:
------------------------
1. Menu Options:
   - Option 1: Add a new student record.
   - Option 2: Display all student records in a formatted table.
   - Option 3: Search for a specific student by Roll Number.
   - Option 4: Save data to the text file manually.
   - Option 5: Save and exit the program.

2. Grade Calculation Rules:
   - Percentage >= 90%         : Grade A+
   - Percentage 80% to 89.9%   : Grade A
   - Percentage 70% to 79.9%   : Grade B
   - Percentage 60% to 69.9%   : Grade C
   - Percentage 50% to 59.9%   : Grade D
   - Percentage < 50%          : Grade Fail

3. File Handling:
   - Read data from "students_data.txt" when starting.
   - If the file does not exist, start with an empty record list without crashing.
   - Save updated records back to "students_data.txt" separated by commas.


Tools & Technology Used:
------------------------
- Programming Language : Python 3
- Data Structures      : Python Lists (Parallel Lists)
- File Storage         : Plain Text File (.txt)
- Concepts Covered     : Functions, Loops (While/For), Conditional Statements (If-Else), File I/O