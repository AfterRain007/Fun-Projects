import re

def find_screenshot(text):
    pattern = r'eos'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches

# Example usage:
text = "eospadkn"
matches = find_screenshot(text)
print(matches)