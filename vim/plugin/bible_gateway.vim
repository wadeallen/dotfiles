function Bible(...)
  let translation = exists('a:1') ? a:1 : "NIV"
  let scripture = exists('a:2') && a:2 != "" ? a:2 : input("Scripture: ")
  let command = '/home/wadeallen/.rbenv/shims/scripture "' . scripture . '", ' . translation
  let text = '>('. scripture . ' ' . translation . ') ' . system(command)
  put = text
endfunction

command! Bi call Bible("NIV")
command! NIV call Bible("NIV")
command! ESV call Bible("ESV")
command! KJV call Bible("KJV")


