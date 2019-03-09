
"install plugins
call plug#begin('~/.config/nvim/plugged')
Plug 'ron89/thesaurus_query.vim'
Plug 'panozzaj/vim-autocorrect'
Plug 'vim-pandoc/vim-pandoc-syntax'
Plug 'tpope/vim-commentary'
Plug 'dbmrq/vim-ditto'
Plug 'reedes/vim-wordy'
call plug#end()

"custom plugins
source $HOME/.config/nvim/custom/python_functions.vim
source $HOME/.config/nvim/custom/bible_gateway.vim

"split up into various files
source $HOME/.config/nvim/general.vim
source $HOME/.config/nvim/keys.vim
source $HOME/.config/nvim/writing.vim
source $HOME/.config/nvim/status.vim
source $HOME/.config/nvim/words.vim



