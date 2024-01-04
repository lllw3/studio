# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:25:12 2020
@author: Lenovo
"""



from PyPDF4 import PdfFileReader
import re

def extract_info(pdf_path):
    with open(pdf_path,'rb') as f:
        pdf=PdfFileReader(f)
        page_a=pdf.numPages
        x=[]
        word=input('输入要查询的词')
        for i in range(page_a):
            page=pdf.getPage(i)
        for pageNum in page:
            match=re.findall(r'word\s',pdf)
            x.append(match)
    print('出现次数为'+str(x))
            
         # pdf=pdffilereader(f)
    #     info=pdf.getDocumentInfo()
    #     number_of_pages=pdf.getNumPages()
    # txt=f"""
    # Information about{pdf_path}:     
    # Author:{}
    # Creater:{}
    # Producer:{}
    # Subject:{}
    # Tittlr:{}
    # NumOfPages:{}
    # """
    # print(txt)
    # return info
if __name__=='__main__':
     # path='xx.pdf'
    pdf_path='f:/算法面试编程宝典.pdf'
    extract_info(pdf_path)