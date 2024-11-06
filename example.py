# Create a list for our placeholders
placeholders = ['NOUN', 'VERB_ING', 'ADJECTIVE']

# Create a function that reads files line by line
def read_files(filename):
    file = open(filename, 'r')

    text = ''
    for line in file:
        text = text + process_line(line)

    file.close()
    return text

# Create a functions that processes each line to spot a placeholder and prompt the user
def process_line(line):
    global placeholders # mark the place holder variable

    processed_line = ''
    words = line.split()

    for word in words:
        stripped = word.strip(',?,!,;.')
        if stripped in placeholders:
            answer = input(f"Enter a {stripped}: ")
            processed_line = processed_line + answer + ' '
            if word[-1] in ',?;.':
                processed_line = processed_line + word[-1] + ' '
            else:
                processed_line + ' '
        else:
            processed_line = processed_line + word + ' '

    return processed_line + '\n'



# Create a functions that calls the other functions reading a particular file
def main():
    file = read_files('files/lib.txt')
    print(file)

if __name__ == '__main__':
    main()
