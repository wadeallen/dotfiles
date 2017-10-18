" ftplugin/mail.vim
setl tw=72
setl fo=watqc
setl nojs
setl nosmartindent

" add two blank lines if already content
function! IsReply()
    if line('$') > 1
        :%!par w72q
        :%s/^.\+\ze\n\(>*$\)\@!/\0 /e
        :%s/^>*\zs\s\+$//e
        :1
        :put! =\"\n\n- Wade\n\n\"
        :1
    endif
endfunction

augroup mail_filetype
    autocmd!
    autocmd! VimEnter /tmp/mutt* :call IsReply()
    autocmd VimEnter /tmp/mutt* :exe 'startinsert'
    autocmd VimEnter /tmp/mutt* :call AutoCorrect()
augroup END
