from datetime import datetime, timedelta
from models import db, ShortURL
from utils.helpers import generate_short_code

def create_short_url(original_url, expiry_days=None):
    short_code = generate_short_code()
    expires_at = None

    if expiry_days:
        expires_at = datetime.utcnow() + timedelta(days=expiry_days)

    url = ShortURL(
        original_url=original_url,
        short_code=short_code,
        expires_at=expires_at
    )

    db.session.add(url)
    db.session.commit()
    return url

def process_redirect(url):
    url.click_count += 1
    url.last_accessed_at = datetime.utcnow()
    db.session.commit()
