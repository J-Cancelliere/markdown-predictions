"""Funtions used to clean up data after initial import"""

def replace_commas(text):
    """ Replaces any commas in the input string with a decimal"""
    text = str(text).replace(",",".")
    return text

def remove_comma(text):
    """ Removes any commas in the input string"""
    text = str(text).replace(",","").strip()
    return text

def make_dash_null(text):
    """ Changes the dash (-) to a np.nan"""
    return np.nan if text == "-" else text

def remove_euro(text):
    """ Removes the euro symbol from input text"""
    text = str(text).replace("€","").strip()
    return text

def remove_percent(text):
    """ Removes the percent symbol from input text"""
    text = str(text).replace("%","").strip()
    return text
