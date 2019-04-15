syntax on
set number
set wrap
set linebreak

"spell check in markdown files only
autocmd BufRead,BufNewFile *.md,*.markdown setlocal spell spelllang=en_us

"make clipboard work
set clipboard+=unnamedplus

"this will add new line without insert mode
nmap <S-Enter> O<Esc>j
nmap <CR> o<Esc>k

"for Ledger program
au BufNewFile,BufRead *.ldg,*.ledger setf ledger 
nmap <leader>2 010li<Space>*<Esc>
nnoremap <leader>d "=strftime("%Y/%m/%d")<CR>PA<Space><Space>
nnoremap <leader>nt G"=strftime("%Y/%m/%d")<CR>PA<Space><Space>
