import re
def validate_phone_number(phone_number):

    # checking whether the phone no is 10 digis long or not
    if re.match(r'^\d{10}$', phone_number):
        return True
    else:
        return False

def validate_message_length(message):
   
    #checking if the message length is within a certain limit
    if len(message) <= 160:
        return True
    else:
        return False

def send_sms(phone_number, message):
   
    #prining a message indicating that the SMS was sent or not
    print(f"Sending SMS to {phone_number}: {message}")
    print("SMS sent successfully!")