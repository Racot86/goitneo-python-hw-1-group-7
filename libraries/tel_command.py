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

def tel_command(cmd, contacts):
    cmd.pop(0)
    if len(cmd) == 1:
        match = False
        for c in contacts:
            if c['name'] == cmd[0]:
                print('\n' + spaces + perssy + f"{c['name']}'s" + c_accept + " telephone number is " + c_end + f"{c['tel']}.\n")
                match = True
                break
        if match == False: print('\n' + spaces + perssy + c_wrong + f'Contact {cmd[0]} not found' + c_end + '\n')
    else:
        print('\n' + perssy + c_wrong + f"Parameters of the tel command not recognised." + c_end + ' Enter' + c_highlight + ' help ' + c_end + 'command to view avaliable options.\n')