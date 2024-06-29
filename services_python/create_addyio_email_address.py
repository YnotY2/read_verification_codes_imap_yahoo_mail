import requests
from config.settings import ADDYIO_API_TOKEN

from utils.colors import Colors
from utils.logger import setup_logger
logger = setup_logger(service_name="create_addyio_email_address")

def create_addyio_email_address():
    logger.info(f"{Colors.CYAN}Attempting to create unique new addy.io email address.{Colors.END}")
    try:
        url = 'https://app.addy.io/api/v1/aliases'
        payload = {
            "domain": "anonaddy.me",

        }
        headers = {
            'Authorization': 'Bearer ' + ADDYIO_API_TOKEN,
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
        }

        logger.info(f"Sending request to addy.io-mail to create and fetch new alias")
        response = requests.request('POST', url, headers=headers, json=payload)

        if response.status_code == 201:
            logger.info(f"{Colors.GREEN}Successful API call!{Colors.END}")

            # Parse the JSON response
            data_dict = response.json()
            alias_data = data_dict.get("data", {})

            local_part = alias_data.get("local_part")
            domain = alias_data.get("domain")
            addy_email_address = alias_data.get("email")
            id = alias_data.get("id")

            logger.info(f"{Colors.CYAN}Created alias-email:")
            logger.info(f"Alias local_part:{Colors.END}:     {Colors.MAGENTA}{local_part}{Colors.END}")
            logger.info(f"{Colors.CYAN}alias domain:          {Colors.END}{Colors.MAGENTA}{domain}{Colors.END}")
            logger.info(f"{Colors.CYAN}full email:    {Colors.END}{Colors.MAGENTA}{addy_email_address}{Colors.END}")
            logger.info(f"{Colors.CYAN}unique ID:    {Colors.END}{Colors.MAGENTA}{id}{Colors.END}")
            logger.info(f"{Colors.CYAN}Returning the mail-address and ID for future usage.{Colors.END}")
            print("")
            return addy_email_address, id

        else:
            logger.info(f"Response status failed, with code {response.status_code}")
            logger.info(f"Response content: {response.text}")
            return None

    except Exception as e:
        logger.error(f"{Colors.RED}Error: {e}{Colors.END}")

if __name__ == "__main__":
    create_addyio_email_address()
