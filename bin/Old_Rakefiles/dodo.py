from doit.tools import CmdAction
from glob import glob
import os
from datetime import datetime, date


home = os.getenv('HOME')
format = '%Y-%m-%d'
today = date.today()
today_string = today.strftime(format)
target_date = today + relativedelta(weekday=SU(+1))
sunday = target_date.strftime(format)

DOIT_CONFIG = {'default_tasks': ['archive', 'planning', 'update_sermons_site', 'pdf', 'delete', 'epub', 'meta']}

def task_archive():
    files = glob('????-??-??_s*.md')
    for f in files:
        base = f.split('.')[0]
        date = base[:10]
        year_dir = base[:4]
        if not os.path.exists(year_dir):
            os.makedirs(year_dir)
        if date < today_string:
            yield {
            'name': ' {} ----> archive folder ({})'.format(f, year_dir),
            'actions': ['mv {} {}/{}'.format(f,year_dir,f)]
            }     
        else:
            return

def delete_old(path,extension,folder):
    location = path
    files = glob('{}/*.{}'.format(location,extension))
    for f in files:
        base=os.path.basename(f)
        date = base[:10]
        if date < today_string:
            yield {
            'name': ' Remove {} from {} Folder'.format(base,folder),
            'actions': ['rm {}'.format(f)]
            }


def convert_files(filetype,args,output_path):
    files = glob('*_sermon.md')
    for f in files:
        base = f.split('.')[0]
        date = base[:10]
        if date >= today_string:
        # convert to pdfs
            yield {
            'name': ' {} ----> {}'.format(f,filetype),
            'actions': ['pandoc {0}.md -o {1}{0}.{2} {3}'.format(base, output_path,filetype, args)],
            'targets': ['{}{}.{}'.format(output_path,base,filetype)],
            'file_dep': [f]
            }
        else:
            return

def task_kindle():
    location = home +'/Dropbox/Preaching'
    files = glob('{}/*.epub'.format(location))
    for f in files:
        base=os.path.basename(f)
        date = base[:10]
        if date == sunday:
            return {
            'actions': ['create_kindle {}'.format(f)]
            }

def task_planning():
        return {
                'actions': ['python3 ' + home + '/bin/update_sermons', 
                        'cd ' + home + '/Dropbox/Sermon_Planning_LaTeX/ && pdflatex planning.tex > log.txt',
                        'cp ' + home + '/Dropbox/Sermon_Planning_LaTeX/planning.pdf ' + home + '/Drive/Worship_Arts_Team/Plans/'
                        ]
        }

def task_update_sermons_site():
        return {
                'actions': ['python3 ' + home + '/bin/update_sermons_site']
        }

def task_pdf():
    yield convert_files('pdf','--template sermon_template.tex', home +'/Drive/Worship_Arts_Team/Sermons/')

def task_epub():
    yield convert_files('epub','--epub-stylesheet=' + home + '/Dropbox/Pandoc/Pandoc_Sermon/epub.css --template sermon_epub.html', home + '/Dropbox/Preaching/')

def task_delete():
    yield delete_old(home + '/Drive/Worship_Arts_Team/Sermons','pdf','Sermons')
    yield delete_old(home + '/Dropbox/Preaching','epub','Epub (Preaching)')
    yield delete_old(home + '/Dropbox/Preaching','mobi','Mobi (Preaching)')

def task_meta():
    return {
        'actions': ['python3 ' + home + '/bin/update_meta']
    }
    
