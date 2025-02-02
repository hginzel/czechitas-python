# 02.py ----------------------------------------------
colors = ["pink", "blue", "red", "green"]
# number of items
print(len(colors))
# add new item at the end of array
colors.append("black")
print(colors)


# 04.py ----------------------------------------------
colors = ["pink", "blue", "red", "green"]
for color in reversed(colors):
    print(color)


# 05.py ----------------------------------------------
colors = [["pink", 0xFF1493], ["blue", 0x0000FF], ["red", 0xFF0000], ["green", 0x00FF00]]
# 1st solution
for color in colors:
    print(f"{color[0]}\r\n{color[1]:x}")


# 2nd solution
for color in colors:
    for parts in color:
        print(parts)

# reading from file
print("Reading from file")
with open('colors.txt') as f:
    colors = f.readlines()

print(colors)


# 06.py ----------------------------------------------
favorite = "blue"
for color in colors:
    # Check if color is my fovorite one
    if color[0] == favorite:
        print(f"I like x:{color[1]:x}")
    else:
        print(f"Don't like {color[0]} color")


# 07.py ----------------------------------------------
def printColor(c, n):
    return "{sc0}:x:{n:x}"

# Array (list) of colors
colors = [["pink", 0xFF1493], ["blue", 0x0000FF], ["red", 0xFF0000], ["green", 0x00FF00]]

for color in colors:
    print(printColor(color[0], color[1]))

# 08.py ----------------------------------------------
import urllib.request

req = urllib.request.Request("http://stepanb-python.azurewebsites.net/")
resp = urllib.request.urlopen(req)

if (resp.getcode() != 200):
    exit()

content = resp.read()
print(content)
