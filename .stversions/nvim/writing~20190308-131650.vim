
"setup markdown files
autocmd BufNewFile,BufFilePre,BufRead *.md,*.markdown set filetype=markdown.pandoc


" Auto Capitalize Sentences
augroup SENTENCES
      au!
        autocmd InsertCharPre * if search('\v(%^|[.!?]\_s+|\_^\-\s|\_^title\:\s|\n\n)%#', 'bcnw') != 0 | let v:char = toupper(v:char) | endif
      augroup END
