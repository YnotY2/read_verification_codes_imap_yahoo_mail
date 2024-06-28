import imaplib
import email

from utils.colors import Colors
from utils.logger import setup_logger
logger = setup_logger(service_name="fetch_recent_emails_from_folder")

def fetch_recent_emails_from_folder(mail, folder, num_emails):
    logger.info(f"{Colors.CYAN}Attempting to select the folder: {Colors.END}{Colors.BLUE}{folder}{Colors.END}")
    emails_data = []

    try:
        mail.select(folder)
        status, messages = mail.search(None, 'ALL')
        email_ids = messages[0].split()
        logger.info(f"{Colors.GREEN}Successfully selected the {folder} folder.{Colors.END}")

        if email_ids:
            logger.info(f"{Colors.CYAN}Attempting to fetching the last {Colors.END}{Colors.MAGENTA}{num_emails}{Colors.END}{Colors.CYAN} emails from the {folder} folder.{Colors.END}")
            print("")
            # Fetch the most recent `num_emails` emails
            email_ids = email_ids[-num_emails:]
            fetching_recent_email_number = num_emails + 1    # Variable to visualize what email number we are on.

            for email_id in email_ids:
                fetching_recent_email_number -= 1
                logger.info(f"{Colors.CYAN}Currently fetching recent email number:{Colors.END}{Colors.MAGENTA}{fetching_recent_email_number}{Colors.END} ")
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
    logger.info(f"{Colors.CYAN}Following example data contained within dictionary:{Colors.END}")
    print(f"{Colors.BLUE}"
                f"{{\n"
                f"    'subject': '{email_subject}',\n"
                f"    'from': '{email_from}',\n"
                f"    'date': '{email_date}',\n"
                f"    'content': 'Example content because actual content is wayyy to long.'\n"
                f"}}\n"
                f"{Colors.END}")
    print("")
    logger.info(f"{Colors.CYAN}Returning dictionary variable.{Colors.END}")
    return emails_data

if __name__ == "__main__":
    fetch_recent_emails_from_folder()
