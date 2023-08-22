# IERY Python Fall 23 Applications GitHub Reporsitory

# Task 1: Email Automation Setup and Test Message Sending
## In this task, you will be setting up an email automation system using a selected API or library. You'll create a dedicated Python file within the project repository, known as the "Gmail_library" to facilitate email sending. Furthermore, you will integrate this library with the main application, allowing users to input a message subject and body for sending test emails.

Acceptance Criteria:

Library Creation:

Create a new Python file named gmail_library.py within the repository.
Inside this file, develop the necessary code to interface with the chosen Gmail API or library for sending emails.
Main Application Integration:

Enhance the main.py file to include a user interface.
Prompt the user to input a message subject and body.
Function for Sending:

In the main.py file, implement a function named send_test_email(subject, body) that interacts with the Gmail library you've developed.
This function should accept the subject and body inputs as parameters and trigger the sending of a test email using the Gmail library.
Test Email:

The test email should be sent to a predefined email address or to yourself for verification purposes.
Confirm that the test email contains the provided subject and body content.
Note: The main goal is to showcase your ability to integrate the Gmail library with the main application and successfully send a test email. The email content can be minimal, but the focus should be on the integration and functioning of the email automation system.

Example Scenario:

You receive a user prompt in the main.py application asking for the subject and body of the email. After inputting the content, you execute the send_test_email() function, which communicates with your Gmail library. This library, in turn, connects to the Gmail API and sends the test email with the provided content. Upon successful execution, you should receive the test email in your inbox, demonstrating that the email automation system is operational.

Remember: Your code should be well-organized, with clear separation between the Gmail library functions and the main application functions. This separation ensures modularity and ease of maintenance.
