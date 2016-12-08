import dmenu_extended
import sys
import subprocess


file = '/home/wadeallen/Dropbox/books.txt'
with open(file) as my_file:
    books = my_file.readlines()

class extension(dmenu_extended.dmenu):

    # Set the name to appear in the menu
    title = 'Bible'

    # Determines whether to attach the submenu indicator
    is_submenu = False


    # Required function, runs when the user fires the menu item
    def run(self, inputText):

        if inputText != '':
            self.menu('Extra information was passed')
        else:
            passage = self.menu(books)
            if passage == '':
                exit
            else:
                subprocess.call(["surf", "https://www.biblegateway.com/passage/?search={}&version=NIV&interface=print".format(passage)])



        
