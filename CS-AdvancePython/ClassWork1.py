# -*- coding: utf-8 -*-
"""
ClassWork 1
By: Neslie Fernandez
"""

# Q1 

'''
A:
    Create a function that converts miles to kilometers and kilometers to miles.
    You should be able to specify whether you want to do a mile or kilometer conversion.
'''
  
def convert_metrics(unit_value, unit_convert):
    
    miles_to_kilo_conversion = 1.61
    kilo_to_miles_conversion = 1 / 1.61
    
    if(unit_convert == 'k'):
        return unit_value * miles_to_kilo_conversion
    else:
        return unit_value * kilo_to_miles_conversion
    
'''
B:
    Create a function that does the same as A but this time with a little tweak:
    Now the user can specify which unit of measurement they enter and the output they want it in, in particular the function should ask the user if they're using feet, meters, miles or kilometers. 
    Additionally the function should ask the user in what unit type they want to return their output.
'''

def convert_tweek():
    print("Choices: feet, meters, miles or kilometers ")
    input_measure = askMeasureInput()
    output_measure = askMeasureOutput()
    input_value = askUserUnitValue()
    print(convert_the_metrics(input_measure, output_measure, input_value))
    

def convert_the_metrics(measure_start, measure_end, unit_value):
    feet_to_feet = unit_value
    feet_to_meter = unit_value / 3.281
    feet_to_miles = unit_value / 5280
    feet_to_kilo = unit_value / 3281
    
    meter_to_feet = unit_value * 3.281
    meter_to_meter = unit_value
    meter_to_miles = unit_value / 1609
    meter_to_kilo = unit_value / 1000
    
    miles_to_feet = unit_value * 5280
    miles_to_meter = unit_value * 1609
    miles_to_miles = unit_value
    miles_to_kilo = unit_value * 1.609
    
    kilo_to_feet = unit_value * 3281
    kilo_to_meter =  unit_value * 1000
    kilo_to_miles = unit_value / 1.609
    kilo_to_kilo = unit_value
    
    
    if(measure_start == 'f'):
        if(measure_end == 'f'):
            return feet_to_feet
        elif(measure_end == 'me'):
            return feet_to_meter
        elif(measure_end == 'm'):
            return feet_to_miles
        elif(measure_end == 'k'):
            return feet_to_kilo
        
    elif(measure_start == 'me'):
        if(measure_end == 'f'):
            return meter_to_feet
        elif(measure_end == 'me'):
            return meter_to_meter
        elif(measure_end == 'm'):
            return meter_to_miles
        elif(measure_end == 'k'):    
            return meter_to_kilo
        
    elif(measure_start == 'm'):
        if(measure_end == 'f'):
            return miles_to_feet
        elif(measure_end == 'me'):
            return miles_to_meter
        elif(measure_end == 'm'):
            return miles_to_miles
        elif(measure_end == 'k'):    
            return miles_to_kilo
        
    elif(measure_start == 'k'):
        if(measure_end == 'f'):
            return kilo_to_feet
        elif(measure_end == 'me'):
            return kilo_to_meter
        elif(measure_end == 'm'):
            return kilo_to_miles
        elif(measure_end == 'k'):    
            return kilo_to_kilo


    
def safetyMeasure():
    user_input = input("Please specify the unit of measurement: ")
    if user_input == 'feet':
        return 'f'
    elif user_input == 'meters':
        return 'me'
    elif user_input == 'miles':
        return 'm'
    elif user_input == 'kilometers':
        return 'k'
    else:
        print("Wrong input, please try again")
        safetyMeasure()
    
    
    
def askMeasureInput():
    print("For the Input Measurement")
    input_measure = safetyMeasure()
    return input_measure

def askMeasureOutput():
    print("For the Output Measurement")
    output_measure = safetyMeasure()
    return output_measure
    
def askUserUnitValue():
    user_value = input("Please enter the unit value: ")
    user_value = float(user_value)
    return user_value


'''
 C: 
     Create a function that is similar to A except this time it is for Fahrenheit, Celcius and Kelvin. 
     The function should offer all three temperature measures given the temperature and the unit type.
'''

def convert_metrics_3():
    input_measurement1 = choose_input_measure()
    input_value1 = choose_input_value()
    convert_text = unit_conversion(input_value1, input_measurement1)
    print(convert_text)



