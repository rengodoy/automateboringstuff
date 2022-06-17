import random

heads = 0

for i in range(1, 1001):
    if random.randint(0, 1) == 0:
        heads += 1
    if i == 500:
        print('Halfway done!')
    #print('Attempt #' + str(i) + ': Throwing a coin... It\'s a ' + ('head' if random.randint(0, 1) == 0 else 'tail') + '! ... Got ' + str(heads) + ' head(s) so far and ' + str(1000 - heads) + ' tail(s) so far.')

print('Heads came up ' + str(heads) + ' times.')