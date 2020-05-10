#!/usr/bin/python3

import pickle

class Birthday:
    def __init__(self, uid, name, day, month):
        self.uid = uid # Unique identififer for person (required for ics events)
        self.name = name
        self.day = day
        self.month = month

    def __str__(self):
        return f'{self.name} ({self.day}/{self.month})'
    
    def __unicode__(self):
        return u'{self.name} ({self.day}/{self.month})'

    def __gt__(self, other):
        if self.month > other.month:
            return True
        elif self.month < other.month:
            return False
        else:
            return self.day > other.day
    
    def __lt__(self, other):
        if self.month < other.month:
            return True
        elif self.month > other.month:
            return False
        else:
            return self.day < other.day

    def __eq__(self, other):
        return (self.month == other.month and self.day == other.day)


with open('birthdays.pkl', 'rb') as pkl_file:
    birthdays = pickle.load(pkl_file)

count = 0
for birthday in birthdays:
    count += 1
    print(f"{count}: {birthday}")
