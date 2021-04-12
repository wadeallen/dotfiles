#!/usr/bin/env python3

import todoist
import config
import calendar
from datetime import date, timedelta

# get  year
year=2021

class LiturgicalYear:
    def __init__(self, year, v2 = False):
        #v2 = "Vatican II" and refers to the reforms made to the calendar
        #which were adopted my many Protestant denominations in the 1970's
        #The only significant change for our purposes, is the date of
        #Transfiguration Sunday, which in turn is used to calculate the number
        #of Sundays after Epiphany.
        self.init_calendar(year, v2)

    def calc_easter(self, year):
        "Returns easter as a date object."
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1    
        return date(year, month, day)
    
    def init_calendar(self, year, v2 = False):
        self.vatican2 = v2
        self.easter = self.calc_easter(year)
        
        #The first Sunday in Advent is always on or after November 27th
        nov27day = date(year, 11, 27).isoweekday()
        if nov27day == 7:
            self.advent1 = date(year, 11, 27)
        else:
            self.advent1 = date(year, 11, 27) + timedelta(7 - nov27day)
            
        self.advent4 = self.advent1 + timedelta(21)
            
        #Now calculate the date of the next First Sunday in Advent in order to
        #calculate Sundays after Trinity.
        nov27day = date(year + 1, 11, 27).isoweekday()
        if nov27day == 7:
            next_advent1 = date(year + 1, 11, 27)
        else:
            next_advent1 = date(year + 1, 11, 27) + timedelta(7 - nov27day)
        
        #First Sunday after Epiphany
        jan6day = date(year + 1, 1, 6).isoweekday()
        if jan6day == 7:
            self.epiphany1 = date(year, 1, 13)
        else:
            self.epiphany1 = date(year, 1, 13) - timedelta(jan6day)
        
        #A bunch of easy ones:    
        self.epiphany = date(year + 1, 1, 6)
        if v2:
            self.transfiguration = self.easter - timedelta(49)
        else:
            self.transfiguration = self.easter - timedelta(70)
        self.septuagesima = self.easter - timedelta(63)
        self.ashWednesday = self.easter - timedelta(46)
        self.lentsunday = self.easter - timedelta(42)
        self.maundyThursday = self.easter - timedelta(3)
        self.goodFriday = self.easter - timedelta(2)
        self.palmSunday = self.easter - timedelta(7)
        self.ascension = self.easter + timedelta(39)
        self.pentecost = self.easter + timedelta(49)
        self.trinity = self.easter + timedelta(56)
        self.trinityLast = next_advent1 - timedelta(7)
        self.pentecostLast = self.trinityLast
        
        #Sundays after Epiphany and Trinity/Pentecost
        #Note: Epiphany Sundays include Transfiguration
        self.epiphanySundays = (self.transfiguration - self.epiphany1).days / 7 + 1
        self.trinitySundays = (next_advent1 - self.trinity).days / 7 - 1
        self.pentecostSundays = self.trinitySundays + 1
        
        #And finally, American Thanksgiving - which shouldn't even be here,
        #but too many people complain if it's not:
        nov1day = date(year, 11, 1).isoweekday()
        if nov1day <= 4:
            self.thanksgiving = date(year, 11, 26 - nov1day)
        else:
            self.thanksgiving = date(year, 11, 33 - nov1day)
        self.thanksgiving_sun = self.thanksgiving - timedelta(4)



# Easter next year

epiphany=LiturgicalYear(year).epiphany1
lent=LiturgicalYear(year).lentsunday
palmSunday=LiturgicalYear(year).palmSunday

easter=LiturgicalYear(year).easter
pentecost=LiturgicalYear(year).pentecost

thanksgiving_sun=LiturgicalYear(year).thanksgiving_sun

advent=LiturgicalYear(year).advent1
advent4=LiturgicalYear(year).advent4


# Now Add tasks to Todoist

api = todoist.TodoistAPI(config.todoist_api)

# #function to add item
def addTodo(holiday,task):
    notify_date = holiday - timedelta(5)
    notify_date = str(notify_date)
    item = api.items.add(f"{task}", project_id=2262511090, date_string=notify_date)

addTodo(epiphany,"Epiphany banners hung this week")
addTodo(lent,"Lent banners hung this week")
addTodo(palmSunday,"Palm Sunday banners hung this week")
addTodo(easter,"Easter banners hung this week")
addTodo(pentecost,"Pentecost banners hung this week")
addTodo(thanksgiving_sun,"Thanksgiving banners hung this week")
addTodo(advent,"Advent banners hung this week")
addTodo(advent4,"Christmas/Christmas Eve banners hung this week")

api.commit()



