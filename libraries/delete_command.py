from libraries.load_contacts import load_contacts
from libraries.save_contacts import save_contacts
from libraries.colors import colors

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

def delete_command(cmd):
    cmd.pop(0)
    contacts = load_contacts()
    if len(cmd) == 1:
        for c in contacts:
            if c['name'] == cmd[0]:
                contacts.remove(c)
                print('\n' + spaces + perssy + c_accept + 'Contact ' + c_end + f'{c['name']}' + c_accept + ' removed.' + c_end + '\n')
                save_contacts(contacts)
                break
    else:
        print('\n' + spaces + perssy + c_wrong + 'Wrong number of parameters.' + c_end + '\n')            
