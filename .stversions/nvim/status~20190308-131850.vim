
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

