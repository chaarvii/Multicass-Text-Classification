import re
def remove_emoji(product_detail):
    '''
    Input: Text to be cleaned (String)

    This function removes numeric characters from the text

    Output: String
    '''
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    text_after_removing_emoji = product_detail
    text_after_removing_emoji = emoji_pattern.sub(r'', string)
    return text_after_removing_emoji