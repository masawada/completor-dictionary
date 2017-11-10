completor-dictionary
====================

Dictionary completion support for [completor.vim](https://github.com/maralla/completor.vim).

Install
-------

[Install completor.vim](https://github.com/maralla/completor.vim#install) first.

For [vim-plug](https://github.com/junegunn/vim-plug)

```vim
Plug 'masawada/completor-dictionary'
```

and write it in your .vimrc:

```
autocmd FileType * execute 'setlocal dictionary='.expand($HOME.'/.vim/dict/'.&filetype.'.dict')
```

then, put your dictionaries in `$HOME/.vim/dict`. The name must be of format `filetype.dict`.
