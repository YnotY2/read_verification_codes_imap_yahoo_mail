from utils.colors import Colors
from utils.logger import setup_logger

from services_python.connect_to_yahoo_imap_server import connect_to_yahoo_imap_server
from services_python.disconnect_from_yahoo_imap_server import disconnect_from_yahoo_imap_server
from services_python.fetch_recent_email_from_folder import fetch_recent_email_from_folder
from services_python.fetch_recent_email import fetch_recent_email

# Setup logger with service name
service_name = "main"
logger = setup_logger(service_name)

def main():
    try:

        logger.info(f"{Colors.CYAN}Starting{Colors.END}{Colors.YELLOW} main.py{Colors.END} {Colors.CYAN} python3 script ...{Colors.END}")

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} connect_to_yahoo_imap_server.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        mail = connect_to_yahoo_imap_server()       # We return a mail object used as a cursor for navigating IMAP protocol cmds. Kinda like db object cursor

        #logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} fetch_recent_email.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        #fetch_recent_email(mail)

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} fetch_recent_email_from_folder.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        fetch_recent_email_from_folder(mail, "inbox")
        fetch_recent_email_from_folder(mail, "Spam")


        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} disconnect_from_yahoo_imap_server.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        disconnect_from_yahoo_imap_server(mail)



    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}{Colors.END}")

if __name__ == "__main__":
    main()
