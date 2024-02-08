from libraries.load_contacts import load_contacts
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

def show_contacts(cmd):
    cmd.pop(0)
    if cmd[0].lower() == 'contacts':
        array = load_contacts()
        if len(array) > 0:
            print ( '\n' + spaces + perssy + '\n')
            print (spaces + spaces + c_highlight + '                  Contact list\n')
            print (spaces + spaces + c_accept + "{:<20} {:^10} {:^15}".format('Name', 'Birth day', 'Tel. number') + c_end)
            for c in array:
                
                if c['birthday'] != '':
                    
                    print (spaces + spaces + c_highlight + "{:<20} {:^10} {:^15}".format(c['name'], c['birthday'].strftime("%d-%m-%Y"), c['tel']))
                else:
                     print (spaces + spaces + c_highlight + "{:<20} {:^10} {:^15}".format(c['name'],'', c['tel']))
            print('\n')
        else:
            print ( spaces + perssy + '\n')
            print ( spaces + spaces + 'Contact list is empty' + '\n')
    else:
        match = False
        for c in load_contacts():
            if c['name'] == cmd[0]:
                match = True
                print('\n' + spaces + perssy + ' Contact details:')
                print( '               ' + "{:>20}: {:<15}".format(c_highlight + 'Name' + c_end, c['name']))
                if c['birthday'] != '':
                    print( '               ' + "{:>20}: {:<15}".format(c_highlight + 'Birthday' + c_end , c['birthday'].strftime("%d-%m-%Y")))
                else:
                    print( '               ' + "{:>20}: {:<15}".format(c_highlight + 'Birthday' + c_end , ''))
                print( '               ' + "{:>20}: {:<15}".format(c_highlight + 'Tel. no' + c_end, c['tel']) + '\n')
        if match == False: print ('\n' + spaces + perssy + c_wrong + 'I did not recognized which data to show.' + c_end + '\n')


