# Git-bash configuration

* Apply `console_colors.reg` file
* Save `git-prompt.sh` file to `<git_install_dir>\etc\profile.d` directory
* Add to `<git_install_dir>\etc\profile.d\aliases.sh` file:
```
alias st='echo && git st && echo && git lg'
alias s='clear && st ${FROM}~..HEAD'
```
