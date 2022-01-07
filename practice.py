parties1= [
    {
        "partyName": "Rodriguez",
        "count": 2
    },
    {
        "partyName": "Smith",
        "count": 2
    }
]
tables1= [
    {
        "tableName": "Table 1",
        "numberOfSeats": 6
    }
]

parties2= [
    {
        "partyName": "Patel",
        "count": 2
    }
]
tables2= [
    {
        "tableName": "Table 1",
        "numberOfSeats": 1
    },
    {
        "tableName": "Table 2",
        "numberOfSeats": 1
    }
]

parties3= [
    {
        "partyName": "Lee",
        "count": 5
    }
]
tables3= [
    {
        "tableName": "Table 1",
        "numberOfSeats": 4
    }
]

def solution1(parties, tables):
    attendees= []
    i= 0
    j= 0
    k= 0
    while i < len(parties):
        while k < len(tables):
            if j >= parties[i]['count']:
                break
            elif tables[k]['numberOfSeats'] > 0:
                attendees.append(str(parties[i]['partyName'] + ' at ' + tables[k]['tableName']))
                tables[k]['numberOfSeats']-= 1
                j+= 1
            else:
                k+= 1
        if k == len(tables) and j < parties[i]['count']:
            return 'We do not have enough seats!'
        i+= 1
        j= 0
    return attendees

# print(solution1(parties1, tables1))
# print(solution1(parties2, tables2))
# print(solution1(parties3, tables3))

parties4= [
    {
        "partyName": "Abara",
        "count": 2,
        "tableSeed": "Table 2"
    }
]
tables4= [
    {
        "tableName": "Table 1",
        "numberOfSeats": 4
    },
    {
        "tableName": "Table 2",
        "numberOfSeats": 4
    }
]

def solution2(parties, tables):
    attendees= []
    i= 0
    j= 0
    k= 0
    while i < len(parties):
        while k < len(tables):
            if j >= parties[i]['count']:
                break
            elif tables[k]['numberOfSeats'] > 0:
                attendees.append(str(parties[i]['partyName'] + ' at ' + tables[k]['tableName']))
                tables[k]['numberOfSeats']-= 1
                j+= 1
            else:
                k+= 1
        if k == len(tables) and j < parties[i]['count']:
            return 'We do not have enough seats!'
        i+= 1
        j= 0
    return attendees

def superReducedString(s):
    string= s
    adjChar= False
    while adjChar is False:
        adjChar= True
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                string= string[:i] + string[i+2:]
                adjChar= False
                break
    if len(string) == 0:
        return 'Empty String'
    return string

def camelcase(s):
    # Initiate a count variable
    if len(s) == 0:
        return 0
    count= 1
    # Loop thru string once with for loop
    for i in range(len(s)):
        if s[i].isupper():
            count+= 1
    return count

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    special_characters = "!@#$%^&*()-+"
    hashTable= {
        'lower': False,
        'upper': False,
        'num': False,
        'spChar': False
    }
    count= 0
    for i in range(len(password)):
        if password[i].islower():
            hashTable['lower']= True
        elif password[i].isupper():
            hashTable['upper']= True
        elif password[i].isnumeric():
            hashTable['num']= True
        elif password[i] in special_characters:
            hashTable['spChar']=True
    for val in hashTable.values():
        if val == False:
            count+= 1
    if len(password)+count < 6:
        count+= 6 - (len(password)+count)
    return count


def caesarCipher(s, k):
    # initalize alphabet characters
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    output= ''
    # for loop
    for i in range(len(s)):
        if s[i].isalpha() is False:
            output+= s[i]
            continue
        if s[i].isupper():
            alphaIdx= alphabet.find(s[i].lower())
        else:
            alphaIdx= alphabet.find(s[i])
        shiftIdx= (alphaIdx+k)%26
        if s[i].isupper():
            output+= alphabet[shiftIdx].upper()
            continue
        output+= alphabet[shiftIdx]
    return output

# print(caesarCipher('middle-Outz', 2))

def hackerrankInString(s):
    '''String as input, returns yes or no if a subsequence within its string spell out      hackerrank'''
    # initailise our comparisn string hackerrank
    compareStr= 'hackerrank'
    i= 0
    j= 0
    # initate a while loop
    while i < len(s):
        if s[i] == compareStr[j]:
            j+= 1
        if j == len(compareStr):
            return 'Yes'
        i+= 1
    return 'No'

print(hackerrankInString('hereiamstackerrank'))