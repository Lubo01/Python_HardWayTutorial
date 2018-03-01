#starter car game

#branch: points distribution 

skoda_dice = 2
nissan_dice = 1
audi_dice = 3

score = [["Skoda ", skoda_dice,0],["Nissan", nissan_dice,0],["Audi  ", audi_dice,0]]
print "score>", score

result_table = sorted(score, key=lambda x: x[1], reverse = True)

print "\n Race Result table:\n "
print "\t", result_table [0][0], ":", result_table [0][1]
print "\t", result_table [1][0], ":", result_table [1][1]
print "\t", result_table [2][0], ":", result_table [2][1], "\n\n"

print "result_table>",result_table

points = result_table [:]
print "points>",points

# points[0].append(0)
# points[1].append(0)
# points[2].append(0)
#print "points added>",points

points[0][2] += 5
points[1][2] += 3
points[2][2] += 2
print "points increased>", points

# del points[0][1]
# del points[1][1]
# del points[2][1]
#print "points cleaned>",points

print "\n Tournament ranking table:\n "
print "\t", points [0][0], ":", points [0][2], " points"
print "\t", points [1][0], ":", points [1][2], " points"
print "\t", points [2][0], ":", points [2][2], " points", "\n\n"