def unit_conversion(unit_value, measure_in):
    fvalue = ""
    cvalue = ""
    kvalue = ""
    
    if(measure_in == 'f'):
        fvalue = unit_value
        cvalue = (unit_value - 32) * (5 / 9) 
        kvalue = cvalue + 273.15 
    if(measure_in == 'c'):
        fvalue = (unit_value * (9/5)) + 32
        cvalue = unit_value
        kvalue = (unit_value + 273.15)
    if(measure_in == 'k'):
        fvalue = (unit_value - 273.15) * (9 / 5) + 32
        cvalue = (unit_value - 273.15)
        kvalue = unit_value
    text = f"You Entered {unit_value} {measure_in}\n For Fahrenheit: {fvalue}\n For Celcius: {cvalue}\n For Kelvin: {kvalue}"
    return text

def choose_input_measure():
    print("Input Measurement")
    print("Choices: Fahrenheit, Celcius, or Kelvin as the input measurement")
    input_me = safetyMeasure2()
    return input_me


def choose_input_value():
    input_value_1 = input("Please enter the Input Value: ")
    input_value_1 = float(input_value_1)
    return input_value_1

def safetyMeasure2():
    user_input = input("Please specify the unit of measurement: ")
    if user_input.lower() == 'fahrenheit':
        return 'f'
    elif user_input.lower() == 'celcius':
        return 'c'
    elif user_input.lower() == 'kelvin':
        return 'k'
    else:
        print("Wrong input, please try again")
        safetyMeasure2()



#Q2:

'''
    A:
        Create a function that can convert seconds to minutes, hours and days your output should be a combination of all three
'''

def convert_seconds(input_value):
    s_minute = input_value / 60
    s_hour = input_value / 3600
    s_day = input_value / 86400

    text1 = f"For Seconds\n {s_minute} minutes \n {s_hour} hours \n {s_day} days"
    print(text1)

'''
    B:
        Create a function that given a distance traveled and the amount of time provided (in seconds) gives the average kilometers and the average miles per hour.

'''

def convert_distance_average(input_distance, input_seconds):
    # per hour
    per_hour = input_seconds / 3600
    k_avg_kilometers = input_distance / per_hour
    m_avg_kilometers = (input_distance / 1.609) / per_hour
    
    m_avg_miles = input_distance  + per_hour
    k_avg_miles = (input_distance * 1.609) + per_hour
    
    text_k = f"For Kilometers\n {k_avg_kilometers} kilometers per hour\n  {m_avg_kilometers} miles per hour\n"
    text_m = f"For Miles\n {m_avg_miles} miles per hour\n {k_avg_miles} kilometers per hour\n"
    ans_a = text_k + text_m
    print(ans_a)
    
'''
    C:
        Create a function that given the amount of time traveled (in seconds) and the average kilometers per hour, returns the total distance traveled
 '''
 
def convert_distance(input_time, input_k_avg):
     # Distance = speed * time
     # Time = Distance / Speed
     # Speed = Distance / time
     per_hour1 = input_time / 3600
     dtraveled = input_k_avg * per_hour1
     text_3 = f"Average Kilometers per Hour {input_k_avg} with amount of time traveled in seconds {input_time}\n"
     text_4 = f"Distance Traveled = {dtraveled} Kilometers\n"
     ans_2 = text_3 + text_4
     print(ans_2)
     

 
'''
Q3: Running
    Someone told you it's healthy to run and you want to try out this routine for yourself (wow, isn't that just a genius idea!>!)
    Because you're a software developer, you have enough money to live by a warm beachfront (think Long Beach or Collins Avenue in Miami). You want to algorithmically figure out running by steadily increasing your pace and improving the amount of time you can run. 

    However, you can only run for one hour a day...
'''
'''
    A: On the boardwalk
        Running on the boardwalk is pretty easy. To start off you can run 1 mile on the boardwalk in 25 minutes (this is more jogging than running...)

        The more you run, the faster you can run. For every ten miles you run on the boardwalk, your time to run decreases by 2 minutes, 
        until you reach a hard limit of 1 mile per 7 minutes (don't ask me how I know this :D )

        ^^^Given a pace you want to achieve, how many days of running on the boardwalk will it take you to achieve that pace?^^^
'''

