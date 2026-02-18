# Delta configuration

* [Download](https://github.com/dandavison/delta/releases) and install
* Select system/global git config location dir:
```bash
git config --list --show-origin
```
* Save `delta.gitconfig` file to the selected system/global dir
* Execute with the selected system/global scope:
```bash
git config set --<system|global> --append include.path delta.gitconfig
```
