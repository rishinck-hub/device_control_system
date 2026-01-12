README – Simple Smart Device Control System (OOP in Python)

1. Overview
This project demonstrates Object-Oriented Programming (OOP) concepts in Python.
A common Device base class is used to create different devices like Motor and Light.
Each device can be turned ON and OFF and maintains its own internal state.
A generic Controller class operates any device without knowing its type.
The system is scalable, safe, and easy to extend with new devices.

2. Environment Setup
No special setup is required.
Python 3.x is enough to run this program.
No external libraries are used.

3. How to Run the Code
1. Save the code in a file named device_control.py
2. Open a terminal or command prompt
3. Navigate to the file location
4. Run the command:
   python device_control.py

4. How to Test the Code
The driver code already tests the system.
It creates Motor and Light objects.
Each device is passed to a Controller.
The controller turns the device ON and then OFF.

Expected Output:
Motor has started
Motor has stopped
Light switched on
Light switched off

5. Assumptions and Limitations
- Device state (ON/OFF) cannot be changed directly from outside the class
- New devices can be added by inheriting from the Device class
- Controller works with any current or future device
- The program runs in a console environment only

6. Dependencies
No external dependencies.
Only standard Python features are used.
