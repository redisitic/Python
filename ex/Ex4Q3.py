import re

txt = """Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams
560-555-5153
806 1st St., Faketown AK 86847
laurawilliams@bogusemail.com"""

phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
matches = phone_regex.findall(txt)
print(matches)