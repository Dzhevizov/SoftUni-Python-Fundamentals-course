class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


input_data = input()
emails = []

while not input_data == "Stop":
    sender, receiver, content = input_data.split()
    e_mail = Email(sender, receiver, content)
    emails.append(e_mail)

    input_data = input()

sent_emails = [int(x) for x in input().split(", ")]

for index in range(len(emails)):
    if index in sent_emails:
        emails[index].send()

for e_mail in emails:
    print(e_mail.get_info())
