import PyPDF2

#after you do all this, make an array of all the files you need
#then, make this a giant for loop and go through each

class Receiver:
    def __init__(self,name, donations, years, total):
        self.name = name
        self.donations = donations
        self.years = years
        self.total = total
    def getName(self):
        return self.name
    def getDonations(self):
        return self.donations
    def getYears(self):
        return self.years
    def getTotal(self):
        return self.total
    def addDonation(self,donation):
        self.donations.append(donation)
    def adjustTotal(self,donation):
        self.total = self.total + donation
    def adjustYears(self,year):
        self.years.append(year)

def yearFunction(listOfReceivers, year):
    top10List = []
    yearTotals = []
    result = []

    for receiver in listOfReceivers:
        yearTotals.append(0)
        for donation in receiver.getDonations():
            if str(receiver.getYears()[receiver.getDonations().index(donation)]) == str(year):
                yearTotals[listOfReceivers.index(receiver)] = yearTotals[listOfReceivers.index(receiver)] + float(donation)

    d=0
    for total in yearTotals:
        if len(top10List) < 25:
            if len(top10List) == 24:
                top10List.append([total,listOfReceivers[d].getName()])
                top10List.sort(reverse = True)
            else:
                top10List.append([total,listOfReceivers[d].getName()])
        elif total > top10List[24][0]:
            top10List.pop(len(top10List)-1)
            top10List.append([total,listOfReceivers[d].getName()])
            top10List.sort(reverse = True)
        d+=1

    '''for item in top10List:
        if top10List.index(item) > 0:
            while top10List.index(item)>0 and item[0] > top10List[top10List.index(item)-1][0]:
                tempItem = top10List[top10List.index(item)-1]
                top10List.pop(top10List.index(item)-1)
                top10List.insert(top10List.index(item)+1,tempItem)'''
            
            
    return top10List

def allTimeList(listOfReceivers):
    top10List = []
    
    for receiver in listOfReceivers:
        if len(top10List) < 10:
            if len(top10List) == 9:
                top10List.append([receiver.getTotal(),receiver.getName()])
                top10List.sort(reverse = True)
            else:
                top10List.append([receiver.getTotal(),receiver.getName()])
        elif receiver.getTotal() > top10List[9][0]:
            top10List.pop(len(top10List)-1)
            top10List.append([receiver.getTotal(),receiver.getName()])
            top10List.sort(reverse = True)
        
    return top10List

def totalPerYear(listOfReceivers,year):
    total = 0
    for receiver in listOfReceivers:
        for donation in receiver.getDonations():
            if str(receiver.getYears()[receiver.getDonations().index(donation)]) == str(year):
                total+= float(donation)

    return total

receiverList = []
donations = []
ignoreTheseWords = []
names = []
years = []

fileNames = ['2020_11daypre.pdf','2020_32daypre.pdf','2020_32dayspecial.pdf','2020_jan.pdf']

    #'2019_10daypost.pdf','2019_11daygen.pdf','2019_11daypre.pdf','2019_27daypost.pdf','2019_32daygen.pdf','2019_32daypre.pdf','2019_jan.pdf','2019_july.pdf']

    #'2018_10daypost.pdf','2018_11daygen.pdf','2018_11daypre.pdf','2018_11dayspec.pdf','2018_27daypost.pdf','2018_27dayspec.pdf','2018_32daygen.pdf','2018_32daypre.pdf',
             #'2018_32dayspec.pdf','2018_jan.pdf','2018_july.pdf']

    #'2017_10daypost.pdf','2017_11daygen.pdf','2017_11daypre.pdf','2017_27daypost.pdf','2017_32daygen.pdf','2017_32daypre.pdf','2017_jan.pdf','2017_july.pdf']

    #'2016_10daypost.pdf','2016_11daygen.pdf','2016_11daypre.pdf','2016_27daypost.pdf','2016_32daygen.pdf','2016_32daypre.pdf','2016_jan.pdf','2016_july.pdf']

