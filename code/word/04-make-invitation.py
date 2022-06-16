#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import xlrd
from docx import Document
from pathlib import Path, PurePath
import datetime

today = datetime.date.today().strftime('%Y-%m-%d')

customer = './invitation/客户信息.xlsx'
invitation = './invitation/template.docx'
invitation_path = './invitation'

replace_content = {
    '<姓名>': 'no_name',
    '<性别>': 'm_f',
    '<今天日期>': today
}


def generate_invitation():
    doc = Document(invitation)
    for para in doc.paragraphs:
        for key, value in replace_content.items():
            if key in para.text:
                para.text = para.text.replace(key, value)
    file_name = PurePath(invitation_path).with_name(replace_content['<姓名>']).with_suffix('.docx')
    doc.save(file_name)


def get_customer(customer_file: Path):
    data = xlrd.open_workbook(customer_file)
    table = data.sheets()[0]

    customer_number = table.nrows

    for line in range(1, customer_number):
        content = table.row_values(rowx=line, start_colx=0, end_colx=None)
        replace_content['<姓名>'] = content[0]
        replace_content['<性别>'] = content[1]
        print(replace_content)
        generate_invitation()


if __name__ == '__main__':
    get_customer(customer)
