def timeConversion(s):
    # Write your code here

    ampm = s[-2:]
    hour = int(s[:2])
    
    if ampm == "PM":
        hour = (hour%12 + 12)
        return (str(hour)+s[2:-2])
    elif ampm == "AM":
        hour = (hour%12)
        if hour == 0:
            return ("00"+s[2:-2])
        else:
            return (s[:-2])
