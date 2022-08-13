import random
import collections


#forrolling dice
def roll_dice(n):
    for i in range(1, n):
        yield random.randint(1, 6)


def dice():
    n = 6
    score = 0
    lit = list(roll_dice(n))
    print(lit)
    hold = []
    hld = input('enter the number on dices to hold if no number to hold please press enter ')
    hld = list(hld.split())
    hld = [int(i) for i in hld]
    for j in hld:
        for i in lit:
            if i == j:
                hold.append(i)
                break
    n = 6 - len(hold)
    lit = list(roll_dice(n))
    print(f'roll={lit} ,hold = {hold}')
    hd = input('enter the number on dices to hold if no number to hold please press enter ')
    hd = list(hd.split())
    hd = [int(i) for i in hd]
    for m in hd:
        for n in lit:
            if m == n:
                hold.append(m)
                break
    print('Do you want to remove the before holded list in y/n')
    if input() == 'y':
        print(hold)
        unhold = input('type the number on dice you want to unhold')
        unhold = list(unhold.split())
        unhold = [int(i) for i in unhold]
        for k in unhold:
            for l in hold:
                if k == l:
                    hold.remove(k)
                    break
    n = 6 - len(hold)
    lit = list(roll_dice(n))
    print(f'roll={lit} ,hold = {hold}')
    for i in lit:
        hold.append(i)
    print(f'final dices = {hold}')
    return hold


#for ones
def num_of_ones(player):
    print('for number of ones')
    score = 0
    hold = dice()
    for j in hold:
        if j == 1:
            score += 1
    print(player, "score in ones", "= ", score)
    return score, hold


#for number of twos
def num_of_twos(player):
    print('for number of twos')
    score=0
    hold = dice()
    for j in hold:
        if j == 2:
            score += 2
    print(player, "score in twos ", "= ", score)
    return score, hold


#for number of threes
def num_of_threes(player):
    print('for number of threes')
    score = 0
    hold = dice()
    for j in hold:
        if j == 1:
            score += 3
    print(player, "score in threes", "= ", score)
    return score, hold


#for fours
def num_of_fours(player):
    print('for number of fours')
    score = 0
    hold = dice()
    for j in hold:
        if j == 4:
            score += 4
    print(player, "score in fours ", "= ", score)
    return score, hold


#for fives
def num_of_fives(player):
    print('for number of fives')
    score = 0
    hold = dice()
    for j in hold:
        if j == 5:
            score += 5
    print(player, "score in fives ", "= ", score)
    return score, hold


#for sixes
def num_of_sixes(player):
    print('for number of sixes')
    score = 0
    hold = dice()
    for j in hold:
        if j==6:
            score+=6
    print(player, "score in sixes ", "= ", score)
    return score, hold


#for pairs
def pair(player):
    print('for pair')
    score = 0
    hold = dice()
    hold.sort(reverse=True)
    for i in hold:
        if hold.count(i) >= 2:  # using count function to count the elements
            score = i*2
            break
    print(player, "score in pair ", "= ", score)
    return score, hold


#for two pair
def two_pair(player):
    print('for number of two pair')
    score = 0
    hold = dice()
    hold.sort(reverse=True)
    out = []
    for i in hold:
        if hold.count(i) >= 2:# using count function to count the elements
            for j in range(2):
                out.append(i)
    out = set(out)
    if len(out) == 2:
        for i in out:
            score += 2*i
    else:
        score = 0
    print(player, "score in two pair ", "= ", score)
    return score, hold


#for three of a kind
def three_of_a_kind(player):
    print('for three of a kind')
    score = 0
    hold = dice()
    hold.sort(reverse=True)
    for i in hold:
        if hold.count(i) >= 3:  # using count function to count the elements
            print(i)
            score = i*3
    print(player, "score in three of a kind ", "= ", score)
    return score, hold


#for four of a kind
def four_of_a_kind(player):
    print('for four of a kind')
    score = 0
    hold = dice()
    hold.sort(reverse=True)
    for i in hold:
        if hold.count(i) >= 4:  # using count function to count the elements
            print(i)
            score = i*4
            break
    print(player, "score in four of a kind ", "= ", score)
    return score, hold


#for small straight
def small_straight(player):
    print('for small straight')
    score = 0
    hold = dice()
    hold.sort()
    small_straigt=[1,2,3,4,5]
    if hold == small_straigt:
        score = 15
    print(player, "score in small straight ", "= ", score)
    return score, hold


#for large straight
def large_straight(player):
    print('for large straight')
    score = 0
    hold = dice()
    hold.sort()
    large_straigt = [2,3,4,5,6]
    if hold == large_straigt:
        score = 20
    print(player, "score in large straight ", "= ", score)
    return score, hold


#for full house
def full_house(player):
    print('for full house')
    score = 0
    hold = dice()
    hold.sort(reverse=True)
    out = []
    for i in hold:
        if hold.count(i) == 3:  # using count function to count the elements
            out.append(i)
        elif hold.count(i) == 2:
            out.append(i)
        else:
            pass
        ot = set(out)
        if len(ot) == 2 and len(out) == 5:
            for i in out:
                if hold.count(i)==3:
                    score += (i*3)
                if hold.count(i) == 2:
                    score += i*2
    print(player, "score in full house ", "= ", score)
    return score, hold


#for chance
def chance(player):
    print('for chance')
    score = 0
    hold = dice()
    score = sum(hold)
    print(player, "score in chance ", "= ", score)
    return score, hold


#for yatzy
def yatzy(player):
    print('for yatzy')
    score = 0
    hold = dice()
    for i in hold:
        if hold.count(i) == 5:  # using count function to count the elements
            print(i)
            score = 50
            break
    print(player, "score in yatzy ", "= ", score)
    return score, hold

player = collections.namedtuple('player',['name','scoring_pad','dice'])
players = []
score_pad = {'num_of_ones': 0, 'num_of_twos': 0, 'num_of_threes': 0, 'num_of_fours': 0, 'num_of_fives': 0, 'num_of_sixes': 0, 'pair': 0, 'two_pair': 0, 'three_of_a_kind': 0, 'four_of_a_kind': 0, 'small_straight': 0, 'large_straight': 0, 'full_house': 0, 'chance': 0, 'yatzy': 0}

print('********************************Welcome to game yatzy********************************')
print('enter the players name and enter "start" to start the game')
num_of_players = 0
while True:
    name = input()
    if name != 'start':
        players.append(player(name, score_pad.copy(),[]))
        num_of_players += 1
    else:
        break

functions = [num_of_ones, num_of_twos, num_of_threes, num_of_fours, num_of_fives, num_of_sixes, pair, two_pair, three_of_a_kind, four_of_a_kind, small_straight, large_straight, full_house, chance, yatzy]
scor = 1

def score_update():
    for fun in functions:
        random.shuffle(players)
        print('-----------')
        for player in players:
            print('-->player',' = ',player[0])
            score, die = fun(player[0])
            funct=fun.__name__
            player.scoring_pad[funct] = score
            player.dice.clear()
            player.dice.append(die)
            print(player)
    for player in players:
        total_score = sum(player[scor].values())
    player_score = dict()
    for player in players:
        player_score[player[0]] = sum(player[scor].values())
    print('-----------final scores-----------')
    for i in range(num_of_players):
        a = max(player_score, key=player_score.get)
        print(f'Total score of {a} = {player_score[a]}')
        del player_score[a]

score_update()
