import re
import sys


def main():
    print(convert(input("Hours: ")))

# 9 AM to 5 PM OUTPUT 09:00 to 17:00
def convert(s):
    if matches := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM)? to (\d{1,2}):?(\d{2})? (AM|PM)?", s):
        # Check if the minutes are valid.
        if matches.group(2) or matches.group(5):
            if int(matches.group(2)) >= 60 or int(matches.group(5)) >= 60:
                raise ValueError
        # Check if the hours are valid.
        if matches.group(1) or matches.group(4):
            if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
                raise ValueError
            if int(matches.group(1)) < 0 or int(matches.group(4)) < 0:
                raise ValueError



        # Create Variables.
        # Entry time.
        h1 = int(matches.group(1))
        if matches.group(3) == "PM":
            h1 += 12
        elif (matches.group(3) == "AM") and (h1 ==12):
            h1 = 0
        if (matches.group(2) == None):
            entry_time = f"{h1:02}:00"
        else:
            entry_time = f"{h1:02}:{matches.group(2)}"

        # Out time.
        h2 = int(matches.group(4))
        if matches.group(6) == "PM" and h2 != 12:
            h2 += 12
        if (matches.group(5) == None):
            out_time = f"{h2:02}:00"
        else:
            out_time = f"{h2:02}:{matches.group(5)}"

        f_hour = f"{entry_time} to {out_time}"

        return f_hour

    # Check if the input matches the pattern.
    else:
        raise ValueError




if __name__ == "__main__":
    main()