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


char_dict.update(small_char_dict)
char_dict.update(capital_char_dict)


with open('input.txt') as file:
  sum = 0
  for line in file:
    line = line.strip('\n')

    first_half = int((len(line) / 2))
    compartment_one = line[0:first_half]
    compartment_two = line[first_half:]

    for char in compartment_one:
      if (char in compartment_two):
        sum+= char_dict[char]
        break;
  
  print(sum)



