from colors import colors
from load_contacts import load_contacts
from format_command import format_command
from save_contacts import save_contacts
from add_command import add_command
from hello_command import hello_command
from show_contacts import show_contacts
from invalid_command import invalid_command

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
            hello_command()
        case 'add':
            add_command(cmd, load_contacts())
        case 'show':
            show_contacts(cmd)
        case _:
            invalid_command(cmd)



while True:

    cmd =  format_command( input(c_cmd + 'You: ' + c_end)) # getting command from user

    print(c_debug + 'cmd parser : ' + '[' + ', '.join(cmd) + ']' + c_end) # parser for cmd

    if cmd[0] == 'exit':
        break
    else:
        process_command(cmd)
