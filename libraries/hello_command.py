from datetime import datetime
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

def hello_command():
    time_of_day = ''
    time = datetime.now()
    if time.hour >= 0 and time.hour < 12: time_of_day = 'morning'
    if time.hour >= 12 and time.hour < 18: time_of_day = 'day'
    if time.hour >= 18 and time.hour <= 23: time_of_day = 'evening'
    print( '\n' + spaces + perssy + f'Good {time_of_day}! How can I help you?\n')