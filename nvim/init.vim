" Wade Allen nvim config file

call plug#begin('~/.config/nvim/plugged')
Plug 'tpope/vim-commentary'
Plug 'ron89/thesaurus_query.vim'
Plug 'panozzaj/vim-autocorrect'
Plug 'vim-pandoc/vim-pandoc-syntax'
Plug 'SirVer/ultisnips'
Plug 'ledger/vim-ledger'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'
Plug '907th/vim-auto-save'
Plug 'SidOfc/mkdx'
Plug 'vim-scripts/loremipsum'
call plug#end()

set bg=light
set go=a
set mouse=a
set nohlsearch
set linebreak
set clipboard=unnamedplus

"includes - inside of word
augroup markdown
    autocmd!
    " Include dash in 'word'
    autocmd FileType markdown setlocal iskeyword+=-
augroup END

let g:auto_save = 1  " enable AutoSave on Vim startup

" Some basics:
	nnoremap c "_c
	set nocompatible
	filetype plugin on
	syntax on
	set encoding=utf-8
	set number relativenumber

" Enable autocompletion:
	set wildmode=longest,list,full

"spell check in markdown files only
    	autocmd BufRead,BufNewFile *.md,*.markdown setlocal spell spelllang=en_us

" set spell check
	hi clear SpellBad
	hi SpellBad cterm=underline

" set color scheme
colorscheme badwolf
" colorscheme nord
hi Normal ctermbg=none
hi NonText ctermbg=none
hi LineNr ctermbg=none

" Replace all is aliased to S.
	nnoremap S :%s//g<Left><Left>

"setup markdown files and tex files
	autocmd BufNewFile,BufFilePre,BufRead *.md,*.markdown set filetype=markdown.pandoc
	autocmd BufRead,BufNewFile *.tex set filetype=tex

"adding shortcut to make verse slide
        nmap <leader>ms 0di(o<Esc>P0i*<Esc>A*<Esc>k0xxxo<Esc>jj

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


"custom plugins
source $HOME/.config/nvim/custom/python_functions.vim
source $HOME/.config/nvim/custom/bible.vim

"for thesaurus plugin
nnoremap <LocalLeader>fw :ThesaurusQueryReplaceCurrentWord<CR>
vnoremap <LocalLeader>fw y:Thesaurus <C-r>"<CR>
let tq_enabled_backends=["thesaurus_com", "openoffice_en", "datamuse_com", "mthesaur_txt"]

" Auto Capitalize Sentences
augroup SENTENCES
      au!
        autocmd InsertCharPre * if search('\v(%^|[.!?]\_s+|\_^\-\s|\_^title\:\s|\n\n)%#', 'bcnw') != 0 | let v:char = toupper(v:char) | endif
      augroup END

" Abbreviations
abbrev i I
abbrev hhs Holy Spirit
abbrev jesus Jesus
abbrev paul Paul
abbrev peter Peter
abbrev john John
abbrev sotm Sermon on the Mount

"for Ledger program
au BufNewFile,BufRead *.ldg,*.ledger setf ledger
nmap <leader>2 010li<Space>*<Esc>
nnoremap <leader>d "=strftime("%Y/%m/%d")<CR>PA<Space><Space>
nnoremap <leader>nt G"=strftime("%Y/%m/%d")<CR>PA<Space><Space>

"for editing sermons files
noremap 99 i---<Esc>
noremap <leader>cv 0llv$y

"this will add new line without insert mode
nmap <S-Enter> O<Esc>j
nmap <CR> o<Esc>k

"Ultisnips
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="<s-tab>"
let g:UltiSnipsSnippetsDir=$HOME."/.config/nvim/Snippets"
let g:UltiSnipsSnippetDirectories = ['Snippets']
let g:UltiSnipsEditSplit="vertical"

"Move keys inside of paragraphs
nnoremap j gj
nnoremap k gk

"Settings for mkdx
