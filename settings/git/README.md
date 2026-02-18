# Git configuration

* [git-config](https://git-scm.com/docs/git-config)

## Show configuration
```
git config --list --show-origin
```
```
git config --list --show-scope
```

## Common options
```bash
# Username and email
git config <scope> user.name "<username>"
git config <scope> user.email <email>

# EOL conversion
git config <scope> core.eol native
git config <scope> core.autocrlf <input|true>

# Fast-forward and rebase policy
git config <scope> merge.ff false
git config <scope> pull.ff only
git config <scope> pull.rebase false

# Enable automatic fetch --prune
git config <scope> fetch.prune true
git config <scope> fetch.pruneTags true

# Log format
git config <scope> format.pretty "%C(yellow)%h%C(auto)%d %Cblue%as (%ar) %Cgreen%an %Creset%s"

# Status format
git config <scope> status.short true
git config <scope> status.branch true

# Set WinMerge as diff tool
git config <scope> diff.guitool winmerge
git config <scope> difftool.prompt false
git config <scope> difftool.guiDefault true
git config <scope> difftool.winmerge.cmd "'<C:\\path\\to\\WinMergeU.exe>' -u -fl -wr -e \"\$LOCAL\" \"\$REMOTE\""

# Set TortoiseMerge as merge tool
git config <scope> merge.guitool tortoisemerge
git config <scope> mergetool.prompt false
git config <scope> mergetool.guiDefault true
git config <scope> mergetool.keepBackup false

# Aliases
git config <scope> alias.aliases "config --get-regexp alias\."
git config <scope> alias.br "branch -vv"
git config <scope> alias.ch "diff --check"
git config <scope> alias.dt "difftool -d"
git config <scope> alias.dt-s "difftool -d --staged"
git config <scope> alias.lg "log --all --graph"
git config <scope> alias.lg-f "log --all --graph --first-parent"
git config <scope> alias.log-h "log --format=\"%C(yellow)%h%C(auto)%d %Cblue%as (%ar) %Cgreen%an %Creset%B\""
git config <scope> alias.ls-i "ls-files --eol"
git config <scope> alias.ls-ig "ls-files --other --exclude-standard --ignored"
git config <scope> alias.ls-un "ls-files --eol --other --exclude-standard"
git config <scope> alias.show-h "show --format=fuller --no-patch"
git config <scope> alias.st "status"
```

`<scope>` options:
* `--system`
* `--global`
* `--local`

`core.autocrlf` options:
* `input`: Git will convert CRLF to LF during commit (Linux, Windows)
* `true`: Git will convert CRLF to LF during commit and LF to CRLF during checkout (Windows)

`merge.ff`/`pull.ff` fast-forward policy options:
* `false` (`--no-ff`)
* `true` (`--ff`, fast-forward when possible)
* `only` (`--ff-only`)

## Set proxy options
```bash
git config <scope> http.proxy <proxy>
git config <scope> http.schannelcheckrevoke false
```

## Set WinMerge as TortoiseGit/SVN diff tool
```
"C:\path\to\WinMergeU.exe" /u /fl /wr /e /dl %bname /dr %yname %base %mine
```
