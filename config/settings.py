import os

# Yahoo mail credentials [used for reading email from acc trough imap protocol]
# Define your email and app password
EMAIL = os.getenv("EMAIL", "kumain_ynoty2_verify_codes@yahoo.com")
APP_PASSWORD = os.getenv("APP_PASSWORD", "vcmqtlrrdteprcec")

# Yahoo IMAP server credentials
# Define the Yahoo IMAP server and port
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.mail.yahoo.com")
IMAP_PORT = os.getenv("IMAP_PORT", 993)