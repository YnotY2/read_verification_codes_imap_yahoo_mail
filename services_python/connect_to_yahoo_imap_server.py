import imaplib
import email
from config.settings import APP_PASSWORD, EMAIL
from config.settings import IMAP_PORT, IMAP_SERVER

from utils.colors import Colors
from utils.logger import setup_logger

logger = setup_logger(service_name="connect_to_yahoo_imap_server")

def connect_to_yahoo_imap_server():
    logger.info(f"{Colors.CYAN}Attempting to connect to the yahoo-mail IMAP server.{Colors.END}")
    try:
        # Connect to the Yahoo IMAP server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(EMAIL, APP_PASSWORD)
        logger.info(f"{Colors.GREEN}Successfully connected to the IMAP server.{Colors.END}")
        logger.info(f"{Colors.BLUE}Connected to the following yahoo-mail account inbox:{Colors.END}")
        logger.info(f"{Colors.MAGENTA} {EMAIL}{Colors.END}")
        logger.info(f"{Colors.CYAN}Returning the mail-object for future usage.{Colors.END}")
        print("")
        return mail

    except Exception as e:
        logger.error(f"{Colors.RED}Error occurred while attempting to connect to yahoo imap server for acc: {EMAIL} {Colors.END}")
        logger.error(f"{Colors.RED}Error message: {e}{EMAIL} {Colors.END}")
        print("")
        return False

if __name__ == "__main__":
    connect_to_yahoo_imap_server()
