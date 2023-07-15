"""
See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types 
for common types.

In a file called extensions.py, implement a program that prompts the user for the name of a 
file and then outputs that file’s media type if the file’s name ends, case-insensitively, 
in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, 
output application/octet-stream instead, which is a common default.
"""

file = input("Enter file name: ")
ext = file.split(".")[1].lower()
match ext:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")



        