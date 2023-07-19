import re
import sys


def main():
    print(parse(input("HTML: ")))

# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
def parse(s):
    if src := re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"',s):
        # https://youtu.be/xvFZjo5PgG0
        link = "https://youtu.be/" + src.group(1)
        return link
    else:
        return "None"

if __name__ == "__main__":
    main()