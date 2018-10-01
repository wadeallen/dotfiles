set nocompatible 
syntax on

set nobackup
set nowritebackup

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-surround'
Plugin 'tpope/vim-commentary'
" Plugin 'vim-pandoc/vim-pandoc'
" Plugin 'vim-pandoc/vim-pandoc-syntax' 
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'vim-scripts/L9'
Plugin 'ron89/thesaurus_query.vim'
Plugin 'panozzaj/vim-autocorrect'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
au BufNewFile,BufRead *.ldg,*.ledger setf ledger 
" au! BufNewFile,BufFilePRe,BufRead *.md,*.markdown,*txt set filetype=markdown.pandoc
"------------------------------------------------------------
set spell spelllang=en_us
set hidden
set wildmenu
set showcmd
set ignorecase
set smartcase
set backspace=indent,eol,start
set autoindent
set nostartofline

set laststatus=2
set confirm
set visualbell
set t_vb=
set cmdheight=2
set number
set notimeout ttimeout ttimeoutlen=200
set pastetoggle=<F11>
set shiftwidth=2
set softtabstop=2
set expandtab
set wrap
set linebreak
"------------------------------------------------------------
"Colorscheme settings
colorscheme badwolf
hi clear SpellBad
hi SpellBad cterm=underline
set nolist  " list disables linebreak
"------------------------------------------------------------
"These keys have to do with bolding words in markdown
let b:surround_45 = "**\r**"
vmap 88 S# :s/#/**/g<CR>
nmap 88 ysiw- 
nmap 77 :s/__//g<CR>
nmap 66 ysiw_
"------------------------------------------------------------
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
"to cut and copy text
" set clipboard=unnamed
:set clipboard=unnamedplus
"------------------------------------------------------------
"mapping for shift/enter to exit insert mode
inoremap jj <Esc>
noremap qq :wq<CR>
"------------------------------------------------------------
"disable arrow keys
noremap <Up> <NOP>
noremap <Down> <NOP>
noremap <Left> <NOP>
noremap <Right> <NOP>
"------------------------------------------------------------
"this is added to disable folding by default
 let g:pandoc#modules#disabled = ["folding"]
"------------------------------------------------------------
"adding shortcut to insert horizontal line above text
nnoremap <C-J> m`o<Esc>``
nnoremap 99 O<Esc>O---<Esc>jj
"------------------------------------------------------------
"adding line to strip verse numbers
nmap <leader>nv :s/\d\+)//g<CR>:s/  */ /g<CR>:nohl<CR>
nmap <leader>ns :s/  */ /g<CR>
"------------------------------------------------------------
"adding shortcut to make verse slide
nmap <leader>ms 0di(o<Esc>P0i*<Esc>A*<Esc>k0xxxo<Esc>jj
"------------------------------------------------------------
"added line to copy summary and verse
"noremap <leader>cs 0lvi"y
noremap <leader>cv 0lv$y
"------------------------------------------------------------
"Quickly Grab information from sermon file
noremap <leader>gt 2gg0wwv$y
"------------------------------------------------------------
"this will add new line without insert mode
nmap <S-Enter> O<Esc>j
nmap <CR> o<Esc>k
"------------------------------------------------------------
"capitalize words and sentences
if (&tildeop)
  nmap gcw guw~l
  nmap gcW guW~l
  nmap gciw guiw~l
  nmap gciW guiW~l
  nmap gcis guis~l
  nmap gc$ gu$~l
  nmap gcgc guu~l
  nmap gcc guu~l
  vmap gc gu~l
else
  nmap gcw guw~h
  nmap gcW guW~h
  nmap gciw guiw~h
  nmap gciW guiW~h
  nmap gcis guis~h
  nmap gc$ gu$~h
  nmap gcgc guu~h
  nmap gcc guu~h
  vmap gc gu~h
endif
"------------------------------------------------------------
"Ledger Files
nmap <leader>2 010li<Space>*<Esc>
nnoremap <leader>d "=strftime("%Y/%m/%d")<CR>PA<Space><Space>
nnoremap <leader>nt G"=strftime("%Y/%m/%d")<CR>PA<Space><Space>

"----------------------------------
"capitalize sentence
nmap <leader>cc 0gcw
nmap <leader>" 0/:<Return>Wi"<Esc>$a"

"Add bullet at beginning of line
nmap <leader>- :s/^/- /<Return>

"insert duration file
nnoremap <leader>dur :r ~/Dropbox/Textbits/duration.txt<cr>

"toggle tab completion key
"inoremap <tab> <c-r>=Smart_TabComplete()<CR>
"

" Vim Markdown settings
let g:vim_markdown_frontmatter = 1
let g:vim_markdown_folding_disabled = 1

"Always open vimrc in side window
nnoremap <leader>ev :vsplit $MYVIMRC<cr>
nnoremap <leader>sv :source $MYVIMRC<cr>

"Change Translation to NIV
nnoremap <leader>re :Replace<CR>

"Snippets
let g:UltiSnipsExpandTrigger="<tab>"
let g:UltiSnipsJumpForwardTrigger="<tab>"
let g:UltiSnipsJumpBackwardTrigger="s-<tab>"

"for compiling executions
:set shortmess=at
:set cmdheight=2

"for thesaurus plugin
nnoremap <LocalLeader>th :ThesaurusQueryReplaceCurrentWord<CR>
vnoremap <LocalLeader>th y:Thesaurus <C-r>"<CR>
let g:tq_enabled_backends=["thesaurus_com","openoffice_en","mthesaur_txt"]

"Auto correct
nnoremap <leader>a :call AutoCorrect()<CR>

" Show syntax highlighting groups for word under cursor
nmap <C-S-P> :call <SID>SynStack()<CR>
function! <SID>SynStack()
  if !exists("*synstack")
    return
  endif
  echo map(synstack(line('.'), col('.')), 'synIDattr(v:val, "name")')
endfunc

" Highlight TODO and FIXME.
augroup HiglightTODO
    autocmd!
    autocmd WinEnter,VimEnter * :silent! call matchadd('Todo', 'TODO\|FIXME\|DRAFT', 10)
augroup END

" Auto Capitalize Sentences
augroup SENTENCES
      au!
        autocmd InsertCharPre * if search('\v(%^|[.!?]\_s+|\_^\-\s|\_^title\:\s|\n\n)%#', 'bcnw') != 0 | let v:char = toupper(v:char) | endif
      augroup END

" for mutt
" autocmd BufNewFile,BufRead /tmp/mutt* set noautoindent filetype=mail
" autocmd BufNewFile,BufRead ~/tmp/mutt* set noautoindent filetype=mail

"to fix background problem
if &term =~ '256color'
    " Disable Background Color Erase (BCE) so that color schemes
    " work properly when Vim is used inside tmux and GNU screen.
    set t_ut=
endif

" To format HTML files
let g:html_indent_script1 = "inc" 
let g:html_indent_style1 = "inc" 
let g:html_indent_inctags = "html,body,head"

" set journal filetype
au BufNewFile,BufRead *.journal.markdown setf journal

" adding support for FZF
set rtp+=~/.fzf
nmap <leader>sw :FZF /home/wadeallen/Dropbox/Administration/Markdown_Files/Sermon_Work<Return>
