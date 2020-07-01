import PyPDF2
import re

pdfFileObj = open('Arihant-general_knowledge.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

pages = pdfReader.numPages
final_dict={}
qno=1

for page in range(pages):
	firstPage = pdfReader.getPage(page) 
	fp_text=firstPage.extractText()


	quizRegex = re.compile(r'\n\d.\n|\n\d\d.\n')
	mo=quizRegex.findall((fp_text))
	questions=len(mo)

	newfp=fp_text.split('\n')

	for x in range(questions):
		new1,new2=0,0
		c=1
		for i in range(len(newfp)):
			if str(c)+"." == newfp[i]:
				new1=i
				c+=1
				break

		for i in range(new1,len(newfp)):
			if str(c)+"." == newfp[i]:
				new2=i
				break

		qs=newfp[new1+1:new2-1]
		qs=''.join(qs)
		newqs=qs.split('(1)',1)
		newqs[1]='(1)'+newqs[1]
		print(x, end=' ')
		print("no data is ")
		print(newqs)
		print("===================")
		final_dict[qno] = newqs
		qno+=1





pdfFileObj.close()