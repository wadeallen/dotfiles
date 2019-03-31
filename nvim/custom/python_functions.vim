function! DefPython()
python3 << PYEND
import vim
import subprocess
import sys, os
from os.path import expanduser
import smtplib
sys.path.insert(0,"/home/wadeallen/bin")
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

home = expanduser("~")

curline = vim.current.line
compile_path = home + '/Documents/Preaching/'
desktop = home + '/Documents/Print/'

def python_input(message = 'input'):
  vim.command('call inputsave()')
  vim.command("let user_input = input('" + message + ": ')")
  vim.command('call inputrestore()')
  return vim.eval('user_input')

def Convert_Kindle():
  # Convert file to epub
  output = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.epub'
  # Convert to mobi
  kindle_file = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.mobi'
  subprocess.call("pandoc " + vim.current.buffer.name + " -o " + compile_path + output + " --css=" + home + "/Documents/Pandoc/Pandoc_Sermon/epub.css --template sermon_epub.html", shell=True)
  subprocess.call("kindlegen " + compile_path + output + " > " + home + "/Documents/Preaching/log.txt", shell=True)
  # Email to Kindle
  fromaddr = config.username
  toaddr  = config.kindle
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "Emailed " + output
  body = "This is a scripted email to send file to kindle"
  msg.attach(MIMEText(body, 'plain'))
  body = output + " has been emailed to your Kindle"
  msg.attach(MIMEText(body, 'plain'))
  filename = (kindle_file)
  attachment = open(compile_path + kindle_file, "rb")
  part = MIMEBase('application', 'octet-stream')
  part.set_payload((attachment).read())
  encoders.encode_base64(part)
  part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  msg.attach(part)
  server = smtplib.SMTP("smtp.gmail.com:587")
  server.starttls()
  server.login(config.username,config.password)
  text = msg.as_string()
  server.sendmail(fromaddr, toaddr, text)
  server.quit()
  print (os.path.basename(vim.current.buffer.name) + " has been sent to your Kindle")
  return

def Print_Backup():
  output = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.pdf'
  subprocess.call("pandoc " + vim.current.buffer.name + " -o " + desktop + output + " --template booklet.tex", shell=True)
  print ("Backup Booklet of " + os.path.basename(vim.current.buffer.name) + " is in the Print Folder of Documents")

PYEND
endfunction
call DefPython()

" command! NIV py3 Scripture("NIV")
" command! ESV py3 Scripture("ESV")
" command! KJV py3 Scripture("KJV")
" command! Bi py3 Scripture("NIV")
command! Kindle py3 Convert_Kindle()
command! Backup py3 Print_Backup()


