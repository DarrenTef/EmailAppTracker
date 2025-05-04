# import imaplib
# import email
# import yaml
# import helpers as helpers

def lambda_handler(event, context):
    message = 'Hello {} !'.format(event['key1'])
    return {
        'message': message
    }

# with open("config.yml") as f:
#     content = f.read()


# my_credentials = yaml.load(content, Loader=yaml.FullLoader)

# user, password = my_credentials["user"], my_credentials["password"]

# # URL for IMAP connection
# imap_url = "imap.gmail.com"

# # Connect with gmail using ssl
# my_mail = imaplib.IMAP4_SSL(imap_url)

# # Login using credentials
# my_mail.login(user, password)

# # Select your inbox to fetch msgs
# my_mail.select("Inbox")

# # key = "(SINCE 28-Apr-2025)"
# # value = "do-not-reply@pike13.com"

# _, since_data = my_mail.search(None, "(SINCE 28-Apr-2025)")
# _, from_data = my_mail.search(
#     None, '(FROM "indeedapply@indeed.com" SINCE 28-Apr-2025)'
# )
# combined_ids = set(since_data[0].split()) | set(from_data[0].split())
# mail_id_list = list(combined_ids)
# # IDs of all emails that we want to fetch
# # mail_id_list = data[0].split()
# # print(mail_id_list)
# msgs = []
# for num in mail_id_list:
#     typ, data = my_mail.fetch(num, '(RFC822)')
#     msgs.append(data)
# # 14:00

# for msg in msgs:
#     for response_part in msg:
#         if type(response_part) is tuple:
#             my_msg = email.message_from_bytes((response_part[1]))
#             subj, fro, body = my_msg['subject'], my_msg['from'], ""
#             if "application submitted" not in (subj or "").lower():
#                 body = helpers.extract_body(my_msg)
#                 if "Indeed Application:" in subj or "application submitted" in body.lower():
#                     helpers.print_results(subj, fro, body)
#             else:
#                 helpers.print_results(subj, fro, body)