for file in fileNames:

    pdfFileObj = open(file,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for x in range(0,pdfReader.numPages):
        pageObj = pdfReader.getPage(x)
        text = pageObj.extractText()
        text = text.upper()

        if text.count("FILER ID:") > 1:
            text = text[text.find("FILER ID:")+10:]

        year = text[text.find("FILER ID:")+9:text.find("FILER ID:")+13]
        
        if text.find("FILER ID:") != -1:
            text = text[text.find("FILER ID:"):]
            
        text = text[text.find('$'):]

        while text.find('$') != -1:
            try:
                donations.append(float(text[text.find('$')+1:text.find('.')+3].replace(',',"")))
            except:
                break
            text = text[text.find('.')+3:]

        if text.find("TOTALNO. OF TRANSACTIONS") != -1:
            text = text[text.find("TOTALNO. OF TRANSACTIONS")+24:]
        else:
            text = text[text.find("RECORD DATE")+11:]

        answer = ""
        name = ""
        keepgoing = True

        print("File: "+file+" Page #: "+str(x+1))
        
        while keepgoing:
            if ((text[:text.find(" ")] in ignoreTheseWords) == True):
                name = name + text[:text.find(" ")]
                text = text[text.find(" ")+1:]
                #can comment the elifs out
                #CAN ALSO MAKE IT SO ELIS APPLY WHEREVER THE WORD IS -- IF ITS NOT -1 AND THE LENGTH IS GREATER, THEN CHECK CUT BASED ON WHERE IT IS
            elif (text[:text.find(" ")].find('COMMITTEESERINO4NYDACC') != -1):
                print("process")
                names.append('NYSDEMOCRATICSENATECAMPAIGNCOMMITTEE')
                years.append(year)
                print('NYSDEMOCRATICSENATECAMPAIGNCOMMITTEE added')
                names.append('SERINO4NY')
                years.append(year)
                print('SERINO4NY added')
                names.append('DACC')
                years.append(year)
                print('DACC added')
                name = text[text.find('DACC')+4:text.find(" ")]
                print(name+" started")
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('PARKERNYSABPRL') != -1):
                print("thing-y")
                name = name + 'PARKER'
                names.append(name)
                years.append(year)
                print(name+" added")
                names.append('NYSABPRL')
                years.append(year)
                print("NYSABPRL added")
                name = ""
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('DACC') != -1 and len(text[:text.find(" ")]) > len('DACC')):
                print("DACC process")
                name = name + text[:text.find('DACC')]
                if len(name)>2:
                    names.append(name)
                    years.append(year)
                    print(name+" added")
                name = 'DACC'
                names.append(name)
                years.append(year)
                print(name+" added")
                name = text[text.find('DACC')+4:text.find(" ")]
                print(name+" started")
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('DSCCELEANOR') != -1):
                print("stupid thing")
                name = name + text[:text.find('DSCC')]
                if len(name)>2:
                    names.append(name)
                    years.append(year)
                    print(name+" added")
                name = 'DSCC'
                names.append(name)
                years.append(year)
                print(name+" added")
                name = text[text.find('DSCC')+4:text.find(" ")]
                print(name+" started")
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('RACC') != -1 and len(text[:text.find(" ")]) > len('RACC') and
                  (text[:text.find(" ")].find('HOUSEKEEPING') and text[text.find(" "):text.find(" ")+15].find("HOUSEKEEPING") == -1) ):
                print("RACC process")
                name = name + text[:text.find('RACC')]
                if len(name)>2:
                    names.append(name)
                    years.append(year)
                    print(name+" added")
                name = 'RACC'
                names.append(name)
                years.append(year)
                print(name+" added")
                name = text[text.find('RACC')+4:text.find(" ")]
                print(name+" started")
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('UNITEMIZED') != -1):
                print("UNITEMIZED process")
                name = name + text[:text.find('UNITEMIZED')]
                if len(name)>2:
                    names.append(name)
                    years.append(year)
                    print(name+" added")
                name = 'UNITEMIZED'
                names.append(name)
                years.append(year)
                print(name+" added")
                name = text[text.find('UNITEMIZED')+10:text.find(" ")]
                print(name+" started")
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('NYSABPRL,INC') != -1):
                print("NYSABPRL process")
                name = name + text[:text.find('NYSABPRL')]
                if len(name)>2:
                    names.append(name)
                    years.append(year)
                    print(name+" added")
                name = 'NYSABPRL,INC'
                names.append(name)
                years.append(year)
                print(name+" added")
                name = text[text.find('NYSABPRL,INC')+12:text.find(" ")]
                print(name+" started")
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('SERINO4NY') != -1):
                print("SERINO4NY process")
                name = name + text[:text.find('SERINO4NY')]
                if len(name)>2:
                    names.append(name)
                    years.append(year)
                    print(name+" added")
                name = 'SERINO4NY'
                names.append(name)
                years.append(year)
                print(name+" added")
                name = text[text.find('SERINO4NY')+9:text.find(" ")]
                print(name+" started")
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")] == 'MURRAYNYSSRCCSICCFRIEND'):
                name = name + 'MURRAY'
                names.append(name)
                years.append(year)
                name = 'NYSSRCC'
                names.append(name)
                years.append(year)
                name = 'SICC'
                names.append(name)
                years.append(year)
                name = 'FRIEND'
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('SICC') != -1 and len(text[:text.find(" ")]) > len('SICC')):
                print("SICC process")
                name = name + text[:text.find('SICC')]
                if len(name)>2:
                    names.append(name)
                    years.append(year)
                    print(name+" added")
                name = 'SICC'
                names.append(name)
                years.append(year)
                print(name+" added")
                name = text[text.find('SICC')+4:text.find(" ")]
                print(name+" started")
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")] == 'TOTALDAVID'):
                name = name + 'DAVID'
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('ASSEMBLY') != -1 and len(text[:text.find(" ")]) > len('ASSEMBLY')+1 and (text[:text.find(" ")].find("MAN")
                or text[:text.find(" ")].find("WOMAN") or text[:text.find(" ")].find("MEMBER")) == -1):
                if text[:text.find(" ")].find('ASSEMBLY') == 0:
                    name = name +text[:len('ASSEMBLY')]
                    names.append(name)
                    years.append(year)
                    name = text[len('ASSEMBLY'):text.find(" ")]
                else:
                    name = name +text[:text[:text.find(" ")].find('ASSEMBLY')]
                    names.append(name)
                    years.append(year)
                    name = text[text[:text.find(" ")].find('ASSEMBLY'):text.find(" ")]
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('SENATE') != -1 and len(text[:text.find(" ")]) > len('SENATE')+1 and text[:text.find(" ")].find('STATE') == -1):
                if text[:text.find(" ")].find('SENATE') == 0:
                    name = name +text[:len('SENATE')]
                    names.append(name)
                    years.append(year)
                    name = text[len('SENATE'):text.find(" ")]
                else:
                    name = name +text[:text[:text.find(" ")].find('SENATE')]
                    names.append(name)
                    years.append(year)
                    name = text[text[:text.find(" ")].find('SENATE'):text.find(" ")]
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('FRIENDS') != -1 and len(text[:text.find(" ")]) > len('FRIENDS')+1):
                if text[:text.find(" ")].find('FRIENDS') == 0:
                    name = name +text[:len('FRIENDS')]
                    names.append(name)
                    years.append(year)
                    name = text[len('FRIENDS'):text.find(" ")]
                else:
                    name = name +text[:text[:text.find(" ")].find('FRIENDS')]
                    names.append(name)
                    years.append(year)
                    name = text[text[:text.find(" ")].find('FRIENDS'):text.find(" ")]
                text = text[text.find(" ")+1:]
            elif (text[:text.find(" ")].find('COMMITTEE') != -1 and len(text[:text.find(" ")]) > len('COMMITTEE')+1):
                if text[:text.find(" ")].find('COMMITTEE') == 0:
                    name = name +text[:len('COMMITTEE')]
                    names.append(name)
                    years.append(year)
                    name = text[len('COMMITTEE'):text.find(" ")]
                else:
                    name = name +text[:text[:text.find(" ")].find('COMMITTEE')]
                    names.append(name)
                    years.append(year)
                    name = text[text[:text.find(" ")].find('COMMITTEE'):text.find(" ")]
                text = text[text.find(" ")+1:]
            else:
                print(text[:text.find(" ")])
                print("Do I need to split this? (y/n) -- type 'done' to end process.")
                answer = input()
                if answer.upper() == 'N':
                    name = name + text[:text.find(" ")]
                    ignoreTheseWords.append(text[:text.find(" ")])
                    text = text[text.find(" ")+1:]
                    #can compile a list of answers, and in future pages not ask if they are within that list
                elif answer.upper().find("DONE") != -1:
                    keepgoing = False
                else:
                    print("What is the first name of the two that need to be split?")
                    answer = input()
                    #you can compile a list of answers, and in future pages automatically add a space after them if there isn't one!!! and recognize that it's the end of a thing
                    #^only do this if desperate b/c it's so overwhelming
                    name = name +text[:len(answer)]
                    names.append(name)
                    years.append(year)
                    name = text[len(answer):text.find(" ")]
                    text = text[text.find(" ")+1:]

        print("------------------------new page------------------------")
        
