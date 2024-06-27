import imaplib
import email
from config.settings import APP_PASSWORD, EMAIL


# Define the Yahoo IMAP server and port
IMAP_SERVER = 'imap.mail.yahoo.com'
IMAP_PORT = 993

def fetch_recent_email(mail):
    # Select the mailbox you want to use (in this case, the inbox)
    mail.select('inbox')

    # Search for all emails in the inbox
    status, messages = mail.search(None, 'ALL')

    # Get the list of email IDs
    email_ids = messages[0].split()

    # Fetch the most recent email
    status, msg_data = mail.fetch(email_ids[-1], '(RFC822)')

    # Print the email content
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            print(response_part[1].decode('utf-8'))


# Fetch and print the most recent email
if __name__ == "__main__":
    fetch_recent_email()
