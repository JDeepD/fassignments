## Fast Assignments

### Why fassignments?
I am too lazy too open up a LibreWord/MS Word and fill up
data for coverpage every single time. Its boring and
wastes a lot of time doing the same thing every single week.

### How fassignments?
It uses Flask as backend and PyFPDF2 for generating the pdf.
For frontend, it uses Bootstrap (I am too lazy to
do anything fancier in the Frontend)

### What is fassignments?
Its a web app to generate the coverpage for assignments.
All you gotta do is fill in the data and whoosh. You
have your Assignment ready in a sexy looking PDF which is sure
to catch the TA's eye.

PS: The pdf also includes my college logo so it probably wont 
work for you if you are not from the same college as mine.
Currently I have no plans to make it more customisable but feel
free to fork it and replace `img/logo.png` with the image you want
in the header. You can also change what details you want to show
in the pdf by modifying `mkpdf.py` file.
