import re
from string import punctuation
def clean_text(product_detail,remove_html_tag):
    '''
    Input: text to be cleaned (String), option to remove html tags (Boolean)

    This function performs the following tasks 
    1. Removes hyperlinks
    2. Converts to lowercase
    3. Removes punctuation 
    4. Removes html tags (optional)

    Output: String
    '''
    cleanedText = re.sub(r"https?://\S+", "",product_detail)
    cleanedText = cleanedText.lower()
    cleanedText = re.sub(f"[{re.escape(punctuation)}]", "", cleanedText)
    cleanedText = " ".join(cleanedText.split())

    if remove_html_tag:
        cleanedText = re.sub(r"<.*?>", " ",cleanedText)

    return cleanedText
