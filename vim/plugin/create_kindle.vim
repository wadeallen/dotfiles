function Create_Kindle(...)
  let file_path = expand('%:p')
  let home = '/home/wadeallen/'
  let compile_path = home . 'Documents/Preaching/'
  let file_name = expand('%:t:r')
  let command = '/usr/bin/pandoc ' . file_path . ' -o ' . compile_path . file_name . '.epub --epub-stylesheet=' . home . '/Documents/Pandoc/Pandoc_Sermon/epub.css --template sermon_epub.html'
  execute system(command)
  echom file_name . ' Kindle version created'
endfunction
