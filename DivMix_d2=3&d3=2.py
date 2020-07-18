import random
import csv
import datetime

def make_Q(No,divisor_D,answer_D):
    a=random.randint(1*10**(divisor_D-1)+1,(1*10**divisor_D)-1)
    b=random.randint(1*10**(answer_D-1)+1,(1*10**answer_D)-1)
    ab='{:,}'.format(a*b)
    Q='{0}÷{1}='.format(ab,a)
    return (No,Q,b)

today = str(datetime.date.today())
TrainingName="DivMix_d2=3&d3=2_"
Filetype=".csv"
Filename= str(TrainingName + today + Filetype)
file = open (Filename,'a')
with open (Filename,'a') as csvFile:
            writer = csv.writer(csvFile,lineterminator ="\n")
            writer.writerow(["No","Q","Answer"])

i=1
while i<=25:
    j=random.randint(1,10)%2
    if j==0:
        l=make_Q(i,2,3)
    else:
        l=make_Q(i,3,2)
    
    with open (Filename,'a') as csvFile:
        writer = csv.writer(csvFile,lineterminator ="\n")
        writer.writerow(l)
    i=i+1

file.close()