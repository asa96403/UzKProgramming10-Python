import datetime as dt

class Mail:
    def __init__(self, sender, subject, message, datetime=None):
        self.subject=subject
        self.sender=sender
        self.message=message
        if datetime is not None:
            self.datetime=datetime
        else :
            self.datetime = dt.datetime.now()
        self.read=False
    
    def __str__(self):
        return f"{self.subject} from {self.sender} on {self.datetime}: {self.message}"
    
    def getHeader(self):
        return f"{"unread" if self.read==False else "read"} | {self.subject} | {self.sender} | {self.datetime} "
    

class Inbox:
    def __init__(self, maillist=None):
        if maillist is None:
            self.maillist=[]
        else:
            self.maillist=maillist.copy()
    
    def printHeaders(self):
        print("----------------- Inbox -------------")
        i=0
        for mail in self.maillist:
            print(f"{i} | {mail.getHeader()}")
            i+=1

    def open(self, index):
        if 0<=index and index<len(self.maillist):
            self.maillist[index].read = True
            print(f"-------- Opened Email: {self.maillist[index].subject} ---------------")
            print(self.maillist[index])
        else :
            print("ERROR: Could not find email!")
        
    def countUnread(self):
        unread = [mail for mail in self.maillist if mail.read is False]
        return len(unread)

if __name__ == '__main__' :
    mail1 = Mail("test@example.com", "Testing", "This is a test mail, please respond shortly if it arrived.")
    #print(mail1.getHeader())
    #print(mail1)
    mail2 = Mail("some@emailprovider.com", "Useless Email", "This Email doesn't server an actual purpose other than testing.")
    mail3 = Mail("person@earth.global", "Hello World", "I am a real person writing from earth.")
    mails =[mail1, mail2, mail3]
    inbox = Inbox(mails)
    inbox.printHeaders()
    print(f"Number of unread mails: {inbox.countUnread()}")
    indexToOpen = input("Enter the index of the email to open (starting at 0): ")
    try:
        indexToOpen = int(indexToOpen)
    except ValueError:
        print("ERROR: You must enter a numeric value!")
    else :
        inbox.open(indexToOpen)
    inbox.printHeaders()
    print(f"Number of unread mails: {inbox.countUnread()}")

    