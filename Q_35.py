# program to remove punctuations from strings

# program to remove punctuations from strings

def remove_punctuations(input_string):
    # Define a string of punctuations
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # Remove punctuations from the input string
    result = ''.join(char for char in input_string if char not in punctuations)
    return result

# Example usage
input_string = "Hello, World! How's it going?"
cleaned_string = remove_punctuations(input_string)
print("Original String:", input_string)
print("String without Punctuations:", cleaned_string)