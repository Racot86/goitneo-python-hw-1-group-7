def save_contacts(data):
    if len(data) > 0:
        with open('contacts.txt','w') as fh:
            for i in data:
                s = []
                for k, v in i.items():
                    if k == 'birthday':
                        v = str(v)
                    s.append(v)
                fh.write(','.join(s) + '\n')





