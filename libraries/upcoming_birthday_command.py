from libraries.colors import colors
from datetime import datetime, timedelta
from libraries.load_contacts import load_contacts

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
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def output_month(data):
    if len(data)>0:
        match_dict = {}
        for c in data:
            i = c['contact']
            match_dict[i['name']] = datetime(datetime.now().year,i['birthday'].month, i['birthday'].day)
        print('\n' + spaces + perssy + 'This month birthdays:\n')
        
        new_d =  dict(sorted(match_dict.items(), key=lambda item: item[1]))
        
        for k,v in new_d.items():
            print('               ' + "{:>20}: {:<15}".format(c_highlight + v.strftime("%d/%m") + c_end, k))
        print('\n')
            
    else:
        print('               ' +  c_wrong + '<no birthdays>' + c_end)


def output_week(data):
    list = {'Monday':[],
            'Tuesday':[],
            'Wednesday':[],
            'Thursday':[],
            'Friday':[],
            'Saturday':[],
            'Sunday':[]
            }
    for c in data:
        i = c['contact']
        wk = c['weekday']
        list[weekdays[wk]].append(i['name'])
    print('\n' + spaces + perssy + 'Next week birthdays:\n')
    for wk,names in list.items():
        if (len(names)) > 0:
            print('               ' + "{:>20}: {:<15}".format(c_highlight + wk + c_end, ', '.join(names)))
        else:
            print('               ' + "{:>20}: {:<15}".format(c_highlight + wk + c_end, c_wrong + '<no birthdays>' + c_end))
    print('\n')



def match_time(today, range):
    
    array = []
    contacts = load_contacts()
    for c in contacts:
        if c['birthday'] != '':            
            check1 = datetime(today.year, c['birthday'].month, c['birthday'].day)
            d1 = (check1.date() - today.date()).days
            if d1 >= 0 and d1 <= range:
                array.append({'contact': c, 'weekday': check1.weekday()})

            check2 = datetime(today.year + 1, c['birthday'].month, c['birthday'].day)
            d2 = (check2.date() - today.date()).days
            if d2 >= 0 and d2 <= range:
                array.append({'contact': c, 'weekday': check2.weekday()})
                
    return array
            
           

def get_time_delta_for_next_week(wk_date):
    
    wk_day = wk_date.weekday()
    delta = 0
    if wk_day != 0:
        delta = 7 - wk_day
    return delta


def upcoming_birthday(cmd):
    cmd.pop(0)
    if len(cmd) == 2 and cmd[1].lower() == 'birthdays':
        today = datetime.now()
        #today = datetime(2024,12,22)
        match_list = []
        match cmd[0].lower():
            case 'week':
                next_week_monday = today + timedelta(days=get_time_delta_for_next_week(today))
                output_week(match_time(next_week_monday, 6))
            case 'month':
                eom = datetime(today.year, today.month+1, 1) - timedelta(days=1)
                output_month(match_time(today, (eom.date()-today.date()).days))
            case _:
                print('\n' + spaces + perssy + c_wrong + 'Time period for command upcoming birthdays not recognised.' +c_end + '\n')
                
    else:
        print('\n' + spaces + perssy + c_wrong + 'Command not recognised.' + c_end + '\n')
