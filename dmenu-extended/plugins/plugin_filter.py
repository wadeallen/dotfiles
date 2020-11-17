import dmenu_extended
import sys
import os
import codecs
import locale

file_prefs = dmenu_extended.path_prefs + '/dmenu_fliter.json'

class extension(dmenu_extended.dmenu):

    title = 'Filters'
    is_submenu = True


    def create_default_filters(self):
        default = {
            'Documents': ['pdf', 'txt', 'html', 'md', 'ps'],
            'Office': ['odf', 'ods', 'doc', 'docx', 'xls', 'xlsx'],
            'Pictures': ['svg', 'png', 'jpg', 'gif', 'xcf'],
            'Media': ['mp3', 'mp4', 'avi', 'm4a', 'ogg'],
            'Archives': ['zip', 'tar', '7z', 'gz'],
            'Source files': ['php', 'py'],
        }
        self.save_json(file_prefs, default)
        return default


    def load_filters(self):
        filters = self.load_json(file_prefs)
        if filters == False:
            filters = self.create_default_filters()
        return filters


    def run(self, inputText):

        self.filters = self.load_filters()

        items = []
        for filter in self.filters:
            items.append(filter)

        item_editPrefs = self.prefs['indicator_edit'] + ' Edit filters'
        items.append(item_editPrefs)

        text = (inputText + ' Select filter:') if inputText else 'Select filter:'
        filter = self.menu(items, prompt=text)

        if filter == item_editPrefs:
            return self.open_file(file_prefs)
        elif filter == '':
            return sys.exit()
        elif filter not in items:
            return sys.exit()

        items = []
        path = self.cache_dir + '/dmenuExtended_files.txt'
        with codecs.open(path,'r',encoding=locale.getpreferredencoding()) as f:
            for line in f:
                fname = line[:-1]
                if os.path.splitext(fname)[1][1:] in self.filters[filter]:
                    items.append(fname)

        if not items:
            return self.run('No files.')

        selected = self.menu(items, prompt='Select file:')
        if selected in items:
            self.open_file(selected)

