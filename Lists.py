week = ['maandag' , 'dinsdag' , 'woensdag' ,'donderdag' ,'vrijdag', 'zaterdag' , 'zondag']
werkdag = [week[i] for i in range(5)]
weekdag = [week[i] for i in range(5,7)]
omgekeerd = [week[i] for i in range(6,-1, -1)]
omgekeerdwerkdag = [week[i] for i in range(4,-1, -1)]
omgekeerdweekdag = [week[i] for i in range(6, 4, -1)]
print (omgekeerdwerkdag)
