from libraries.save_contacts import save_contacts
from libraries.validate_date_format import validate_date
from libraries.colors import colors
from datetime import datetime

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

def add_command(cmd, contacts_data):
    cmd.pop(0)
    data = {
        'name': '',
        'birthday': '',
        'tel': ''
    }
    match len(cmd):
        case 1:
            data['name'] = cmd[0]
        case 2:
            data['name'] = cmd[0]
            
            if validate_date(cmd[1]) == True:
                data['birthday'] = convert_string_date(cmd[1])
            else:
                print('\n' + spaces + c_perssy + f"Perssy:" + c_end + c_wrong + f" '{cmd[1]}' is wrong date format. Correct date format: dd-mm-yyyy" + c_end)


        case 3:
            data['name'] = cmd[0]

            if validate_date(cmd[1]) == True:
                data['birthday'] = convert_string_date(cmd[1])
            else:
                print('\n' + spaces + c_perssy + f"Perssy:" + c_end + c_wrong + f" '{cmd[1]}' is wrong date format. Correct date format: dd-mm-yyyy" + c_end)

            data['tel'] = cmd[2]
    
    u = 'added'
    match = False
    for c in contacts_data:
        
        if c['name'].lower() == data['name'].lower():
            cmd = input('\n' + spaces + perssy + f"You have user with name '{c['name']}' . Would you like to amend this contact?(Y/N)\n\n" + c_cmd + "You: " + c_end)
            if cmd.lower() == 'y':
                c['birthday'] = data['birthday']
                c['tel'] = data['tel']
                u = 'amended'
                match = True
                break
            else:
                c = data
                c['name'] = c['name'] + '_copy'

    if match == False: contacts_data.append(data)    
    save_contacts(contacts_data)
    if data['birthday'] != '':
        print ('\n' + spaces + c_perssy + f"Perssy:" + c_end + c_accept + f" Contact '{data['name']}' with birth day '{data['birthday'].strftime("%d-%m-%Y")}' and tel no '{data['tel']}' {u} " + c_end + '\n')
    else:
         print ('\n' + spaces + c_perssy + f"Perssy:" + c_end + c_accept + f" Contact '{data['name']}' with birth day '' and tel no '{data['tel']}' {u} " + c_end + '\n')

            
