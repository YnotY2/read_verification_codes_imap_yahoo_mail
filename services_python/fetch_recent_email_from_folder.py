import imaplib
import email

from utils.colors import Colors
from utils.logger import setup_logger
logger = setup_logger(service_name="connect_to_yahoo_imap_server")

def fetch_recent_email_from_folder(mail, folder):
    logger.info(f"{Colors.CYAN}Attempting to select the folder:  {Colors.END}{Colors.BLUE}{folder} {Colors.END}")
    try:
        mail.select(folder)
        status, messages = mail.search(None, 'ALL')
        email_ids = messages[0].split()
        logger.info(f"{Colors.GREEN}Successfully selected the {folder} folder.{Colors.END}")

        if email_ids:
            logger.info(f"{Colors.GREEN}Fetching the most recent email from the {folder} folder.{Colors.END}")
            status, msg_data = mail.fetch(email_ids[-1], '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    logger.info(f"{Colors.BLUE}Email Subject: {msg['subject']}{Colors.END}")
                    logger.info(f"{Colors.BLUE}Email From: {msg['from']}{Colors.END}")
                    logger.info(f"{Colors.BLUE}Email Date: {msg['date']}{Colors.END}")
                    print(msg.get_payload(decode=True).decode())
        else:
            logger.info(f"{Colors.YELLOW}No emails found in the {folder} folder.{Colors.END}")

    except Exception as e:
        logger.error(f"{Colors.RED}Error occurred while attempting to fetch emails from the {folder} folder: {e}{Colors.END}")
if __name__ == "__main__":
    fetch_recent_email_from_folder()
