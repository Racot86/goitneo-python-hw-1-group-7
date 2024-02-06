from load_contacts import load_contacts
def show_contacts(cmd):
    cmd.pop(0)
    if cmd[0].lower() == 'contacts':
        array = load_contacts()
        print ('Perssy:')
        print ('                  Contact list')
        print ("{:<20} {:^10} {:^15}".format('Name', 'Birth day', 'Tel. number'))
        for c in array:
            print ("{:<20} {:^10} {:^15}".format(c['name'], c['birthday'], c['tel']))

