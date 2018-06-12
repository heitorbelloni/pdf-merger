import datetime, os, PyPDF2

def get_folder(folder_name):
    current_folder = os.getcwd()
    folder = os.path.join(current_folder, folder_name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def get_pdf_files_from_folder(folder):
    pdf_files = []
    for file_name in os.listdir(folder):
        if file_name.endswith('.pdf'):
            full_file_name = os.path.join(folder, file_name)
            pdf_files.append(full_file_name)
    pdf_files.sort(key = str.lower)
    return pdf_files

def merge_pdf_files(pdf_files):
    pdf_merger = PyPDF2.PdfFileMerger()
    for file_name in pdf_files:
        pdf_file = open(file_name, 'rb')
        pdf_merger.append(pdf_file)
    return pdf_merger

def get_output_file_name(output_folder):
    now = datetime.datetime.utcnow()
    file_name = now.strftime('%Y%m%d%H%M%S') + '.pdf'
    return os.path.join(output_folder, file_name)

def write_file(pdf_merger, file_name):
    file = open(file_name, 'wb')
    pdf_merger.write(file)

print('pdf merger tool')

input_folder = get_folder('input')
print('looking for pdf files in ' + input_folder)

pdf_files = get_pdf_files_from_folder(input_folder)
file_count = len(pdf_files)
print(str(file_count) + ' files found')

if file_count > 0:
    pdf_merger = merge_pdf_files(pdf_files)
    
    output_folder = get_folder('output')
    print('saving file to ' + output_folder)

    output_file_name = get_output_file_name(output_folder)
    write_file(pdf_merger, output_file_name)
    print('saved file ' + output_file_name)

print('finished')