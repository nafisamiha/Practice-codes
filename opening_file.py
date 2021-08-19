#input file name
name=input('Enter file name:')
handle=open(name,'r')

#counting word freq
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
print(words)
#finding most common words
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=words
        bigcount=counts

print(bigword,bigcount)
#done