# Constraint: You can only Run for ONE HOUR a day

# Thought Process: If we had a steady pace we could run for 4 miles per hour with 1 session
# We Already 1 mile in 25 minutes
# Therefore we have 35 minutes left 
# But Every 10 miles we hit a booster that speeds us up and decreases our time by 2 minutes
# Goal is 1 mile per 7 minutes (Whoa that's fast)
# How many days of the running in the boardwalk will it take you to achieve the pace

# Day 1 = 2 Miles (50 Minutes / 10 Minutes Left)
# Day 2 = 2 Miles (50 Minutes / 10 Minutes Left)
# Day 3 = 2 Miles (50 Minutes / 10 Minutes Left)
# Day 4 = 2 Miles (50 Minutes / 10 Minutes Left)
# Day 4 they hit 10 Miles
# Therefore we decrease the time by 2 minutes

# Day 5 = 2 Miles (46 Minutes / 14 Minutes Left)
# Day 6 = 2 Miles (46 Minutes / 14 Minutes Left)
# Day 7 = 2 Miles (46 Minutes / 14 Minutes Left)
# Day 8 = 2 Miles (46 Minutes / 14 Minutes Left)
# Day 8 they hit 10 Miles
# Therefore we decrease the time by 2 minutes

# Day 9 = 2 Miles (44 Minutes / 16 Minutes Left)
# Day 10 = 2 Miles (44 Minutes / 16 Minutes Left)
# Day 11 = 2 Miles (44 Minutes / 16 Minutes Left)
# Day 12 = 2 Miles (44 Minutes / 16 Minutes Left)
# Day 12 they hit 10 Miles
# Therefore we decrease the time by 2 minutes 

# Day 13 = 2 Miles (42 Minutes / 18 Minutes Left)
# Day 14 = 2 Miles (42 Minutes / 18 Minutes Left)
# Day 15 = 2 Miles (42 Minutes / 18 Minutes Left)
# Day 16 = 2 Miles (42 Minutes / 18 Minutes Left)
# There we decrease the time by 2 Minutes

# We hit the Half Way Point
# It takes him 20 Minutes Per Mile Now
# Day 17 = 2 Miles (40 Minutes / 20 Minutes Left)
# Day 18 = 2 Miles (40 Minutes / 20 Minutes Left)
# Day 19 = 2 Miles (40 Minutes / 20 Minutes Left)
# Day 20 = 2 Miles (40 Minutes / 20 Minutes Left)
# 8 Miles + 4 = 12 Miles 


# Day 21 = 2 Miles (38 Minutes / 22 Minutes Left)
# Day 22 = 2 Miles (38 Minutes / 22 Minutes Left)
# Day 23 = 2 Miles (38 Minutes / 22 Minutes Left)
# Day 24 = 2 Miles (38 Minutes / 22 Minutes Left)
# 8 Miles + 2 Miles etc 

# Answer: 100 days if we ran daily
    
def runnerMethod1():
    daily_minute_cap = 60
    day_count = 0
    miles_count = 0
    remaining_minute = 0
    per_mile = 25
    
    while per_mile >= 7:
        
        remaining_minute = remaining_minute + (daily_minute_cap - per_mile)
        miles_count = miles_count + 1
        
        if(remaining_minute == per_mile):
            miles_count = miles_count + 1
            
        if miles_count == 10:
            per_mile = per_mile - 2
            miles_count = 0
        
        #print(per_mile)
        day_count = day_count + 1
        
    print(day_count)
    return day_count




'''
    B: On the beach
        Running on the beach is a little more difficult...to start off you can run 1 mile in 40 minutes. 
        However for every 7 miles you run, you'll be able to improve your pace by 3 minutes, 
        until you hit a hard limit of 1 mile per 10 minutes.

        The other problem is that if you run over 3.5 miles on the beach in 4 days, you'll exhaust yourself and you won't be able to run for the 3 following days.

        ^^^Given those constraints and a pace you want to achieve, what is the minimal number of days of running on the beach to achieve the pace you'd like to achieve.
'''

