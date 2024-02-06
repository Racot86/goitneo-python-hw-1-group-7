from colors import colors
from load_contacts import load_contacts

# colors to be used in design
c_perssy = colors.CBEIGE # assistant color
c_wrong = colors.CRED # wrong command color
c_highlight = colors.CBLUE2 # command highlight
c_accept = colors.CGREEN #command accepted
c_end = colors.CEND # end of color


contacts_data = []
print(load_contacts())
