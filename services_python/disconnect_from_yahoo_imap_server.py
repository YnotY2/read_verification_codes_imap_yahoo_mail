from utils.colors import Colors
from utils.logger import setup_logger

from config.settings import EMAIL
logger = setup_logger(service_name="connect_to_yahoo_imap_server")



def disconnect_from_yahoo_imap_server(mail):
    logger.info(f"{Colors.CYAN}Attempting to disconnect from the yahoo-mail IMAP server.{Colors.END}")
    try:
        # Logout from the Yahoo IMAP server
        mail.logout()
        logger.info(f"{Colors.GREEN}Successfully disconnected from the IMAP server.{Colors.END}")
        return True

    except Exception as e:
        logger.error(f"{Colors.RED}Error occurred while attempting to disconnect from yahoo imap server for acc: {EMAIL} {Colors.END}")
        logger.error(f"{Colors.RED}Error message: {e}{Colors.END}")
        return False

if __name__ == "__main__":
    disconnect_from_yahoo_imap_server()
