from colors import colors
from load_contacts import load_contacts
from format_command import format_command
from save_contacts import save_contacts
from add_command import add_command

# colors to be used in design
c_perssy = colors.CBEIGE # assistant color
c_wrong = colors.CRED # wrong command color
c_highlight = colors.CBLUE2 # command highlight
c_accept = colors.CGREEN # command accepted
c_end = colors.CEND # end of color
c_cmd = colors.CYELLOW # commnd color
c_debug = colors.CGREY # for debugging



def process_command(cmd):
    
    match cmd[0]:
        case 'hello':
            print('Perssy: : Hi!\n')
        case 'add':
            add_command(cmd, load_contacts())


while True:

    cmd =  format_command( input(c_cmd + 'You: ' + c_end)) # getting command from user

    # print(c_debug + 'debugger: ' + '[' + ', '.join(cmd) + ']') # debugger for cmd

    if cmd[0] == 'exit':
        break
    else:
        process_command(cmd)
