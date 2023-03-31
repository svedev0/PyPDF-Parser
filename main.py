from tkinter import Tk, filedialog
from tika import parser

file_picker = Tk()
file_picker.withdraw()
file = filedialog.askopenfilename()

with open(file, 'rb') as f:
	input = parser.from_file(f)
	content = input['content']
	content = content.strip()

output = open('pdf_content.txt', mode='w+', encoding='utf-8')
output.write(content)
output.close()
