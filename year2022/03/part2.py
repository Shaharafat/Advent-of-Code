# create two dictionaries that contains 
# capital and small letters with value
small_char_dict = {}
capital_char_dict = {}
char_dict = {}

idx=1

for c in range(ord('a'), ord('z')+1):
  small_char_dict[chr(c)] = idx
  idx+=1

for c in range(ord('A'), ord('Z')+1):
  capital_char_dict[chr(c)] = idx
  idx+=1


# make one complete dictionary
char_dict.update(small_char_dict)
char_dict.update(capital_char_dict)

with open('input.txt') as file:
  line_groups = []
  line_count = 0
  line_group = []
  for line in file:
    line = line.strip('\n')

    line_group.append(line)
    line_count += 1
    if line_count % 3 == 0:
      line_groups.append(line_group)
      line_group = []
    

sum = 0
for lines in line_groups:
  for item in lines[0]:
      if ((item in lines[1]) and (item in lines[2])) :
        sum += char_dict[item]
        break

print(sum)
  



