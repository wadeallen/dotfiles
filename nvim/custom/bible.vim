function Bible(...)
  let scripture = exists('a:2') && a:2 != "" ? a:2 : input("Scripture: ")
  let command = '/home/wadeallen/bin/scripture -p ' . scripture
  let text = system(command)
  put = text
endfunction

command! Bi call Bible()

