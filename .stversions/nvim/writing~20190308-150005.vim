"setup markdown files
autocmd BufNewFile,BufFilePre,BufRead *.md,*.markdown set filetype=markdown.pandoc

" Auto Capitalize Sentences
augroup SENTENCES
      au!
        autocmd InsertCharPre * if search('\v(%^|[.!?]\_s+|\_^\-\s|\_^title\:\s|\n\n)%#', 'bcnw') != 0 | let v:char = toupper(v:char) | endif
      augroup END

"for thesaurus plugin
nnoremap <LocalLeader>th :ThesaurusQueryReplaceCurrentWord<CR>
vnoremap <LocalLeader>th y:Thesaurus <C-r>"<CR>
let g:tq_enabled_backends=["thesaurus_com","openoffice_en","mthesaur_txt"]
