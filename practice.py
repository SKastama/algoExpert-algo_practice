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

# print(hackerrankInString('hereiamstackerrank'))

def pangrams(s):
    '''Recieves a string as an input and returns boolean stating if the string is a pangram'''
    # initiate a set variable
    alphabet_set= set()
    for i in range(len(s)):
        alphabet_set.add(s[i].lower())
    if len(alphabet_set)-1 == 26:
        return 'pangram'
    return 'not pangram'

# print(pangrams('We promptly judged antique ivory buckles for the next prize'))
# print(pangrams('We promptly judged antique ivory buckles for the prize'))

def weightedUniformStrings(s, queries):
    '''Takes a string and a query of integers as an input, returns if the weight of characters eqauls an integer within the query array'''
    # Create a output array
    string_weights= []
    output= []
    current= ''
    # Create alphabet string
    alphabet= 'abcdefghijklmnopqrstuvqxyz'
    i= 0
    # weigth of characters
    current_weight= 0
    # initiate while loop
    while i < len(s):
        if s[i] not in current:
            current= ''
            current_weight= 0
        alpha_idx= alphabet.find(s[i])
        current_weight+= alpha_idx + 1
        string_weights.append(current_weight)
        current+= s[i]
        i+=1
    for j in range(len(queries)):
        if queries[j] in string_weights:
            output.append('Yes')
        else:
            output.append('No')
    return output

# print(weightedUniformStrings('abccddde', [6, 1, 3, 12, 5, 9, 10]))





def firstNonRepeatingCharacter(string):
    '''Given a string as input where we are returning the first non-repeated character'''
    characteres_seen= {}
    order_arr= []
    # Initalize a for loop to count how many times a character is seen
    for i in range(len(string)):
        if string[i] not in characteres_seen:
            characteres_seen[string[i]]= 0
            order_arr.append(string[i])
        characteres_seen[string[i]]+= 1
    # Initlize a for loop to find values in dicitonary
    for i in range(len(order_arr)):
        if characteres_seen[order_arr[i]] == 1:
            return order_arr[i]
    return None

# print(firstNonRepeatingCharacter("abbcdcaf"))

def longestSubstringWithoutDuplication(string):
    '''Given a string as input, we return the longest substring without duplicates'''
    longest_substring= ''
    # initalize a string called current that represnts the current substring we are inerating over
    current= ''
    i= 0
    j= i
    while i < len(string):
        if j == len(string):
            i+= 1
            j= i
        # check if element is in current string
        elif string[j] in current:
            if len(current) > len(longest_substring):
                longest_substring= current
            current= ''
            i+= 1
            j= i
        else:
            current+= string[j]
            j+= 1
    return longest_substring

# print(longestSubstringWithoutDuplication("clementisacap"))


def twoStrings(s1, s2):
    '''Two string as inputs, where we are returning a substring that is contained in each inputed strings'''
    # inilize output string to store shared subsequence
    shared_subsequence= ''
    i= 0
    for i in range(len(s1)):
        # check if s1[i] is in s2
        if s1[i] not in s2:
            continue
        # add the s1[i] element to our shared_subsequence
        shared_subsequence+= s1[i]
    # check if shared subsequence is filled
    output= 'YES' if len(shared_subsequence) > 0 else 'NO'
    return output


def longestAnagram(array):
    anagramHash= {}
    longest= []
    for i in range(len(array)):
        sortedAnagram= ''.join(sorted(array[i]))
        if sortedAnagram not in anagramHash:
            anagramHash[sortedAnagram]= [array[i]]
        else:
            anagramHash[sortedAnagram].append(array[i])
    for key in anagramHash.keys():
        if len(longest) == 0:
            longest= anagramHash[key]
        elif len(key) == len(longest[0]):
            longest.append(anagramHash[key])
        elif len(key) > len(longest[0]):
            longest= anagramHash[key]
    return longest

# print(longestAnagram(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))


def longestSequence(words, characters):
    longest= []
    charIdx= 0
    idx= 0
    while idx < len(words):
        for i in range(len(words[idx])):
            if charIdx == len(characters):
                break
            if words[idx][i] == characters[charIdx]:
                charIdx+= 1
        if charIdx == len(characters):
            if len(longest) == 0:
                longest= [words[idx]]
            if len(words[idx]) == len(longest[0]):
                longest.append(words[idx])
            elif len(words[idx]) > len(longest[0]):
                longest= [words[idx]]
        charIdx= 0
        idx+= 1
    return longest

# print(longestSequence(['hello', 'ghelloo', 'ghelloo', 'ee'], 'hello'))


def staircase(n):
    output= ''
    for i in range(n + 1):
        elements= '#' * i
        output+= '{} \n'.format(elements)
    return output

print(staircase(6))