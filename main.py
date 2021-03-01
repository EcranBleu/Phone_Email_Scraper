#! python3

import re, pyperclip # pdfminer might work better if the source file is a badly-formed PDF

# TODO: Create a regex for US phone numbers

phone_regex = re.compile(r'''
# number formats: 123-456-7890, 456-7890 (no prefix), (123)-456-7890 (prefix in parentheses), 
# 456-7890 ext 12345, ext. 12345, x12345

(                               # One large group so that the 'findall' method doesn't return a broken list of tuples
((\d{3}) | (\(\d{3}\)))?        # area code (optional)
(\s|-)                          # first separator
\d{3}                           # first 3 digits
-                               # separator
\d{4}                           # last 4 digits
(((ext(\.)?\s)|x)               # extension word-part(optional)
(\d{2,5}))?                     # extension number-part (optional)
)
''', re.VERBOSE)

# TODO: Create a regex for email addresses

email_regex = re.compile(r'''

[a-zA-Z0-9_.+]+             # Name part
@                           # @
[a-zA-Z0-9_.+]+             # Domain part
\.[a-zA-Z0-9-.]+            # TLD

''', re.VERBOSE)

# TODO: Get the text off the clipboard

text = pyperclip.paste()

# TODO: Extract the email/phone from this text

extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_numbers = [phone_number[0] for phone_number in extracted_phone]
all_emails = [email for email in extracted_email]

# TODO: Copy the extracted email/phone to the clipboard

pyperclip.copy('\n'.join(all_phone_numbers + all_emails))