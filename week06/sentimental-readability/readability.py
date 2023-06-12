def main():

    text = str(input('Text: '))
    count(text)

def count(text):

    letters = 0
    words = 1
    sentences = 0
    result = 0

    for i in text:
        if i.isalpha():
            letters += 1

        elif i == ' ':
            words += 1

        elif i == '.' or i == '?' or i == '!':
            sentences += 1

    l = average_number_of_letters(letters, words)
    s = average_number_of_sentences(sentences, words)

    result = round(0.0588 * l - 0.296 * s - 15.8)
    grade(result)


def average_number_of_letters(letters, words):
    l = letters / words * 100
    return l

def average_number_of_sentences(sentences, words):
    s = sentences / words * 100
    return s

def grade(result):
    if result < 1:
        print('Before Grade 1')

    elif result > 16:
        print('Grade 16+')

    else:
        print(f'Grade {result}')

if __name__ == '__main__':
    main()