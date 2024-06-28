# This function will fetch all incomming email, from both inbox and spam folders :D
# then we will add all the emails to a dicionary!
# actually searching trough ALL emails is quite slow, we can better search for last 20

import imaplib
import email

from utils.colors import Colors
from utils.logger import setup_logger
logger = setup_logger(service_name="fetch_all_email_from_folder")

def fetch_all_email_from_folder(mail, folder):
    logger.info(f"{Colors.CYAN}Attempting to select the folder: {Colors.END}{Colors.BLUE}{folder}{Colors.END}")
    emails_data = []

    try:
        mail.select(folder)
        status, messages = mail.search(None, 'ALL')
        email_ids = messages[0].split()
        logger.info(f"{Colors.GREEN}Successfully selected the {folder} folder.{Colors.END}")

        if email_ids:
            logger.info(f"{Colors.GREEN}Attempting to fetch all emails from the {folder} folder.{Colors.END}")
            for email_id in email_ids:
                status, msg_data = mail.fetch(email_id, '(RFC822)')
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        email_date = msg['date']

                        logger.info(f"{Colors.CYAN}Email Subject: {Colors.END}{Colors.BLUE}{email_subject}{Colors.END}")
                        logger.info(f"{Colors.CYAN}Email From: {Colors.END}{Colors.BLUE}{email_from}{Colors.END}")
                        logger.info(f"{Colors.CYAN}Email Date: {Colors.END}{Colors.BLUE}{email_date}{Colors.END}")

                        # Check if message has a payload to decode
                        if msg.is_multipart():
                            payload = msg.get_payload(0).get_payload(decode=True)
                        else:
                            payload = msg.get_payload(decode=True)

                        email_content = payload.decode() if isinstance(payload, bytes) else None

                        if email_content:
                            email_data = {
                                'subject': email_subject,
                                'from': email_from,
                                'date': email_date,
                                'content': email_content
                            }
                            emails_data.append(email_data)
                        else:
                            logger.warning(f"{Colors.YELLOW}No valid payload to decode in the email.{Colors.END}")
        else:
            logger.info(f"{Colors.YELLOW}No emails found in the {folder} folder.{Colors.END}")

    except Exception as e:
        logger.error(f"{Colors.RED}Error occurred while attempting to fetch emails from the {folder} folder: {e}{Colors.END}")

    logger.info(f"{Colors.GREEN}Successfully fetched all emails from folder {folder}, and added data to dictionary.{Colors.END}")
    logger.info(f"{Colors.CYAN}Following data contained within dictionary:{Colors.END}")
    logger.info(f"{Colors.BLUE}"
                f"{{\n"
                f"    'subject': 'Meeting Reminder',\n"
                f"    'from': 'boss@example.com',\n"
                f"    'date': 'Fri, 27 Jun 2024 12:34:56 +0000',\n"
                f"    'content': 'Dear team, this is a reminder for our meeting tomorrow at 10 AM. Please be prepared with your reports.'\n"
                f"}}\n"
                f"{Colors.END}")
    print("")
    logger.info(f"{Colors.CYAN}Returning dictionary variable.{Colors.END}")
    return emails_data

if __name__ == "__main__":
    fetch_all_email_from_folder()
