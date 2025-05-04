import imaplib
import email
import yaml
from bs4 import BeautifulSoup


def print_results(subj, fro, body, body_len=200):
    print("___________________________________")
    print("subj: ", subj)
    print("from: ", fro)
    print("BODY SNIPPET: ", body)


def extract_body(msg):
    body = ""
    html = ""

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_dispo = str(part.get("Content-Disposition"))

            if "attachment" in content_dispo:
                continue

            if content_type == "text/plain":
                body = part.get_payload(decode=True).decode(errors="ignore")
            elif content_type == "text/html" and not body:
                html = part.get_payload(decode=True).decode(errors="ignore")
    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain":
            body = msg.get_payload(decode=True).decode(errors="ignore")
        elif content_type == "text/html":
            html = msg.get_payload(decode=True).decode(errors="ignore")
    # print(msg.get_content_type(), msg["from"])
    if body:
        return body
    elif html:
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text(separator=' ', strip=True)

    else:
        return ""
