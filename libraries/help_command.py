from libraries.colors import colors

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

def help_command(cmd):
    cmd_list =[
        {'cmd': 'show',
         'syntax': c_accept + 'Syntax: ' + c_end + 'show <contact name> or <contacts>',
         'short': c_accept + ' Description: ' + c_end + 'Displays contact details or list of avaliable contacts. ' + c_accept + 'Examples: ' + c_end + 'show Dmytro, show contacs',
         'full': 'Displays contact details or list of avaliable contacts\n<contact name> - name of the contact from the saved contacts\n<contacts> - use this parameter to view all avaliable contacts\n'
         },
         {'cmd': 'upcoming',
         'syntax': c_accept + 'Syntax: ' + c_end + 'upcoming <week> or <month> birthdays',
         'short': c_accept + ' Description: ' + c_end + 'Displays list of contacts who have birthdays next week or until end of current month. ' + c_accept + 'Examples: ' + c_end + 'upcoming week birthdays, upcoming month birthdays',
         'full': 'Displays list of contacts who have birthdays next week or until end of current month\n<week> - shows list of birthdays of contacts for next week\n<month> - use this parameter to view list of birthdays until end of the current month\n'
         },
         {'cmd': 'add',
         'syntax': c_accept + 'Syntax: ' + c_end + 'add <contact name> <birth day> <tel no>',
         'short': c_accept + ' Description: ' + c_end + 'Adds contact to contact list. ' + c_accept + 'Examples: ' + c_end + 'add Dmytro, add Dmytro 04-06-1986, add Dmytro 04-06-1986 0970279618',
         'full': 'Adds contact to contact list\n<contact name> - compulsory parameter. Defines user name\n<birth day> - use this parameter to view list of birthdays until end of the current month\n'
         },
         {'cmd': 'delete',
         'syntax': c_accept + 'Syntax: ' + c_end + 'delete <contact name>',
         'short': c_accept + ' Description: ' + c_end + 'deletes contact from contact list. ' + c_accept + 'Examples: ' + c_end + 'delete Dmytro',
         'full': ''
         },
         {'cmd': 'change',
         'syntax': c_accept + 'Syntax: ' + c_end + 'change <contact name> <name or birthday or tel> <new data>',
         'short': c_accept + ' Description: ' + c_end + 'Changes contacts data. ' + c_accept + 'Examples: ' + c_end + 'change Dmytro name Mr.Dmytro, change Dmytro tel 097000000',
         'full': ''
         },
         {'cmd': 'tel',
         'syntax': c_accept + 'Syntax: ' + c_end + 'tel <contact name>',
         'short': c_accept + ' Description: ' + c_end + 'Shows telephone number of contact. ' + c_accept + 'Examples: ' + c_end + 'tel Dmytro',
         'full': ''
         },
         {'cmd': 'birthday',
         'syntax': c_accept + 'Syntax: ' + c_end + 'birthday <contact name>',
         'short': c_accept + ' Description: ' + c_end + 'Shows birthday of contact. ' + c_accept + 'Examples: ' + c_end + 'birthday Dmytro',
         'full': ''
         }

    ]
    
    for i in cmd_list:
        print('\n')
        print('{:^10} - {:<}{:<}'.format(i['cmd'],i['syntax'],'\n' + i['short']))
    print('\n')
        
