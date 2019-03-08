syntax on
set number

"map keys for easy exit
inoremap jj <Esc>
noremap qq :wq<CR>

colorscheme badwolf

"install plugins
call plug#begin('~/.config/nvim/plugged')
Plug 'ron89/thesaurus_query.vim'
Plug 'panozzaj/vim-autocorrect'
Plug 'vim-pandoc/vim-pandoc-syntax'
call plug#end()

"setup markdown files
autocmd BufNewFile,BufFilePre,BufRead *.md set filetype=markdown.pandoc

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
