import sys

# for each of the sentences in the file filter the sentences that only repeat once.

unique = []

for sent in sys.stdin.read().split('\n'):
    sent.strip()
    #print(sent[0])
    if sent not in unique:
        unique.append(sent)

unique = [i.strip() for i in unique]
print('\n'.join(unique))
