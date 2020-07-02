import PyPDF2
import re


def extract_questions(start_page, last_page):

	pdfFileObj = open('Arihant-general_knowledge.pdf', 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

	pages = pdfReader.numPages
	final_dict={}
	qno=1
	c=1

	for page in range(start_page,last_page+1):

		print("==========PAGE " + str(page) + "==============")

		firstPage = pdfReader.getPage(page-1) 
		fp_text=firstPage.extractText()


		quizRegex = re.compile(r'\n\d.\n|\n\d\d.\n')
		mo=quizRegex.findall((fp_text))
		questions=len(mo)

		newfp=fp_text.split('\n')

		for x in range(questions):
			new1,new2=0,0
			qno=c
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
			print(qno, end=' ')
			print("no data is ")
			print(newqs)
			print("===================")
			#final_dict[qno] = newqs
			qno+=1


	pdfFileObj.close()




if __name__ == '__main__':
	chapters= {
		1: [1,65],
		2: [156,163],
		3: [177,183],
		4: [196,251],
		5: [320,341],
		6: [374,413],
		7: [470,479],
		8: [495,514],
		9: [544,583],
		10: [638,680],
		11: [743,783],
		12: [849,914],
		13: [1008,1021],
		14: [1040,1044],
		15: [1054,1058],
		16: [1071,1080],
		17: [1099,1106],
		18: [1120,1121],
		19: [1125,1132],
		20: [1048,1160],
		21: [1182,1186],
		22: [1197,1199],
		23: [1206,1224]
	}

	print("Enter the chapter you want questions from")
	ch=int(input())
	extract_questions(chapters[ch][0], chapters[ch][1])

