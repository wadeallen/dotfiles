" run awk on external thesaurus to find synonyms
" ==================================================
function! OmniComplete(findstart, base)
    if ! exists("b:thesaurus")
        return
    endif
    if a:findstart
        " first, must find word
        let line = getline('.')
        let wordStart = col('.') - 1
        " check backward, accepting only non-white space
        while wordStart > 0 && line[wordStart - 1] =~ '\S'
            let wordStart -= 1
        endwhile
        return wordStart
    else
      " a word with single quotes would produce a shell error
        if match(a:base, "'") >= 0
            return
        endif
        let searchPattern = '/^' . tolower(a:base) . '\|/'
        " search pattern is single-quoted
        let thesaurusMatch = system('awk'
            \ . " '" . searchPattern . ' {printf "%s", NR ":" $0}' . "'"
            \ . " '" . b:thesaurus . "'"
        \)
        if thesaurusMatch == ''
            return
        endif
        " line info was returned by awk
        let matchingLine = substitute(thesaurusMatch, ':.*$', '', '')
        " entry count was in the thesaurus itself, right of |
        let entryCount = substitute(thesaurusMatch, '^.*|', '', '')
        let firstEntry = matchingLine + 1
        let lastEntry = matchingLine + entryCount
        let rawOutput = system('awk'
            \ . " '" . ' NR == ' . firstEntry . ', NR == ' . lastEntry
            \ . ' {printf "%s", $0}' . "'"
            \ . " '" . b:thesaurus . "'"
        \)
        " remove dash tags if any
        let rawOutput = substitute(rawOutput, '^-|', '', '')
        let rawOutput = substitute(rawOutput, '-|', '|', 'g')
        " remove grammatical tags if any
        let rawOutput = substitute(rawOutput, '(.\{-})', '', 'g')
        " clean spaces left by tag removal
        let rawOutput = substitute(rawOutput, '^ *|', '', '')
        let rawOutput = substitute(rawOutput, '| *|', '|', 'g')
        let listing = split(rawOutput, '|')
        return listing
    endif
endfunction

" configure completion
" ==================================================
set omnifunc=OmniComplete
set completeopt=menuone
