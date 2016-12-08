" Markdown
autocmd BufNewFile,BufRead *.{md,mkd,mkdn,mark*} set filetype=markdown  
"this is a function that puts vim in writing mode
setlocal formatoptions=1 
setlocal noexpandtab 
map j gj 
map k gk
setlocal spell spelllang=en_us 
set thesaurus+=/Users/wade/.vim/thesaurus/mthesaur.txt
set complete+=s
set formatprg=par
setlocal wrap 
setlocal linebreak 
