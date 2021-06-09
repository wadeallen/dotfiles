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
print_folder = home + '/Print/'
output_pdf = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.pdf'
pandoc_print = f"pandoc -s {vim.current.buffer.name} -o {print_folder}{output_pdf} --template booklet.tex --pdf-engine=xelatex"
output_epub = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.epub'
kindle_file = os.path.splitext(os.path.basename(vim.current.buffer.name))[0]+'.mobi'
pandoc_epub = f"pandoc {vim.current.buffer.name} -o {compile_path}{output_epub} --css={home}/Documents/Pandoc/Pandoc_Sermon/epub.css --template sermon_epub.html"

def python_input(message = 'input'):

  vim.command("let user_input = input('" + message + ": ')")
  vim.command('call inputrestore()')
  return vim.eval('user_input')

def Convert_Kindle():
  subprocess.call(pandoc_epub, shell=True)
  subprocess.call(f"kindlegen {compile_path}{output_epub} > {home}/Documents/Preaching/log.txt", shell=True)
  # Email to Kindle
  fromaddr = config.username
  toaddr  = config.kindle
  msg = MIMEMultipart()
  msg['From'] = fromaddr
  msg['To'] = toaddr
  msg['Subject'] = "Emailed " + output_epub
  body = "This is a scripted email to send file to kindle"
  msg.attach(MIMEText(body, 'plain'))
  body = output_epub + " has been emailed to your Kindle"
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
  subprocess.call(pandoc_print, shell=True)
  print ("Backup Booklet of " + os.path.basename(vim.current.buffer.name) + " is in the Print Folder of Documents")
  return

def Test():
  print(pandoc_print)

PYEND
endfunction
call DefPython()

command! Kindle py3 Convert_Kindle()
command! Backup py3 Print_Backup()
command! Test py3 Test()
