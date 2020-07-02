import PyPDF2
import re


def extract_questions(total_pages):

	#Open the PDF file
	pdfFileObj = open('Arihant-general_knowledge.pdf', 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

	#pages = pdfReader.numPages

	#Final dictionary to store the questions
	final_dict={}
	qno=1
	c=1

	for page in range(total_pages):

		#Extract text from each page
		firstPage = pdfReader.getPage(page) 
		fp_text=firstPage.extractText()


		#regex to determine how many questions there are in each page
		quizRegex = re.compile(r'\n\d.\n|\n\d\d.\n')
		mo=quizRegex.findall((fp_text))
		questions=len(mo)

		#make a list of the string file obtained for each page
		newfp=fp_text.split('\n')

		#do this for each question
		for x in range(questions):
			new1,new2=0,0

			#find the question number
			for i in range(len(newfp)):
				if str(c)+"." == newfp[i]:
					new1=i
					c+=1
					break

			#find the next question number
			for i in range(new1,len(newfp)):
				if str(c)+"." == newfp[i]:
					new2=i
					break

			#insert the data in between to a new list
			qs=newfp[new1+1:new2-1]

			#join this to make a string
			qs=''.join(qs)

			#split the question and multiple choice answers seperately
			newqs=qs.split('(1)',1)
			newqs[1]='(1)'+newqs[1]
			#print(qno, end=' ')
			#print("no data is ")
			#print(newqs)
			#print("===================")

			#add the question and answer to the dictionary
			#key: question number, value: list of MCQs
			final_dict[qno] = newqs
			qno+=1


	#close the PDF file
	pdfFileObj.close()

	#return the final dictionary
	return final_dict



if __name__=='__main__':
	print("Enter how many pages you want questions for: ")
	pages=int(input())
	final_dict={}
	final_dict=extract_questions(pages)

	for i,j in final_dict.items():
		print(i, end='. ')
		print(j)
		print("=============================")