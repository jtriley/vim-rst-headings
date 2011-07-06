import vim

levels = {1: '#',
          2: '*',
          3: '=',
          4: '-',
          5: '^',
          6: '"'}


def reverse_levels(char):
    for k, v in levels.iteritems():
        if v == char:
            return k


def is_heading_char(c):
    return c in levels.values()


def get_line_heading():
    b = vim.current.buffer
    lineno, col = vim.current.window.cursor
    i = lineno - 1
    over = None
    under = None

    if i >= 1:  # is there a previous line?
        over = b[i - 1]
    if i < len(b) - 1:  # is there a next line?
        under = b[i + 1]
    if not under:
        return None
    if len(filter(is_heading_char, under)) == len(under):
        if over and len(filter(is_heading_char, over)) == len(over):
            return reverse_levels(over[0])
        else:
            return reverse_levels(under[0])


def vim_exec(unescaped_key_sequence):
    """think of ``:map KEY SEQUENCE`` and give SEQUENCE to me"""
    e = "execute 'normal %s'" % unescaped_key_sequence
    vim.command(str(e))


def remove_underline():
    vim_exec('jddk')


def remove_underline_and_overline():
    vim_exec('kddjddk')


def underline(char):
    vim_exec('yypVr%sk' % char)


def underline_and_overline(char):
    underline(char)
    vim_exec('PVr%sj' % char)  # ugly but quick


def update_heading(level):
    if level not in levels or len(vim.current.line) == 0:
        return
    x = get_line_heading()
    if x in [1, 2]:
        remove_underline_and_overline()
    elif x in [3, 4, 5, 6]:
        remove_underline()
    char = levels[level]
    if level in [1, 2]:
        underline_and_overline(char)
    if level in [3, 4, 5, 6]:
        underline(char)
