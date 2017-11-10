# -*- cofing: utf-8 -*-

import os
import vim
from completor import Completor

_words_cache = {}

class Dictionary(Completor):
    filetype = 'dictionary'
    sync = True

    @staticmethod
    def _get_words_from_dictionary():
        current_buffer = vim.current.buffer
        dictionary_path = current_buffer.options['dictionary']
        f = open(os.path.expanduser(dictionary_path))
        dictionary = f.read()
        f.close()
        return dictionary[:-1].split('\n')

    def parse(self, base):
        if not self.ft or not base:
            return []

        if self.ft not in _words_cache:
            try:
                _words_cache[self.ft] = self._get_words_from_dictionary()
            except Exception:
                _words_cache[self.ft] = []

        token = self.input_data.split()[-1]
        filtered_words = filter((lambda word: word.startswith(token.encode('utf-8'))), _words_cache[self.ft])

        return [{
            'word': item,
            'dup': 1,
            'menu': b'[dict]',
        } for item in filtered_words]
