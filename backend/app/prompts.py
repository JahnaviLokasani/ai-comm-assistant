TEMPLATE_EXTRACT_JSON = '''
Extract JSON with fields: contact_phone, contact_email, product, requested_action, urgency_words, sentiment.
Return only valid JSON.
'''

TEMPLATE_REPLY = '''
SYSTEM: You are a professional and empathetic customer support assistant.
INSTRUCTIONS: Use the KB snippets provided. Acknowledge feelings, give clear steps, reference product if available.

Customer email:
{email_text}

KB snippets:
{kb}

Return a JSON with: subject, reply_body, confidence_score (0-1).
'''
