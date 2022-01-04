# Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.


class Textfile_proc:

    """
    performs statistical processing of a text file
    - counting characters, words, sentences
    """

    def __init__(self, file_name: str):

        self.f1 = open(file_name, 'r')
        self.st = self.f1.read()
        self.f1.close()

    def char_count(self):
        return len(self.st.replace(' ', ''))

    def word_count(self):
        return len(self.st.split())

    def sentense_count(self):
        res = self.st.replace('!', '.')
        res = res.replace('?', '.')
        return len(res.split('.'))-1

    def __str__(self):
        return self.st


if __name__ == '__main__':
        try:
            f = (Textfile_proc('test.txt'))
            print(f)
            print(f.char_count())
            print(f.word_count())
            print(f.sentense_count())
        except Exception as error:
            print(error)

