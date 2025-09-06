import csv, re
from datetime import datetime

SUPPORT_KEYWORDS = ['support','query','request','help']

phone_regex = re.compile(r"(\+?\d[\d\-\s]{7,}\d)")
email_regex = re.compile(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}")

def load_emails_from_csv(path):
    emails = []
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                emails.append({
                    'sender': row.get('sender') or row.get('from') or '',
                    'subject': row.get('subject',''),
                    'body': row.get('body') or row.get('message') or '',
                    'received_at': row.get('received_at') or datetime.now().isoformat(),
                })
    except FileNotFoundError:
        print("CSV not found at", path)
    return [e for e in emails if any(k in e['subject'].lower() for k in SUPPORT_KEYWORDS)]

def simple_extract(email):
    body = email['body']
    phones = phone_regex.findall(body)
    emails = email_regex.findall(body)
    sentiment = 'Neutral'
    if any(w in body.lower() for w in ['not happy','frustrat','angry','upset','cannot','unable','fail']):
        sentiment = 'Negative'
    elif any(w in body.lower() for w in ['thanks','thank you','great','good','appreciate']):
        sentiment = 'Positive'
    return {
        'sender': email['sender'],
        'subject': email['subject'],
        'body': body,
        'received_at': email['received_at'],
        'extracted': {'phones': phones, 'emails': emails},
        'sentiment': sentiment,
        'status': 'pending'
    }

def detect_priority(email_parsed):
    urgent_words = ['immediately','urgent','asap','critical','cannot access','meeting']
    body = (email_parsed.get('body') or '').lower()
    subj = (email_parsed.get('subject') or '').lower()
    if any(w in body for w in urgent_words) or any(w in subj for w in urgent_words):
        return 'Urgent'
    if email_parsed.get('sentiment') == 'Negative':
        return 'Urgent'
    return 'Not urgent'
