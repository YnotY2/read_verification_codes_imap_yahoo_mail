import time

from utils.colors import Colors
from utils.logger import setup_logger

#from services_python.fetch_recent_email import fetch_recent_email
#from services_python.fetch_all_email_from_folder import fetch_all_email_from_folder

from services_python.create_addyio_email_address import create_addyio_email_address
from services_python.delete_addyio_email_address import delete_addyio_email_address

from services_python.connect_to_yahoo_imap_server import connect_to_yahoo_imap_server
from services_python.disconnect_from_yahoo_imap_server import disconnect_from_yahoo_imap_server
from services_python.fetch_recent_emails_from_folder import fetch_recent_emails_from_folder
from services_python.extract_all_emails_with_specified_subject import extract_all_emails_with_specified_subject

# Setup logger with service name
service_name = "main"
logger = setup_logger(service_name)

def main():
    try:

        logger.info(f"{Colors.CYAN}Starting{Colors.END}{Colors.YELLOW} main.py{Colors.END} {Colors.CYAN} python3 script ...{Colors.END}")

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} create_addyio_email_address.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        addy_email_address, id = create_addyio_email_address()

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} connect_to_yahoo_imap_server.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        mail = connect_to_yahoo_imap_server()       # We return a mail object used as a cursor for navigating IMAP protocol cmds. Kinda like db object cursor

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} fetch_recent_email_from_folder.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        emails_data = fetch_recent_emails_from_folder(mail, "inbox", num_emails=20)
        #print(emails_data)
        time.sleep(2)

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} fetch_recent_email_from_folder.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        emails_data_spam = fetch_recent_emails_from_folder(mail, "Bulk", num_emails=20)
        #print(emails_data)
        time.sleep(2)

        # Combine the results from both folders within the dictionary "emails_data"
        emails_data.extend(emails_data_spam)
        #print(emails_data)

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} extract_all_emails_with_specified_subject.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        subjects_to_extract = ['Welcome to Uber Eats!', 'Welcome to Uber']
        emails_specified_subject_data = extract_all_emails_with_specified_subject(emails_data, subjects_to_extract)
        print(emails_specified_subject_data)

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} delete_addyio_email_address.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        delete_addyio_email_address(addy_email_address, id)

        logger.info(f"{Colors.CYAN}Calling{Colors.END}{Colors.YELLOW} disconnect_from_yahoo_imap_server.py{Colors.END} {Colors.CYAN}service -function{Colors.END}")
        disconnect_from_yahoo_imap_server(mail)
        # print(msg.get_payload(decode=True).decode())



    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}{Colors.END}")

if __name__ == "__main__":
    main()
