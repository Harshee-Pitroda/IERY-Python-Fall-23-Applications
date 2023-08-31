# IERY Python Fall 23 Applications GitHub Repository

##SMS Automation System with Validation

Project Overview:

The project consists of two main components: sms.py and main.py.

sms.py - SMS Handling Functions: In the sms.py file, a set of functions has been implemented to handle various aspects of SMS validation and sending.

main.py - User Interaction: The main.py file interacts with users, prompting them to provide a phone number and a message. It then communicates with the functions in sms.py to perform the necessary operations.

Validation and Sending: In the sms.py file, phone numbers are validated against a standard format that includes the country code. Additionally, the length of messages is checked to ensure they fall within an acceptable range. The project makes use of a reliable SMS library to simulate the sending of messages.

Outcome Notification: After attempting to send the SMS, users receive immediate feedback via the main.py interface. The system informs users about the success of the message delivery or any issues that might have arisen.

Handling Invalid Inputs: To enhance user experience, the system provides appropriate responses when invalid inputs are provided. This includes scenarios where phone numbers are improperly formatted or messages exceed the allowed length.

Undeliverable Messages: The project accounts for situations where valid messages cannot be delivered due to network issues. Through this, users receive accurate notifications about the status of their messages.

Example Scenario: Upon running main.py, users are prompted to input a phone number and a message. The system validates the inputs and proceeds to send the message if validation is successful. Users are provided with instant feedback on the outcome. For cases of input errors or undeliverable messages, the system ensures that users receive timely and relevant responses.


I'm open to feedback, suggestions, and questions regarding this project. Thank you for your interest and time!

Best regards, Syed Husna
