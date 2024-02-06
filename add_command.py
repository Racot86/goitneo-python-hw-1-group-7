from save_contacts import save_contacts
from validate_date_format import validate_date
from colors import colors

# colors to be used in design
c_perssy = colors.CBEIGE # assistant color
c_wrong = colors.CRED # wrong command color
c_highlight = colors.CBLUE2 # command highlight
c_accept = colors.CGREEN # command accepted
c_end = colors.CEND # end of color
c_cmd = colors.CYELLOW # commnd color
c_debug = colors.CGREY # for debugging

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
                data['birthday'] = cmd[1]
            else:
                print(c_perssy + f"Perssy:" + c_end + c_wrong + f" '{cmd[1]}' is wrong date format. Correct date format: dd-mm-yyyy" + c_end)


        case 3:
            data['name'] = cmd[0]

            if validate_date(cmd[1]) == True:
                data['birthday'] = cmd[1]
            else:
                print(c_perssy + f"Perssy:" + c_end + c_wrong + f" '{cmd[1]}' is wrong date format. Correct date format: dd-mm-yyyy" + c_end)

            data['tel'] = cmd[2]
    
    
    contacts_data.append(data)    
    save_contacts(contacts_data)
    print (c_perssy + f"Perssy:" + c_end + c_accept + f" Contact '{data['name']}' with birth day '{data['birthday']}' and tel no '{data['tel']}' added " + c_end)
            
