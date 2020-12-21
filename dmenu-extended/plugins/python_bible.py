import dmenu_extended
import sys
import requests
import webbrowser
import i3

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
    	book = passage.split(':')[0]

    	bible_url=(f"https://netbible.org/bible/{passage}")
    	ew_url=(f"about:reader?url=https://enduringword.com/bible-commentary/{book}")

    	i3.msg("command", f"workspace 7: ❼ Bible; exec firefox -new-window {bible_url}")
    	# i3.msg("command", f"workspace 7: ❼ Bible; exec firefox {ew_url}")


    	# webbrowser.open_new(f"{ew_url}")


    	# self.open_url(f"https://netbible.org/bible/{passage}")
        # self.open_url(f"about:reader?url=https://enduringword.com/bible-commentary/{book}")
