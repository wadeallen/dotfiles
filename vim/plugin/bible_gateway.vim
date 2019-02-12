function Bible(...)
  let translation = exists('a:1') ? a:1 : "NIV"
  let scripture = exists('a:2') && a:2 != "" ? a:2 : input("Scripture: ")
  let command = '/usr/bin/scripture "' . scripture . '", ' . translation
  let text = '>('. scripture . ' ' . translation . ') ' . system(command)
  put = text
endfunction

function ReplaceBible(...)
  let line = getline('.')
  let passage = matchstr(line, ">\(\\zs\\w.*\\zeESV\)") 
  let scripture = passage
  let translation = "NIV"
  let command = '/usr/bin/scripture "' . scripture . '", ' . translation
  let text = '>('. scripture . translation . ') ' . system(command)
  " put = getreg('s')
  put = text
endfunction

command! Bi call Bible("NIV")
command! NIV call Bible("NIV")
command! ESV call Bible("ESV")
command! KJV call Bible("KJV")

command! Replace call ReplaceBible("NIV")

