import re
from string import punctuation
def clean_text(product_detail : str,remove_html_tag : bool):
    '''
            This function performs the following tasks 
            1. Removes hyperlinks
            2. Converts to lowercase
            3. Removes punctuation 
            4. Removes html tags (optional)
            Arguments: 
            product_detail: String contating product details and labels. 
            It assumes that the input is according to fasttext format.
            remove_html_tag: boolean value, if True  removes html tags 
            from the text

            Output:
            cleaned string in fasttext format
    '''

    #cleaning the text 
    cleanedText = re.sub(r"https?://\S+", "",product_detail)
    cleanedText = cleanedText.lower()
    cleanedText = re.sub(f"[{re.escape(punctuation)}]", "", cleanedText)
    cleanedText = " ".join(cleanedText.split())

    if remove_html_tag:
        cleanedText = re.sub(r"<.*?>", " ",cleanedText)

    return cleanedText
