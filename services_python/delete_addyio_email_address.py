import requests
from config.settings import ADDYIO_API_TOKEN

from utils.colors import Colors
from utils.logger import setup_logger
logger = setup_logger(service_name="delete_addyio_email_address")

def delete_addyio_email_address(addy_email_address, id):
    logger.info(f"{Colors.CYAN}Attempting to delete unique utilised addy email address.{Colors.END}")
    try:
        url = f'https://app.addy.io/api/v1/aliases/{id}'
        headers = {
            'Authorization': 'Bearer ' + ADDYIO_API_TOKEN,
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }

        logger.info(f"{Colors.CYAN}Sending request to addy.io-mail to delete specified alias.{Colors.END}")
        logger.info(f"{Colors.CYAN}Alias:{Colors.END}{Colors.MAGENTA}{addy_email_address}{Colors.END}")
        response = requests.request('DELETE', url, headers=headers)

        if response.status_code == 204:
            logger.info(f"{Colors.GREEN}Successful API call!{Colors.END}")
            logger.info(f"{Colors.GREEN}Successful deleted alias {addy_email_address}.{Colors.END}")
            print("")
            return True

        else:
            logger.info(f"Response status failed, with code {response.status_code}")
            logger.info(f"Response content: {response.text}")
            return False

    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}{Colors.END}")

if __name__ == "__main__":
    delete_addyio_email_address()
