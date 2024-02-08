from libraries.colors import colors
from libraries.save_contacts import save_contacts
from datetime import datetime
from libraries.validate_date_format import validate_date
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

def convert_string_date(data):
    l = data.split('-')
    return datetime(year=int(l[2]),month=int(l[1]),day=int(l[0]))

def change_command(cmd, contacts):
    cmd.pop(0)
    if len(cmd) == 3:
        for c in contacts:
            if cmd[0].lower() == c['name'].lower():
                match cmd[1].lower():
                    case 'name':
                        c['name'] = cmd[2]
                        print('\n' + spaces + perssy + c_accept + 'Contact ' + c_end + cmd[0] + c_accept + ' changed to ' + c_end + cmd[2] + '\n')
                    case 'birthday':
                        if validate_date(cmd[2]):
                            c['birthday'] = convert_string_date(cmd[2])
                            print('\n' + spaces + perssy + cmd[0] + "'s " + c_accept + 'birth day changed to ' + c_end + cmd[2] + '\n')
                        else:
                            print('\n' + spaces + perssy + c_wrong + 'Wrong date format. Correct format is dd-mm-yyyy. Order aborted.\n')
                    case 'tel':
                        if cmd[2].isdigit() == True:
                            c['tel'] = cmd[2]
                            print('\n' + spaces + perssy + cmd[0] + "'s " + c_accept + 'telephone changed to ' + c_end + cmd[2] + '\n')
                        else:
                            print('\n' + spaces + perssy + c_wrong + 'Wrong telephone format. Number must be a digit. Order aborted.\n')
                    case _:
                        print('\n' + spaces + perssy + c_wrong + 'Wrong number of parameters.\n')
                save_contacts(contacts)
                break
            else:
                print('\n' + spaces + perssy + c_wrong + 'Contact does not exists.\n')

    else:
        print('\n' + spaces + perssy + c_wrong + 'Wrong number of parameters.\n')