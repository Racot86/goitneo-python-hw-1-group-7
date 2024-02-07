def format_command(cmd):
    if len(cmd) > 0:
        cmd = cmd.strip()    
        l = cmd.split(' ')
        l[0] = l[0].lower()
        return l
    else:
        return []

        