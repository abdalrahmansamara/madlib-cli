import re

# goal 0 => create a function that is responsible for all the rendering

def render(route):
    file_content = read_template(route)
    text_in_brackets = parse_template(file_content)
    answers = inputs(text_in_brackets)
    merged_file = merge(answers,file_content,text_in_brackets)
    print(merged_file)

# goal 1 => read the txt file

def read_template(route):
    try:
        with open(route) as file:
            s = file.read()
            return s
    except FileNotFoundError:
        return 'file not found'

# goal 2 => get the curley brackets content

def parse_template(s):
    try:
        s_without_parens = re.sub('\(.+?\)','',s)
        text_in_brackets = re.findall('{(.+?)}',s_without_parens)
        return text_in_brackets
    except:
        return 'an error occured while tracing the curlies'

# goal 3 => ask the user to enter all the inputs and store them in an array

def inputs(text_in_brackets):
    answers = []
    for question in range(len(text_in_brackets)):
        a = input(f'please Enter {text_in_brackets[question]}')
        answers.append(a)
    return answers
    

# goal 4 => concatinate and print
def merge(answers,s,text_in_brackets):
    try:
        for i in range(len(answers)):
            s = s.replace("{"+text_in_brackets[i]+"}",answers[i])
        return s
    except:
        return 'merging error'
route = '../assets/template.txt'
print(render(route))