if exists('g:loaded_completor_dictionary_plugin')
  finish
endif

let g:loaded_completor_dictionary_plugin = 1
let s:py = has('python3') ? 'py3' : 'py'

function! s:enable()
  exe s:py 'import completor_dictionary'
  exe s:py 'import completor, completers.common'
  exe s:py 'completor.get("common").hooks.append(completor_dictionary.Dictionary.filetype)'
  call s:disable()
endfunction

function! s:disable()
  augroup completor_dictionary
    autocmd!
  augroup END
endfunction

augroup completor_dictionary
  autocmd!
  autocmd InsertEnter * call s:enable()
augroup END
