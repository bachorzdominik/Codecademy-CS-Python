import csv
import json
compromised_users = []

with open('text-files/passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
      compromised_users.append(password_row['Username'])

with open('text-files/compromised-users.txt', 'w') as compromised_user_file:
  for username in compromised_users:
    compromised_user_file.write(username + '\n')


with open('text-files/boss-message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

with open('text-files/new-passwords.csv', 'w') as new_passwords:
  slash_null_sig = r'''
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

'''
  new_passwords.write(slash_null_sig)
