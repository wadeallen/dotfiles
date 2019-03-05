
" offer choice among installed thesauri
" ==================================================
let s:thesaurusPath = expand("<sfile>:p:h") . "/thes"

function! s:PickThesaurus()
    " 1, 1: glob does not ignore any pattern, returns a list
    let thesaurusList = glob(s:thesaurusPath . "/*", 1, 1)
    if len(thesaurusList) == 0
        echo "Nothing found in " . s:thesaurusPath
        return
    endif
    let index = 0
    let optionList = []
    for name in thesaurusList
        let index = index + 1
        let shortName = fnamemodify(name, ":t:r")
        let optionList += [index . ". " . shortName]
    endfor
    let choice = inputlist(["Select thesaurus:"] + optionList)
    let indexFromZero = choice - 1
    if (indexFromZero >= 0) && (indexFromZero < len(thesaurusList))
        let b:thesaurus = thesaurusList[indexFromZero]
    endif
endfunction

command! Thesaurus call s:PickThesaurus()
