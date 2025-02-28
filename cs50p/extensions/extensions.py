a = input("File Name: ")
a = a.strip()
a = a.lower()

if a.endswith(".jpg"):
    print("image/jpeg")

elif a.endswith(".jpeg"):
    print("image/jpeg")

elif a.endswith(".png"):
    print("image/png")

elif a.endswith(".gif"):
    print("image/gif")

elif a.endswith(".pdf"):
    print("application/pdf")

elif a.endswith(".txt"):
    print("text/plain")

elif a.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")

