


import pyautogui as gui
import yagmail

def main():

    gui.FAILSAFE = False
    # disable failsafe function.

    emailAddress, password = getCredentials()

    gmail = gmailInstance(emailAddress, password)

    testMailer(gmail)

    exit()

def getCredentials():
# get email address and password input for gmail and return values. 

    emailAddress = gui.prompt(text= 'enter user gmail:', title= 'email prompt')
    password = gui.password(text =  'enter gmail password:',
                            title = 'password prompt', 
                            mask =  '*')
    return emailAddress, password

def gmailInstance(email, password):
# create gmail instance and return object. 

    gmail = yagmail.SMTP(email, password)
    return gmail

def testMailer(gmail):
# send test email.

    recipientList = []

    for recipient in recipientList:

        subject = 'testing testing testing'
        contents = 'this is a test message. this is a test message. this is a \
            test message. this is a test message. this is a test message. this\
            is a test message. this is a test message. this is a test message.'

        gmail.send( to=             recipient, 
                    subject=        subject,
                    contents=       contents,
                    attachments=    'ring_wallpaper.jpg')

        gui.alert(f'email sent to {recipient}.', 'email sent', 'OK')

main()