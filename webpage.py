import pdfkit


print("\n========================================================================================")
print("Note : If the processing time is more than 05 seconds, close the program and restart it.")
print("========================================================================================")
url = input("Paste URL Here : ")+"/"
print("Processing...")
pdfkit.from_url(str(url), 'webpage.pdf', configuration=pdfkit.configuration(
    wkhtmltopdf=r"Webpage Download\wkhtmltopdf.exe"))
print("#-----------------------------#")
print("| Webpage converted into PDF! |")
print("#-----------------------------#")
print("Made By - Karan Jaswani")
input("\nPress Enter To Exit")