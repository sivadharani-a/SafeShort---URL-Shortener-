import re

def is_valid_url(url):
    pattern = re.compile(
        r'^(http|https)://[^\s/$.?#].[^\s]*$', re.IGNORECASE
    )
    return re.match(pattern, url) is not None
