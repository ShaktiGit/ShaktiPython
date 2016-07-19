print("Please enter a 10 digit ATT BTN as NPA-NXX-LINE-CUS: ")
telno=input()
print("The Telephone No is: ",telno)
#Telephone Validation
i=len(telno)
print("Size of input string: ",i)
telstrip=telno.replace('-','')
errcode=0
j=0
list=[210,326,346]
strnpa=telno[0:3]
print("NPA is: ",strnpa)
for j in range(len(list)) :
    if list[j]==int(strnpa):
        break
    else:
        print("Invalid NPA-should be 210/326/346 !!")
        
    

if telstrip.isdigit():
    pass
else:
    print("(ERR2)Invalid BTN: The BTN should be numeric")

while(i>=0):
    i=i-1
    if len(telno) !=16:
        print("(ERR1)Input Format Error: The BTN Should be in NPA-NXX-LINE-CUS format")
        errcode=errcode+1
        break
    if telno[3]!='-':
        print("(ERR3)Invalid BTN: BTN should be \"-\" separated")
        errcode=errcode+1
        break
    if telno[7]!='-':
        print("(ERR4)Invalid BTN: BTN should be \"-\" separated")
        errcode=errcode+1
        break
    if telno[12]!='-':
        print("(ERR5)Invalid BTN: BTN should be \"-\" separated")
        errcode=errcode+1
        break
print("Telephone No Validated.........")
if errcode >0:
    print("The BTN is in error !!!")
