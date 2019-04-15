syntax on
set number
set wrap
set linebreak

"spell check in markdown files only
autocmd BufRead,BufNewFile *.md,*.markdown setlocal spell spelllang=en_us

"make clipboard work
set clipboard+=unnamedplus
