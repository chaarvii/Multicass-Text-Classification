import re
def remove_numbers(product_detail):
    '''
    Input: Text to be cleaned (String)

    This function removes numeric characters from the text

    Output: String
    '''
    text_after_removing_numbers = re.sub(r"\b[0-9]+\b\s*", "",product_detail)
    return text_after_removing_numbers