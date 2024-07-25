# Fetch verification Codes from incoming yahoo emails using IMAP Protocol
This code is a template designed to easily read incoming emails from a specified Yahoo Mail account using simple credentials:

- **App Password Yahoo**
- **Yahoo Mail Account Name**
- **Addyio free subscription API KEY**

I am using addyio emails to fowared all incoming email to the specified yahoo mail inbox. A.K.A all incoming verification code's when signing-up for a service! 

## This approach is entirely free 
**Yahoo Mail**: 
- free till 1TB storage!
	+ I can delete all emails from all inboxes every-day at 5:00 circumventing ever hitting limit.

**Addyio email**
- free till hourly rate limit 
- free till account get's banned for abusing promo-code harvestin against terms of service 
	-*I can circumvent either limits by having a bunch of unique addy.io subscriptions with there own unique API-keys I can switch trough.*


## Features
- Check for emails containing the verification code from both the **inbox** and **spam** folders.
- Identify if the body of the 20 most recent emails contains the subject (using regular expressions) from the promotion company/service you are targeting. And extract these specified emails.
- Identify if either of these recent email's with specified subject contains the unique addy.io email address used to sign-up for service. And extract this/these unique emails. 
- Extract the verification code from the email with specified subject and addy.io mail address using a custom regular expression pattern.

## How to Use
For each new service, simply modify the subject and expression pattern for extracting code from the email itself. This flexibility allows you to use this code across multiple services with ease.

### Steps
1. **Set Up Yahoo Mail App Password:**
   - Generate an app password in your Yahoo account settings.
   - Use this app password along with your Yahoo Mail account name as credentials in the code.

2. **Modify Regular Expression Patterns:**
   - Update the subject expression to match the specified email'(s) we want to extract code from.
   - Update the regular expression patterns to match the specific email content and verification code format for the service you are targeting.

## Example

Here's a basic outline of what the code does:

1. Create account for specifed service using freshly created unique addy.io email address.

2. Connect to Yahoo Mail using IMAP.
3. Search for 20 most recent emails in the inbox and spam folders.
4. Use regular expressions to find emails containing specific subject within emails. Then return all emails found.
5. Use regular expression to find addy.io email address specified within email content. Then return all emails found. (usually only one)
6. Extract the verification code using another regular expression pattern. (if multiple emails found, fetch code from most recent email)

## Requirements
- A Yahoo Mail account with an app password.
- Multiple addy.io API-keys
- Python with the necessary libraries installed.

## Installation
1. Clone this repo:
```sh
https://github.com/YnotY2/read_verification_codes_imap_yahoo_mail.git
```

# Update code usage for a different service:

## Update the credentials if needed 

```sh
./read_verification_codes_imap_yahoo_mail/config/settings.py
```

- Content within the file: 
```sh
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
```
## Modify the following variables within 'main.py':

-**Test-Addyio-Address**
This is the addy.io address which you used to sign up for the service you wish to receive 
a verification code from. First manually sign up and confirm you can find the email-address using code.

  - addy_email_address = "vkm7565m@anonaddy.me"

    
-**Sender-Domain**
  -sender_domain = "+admin=uber.com@anonaddy.me"


## Modify the following python services
```ssh
./read_verification_codes_imap_yahoo_mail/services_python
```

```sh
extract_all_emails_with_specified_subject.py
```
- Here you only need to modify the actually subject value's passed to the function, we are searching for. No code modification needed. 

```sh
extract_verification_code_from_matched_email.py
```
- Here you need to modify the actual logic of the code to correctly parse the content tag of the email. And extract the verification code using custom logic. 

### Read the main.py code file for the actuall logic. 

```sh
./read_verification_codes_imap_yahoo_mail/main.py
```
- It is important for you to actually fully understand the logic of the code it's self. You can easily do this by reading the main.py python file!

