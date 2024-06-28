# This function will loop trough all emails we have saved within the dictionary
# returned from the function "fetch_all_email_from_folder.py"
# and extract all emails with specified subject and save within a new dictionary
# We pass the subjects it should search for in a list, because the service we are fetching verification
# codes for can use multiple subjects. In our case for uber it uses 2 unique subjects.
# then we return that dictionary :D

import random
from utils.colors import Colors
from utils.logger import setup_logger
logger = setup_logger(service_name="extract_all_emails_with_specified_subject")


def extract_all_emails_with_specified_subject(emails_data, subjects_to_extract):
    logger.info(f"{Colors.CYAN}Attempting to extract all emails with specified subjects: {Colors.END}{Colors.BLUE}{subjects_to_extract}{Colors.END}")
    emails_specified_subject_data = []

    try:
        for email in emails_data:
            if email['subject'].lower() in [subject.lower() for subject in subjects_to_extract]:
                emails_specified_subject_data.append(email)

    except Exception as e:
        logger.error(f"Error: {e}")

    logger.info(f"{Colors.GREEN}Successfully extracted all emails with specified subject '{subjects_to_extract}' and added data to dictionary 'emails_specified_subject_data'.{Colors.END}")
    logger.info(f"{Colors.CYAN}Example data contained within dictionary:{Colors.END}")
    logger.info(f"{Colors.BLUE}"
                f"{{\n"
                f"    'subject': '{random.choice(subjects_to_extract)}',\n"
                f"    'from': 'sender@example.com',\n"
                f"    'date': 'Thu, 01 Jan 1970 00:00:00 +0000',\n"
                f"    'content': 'Example content because actual content is way too long.'\n"
                f"}}\n"
                f"{Colors.END}")

    logger.info(f"{Colors.CYAN}Returning dictionary variable.{Colors.END}")
    return emails_specified_subject_data

if __name__ == "__main__":
    extract_all_emails_with_specified_subject()
