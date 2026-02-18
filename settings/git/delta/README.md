# Delta configuration

* [Download](https://github.com/dandavison/delta/releases)
* Select system/global git config location dir:
```bash
git config --list --show-origin
```
* Save `delta.gitconfig` file to system/global dir
* Execute:
```bash
git config set --<system|global> --append include.path delta.gitconfig
```
