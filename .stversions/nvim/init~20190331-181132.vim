" Wade Allen nvim config file

call plug#begin('~/.config/nvim/plugged')
Plug 'tpope/vim-surround'
Plug 'junegunn/goyo.vim'
Plug 'PotatoesMaster/i3-vim-syntax'
Plug 'tpope/vim-commentary'
Plug 'ron89/thesaurus_query.vim'
Plug 'panozzaj/vim-autocorrect'
Plug 'vim-pandoc/vim-pandoc-syntax'
Plug 'SirVer/ultisnips'
Plug 'ledger/vim-ledger'
Plug 'junegunn/fzf.vim'
call plug#end()

set bg=light
set go=a
set mouse=a
set nohlsearch
set clipboard=unnamedplus

" Some basics:
	nnoremap c "_c
	set nocompatible
	filetype plugin on
	syntax on
	set encoding=utf-8
	set number relativenumber

" Enable autocompletion:
	set wildmode=longest,list,full

" Disables automatic commenting on newline:
	autocmd FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o

" Goyo plugin makes text more readable when writing prose:
	map <leader>f :Goyo \| set bg=light \| set linebreak<CR>

" Spell-check set to <leader>o, 'o' for 'orthography':
	map <leader>o :setlocal spell! spelllang=en_us<CR>

"spell check in markdown files only
    	autocmd BufRead,BufNewFile *.md,*.markdown setlocal spell spelllang=en_us

" set spell check
	hi clear SpellBad
	hi SpellBad cterm=underline

" set color scheme
colorscheme badwolf

" Splits open at the bottom and right, which is non-retarded, unlike vim defaults.
	set splitbelow splitright

" Shortcutting split navigation, saving a keypress:
	map <C-h> <C-w>h
	map <C-j> <C-w>j
	map <C-k> <C-w>k
	map <C-l> <C-w>l

" Replace all is aliased to S.
	nnoremap S :%s//g<Left><Left>

" Compile document, be it groff/LaTeX/markdown/etc.
	map <leader>c :w! \| !compiler <c-r>%<CR>

" Open corresponding .pdf/.html or preview
	map <leader>p :!opout <c-r>%<CR><CR>

"setup markdown files and tex files
	autocmd BufNewFile,BufFilePre,BufRead *.md,*.markdown set filetype=markdown.pandoc
	autocmd BufRead,BufNewFile *.tex set filetype=tex

" Copy selected text to system clipboard (requires gvim/nvim/vim-x11 installed):
	vnoremap <C-c> "+y
	map <C-p> "+P

" Enable Goyo by default for mutt writting
	" Goyo's width will be the line limit in mutt.
	autocmd BufRead,BufNewFile /tmp/neomutt* let g:goyo_width=80
	autocmd BufRead,BufNewFile /tmp/neomutt* :Goyo \| set bg=light

" Automatically deletes all trailing whitespace on save.
	autocmd BufWritePre * %s/\s\+$//e

" When shortcut files are updated, renew bash and ranger configs with new material:
	autocmd BufWritePost ~/.config/bmdirs,~/.config/bmfiles !shortcuts

" Run xrdb whenever Xdefaults or Xresources are updated.
	autocmd BufWritePost *Xresources,*Xdefaults !xrdb %

" Navigating with guides
	inoremap <leader><leader> <Esc>/<++><Enter>"_c4l
	vnoremap <leader><leader> <Esc>/<++><Enter>"_c4l
	map <leader><leader> <Esc>/<++><Enter>"_c4l


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
source $HOME/.config/nvim/custom/bible_gateway.vim

"for thesaurus plugin
nnoremap <LocalLeader>th :ThesaurusQueryReplaceCurrentWord<CR>
vnoremap <LocalLeader>th y:Thesaurus <C-r>"<CR>
let g:tq_enabled_backends=["thesaurus_com","openoffice_en","mthesaur_txt"]

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

"for Ledger program
au BufNewFile,BufRead *.ldg,*.ledger setf ledger
nmap <leader>2 010li<Space>*<Esc>
nnoremap <leader>d "=strftime("%Y/%m/%d")<CR>PA<Space><Space>
nnoremap <leader>nt G"=strftime("%Y/%m/%d")<CR>PA<Space><Space>

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
