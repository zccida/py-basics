

'''
.gif image/gif
.jpg image/jpg
.jpeg image/jpeg
.png image/png
.pdf application/pdf
.txt text/plain
.zip application/zip
nothing - application/octet-stream
'''

file_name = input("File name: ").lower()
end = ''

if '.gif' in file_name:
    end = 'image/gif'
elif '.jpg' in file_name:
    end = 'image/jpeg'
elif '.jpeg' in file_name:
    end = 'image/jpeg'
elif '.png' in file_name:
    end = 'image/png'
elif '.pdf' in file_name:
    end = 'application/pdf'
elif '.txt' in file_name:
    end = 'text/plain'
elif '.zip' in file_name:
    end = 'application/zip'
else:
    end = 'application/octet-stream'

print(end)
