# Fetch Verification Emails from Mail Inbox using IMAP Protocol

This code is a template designed to easily read emails from a specified Yahoo Mail account using simple credentials:

- **App Password Yahoo**
- **Yahoo Mail Account Name**

This approach is entirely free, till 1TB!

## Features

- Check for emails containing the verification code from both the **inbox** and **spam** folders.
- Identify if the body of the most recent emails contains the text (using regular expressions) from the promotion company/service you are targeting.
- Extract the verification code from the email using a custom regular expression pattern.

## How to Use

For each new service, simply modify the regular expression pattern for the email itself. This flexibility allows you to use this code across multiple services with ease.

### Steps

1. **Set Up Yahoo Mail App Password:**
   - Generate an app password in your Yahoo account settings.
   - Use this app password along with your Yahoo Mail account name as credentials in the code.

2. **Modify Regular Expression Patterns:**
   - Update the regular expression patterns to match the specific email content and verification code format for the service you are targeting.

3. **Run the Code:**
   - The code will search through your inbox and spam folders for emails matching the criteria.
   - It will then extract the verification code from the matching emails.

## Example

Here's a basic outline of what the code does:

1. Connect to Yahoo Mail using IMAP.
2. Search for emails in the inbox and spam folders.
3. Use regular expressions to find emails containing specific text.
4. Extract the verification code using another regular expression pattern.

## Requirements

- A Yahoo Mail account with an app password.
- Python with the necessary libraries installed (e.g., `imaplib`, `re`).

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
