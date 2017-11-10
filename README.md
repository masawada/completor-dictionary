completor-dictionary
====================

## Usage

if you use vim-plug:

```
Plug 'masawada/completor-dictionary'
```

and write it in your .vimrc:

```
autocmd FileType * execute 'setlocal dictionary='.expand($HOME.'/.vim/dict/'.&filetype.'.dict')
```

and put your dictionaries in `$HOME/.vim/dict`