print("# of Names: "+str(len(names))+" # of Donations: "+str(len(donations))+" # of Years: "+str(len(years)))
print("Donations:")
print(donations)
print()
print("Names")
print(names)
input()

y = 0
for name in names:
    isRepeat = False
    for receiver in receiverList:
        if (name in receiver.getName()) == True:
            receiver.addDonation(donations[y])
            receiver.adjustTotal(donations[y])
            receiver.adjustYears(years[y])
            isRepeat = True
    if isRepeat == False:
        receiverList.append(Receiver(name,[donations[y]],[years[y]],donations[y]))
    y+=1

rawData = open("rawData2020.txt","w")
for receiver in receiverList:
    rawData.write("Name: "+receiver.getName())
    rawData.write(" Donations: ")
    a = 0
    for donation in receiver.getDonations():
        rawData.write("["+str(donation)+", "+str(receiver.getYears()[a])+"]")
        a+=1
    rawData.write(" Total: "+str(receiver.getTotal())+"\n\n")

try:
    rawData.write("[")
    for name in names:
        if names.index(name) != len(names)-1:
            rawData.write(name+",")
        else:
            rawData.write(name+"]\n")

    for donation in donations:
        if donations.index(donation) != len(donations)-1:
            rawData.write(str(donation)+",")
        else:
            rawData.write(str(donation)+"]")
