function! DefPython()
python << PYEND
import vim
import subprocess
import sys, os
from os.path import expanduser
import smtplib
import /home/wadeallen/bin/config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

home = expanduser("~")

curline = vim.current.line
compile_path = home + '/Dropbox/Preaching/'
desktop = home + '/Desktop/'  

def python_input(message = 'input'):
  vim.command('call inputsave()')
  vim.command("let user_input = input('" + message + ": ')")
  vim.command('call inputrestore()')
  return vim.eval('user_input')

def Scripture(version):
  text = python_input('Passage')
  passage = subprocess.check_output('/home/wadeallen/.rvm/gems/ruby-2.3.0/bin/scripture "' + text + '", ' + version, shell=True)
  vim.current.line = curline + '>(' + text + ' ' + version + ') ' + passage

def Convert_Kindle():
  # Convert file to epub
  output = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.epub'
  # Convert to mobi
  kindle_file = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.mobi'
  subprocess.call("pandoc " + vim.current.buffer.name + " -o " + compile_path + output + " --epub-stylesheet=" + home + "/Dropbox/Pandoc/Pandoc_Sermon/epub.css --template sermon_epub.html", shell=True) 
  subprocess.call("kindlegen " + compile_path + output + " > " + home + "/Dropbox/Preaching/log.txt", shell=True)
  # Email to Kindle

  print (os.path.basename(vim.current.buffer.name) + " has been sent to your Kindle")
  return

def Print_Backup():
  output = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.pdf'
  subprocess.call("pandoc " + vim.current.buffer.name + " -o " + desktop + output + " --template booklet.tex", shell=True)
  print ("Backup Booklet of " + os.path.basename(vim.current.buffer.name) + " is on the Desktop")

PYEND
endfunction
call DefPython()

" command! NIV py3 Scripture("NIV")
" command! ESV py3 Scripture("ESV")
" command! KJV py3 Scripture("KJV")
" command! Bi py3 Scripture("NIV")
command! Kindle py Convert_Kindle()
command! Backup py Print_Backup()


