import os
import os

# Yahoo mail credentials [used for reading email from acc trough imap protocol]
# Define your email and app password
EMAIL = os.getenv("EMAIL", "YOUR_YAHOO_EMAIL_ADDRESS_HERE@yahoo.com")
APP_PASSWORD = os.getenv("APP_PASSWORD", "YOUR_APP_PASSWORD_HERE")

# Yahoo IMAP server credentials
# Define the Yahoo IMAP server and port
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.mail.yahoo.com")
IMAP_PORT = os.getenv("IMAP_PORT", 993)

# I am using addyio to read verification codes fowarded to above yahoo account :D
# Addyio email API
ADDYIO_API_TOKEN = os.getenv("ADDYIO_API_TOKEN", "YOUR_ADDYIO_API_KEY_HERE")
