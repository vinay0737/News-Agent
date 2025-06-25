
from newsapi import NewsApiClient

# Replace with your actual key
newsapi = NewsApiClient(api_key='04dee33cef7145de8f478844ef342941')

from datetime import datetime

def get_current_year_wrapper() -> int:
    """
    Returns the current year.

    Example:
        >>> get_current_year_wrapper()
        2025
    """
    return datetime.now().year


def get_top_headlines_wrapper(**kwargs):
    """
    Description:
        Use this tool to fetch the latest top news headlines.
        It's ideal when the user wants trending, breaking, or popular news articles 
        filtered by topic, country, language, or specific news sources.

    Parameters:
        q (str, optional): Keywords or phrases to search in the headline.
        sources (str, optional): Comma-separated identifiers of news sources (e.g., "bbc-news,the-verge").
        category (str, optional): News category like "business", "sports", "technology", etc.
        language (str, optional): Language code (e.g., "en" for English").
        country (str, optional): Country code (e.g., "us" for United States").
        pageSize (int, optional): Number of results to return (max 100). Default to 5.
        page (int, optional): Page number for pagination.

    Use When:
        - User asks for "top headlines", "breaking news", or "what’s trending".
        - Request includes a country/category or mentions specific news sources.

    Example:
        "Show me top tech headlines in India"
        → get_top_headlines_wrapper(category="technology", country="in", pageSize=5)
    """
    kwargs.setdefault("pageSize", 5)
    return newsapi.get_top_headlines(**{k: v for k, v in kwargs.items() if v is not None})



def get_sources_wrapper(**kwargs):
    """
    Description:
        Use this tool to get a list of available news sources (publishers, blogs).
        Helpful for identifying the correct `source` ID (e.g., "bbc-news") when users mention specific outlets.

    Parameters:
        category (str, optional): News category such as "business", "sports", "technology".
        language (str, optional): 2-letter ISO language code (e.g., "en" for English).
        country (str, optional): 2-letter ISO country code (e.g., "us" for United States).

    Use When:
        - User asks: "Which sources are available?", "Give me a list of English science publishers."
        - You need to look up the correct `source` ID to use in get_top_headlines_wrapper or get_everything_wrapper.

    Example:
        "Get all English-language tech news sources"
        → get_sources_wrapper(language="en", category="technology")
    """
    return newsapi.get_sources(**{k: v for k, v in kwargs.items() if v is not None})



def get_everything_wrapper(**kwargs):
    """
    Description:
        Use this tool to search and analyze news articles published within the last 5 years 
        from over 150,000 news sources and blogs. Ideal for deep discovery, trend tracking, 
        or keyword-based research across custom timeframes.

    Parameters:
        q (str, optional): Keywords or phrases to search for. 
            - Supports advanced syntax: 
              * "quoted phrases" for exact match
              * +term to require
              * -term to exclude
              * AND / OR / NOT for logical combinations
        searchIn (str, optional): Restrict search to specific fields (comma-separated: title, description, content).
        sources (str, optional): Comma-separated list of source identifiers (max 20). Example: "bbc-news,cnn".
        domains (str, optional): Limit search to specific domains. Example: "nytimes.com,techcrunch.com".
        excludeDomains (str, optional): Exclude results from specific domains.
        from_param (str, optional): Start date in ISO 8601 format (e.g., "2025-06-20").
        to (str, optional): End date in ISO 8601 format (e.g., "2025-06-24").
        language (str, optional): ISO 639-1 language code (e.g., "en" for English).
        sort_by (str, optional): Sort results by:
            - "relevancy": best match to `q`
            - "popularity": most viewed sources first
            - "publishedAt": most recent first
        pageSize (int, optional): Number of articles to return per page. Default is 100. Max is 100.
        page (int, optional): Page number for pagination (default: 1).

    Use When:
        - User asks for articles on a specific topic, trend, or event.
        - Historical, date-filtered, or source-specific results are requested.
        - Research or analytical queries over a broad news dataset.

    Example:
        "Find articles about 'climate change' published on BBC and CNN this month sorted by relevance"
        → q="climate change", sources="bbc-news,cnn", from_param="2025-06-01", to="2025-06-24", sort_by="relevancy", pageSize=5
    """
    return newsapi.get_everything(**{k: v for k, v in kwargs.items() if v is not None})



import dateparser
from datetime import timezone
import pytz

def parse_to_ist_wrapper(text: str) -> str:
    """
    Parses a natural language date/time string into ISO 8601 format in IST.

    Args:
        text (str): A human-readable date/time string like "next Friday at 5 PM" or "tomorrow morning"

    Returns:
        str: Date and time string in ISO 8601 format with IST timezone (e.g., '2025-06-26T17:00:00+05:30')

    Raises:
        ValueError: If the input text cannot be parsed.
    """
    dt = dateparser.parse(text, settings={'TIMEZONE': 'Asia/Kolkata', 'RETURN_AS_TIMEZONE_AWARE': True})

    if not dt:
        raise ValueError(f"Could not parse date from: '{text}'")

    ist_dt = dt.astimezone(pytz.timezone('Asia/Kolkata'))
    return ist_dt.isoformat()

from datetime import datetime
import pytz

def get_current_date_ist() -> str:
    """
    Returns the current date in IST (Indian Standard Time) in ISO 8601 format (YYYY-MM-DD).
    
    Example Output:
        "2025-06-24"
    """
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.now(ist)
    return now_ist.strftime("%Y-%m-%d")