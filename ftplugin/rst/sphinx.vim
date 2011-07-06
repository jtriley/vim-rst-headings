" Only do this when not done yet for this buffer
if exists("g:loaded_vim_sphinx_ftplugin")
    finish
endif
let loaded_vim_sphinx_ftplugin = 1

python << endpython
import os
import sys
import vim
# get the directory this script is in: the sphinxvim python module should be there
scriptdir = os.path.dirname(vim.eval('expand("<sfile>")'))
if scriptdir not in sys.path:
    sys.path.insert(0, scriptdir)
from sphinxvim import *
for i in range(6):
    vim.command('map <leader><leader>%(i)d :python update_heading(%(i)d)<CR>' % dict(i=i))
endpython

"fun! RstMappingsHeading()
    "" explicit is better than implicit
    "map <leader><leader>i :python update_heading(1)<CR>
    "map <leader><leader>i :python update_heading(2)<CR>
    "map <leader><leader>i :python update_heading(3)<CR>
    "map <leader><leader>i :python update_heading(4)<CR>
    "map <leader><leader>i :python update_heading(5)<CR>
    "map <leader><leader>i :python update_heading(6)<CR>
"endfun
"call RstMappingsHeading()

" select mode and call mapping function accordingly
"let modes = ['1. Headings']
"fun! RstModeselect()
    "let num = inputlist(g:modes)
    "if num == 1
        "call RstMappingsHeading()
    "endif
"endfun
"execute 'map <F12> :call RstModeselect()<CR>'
