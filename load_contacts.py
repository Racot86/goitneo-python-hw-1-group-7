from pathlib import Path

def load_contacts():
    if Path.is_file(Path('contacts.txt')):
        with open('contacts.txt', 'r') as fh:
            t = fh.read()
            if len(t) > 0:
                array = t.split('\n')
                array.remove('')
                dict_data = []
                for c in array:
                    data = {'name': '',
                        'birthday': '',
                        'tel': ''
                        }
                    s = c.split(',')
                    
                    match len(s):
                        case 1:
                            data['name'] = s[0]
                        case 2:
                            data['name'] = s[0]
                            data['birthday'] = s[1]
                        case 3:
                            data['name'] = s[0]
                            data['birthday'] = s[1]
                            data['tel'] = s[2]
                    dict_data.append(data)
                return dict_data    
            else:
                print ('no contacts')
                return []
            
    else:
        print ('no contacts')
        return []
    
    return []

print (load_contacts())