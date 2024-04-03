# now our assignment is gonna be, if tom was born 50 years before year 2035 and he went back to the future 3 years 
# and came back 5 years younger create a format for his age in a flipped format

# 1. Python Regular Expressions Mastery

# Task 1: Code Correction

import re
text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
# emails = re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,}", text)
# errors included missing the begining boundary beacon, missing lower case character identifiers,. missing a backslash for the '.'
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
print(emails)

# 2. Python Regular Expressions Deep Dive

# Task 1: Email Extraction Enhancement


text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
import re

# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)