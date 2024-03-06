# #1
import re
pattern = re.compile("^a(b*)$")
n=input("Enter the text: ")
print (pattern.search(n))

#2
import re
pattern = re.compile("^a(b{2,3})$")
n=input("Enter the text: ")
print (pattern.search(n))

#3
import re

def find_sequences(text):
    pattern = r'\b[\w]+_[\w]+\b'
    return re.findall(pattern, text)

text = input("Enter the text: ")
sequences = find_sequences(text)
print(sequences)

4
import re
pattern = re.compile("^a([A-Za-z]*)b$")
n=input("Enter the text: ")
print (pattern.search(n))

#5
import re

def match_pattern(string):
    pattern = r'a.*b$'
    if re.match(pattern, string):
        return True
    else:
        return False

test_string = input()
print(match_pattern(test_string))  


#6
def replace_characters(string):
    return string.replace(' ', ':').replace(',', ':').replace('.', ':')

test_string =input()
print(replace_characters(test_string))

#7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

test_string = input()
print(snake_to_camel(test_string))  

#8
def split_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)

test_string = input()
print(split_at_uppercase(test_string)) 

#9
def insert_spaces(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)

test_string = input()
print(insert_spaces(test_string))  

#10
def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

test_string = "convertThisCamelCaseStringToSnakeCase"
print(camel_to_snake(test_string)) 