except:
    rawData.close()

rawData.close()

outfile = open("dataFrom2020.txt","w")

top10For2020 = yearFunction(receiverList,'2020')
totalFor2020 = totalPerYear(receiverList,'2020')
outfile.write("Top 10 For 2020 \n\n")

for person in top10For2020:
    outfile.write(str(top10For2020.index(person)+1)+". "+person[1]+" Amount: $"+str(person[0])+"\n")

outfile.write("\nTotal For 2020: "+str(totalFor2020)+"\n")
'''
top10For2019 = yearFunction(receiverList,'2019')
totalFor2019 = totalPerYear(receiverList,'2019')
outfile.write("Top 10 For 2019 \n\n")

for person in top10For2019:
    outfile.write(str(top10For2019.index(person)+1)+". "+person[1]+" Amount: $"+str(person[0])+"\n")

outfile.write("\nTotal For 2019: "+str(totalFor2019)+"\n")

top10For2018 = yearFunction(receiverList,'2018')
totalFor2018 = totalPerYear(receiverList,'2018')
outfile.write("Top 10 For 2018 \n\n")

for person in top10For2018:
    outfile.write(str(top10For2018.index(person)+1)+". "+person[1]+" Amount: $"+str(person[0])+"\n")

outfile.write("\nTotal For 2018: "+str(totalFor2018)+"\n")

top10For2017 = yearFunction(receiverList,'2017')
totalFor2017 = totalPerYear(receiverList,'2017')
outfile.write("Top 10 For 2017 \n\n")

for person in top10For2017:
    outfile.write(str(top10For2017.index(person)+1)+". "+person[1]+" Amount: $"+str(person[0])+"\n")

outfile.write("\nTotal For 2017: "+str(totalFor2017)+"\n")

top10For2016 = yearFunction(receiverList,'2016')
totalFor2016 = totalPerYear(receiverList,'2016')
outfile.write("Top 10 For 2016 \n\n")

for person in top10For2016:
    outfile.write(str(top10For2016.index(person)+1)+". "+person[1]+" Amount: $"+str(person[0])+"\n")

outfile.write("\nTotal For 2016: "+str(totalFor2016)+"\n")

allTimeHighest = allTimeList(receiverList)
outfile.write("\nTop 10 From 2016-2020 \n\n")
for person in allTimeHighest:
    outfile.write(str(allTimeHighest.index(person)+1)+". "+person[1]+" Amount: $"+str(person[0])+"\n")'''

outfile.close()

pdfFileObj.close()
        
        
        
