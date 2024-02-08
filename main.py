from libraries.colors import colors
from libraries.load_contacts import load_contacts
from libraries.format_command import format_command
from libraries.save_contacts import save_contacts
from libraries.add_command import add_command
from libraries.hello_command import hello_command
from libraries.show_contacts import show_contacts
from libraries.invalid_command import invalid_command
from libraries.tel_command import tel_command
from libraries.delete_command import delete_command
from libraries.change_command import change_command
from libraries.birthday_command import birthday_command

def main():
    # colors to be used in design
    c_perssy = colors.CBEIGE # assistant color
    c_wrong = colors.CRED # wrong command color
    c_highlight = colors.CBLUE2 # command highlight
    c_accept = colors.CGREEN # command accepted
    c_end = colors.CEND # end of color
    c_cmd = colors.CYELLOW # commnd color
    c_debug = colors.CGREY # for debugging
    spaces = '     '
    perssy = c_perssy + 'Perssy: ' + c_end

    exit_synonims = ['exit', 'quit', 'end']

    print('\n' + '             ' + colors.CBEIGEBG +  ' Personal Assistant App ' + c_end + ' ver 1.0')
    print('                ' + 'created by MAYEVSKY Dmytro')
    print('\n                        ' + c_perssy + '≽^•⩊•^≼' + c_end + '\n')
    print(spaces + perssy + "Hi! I am " + c_perssy + 'Perssy' + c_end + '! Your personal assistant.\n')

    def process_command(cmd):
        
        match cmd[0]:
            case 'hello':
                hello_command()
            case 'hi':
                hello_command()
            case 'good':
                hello_command()
            case 'add':
                add_command(cmd, load_contacts())
            case 'show':
                show_contacts(cmd)
            case 'tel':
                tel_command(cmd, load_contacts())
            case 'birthday':
                birthday_command(cmd, load_contacts())
            case 'delete':
                delete_command(cmd)
            case 'change':
                change_command(cmd, load_contacts())
            case _:
                invalid_command(cmd)



    while True:

        cmd =  format_command( input(c_cmd + 'You: ' + c_end)) # getting command from user

        #print(c_debug + 'cmd parser : ' + '[' + ', '.join(cmd) + ']' + c_end) # parser for cmd

        if cmd[0] in exit_synonims:
            print('\n' + spaces + perssy + 'Good bye! See you next time!\n')
            print('                       ' + c_perssy + '/ᐠ - ˕ -マ' + c_end + 'ᶻ 𝗓 𐰁' + '\n')
            break
        else:
            process_command(cmd)

if __name__ == "__main__":
    main()
