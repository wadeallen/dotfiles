function Bible(...)
  let translation = exists('a:1') ? a:1 : "NIV"
  let scripture = exists('a:2') && a:2 != "" ? a:2 : input("Scripture: ")
  let command = '/home/wadeallen/bin/scripture -p ' . scripture . ' -v ' . translation 
  let text = system(command)
  put = text
  
endfunction

command! NIV call Bible("NIV")
command! ESV call Bible("ESV")
command! MSG call Bible("MSG")
command! NLT call Bible("NLT")
command! NTE call Bible("NTE")

