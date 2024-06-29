# Fetch verification Codes within email('s) from incoming yahoo emails using IMAP Protocol

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
	+ I can circumvent either limits by having a bunch of unique addy.io subscriptions with there own unique API-keys I can switch trough.


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
