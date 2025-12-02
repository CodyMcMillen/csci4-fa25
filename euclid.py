#python

import math

def euclidian_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

print(euclidian_distance((2, 8), (-2, -5)))

# I chose to do import math because at first when I tried to square root it I didnt know how and I searched devdocs and couyldnt find 
# anything. Eventually I gave up and searcher how to do square root in python 3.9 and what I got is that I have to have import math so 
# that it will allow me to use math.sqrt. I dont know why exactly it does this but I do know if you try to it will say NameError: name 
# 'math' is not defined. You know now that I look back it makes a lot of sense why it wont allow me to use math.sqrt wihtout import math.
# I chose to def euclidian distance just so it wasnt confusing and so I knew what I was doing. but i chose to define it as p1 and p2 as
# the two points that i was trying to find the distance between i found it a lot easier than using x,y. the function really comes from
# wikipidia when I was trying to find information on euclidian distance I wanted to find the exact equation that allows you to get the 
# points. and I chose print because I wanted it to actually show what the distance was between the points that are given and I chose 
# (2,8) and (-2, -5 ) because when you graph it and connect the points the triangle goes through all four quadrants like you wanted us to
