syntax on
set number
set wrap
set linebreak

"spell check in markdown files only
autocmd BufRead,BufNewFile *.md,*.markdown setlocal spell spelllang=en_us

"map keys for easy exit
inoremap jj <Esc>
noremap qq :wq<CR>

"install plugins
call plug#begin('~/.config/nvim/plugged')
Plug 'ron89/thesaurus_query.vim'
Plug 'panozzaj/vim-autocorrect'
Plug 'vim-pandoc/vim-pandoc-syntax'
call plug#end()

"setup markdown files
autocmd BufNewFile,BufFilePre,BufRead *.md,*.markdown set filetype=markdown.pandoc

" Auto Capitalize Sentences
augroup SENTENCES
      au!
        autocmd InsertCharPre * if search('\v(%^|[.!?]\_s+|\_^\-\s|\_^title\:\s|\n\n)%#', 'bcnw') != 0 | let v:char = toupper(v:char) | endif
      augroup END

"make clipboard work
set clipboard+=unnamedplus

"for thesaurus plugin
nnoremap <LocalLeader>th :ThesaurusQueryReplaceCurrentWord<CR>
vnoremap <LocalLeader>th y:Thesaurus <C-r>"<CR>
let g:tq_enabled_backends=["thesaurus_com","openoffice_en","mthesaur_txt"]

"this will add new line without insert mode
nmap <S-Enter> O<Esc>j
nmap <CR> o<Esc>k

source $HOME/.config/nvim/custom/bible_gateway.vim
source $HOME/.config/nvim/custom/python_functions.vim

"I am adding the following content to display word count in status bar
let g:word_count="<unknown>"
function! WordCount()
    return g:word_count
endfunction
function! UpdateWordCount()
     let lnum = 1
     let n = 0
       while lnum <= line('$')
            let n = n + len(split(getline(lnum)))
            let lnum = lnum + 1
       endwhile
    let g:word_count = n
endfunction

" Update the count when cursor is idle in command or insert mode.
" " Update when idle for 1000 msec (default is 4000 msec).
set updatetime=1000
augroup WordCounter
    au! CursorHold,CursorHoldI * call UpdateWordCount()
augroup END
" Set statusline, shown here a piece at a time
highlight User1 ctermbg=green guibg=green ctermfg=black guifg=black
set statusline=%1*      " Switch to User1 color highlight
set statusline+=%<%F      " file name, cut if needed at start
set statusline+=%M      " modified flag
set statusline+=%y      " file type
set statusline+=%=      " separator from left to right justified
set statusline+=\ %{strftime('%a\ %b\ %e\ %I:%M\ %p')},
set statusline+=\ %{WordCount()}\ words,
set statusline+=\ %l/%L\ lines,\ %P " percentage through the file
"------------------------------------------------------------
"
