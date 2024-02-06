from save_contacts import save_contacts

def add_command(cmd, contacts_data):
    print('save_contacts:')
    print(contacts_data)
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
            data['birthday'] = cmd[1]
        case 3:
            data['name'] = cmd[0]
            data['birthday'] = cmd[1]
            data['tel'] = cmd[2]
    
    contacts_data.append(data)
    save_contacts(contacts_data)
            
