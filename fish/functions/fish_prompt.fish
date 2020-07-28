function fish_prompt
    set_color magenta
    echo -n (hostname) ' '
    set_color $fish_color_cwd
    echo -n (basename $PWD)
    set_color normal
    echo -n ' ) '
end
