# read file dry and split
f = open("dry.txt", "r")
lines = f.readlines()

list_lines = []
for i in lines:
    list_lines += [i.split('|')]

phrases = []
for i in list_lines:
    try:
        phrases.append(i[2])
    except Exception as e:
        continue

phrases_list = []
for i in phrases:
    phrases_list += [i.split(':')]

list_phrases = []
for i in phrases_list:
    try:
        list_phrases.append(i[1])
    except Exception as e:
        continue

# write into file
f = open("phrase.txt", "w")
for i in list_phrases:
    f.writelines(i)