# Thought Process: Starting from the beach we begin with 1 mile in 40 minutes
# Therefore we only have 20 minutes left to run because we can only run ONE HOUR a day
# Every 7 miles we run we improve by 3 minutes therefore we lose 3 minutes 
# Until we hit a hard limit of 1 mile per 10 minutes
# Constraint: If you run over 3.5 miles on the beach in 4 days, it exhaust you 
# therefore we have to take 3 days off
#  Minimal Number of days to achieve the pace. 1 mile per 10 minutes

# Answer: 114 Days

def runnerMethod2():
    daily_minute_cap = 60
    day_count = 0
    four_days = 0
    miles_count = 0
    remaining_minute = 0
    per_mile = 40
    
    while per_mile >= 10:
        
        remaining_minute = remaining_minute + (daily_minute_cap - per_mile)
        miles_count = miles_count + 1
        four_days = four_days + 1
        
        
        if(remaining_minute == per_mile):
            miles_count = miles_count + 1
            
        if miles_count == 7:
            per_mile = per_mile - 3
            miles_count = 0
        
        if miles_count == 3.5 and four_days == 4:
            day_count = day_count + 3
            four_days = 0
        else:
            day_count = day_count + 1
            
        #print(per_mile)
        
    print(day_count)
    return day_count

'''
    C: Putting the two together

        Given the constraints in A and B above and a pace, what is the minimal number of days you'll need to achieve your pace?
        Assume that running on the boardwalk can increase your beach running speed by 1.5 minutes for every 10 miles.
        Also assume that running on the beach can increase your boardwalk running speed by 4.5 minutes for every 7 miles.
'''
# Thought Process: The constraints in A and B above a pace, what is the minimal number of days we'll need to achievemy pace.
# Running on the boardwalk gives us a speed boost of 1.5 miles for every 10 minutes
# The beach increases my boardwalk running by 4.5 minutes for every 7 miles

# Answer: 
# Beach = 209 Days
# Broadwalk = 110 Days


def runnerMethod3(runPath):
    daily_minute_cap = 60
    day_count = 0
    four_days = 0
    miles_count = 0
    remaining_minute = 0
    per_mile = 40
    
    # Beach
    if(runPath == 'Beach'):
        
        while per_mile >= 10:
            
            remaining_minute = remaining_minute + (daily_minute_cap - per_mile)
            miles_count = miles_count + 1
            four_days = four_days + 1
              
            if(remaining_minute == per_mile):
                miles_count = miles_count + 1
            
            if miles_count == 10:
                per_mile = per_mile - 1.5
                miles_count = 0
                
            if miles_count == 3.5 and four_days == 4:
                day_count = day_count + 3
                four_days = 0
            else:
                day_count = day_count + 1
            
    if(runPath == 'Broadwalk'):
        
        while per_mile >= 7:
            
            remaining_minute = remaining_minute + (daily_minute_cap - per_mile)
            miles_count = miles_count + 1
            four_days = four_days + 1
            
            
            if(remaining_minute == per_mile):
                miles_count = miles_count + 1
            
            if miles_count == 7:
                per_mile = per_mile - 4.5
                miles_count = 0
                
            if miles_count == 3.5 and four_days == 4:
                day_count = day_count + 3
                four_days = 0
            else:
                day_count = day_count + 1
                
            day_count = day_count + 1
        
        
    print(day_count)
    return day_count


'''
    D: An array of locations, speeds, constraints and resulting speedups

        You are not required to code this question, but it is something you might see on an interview.
        Given any number of locations, the initial speeds you can run in them, constraints (like in question B) and the ability to run in any of them at any given time, 
            construct an algorithm that produces the optimal combination of those locations and runtimes to give you the best pace you can achieve in a limited time.
        
        You do not have to code this! But you should think about this, because you may well have to answer a question like this in a timed interview...
'''

# Though Process: 
    # We will use an 
    # array of locations
    # Speed
    # Constraints
    # Resulting Speedups
    
#if __name__ == "__main__":
   #ans = convert_metrics(20, "m")
   #print(ans)
   #ans1 = convert_metrics_3()
   #print(ans1)
   #ans2 = convert_seconds(60)
   #print(ans2)
   #ans3 = convert_distance(1,20)
   #print(ans3)
   #ans4 = convert_distance(3600 * 4, 70)
   #print(ans4)
   #runnerMethod1() # 100
   #runnerMethod2() # 76
   #runnerMethod3("Beach") # 209
   #runnerMethod3("Broadwalk") # 110