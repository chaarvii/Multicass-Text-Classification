import re
def remove_numbers(product_detail: str):
    '''
            This function removes numeric characters from the text
            Arguments:
            product_detail: String contating product details and labels. 
            It assumes that the input is according to fasttext format

            Output:
            cleaned string in fasttext format
    '''
    text_after_removing_numbers = re.sub(r"\b[0-9]+\b\s*", "",product_detail)
    return text_after_removing_numbers
