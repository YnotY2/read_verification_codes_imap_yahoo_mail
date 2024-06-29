# This function will find email by specified subject and specified addyio unique email
# We give this function a dictionary containing all emails with a specified subject.
# then we loop through that dictionary finding the anonaddy domain email we want.
# Then we return that specified email :D
# If there are 2 of them we return the one with the most recent date.


# <rg0z23it+admin=uber.com@anonaddy.me> We can find the addy.io email domain by removing
# <> brackets and everything before the + then adding @anonaddy.me !

# This function will loop trough all emails we have saved within the dictionary
# returned from the function "fetch_all_email_from_folder.py"
# and extract all emails with specified subject and save within a new dictionary
# We pass the subjects it should search for in a list, because the service we are fetching verification
# codes for can use multiple subjects. In our case for uber it uses 2 unique subjects.
# then we return that dictionary :D

import random
from utils.colors import Colors
from utils.logger import setup_logger
logger = setup_logger(service_name="find_email_by_subject_and_addyio_mail_sender")


def find_email_by_subject_and_addyio_mail_sender(emails_data, addy_email_address):
    logger.info(f"{Colors.CYAN}Attempting to extract email('s) with specified addyio address.{Colors.END}")
    logger.info(f"{Colors.CYAN}Addyio email:    {Colors.END}{Colors.MAGENTA}{addy_email_address}{Colors.END}")

    matched_incoming_addyio_email = []

    # Create the string to search for within email
    # cut @anonaddy.me from addy_email_address
    local_addyio_part = addy_email_address.split('@')[0]
    addyio_match = f"{local_addyio_part}+admin=uber.com@anonaddy.me>"

    try:
        for email in emails_data:
            if addyio_match in email['from']:       # We find the match in the from email field
                logger.info(f"Successfully found incoming email matching recently used addyio-email address. ")
                matched_incoming_addyio_email.append(email)

    except Exception as e:
        logger.error(f"Error: {e}")

    logger.info(f"{Colors.GREEN}Successfully extracted all emails with specified addyio address and added data to list 'emails_specified_subject_data'.{Colors.END}")
    logger.info(f"{Colors.CYAN}Returning matched email data.{Colors.END}")
    print("")
    return matched_incoming_addyio_email

if __name__ == "__main__":
    find_email_by_subject_and_addyio_mail_sender()
