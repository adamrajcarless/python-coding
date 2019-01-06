# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the array.
# For example: ["3:1", "2:2", "0:1", ...]
# Write a function that takes such list and counts the points of our team in the championship. Rules for counting points for each match:
# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point

def points(games):
    count = []
    for score in games:
        a = score[0]
        a = int(a)
        b = score[2]
        b = int(b)
        if a > b:
            count.append(3)
        elif a < b:
            count.append(0)
        elif a == b:
            count.append(1)
    return sum(count)

print(points(['1:0', '2:0', '3:0', '4:4', '2:1', '3:1', '4:1', '3:2', '4:2', '1:3']))

# sure there is a less round the houses way to do it than this, but this is how my brain worked it out, so i'm happy :)
