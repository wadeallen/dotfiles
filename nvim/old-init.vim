syntax on

"install plugins
call plug#begin('~/.config/nvim/plugged')
Plug 'ron89/thesaurus_query.vim'
Plug 'panozzaj/vim-autocorrect'
Plug 'vim-pandoc/vim-pandoc-syntax'
Plug 'tpope/vim-commentary'
Plug 'reedes/vim-wordy'
Plug 'ledger/vim-ledger'
Plug 'jiangmiao/auto-pairs'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
call plug#end()

"custom plugins
source $HOME/.config/nvim/custom/python_functions.vim
source $HOME/.config/nvim/custom/bible_gateway.vim

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

"------------------------------------------------------------
"adding shortcut to make verse slide
nmap <leader>ms 0di(o<Esc>P0i*<Esc>A*<Esc>k0xxxo<Esc>jj
"------------------------------------------------------------
"added line to copy summary and verse
"noremap <leader>cs 0lvi"y
noremap <leader>cv 0lv$y
"------------------------------------------------------------

"map keys for easy exit
inoremap jj <Esc>
noremap qq :wq<CR>

"setup markdown files
autocmd BufNewFile,BufFilePre,BufRead *.md,*.markdown set filetype=markdown.pandoc

"call autocorrect on markdown files
autocmd filetype pandoc.markdown call AutoCorrect()

" Auto Capitalize Sentences
augroup SENTENCES
      au!
        autocmd InsertCharPre * if search('\v(%^|[.!?]\_s+|\_^\-\s|\_^title\:\s|\n\n)%#', 'bcnw') != 0 | let v:char = toupper(v:char) | endif
      augroup END

"for thesaurus plugin
nnoremap <LocalLeader>th :ThesaurusQueryReplaceCurrentWord<CR>
vnoremap <LocalLeader>th y:Thesaurus <C-r>"<CR>
let g:tq_enabled_backends=["thesaurus_com","openoffice_en","mthesaur_txt"]

set wrap linebreak nolist
" nnoremap j gj
" vnoremap j gj
" onoremap j gj
" nnoremap k gk
" vnoremap k gk
" onoremap k gk
" nnoremap 0 g0
" nnoremap $ g$

"set up dictionary
" set dictionary+=/home/wadeallen/Downloads/hunspell-en_US-2018.04.16/en_US.dic
" set complete+=k

"spell
hi clear SpellBad
hi SpellBad cterm=underline



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
abbrev i I
abbrev hhs Holy Spirit
abbrev jesus Jesus
abbrev paul Paul
abbrev peter Peter
abbrev john John

" autopairs
let g:AutoPairsMapCR=0

"Ultisnips
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"
let g:UltiSnipsSnippetsDir=$HOME."/.config/nvim/Snippets"
let g:UltiSnipsSnippetDirectories = ['Snippets']
let g:UltiSnipsEditSplit="vertical"
