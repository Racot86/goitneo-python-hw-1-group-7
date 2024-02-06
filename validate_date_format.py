
def validate_date(data):
    l = data.split('-')
    if len(l) == 3:
        if l[0].isdigit() and int(l[0]) <= 31 and int(l[0]) > 0 and l[1].isdigit() and int(l[1]) <= 12 and int(l[1]) > 0 and l[2].isdigit() and len(l[2]) == 4 and int(l[2]) > 0:
            return True
        else:
            return False
    else:
        return False