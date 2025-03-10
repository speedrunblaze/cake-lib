import requests

CMS_PATTERNS = {
    "WordPress": "/wp-content/",
    "Joomla": "/administrator/",
    "Drupal": "/sites/default/",
}

def get_cms(url):
    for cms, pattern in CMS_PATTERNS.items():
        response = requests.get(url + pattern)
        if response.status_code == 200:
            return cms
    return "Unknown"
