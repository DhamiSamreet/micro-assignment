import PyPDF2 
#import camelot
#import tabula
import re
import time

start = time.time()

file = "Arihant-general_knowledge.pdf" 
pdfFile = open('Arihant-general_knowledge.pdf', 'rb')  
pdfReader = PyPDF2.PdfFileReader(pdfFile)  
questions=[]
answers=[] 
string=re.compile(r'^[\([1-4]|\*\)]')
#print(string)
#pageObj = pdfReader.getPage(66)
#text=pageObj.extractText()
#result1=re.split(r'\d+\.\n',text)
#for x in result1:
##    print(len(x))
#    if len(x)>20:
#        print(x)
#        print("mistake")
print("Extracting.................................")
for i in range(pdfReader.numPages):
    page = pdfReader.getPage(i)
    text=page.extractText()
    content=re.split(r'\d+\.\n',text)
    content.pop(0)
    for x in content:
        if len(x)<30:
            answers.append(x)
        else:
            m=string.search(str(x))
            if(m==None):
                questions.append(x)
            #questions.append(x)

res = dict(zip(questions,answers))
print("Extraction Done\nWriting....................")
f= open("output.txt","w+")
k=1
#str.decode('utf-8',errors='ignore')
for key,ans in res.items():
    f.write(str(k)+".")
    f.write("\n")
    try:
        f.write(str(key))
    except UnicodeEncodeError:
        pass
    f.write("\n")
    f.write("Answer="+str(ans))
    f.write("------------------------------------------------------------------------------------------\n")
    k=k+1
print("output.txt is ready")
end = time.time()
print("Time Taken:", (end - start))
f.close()
pdfFile.close() 
