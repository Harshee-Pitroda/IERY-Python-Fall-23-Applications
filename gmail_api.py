import smtplib, ssl


class Gmail:

    def send_mail(gmail_to, subject, message):
            
        gmail_user = 'b9703016043b@gmail.com'
        gmail_password = 'gbdzjsfafxiuunyw'

        #assigning the details of email, subject and etc
        sent_from = gmail_user   
        to = gmail_to    
        subject = subject

        body = f"""This is test mail\nMessage : \n{message}"""
        
        email_text = """To: <%s>
    MIME-Version: 1.0
    Content-type: text/html
    Subject: %s

    %s


    """ % (gmail_to,subject,body)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            print ('Email sent!')
        except:
            print ('Something went wrong...')
    #-------------------------------------------------------------------

