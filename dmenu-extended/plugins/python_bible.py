import dmenu_extended
import sys

file = '/home/wadeallen/dotfiles/dmenu-extended/bible_books.json'

class extension(dmenu_extended.dmenu):

    # Set the name to appear in the menu
    title = 'Bible'

    # Determines whether to attach the submenu indicator
    is_submenu = True


    # Required function, runs when the user fires the menu item
    def run(self, inputText):
    	books_json = self.load_json(file)
    	books =[]
    	for b in books_json['sections']:
    		books.append(b['key'])

    	passage = self.menu(books, prompt='Enter passage')
    	passage = passage.replace(" ", "+")
    	self.open_url(f"https://netbible.org/bible/{passage}")
