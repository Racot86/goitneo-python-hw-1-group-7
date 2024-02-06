def save_contacts(data):
    if len(data) > 0:
        with open('contacts.txt','w') as fh:
            for i in data:
                s = []
                for v in i.values():
                    s.append(v)
                fh.write(','.join(s) + '\n')

save_contacts([{'name':'me'},{'name':'you'}])



