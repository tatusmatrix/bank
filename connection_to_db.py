import sqlite3
conn = sqlite3.connect('./demo/db.sqlite3')
c = conn.cursor()
#c.execute("SELECT name FROM sqlite_master;")
#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(c.fetchall()), print("\n")
SUMMA = 0.00
print ("SUMMA perioda sākumā: %7.2f\n"%(SUMMA))
i = 0
for row in c.execute('SELECT * FROM report_app_seriousbank order by dateExecute, charDocument;'):
    #print (row)
    i = i + 1
    print ("Dokumenta numurs: %10s\tIzpildīšanas datums: %16s"%(row[1],row[13]))

    print ("Maksātājs: %17s\tMaksātāja rģ. numurs: %15s"%(row[2],row[3]))
    print ("Maksātāja konts: %11s\t%s"%(row[4],row[5]))

    print ("Saņēmējs: %18s\tSaņēmēja rģ. numurs: %16s"%(row[6],row[9]))
    print ("Saņēmēja konts: %12s\t%s"%(row[7],row[8]))

    print ("Maksājuma mērķis: %s"%(row[11]))
    print ("\t\t      Summa:\t%5.2f"%(row[10]))
    print ("       Pakalpojuma izmaksas:\t%5.2f\n"%(row[12]))
    SUMMA = SUMMA + row[10] + row[12]
    if i%2 == 0:
       print ("Starpsumma: %7.2f\n"%(SUMMA))

print ("Summa perioda beigās: %7.2f"%(SUMMA))

'''
charDocument; dateExecute;
charPayer; charPayerReg; charPayerAccount; charPayerBank
charReceiver; charReceiverAccount; charReceiverBank; charReceiverReg
floatSum; charAim; floatCost
'''
