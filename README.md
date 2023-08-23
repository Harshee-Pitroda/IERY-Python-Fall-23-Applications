# IERY Python Fall 23 Applications GitHub Repository

### Please choose one of the task you want to perform from the below mentioned tasks and make a pull request for your submissions

### Task 1: Email Automation Setup and Test Message Sending

In this task, you will be setting up an email automation system using a selected API or library. You'll create a dedicated Python file within the project repository, known as the "Gmail_library" to facilitate email sending. Furthermore, you will integrate this library with the main application, allowing users to input a message subject and body for sending test emails.

Acceptance Criteria:

Library Creation:

Create a new Python file named gmail_library.py within the repository.
Inside this file, develop the necessary code to interface with the chosen Gmail API or library for sending emails.

Main Application Integration:

In the main application prompt the user to input a message subject and body and perform the automation of sending emails by just calling the gmail_library.py

Function for Sending:

In the main.py file, implement a function named send_test_email(subject, body) that interacts with the Gmail library you've developed. This function should accept the subject and body inputs as parameters and trigger the sending of a test email using the Gmail library.

Test Email:

The test email should be sent to a predefined email address or to yourself for verification purposes.
Confirm that the test email contains the provided subject and body content.
Note: The main goal is to showcase your ability to integrate the Gmail library with the main application and successfully send a test email. The email content can be minimal, but the focus should be on the integration and functioning of the email automation system.

Example Scenario:

You receive a user prompt in the main.py application asking for the subject and body of the email. After inputting the content, you execute the send_test_email() function, which communicates with your Gmail library. This library, in turn, connects to the Gmail API and sends the test email with the provided content. Upon successful execution, you should receive the test email in your inbox, demonstrating that the email automation system is operational.

Remember: Your code should be well-organized, with clear separation between the Gmail library functions and the main application functions. This separation ensures modularity and ease of maintenance.

### Task 2: SMS Automation Setup and Validation

Description: Develop a user-friendly SMS handling system that prompts users for a phone number and a message. The system will ensure the validity of these inputs, send the message if valid, and provide notifications about the outcome. This task also requires handling cases of invalid phone numbers, invalid messages, and undeliverable messages.

Acceptance Criteria:

Create SMS Handling Functions:

Create a new Python file named sms.py to contain your SMS handling functions.
Implement various functions to perform the task mentioned in the description.

User Interaction:

Make a main.py to interact with users.
Prompt users for a phone number and the desired message.

Validation and Sending:

In sms.py, ensure you validate phone numbers in a standard format (with country code) and checks message length.
Use sendSMS(phone_number, message) in sms.py to send the message using a reliable SMS library (that you are free to use any).

Outcome Notification:

After attempting to send the SMS, notify users in main.py whether the message was sent successfully.

Handling Invalid Inputs:

Print a response to the user for invalid inputs.

Undeliverable Messages:

Implement handling for scenarios where valid messages can't be delivered due to network issues.
Simulate this scenario and ensure users receive appropriate notifications.
Note: The main goal is to showcase your ability to create a functional SMS handling system with validation. Organize your code into logical sections, differentiating between the main application and the SMS handling functions stored in sms.py. 

Example Scenario:

Upon running main.py, the SMS system prompts users for a phone number and a message. The system validates inputs and sends the message when validation is successful. Users receive feedback on the outcome. For input errors like incorrect phone number formatting or too-long messages, the system should provide appropriate responses. Additionally, demonstrate how the system handles undeliverable messages despite valid inputs.
