1.	Project Title	
 
A Simulated Device Temperature Monitoring System Using Python

2.	Student Name

Johnna Freya A. Bangsoy

4.	Student Number
   
2601274

6.	Section
    
1CPE-A

8.	Project Description	Two to four sentences: what the program does and why?

   
It allows users to view existing readings, add new valid readings, classify temperatures as NORMAL, WARNING, or CRITICAL, and generate a summary containing the total, average, minimum, maximum, and percentage of each category. The program helps users understand how temperature monitoring works and determine the overall status of a device based on its readings.

10.	Features:

View Readings: Displays all current temperature readings in degrees Celsius.
Add Reading: Allows users to enter new temperature readings from 0 to 100.
Input Validation: Rejects empty inputs, non-whole numbers, and values outside the accepted range.
Classify Readings: Classifies each temperature as NORMAL, WARNING, or CRITICAL.
Compute Summary: Calculates the total, average, minimum, and maximum temperatures.
Count Categories: Determines the number and percentage of NORMAL, WARNING, and CRITICAL readings.
Determine Overall Status: Displays NORMAL, MONITOR, or ATTENTION REQUIRED based on the readings.
Menu-Driven Interface: Provides options for viewing readings, adding readings, classifying temperatures, generating a summary, and exiting the program.

11.	Requirements
    
A text editor or Python IDE, such as IDLE or Visual Studio Code.
A terminal or command prompt to run the program.
No additional libraries are required because the program uses Python's built-in functions.

12.	How to Run
    
Copy the Python source code into a file named device_monitor.py.
Save the file in your preferred folder.
Open a terminal in that folder.
Run the command

14.	Sample Output

SIMULATED DEVICE MONITORING SYSTEM

----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 4

MONITORING SUMMARY 

------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED

14.	Test Cases
A summary of your tests and a link to test_cases.md

| Test Case| Input or Action | Expected Result | Actual Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| TC01 | Choose 1 | Shows readings 28, 31, 35, 37, 29 | Five readings displayed correctly | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | Reading added successfully | Pass |
| TC03 | Choose 2, enter abc | Input rejected and list unchanged | Invalid input message displayed | Pass |
| TC04 | Choose 2, enter -5 | Reading rejected | Invalid reading message displayed | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged. | Invalid reading message displayed | Pass |
| TC06 | Add 30, then choose 3 | 30 C -\> WARNING | 30 C classified as WARNING | Pass |
| TC07 | Choose 3 | 35 C -\> WARNING | 35 C classified as WARNING | Pass |
| TC08 | Choose 4 with initial data | Total 160, average 32.00, minimum 28, maximum 37, status ATTENTION REQUIRED | Summary values match the expected results | Pass |
| TC09 | Enter 9 | Error message displayed and menu repeats | Invalid choice message displayed and menu shown again | Pass |
| TC10 | Choose 5 | Exit message displayed and program ends | Thank-you message appears; program ends. | Pass |


15.	Known Limitations
    
Does not use real temperature sensors.
Readings are not saved after exiting.
Accepts whole numbers only.

16.	Reflection
    
I learned how to use Python functions, lists, loops, and conditional statements. I learned to validate inputs and calculate temperature summaries. The most challenging part was organizing the functions and handling invalid inputs. This project improved my programming and problem-solving skills.
