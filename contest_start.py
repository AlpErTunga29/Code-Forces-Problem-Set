
def main():
 
    number_of_test_cases = int(input())
 
 
    for i in range(number_of_test_cases):
        n, x, t = input().split()
        n = int(n) #number of participants
        x = int(x) # starting intervals
        t = int(t) # time required to finish the contest
 
        period = t // x #Period means number of dissatisfaction for each participant.
        
        if(period > n): #When period is greater than number of participants, each participant's dissatisfaction is number of people left in the contest.
                      
            dissatisfaction = (n * (n - 1) ) // 2
        else: #period<=n, participant's dissatisfaction is equal to period. However, if we have period of 3, then last three people have 2,1 and 0
              #dissatisfactions, recpectively.
            dissatisfaction = period * (n-period) + (period * (period-1) ) // 2
            #First part of the formula for n-period number people having period number dissatisfaction and last part for people having last than period
            #number dissatisfaction.
 
        print(dissatisfaction)
 
 
if __name__=="__main__":
    main()
