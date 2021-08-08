from pdf2image import convert_from_path

c = 345 
# c = int(input(''))
poppler_path = r'C:/Users/Mert Koksal/Desktop/Downloads/Release-21.03.0/poppler-21.03.0/Library/bin' # This lib needs that thing
def split_pdf(path):
    maxPages = c
    for page in range(1, maxPages+1, 10): 
        images = convert_from_path(path, dpi=200, first_page=page, last_page = min(page+10-1,maxPages),
            poppler_path=poppler_path)
        # print(page)
        for i in range(0, 10):
            images[i].save('page'+ str(i + page) +'.jpg', 'JPEG')

split_pdf(r'C:/Users/Mert Koksal/Desktop/Programming/PDF Viewer Bot/a.pdf')