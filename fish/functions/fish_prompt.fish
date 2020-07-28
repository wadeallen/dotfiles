function fish_prompt
    set -l textcol  white
    set -l arrowcol green
    set -l filebase yellow
    echo -n "$hostname"
    set_color $filebase
    echo -n " "(basename $PWD)" "
    set_color $arrowcol -b normal
    echo -n "⮀ "
end
