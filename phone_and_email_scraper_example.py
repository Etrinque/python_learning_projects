import re
import pyperclip

'''Use to scrape documents for phone number and email lists'''


# Create a regex for phone numbers
phone_regex = re.compile(r'''
                    # 415-555-5555, 555-5555, 
                    # (415) 555-5555, 555-5555 
                    # ext 12345, 
                    # ext. 12345, 
                    # x12345

((\d\d\d) | (\(\d\d\d))?           # area code (optional)
(\s|-)              # first separator
(\d\d\d)              # first 3 digits
-                   # separator
(\d\d\d\d)            # last 4 digits
((ext(\.)?\s)|x)    # extension
(\d{2,5})?          # optional''', re.VERBOSE)



# Create a regex for email
email_regex = re.compile(r'''
[a-zA-Z0-9_.+]+     # name portion
@                   # @ symbol
[a-zA-Z0-9_.+]+     # domain name portion

    
''', re.VERBOSE)



# Get text off clipboard
text = (r''' ''') # Enter copied text or change to file import/open path



# Extract the email/phone from text list
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_number = []
for phone_number in extracted_phone:
    all_phone_number.append(phone_number[0])

print(all_phone_number)
print(extracted_email)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(all_phone_number) + '\n' + '\n'.join(extracted_email)
pyperclip.copy(results)



