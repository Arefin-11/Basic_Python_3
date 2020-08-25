a=int(input())
p=[]
import string
st=string.ascii_uppercase[:]
for i in range(a):
    p.append(input())
for cell in p:
    if "R" in cell and cell[1].isdigit() and "C" in cell:
        c=cell.index("C")
        row=cell[1:c]
        column=cell[c+1:]
        fin=""
        c=int(column)
        while c>0:
            c,rem = divmod(c-1,26)
            fin = st[rem] + fin
        print(fin+row)
    else:
        for char in cell:
            if char.isdigit():
                r=cell.index(char)
                row=cell[r:]
                column=cell[0:r]
                exp=len(column)-1
                count=0
                for cno in column:
                    p=st.index(cno)
                    count+=(p+1)*(26**exp)
                    exp-=1
                print("R{}C{}".format(row,count))
                break
