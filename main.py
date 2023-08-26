from gmail_api import Gmail

def main(to, sub, message):
    print(Gmail.send_mail(to, sub, message))


if __name__ == "__main__":
    print("Welcome to Simple mail using API:")
    print("_"*30)
    to = input("Enter the mail id of the receiver: ")
    sub = input("Enter the subject of the mail: ")
    message = input("Enter the message of the mail: ")
    
    main(to, sub, message)