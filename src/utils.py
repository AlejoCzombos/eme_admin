from urllib.parse import urlparse, urlunparse

def remove_query_params(url: str) -> str:
    parsed_url = urlparse(url)
    clean_url = urlunparse(parsed_url._replace(query=""))
    return clean_url