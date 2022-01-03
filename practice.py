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
