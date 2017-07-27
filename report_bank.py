# Good tutorial:
# https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

canvas = canvas.Canvas("report.pdf")
#print(canvas.getAvailableFonts())

import sqlite3
conn = sqlite3.connect('./demo/db.sqlite3')
c = conn.cursor()
#c.execute("SELECT name FROM sqlite_master;")
#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(c.fetchall()), print("\n")
SUMMA = 0.00
#canvas.drawString(30,750,'OFFICIAL COMMUNIQUE')
#print ("SUMMA perioda sākumā: %7.2f\n"%(SUMMA))
#canvas.drawString(30,750,("SUMMA perioda sākumā: %7.2f"%(SUMMA)))
#canvas.line(480,747,580,747)

i = 0

for row in c.execute('SELECT * FROM report_app_seriousbank order by dateExecute, charDocument;'):
    canvas.setLineWidth(.3)
    canvas.setFont('Courier', 12)

    #print (row)
    i = i + 1
    #print ("Dokumenta numurs: %10s\tIzpildīšanas datums: %16s"%(row[1],row[13]))
    canvas.drawString(30,800-i*100,("Dokumenta numurs: %10s        Izpildīšanas datums: %16s"%(row[1],row[13])))

    #print ("Maksātājs: %17s\tMaksātāja rģ. numurs: %15s"%(row[2],row[3]))
    #print ("Maksātāja konts: %11s\t%s"%(row[4],row[5]))
    canvas.drawString(30,800-10-i*100,("Maksātājs: %16s         Maksātāja rģ. numurs: %15s"%(row[2],row[3])))
    canvas.drawString(30,800-20-i*100,("Maksātāja konts: %10s         %s"%(row[4],row[5])))

    #print ("Saņēmējs: %18s\tSaņēmēja rģ. numurs: %16s"%(row[6],row[9]))
    #print ("Saņēmēja konts: %12s\t%s"%(row[7],row[8]))
    canvas.drawString(30,800-30-i*100,("Saņēmējs: %18s       Saņēmēja rģ. numurs: %16s"%(row[6],row[9])))
    canvas.drawString(30,800-40-i*100,("Saņēmēja konts: %12s       %s"%(row[7],row[8])))

    #print ("Maksājuma mērķis: %s"%(row[11]))
    #print ("\t\t      Summa:\t%5.2f"%(row[10]))
    #print ("       Pakalpojuma izmaksas:\t%5.2f\n"%(row[12]))
    canvas.drawString(30,800-50-i*100,("Maksājuma mērķis: %s"%(row[11])))
    canvas.drawString(30,800-60-i*100,("                     Summa:\t%5.2f"%(row[10])))
    canvas.drawString(30,800-70-i*100,("       Pakalpojuma izmaksas:\t%5.2f\n"%(row[12])))

    SUMMA = SUMMA + row[10] + row[12]
    if i%2 == 0:
       i = 0
       #print("Starpsumma: %7.2f\n"%(SUMMA))
       canvas.drawString(30,200,("Starpsumma: %7.2f\n"%(SUMMA)))
       canvas.showPage()

#print ("Summa perioda beigās: %7.2f"%(SUMMA))
canvas.drawString(30,100,("Summa perioda beigās: %7.2f"%(SUMMA)))
canvas.save()


'''
charDocument; dateExecute;
charPayer; charPayerReg; charPayerAccount; charPayerBank
charReceiver; charReceiverAccount; charReceiverBank; charReceiverReg
floatSum; charAim; floatCost
'''
