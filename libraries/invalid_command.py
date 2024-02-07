from libraries.colors import colors

# colors to be used in design
c_perssy = colors.CBEIGE # assistant color
c_wrong = colors.CRED # wrong command color
c_highlight = colors.CBLUE2 # command highlight
c_accept = colors.CGREEN # command accepted
c_end = colors.CEND # end of color
c_cmd = colors.CYELLOW # commnd color
c_debug = colors.CGREY # for debugging
perssy = c_perssy + 'Perssy: ' + c_end
spaces = '     '

def invalid_command(cmd):
    print('\n'+ spaces + perssy + c_wrong + f"Command '{cmd[0]}' not recognised." + c_end + ' Enter' + c_highlight + ' help ' + c_end + 'command to view avaliable options.\n')
    