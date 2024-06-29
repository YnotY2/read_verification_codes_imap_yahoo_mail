# This function will take the dictionary containing the matched email('s)
# and check the content from the dict, and extract the verif code from it.

from bs4 import BeautifulSoup
import re

from utils.colors import Colors
from utils.logger import setup_logger
logger = setup_logger(service_name="extract_verification_code_from_matched_email")


def extract_verification_code_from_matched_email(matched_incoming_addyio_email):
    logger.info(f"{Colors.CYAN}Attempting to extract email('s) with specified addyio address.{Colors.END}")

    try:
        verification_code = None

        if isinstance(matched_incoming_addyio_email, list):
            for email in matched_incoming_addyio_email:
                email_content = email.get('content', '')  # Get the 'content' key from the email dictionary

                soup = BeautifulSoup(email_content, 'lxml')

                # Find all <p> tags containing "Verification code:"
                p_tags = soup.find_all('p', text=re.compile(r'Verification code:', re.IGNORECASE))

                for p_tag in p_tags:
                    # Find the next <p> tag which contains the verification code
                    next_p = p_tag.find_next('p')
                    if next_p:
                        # Extract the verification code using regex
                        match = re.search(r'\b(\d{4})\b', str(next_p))
                        if match:
                            verification_code = match.group(1)
                            logger.info(f"Successfully found the verification code!")
                            break  # Stop processing if verification code is found

                    # If verification code is found, break out of the loop
                    if verification_code:
                        break

    except Exception as e:
        logger.error(f"Error occurred while extracting verification code: {e}")
        return None

    logger.info(f"{Colors.BLUE}Verification code extracted:    {Colors.END}{Colors.MAGENTA}{verification_code}{Colors.END}")
    logger.info(f"{Colors.CYAN}Returning verification code variable.{Colors.END}")
    print("")
    return verification_code


if __name__ == "__main__":
    extract_verification_code_from_matched_email()
