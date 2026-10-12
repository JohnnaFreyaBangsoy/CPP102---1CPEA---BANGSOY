Test Cases – Simulated Device Monitoring and Alert System

Tested by: Johnna Freya A. Bangsoy
Date: October 12, 2026

Test Case	Input or Action	Expected Result	Actual Result	Pass/Fail
TC01	Choose 1	Displays five initial readings	Five readings displayed	Pass
TC02	Choose 2, enter 33	Reading added successfully	Reading added successfully	Pass
TC03	Choose 2, enter abc	Input rejected; list unchanged	Invalid input message displayed	Pass
TC04	Choose 2, enter -5	Input rejected	Invalid reading message displayed	Pass
TC05	Choose 2, enter 101	Input rejected	Invalid reading message displayed	Pass
TC06	Choose 3	Displays classifications	Classifications displayed	Pass
TC07	Choose 4	Displays correct summary	Total: 160; Average: 32.00 C	Pass
TC08	Classify 30	WARNING	WARNING	Pass
TC09	Classify 37	CRITICAL	CRITICAL	Pass
TC10	Choose 6	Displays invalid choice message	Invalid choice message displayed	Pass
Bugs Found and Fixed

The program initially used an empty list instead of the five initial temperature readings. I fixed this by initializing the list with [28, 31, 35, 37, 29] in the main() function.

