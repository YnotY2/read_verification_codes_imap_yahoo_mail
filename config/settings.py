import os

# Yahoo mail credentials [used for reading email from acc trough imap protocol]
# Define your email and app password
EMAIL = os.getenv("EMAIL", "kumain_ynoty2_verify_codes@yahoo.com")
APP_PASSWORD = os.getenv("APP_PASSWORD", "vcmqtlrrdteprcec")

# Yahoo IMAP server credentials
# Define the Yahoo IMAP server and port
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.mail.yahoo.com")
IMAP_PORT = os.getenv("IMAP_PORT", 993)

# I am using addyio to read verification codes fowarded to above yahoo account :D
# Addyio email API
ADDYIO_API_TOKEN = os.getenv("ADDYIO_API_TOKEN", "addy_io_cEHFa0ySNsGJinMlnSlZLVI1jp7vtrVhGYrGDCYV9c8be69e")