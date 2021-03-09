n=float(input())
i=0
tab=[]
c="Celsius"
f="Fahrenheit"
k="Kelvin"
help_shit=0.0
result=0.0
final_values=[]
while i!=n:
    tab.append(input().split())
    i+=1
for i in range(len(tab)):

    if tab[i][1]==c:
        help_shit=float(tab[i][0])
        if tab[i][2]==f:
            result=(help_shit*1.8)+32
            if result<-459.67:
                final_values.append("NO")
            else:
                final_values.append(result)
        elif tab[i][2] == k:
            result=help_shit+273.15
            if result<0:
                final_values.append("NO")
            else:
                final_values.append(result)
        else:
            final_values.append(help_shit)

    if tab[i][1]==f:
        help_shit=float(tab[i][0])
        if tab[i][2]==c:
            result=(help_shit-32)/1.8
            if result<-273.15:
                final_values.append("NO")
            else:
                final_values.append(result)
        elif tab[i][2]==k:
            result=(help_shit-32)/(1.8)+273.15
            if result<0:
                final_values.append("NO")
            else:
                final_values.append(result)
        else:
            final_values.append(help_shit)

    if tab[i][1]==k:
        help_shit=float(tab[i][0])
        if tab[i][2]==f:
            result=help_shit*1.8-459.67
            if result<-459.67:
                final_values.append("NO")
            else:
                final_values.append(result)
        elif tab[i][2]==c:
            result=help_shit-273.15
            if result<-273.15:
                final_values.append("NO")
            else:
                final_values.append(result)
        else:
            final_values.append(help_shit)
for i in  range(len(final_values)):
    try:
        print(format(final_values[i], ".2f"))
    except:
        print(final_values[i])
