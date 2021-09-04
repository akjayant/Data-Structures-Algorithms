#https://interviewprep.appliedroots.com/lecture/2/interview-preparation-course/1005/find-missing-number/18/module-5-problem-solving

n = int(input())
for i in range(n):
    al = int(input())
    x = input().split(" ")
    x = [int(k) for k in x]
    l = len(x)
    #method1 - sum
    sum = 0
    for k in range(len(x)):
        sum+=x[k]

    total_sum = al*(al+1)/2    #--------flaw in method if al is very large may cause numerical overflow
    missing = total_sum - sum
    print(missing)

    #method2 - xor intuition xor-ing two same numbers give 0
    s1 = x[0]
    for k in range(1,len(x)):
        s1=s1^x[k]
    s2 = 1
    for k in range(2,al+1):
        s2=s2^k
    missing = s1^s2
    print(missing)
