#Writing into a Tab-SV file
import csv
outfile=open("csvfile.csv","w",newline='')
outwriter=csv.writer(outfile,delimiter='\t', lineterminator='\n\n')
#Writing rows into the tsv file
print("Writing the contents into the file...")
outwriter.writerow(['Sri','Jagannath','Subhadra','Balabhadra'])
print("File Writing Completed,Closing the file...")
outfile.close()
print("Opening the output file for view....")
file1=open("csvfile.csv")
file1rdr=csv.reader(file1)
for row in file1rdr:
    print("Row No."+str(file1rdr.line_num)+" "+str(row))
