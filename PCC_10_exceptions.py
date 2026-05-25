""" Python Crash Course. Chapter 10. Exceptions"""
#Standard imports
import chardet

#Local imports
from PCC_input_functions import getuserint

# 10-6 Sum \ 10-7 Calculator


programname = '"Summer"'
prompt = ("Enter two numbers to get their sum.\nEnter 'q' anytime to quit.")
prompt_num1 = ("Enter first number: ")
prompt_num2 = ("Enter second number: ")





                 
while True:
    print(prompt)
    input1 = getuserint(prompt_num1)
    if input1 is None:
        break
    input2 = getuserint(prompt_num2)
    if input2 is None:
        break
    else:
        result = input1 + input2
        print(f"Sum of {input1} and {input2} equals to {result}\n\n")
print(f'Thanks for using {programname}. Goodbye.')

#10-8 10-9 Cats and dogs
          
filenames = ['cats.txt', 'dogs.txt']

def output_text_file(file):
    """Outputs a file contents into strings"""
    try:
        with open(file) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
#        print(f"File {file} not Found.")
        pass
    else:
        print(f"\nHere's a contents of {file}:")
        for line in lines:
            print(line.rstrip())

for file in filenames:
    output_text_file(file)



#10-10 Often words

filenames = ['crime_and_punishment.txt', 'frankenstein.txt', 'moby_dick.txt']
searchword = 'the'

def detect_encoding(file):
    """Detect file encoding"""
    with open(file, 'rb') as f_obj:
        raw_data = f_obj.read(10000)  # читаем первые 10KB для определения
        result = chardet.detect(raw_data)
        return result['encoding']

def read_text_file(file):
    """Reads text file and returns it's contents to a single sting"""
    try:
        encoding = detect_encoding(file)
        print(encoding)
        with open(file, 'r', encoding=encoding, errors='ignore') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        return None
    else:
        return(contents)
    
for file in filenames:
    contents = read_text_file(file)
    if file is None:
        print(f'File {file} not found')
    else:
       num = contents.lower().count(searchword)
       print(f'Word "{searchword}" appears {num} times in {file}')