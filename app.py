from tkinter import * 

def save_info():
    ID_info   = ID.get()
    Name_info = Name.get()
    DOB_info  = DOB.get()
    Age_info  = Age.get()
    Gender_info = Gender.get()
    School_info = School.get()
    City_info   = City.get()
    print(Name_info, DOB_info, Age_info)
    file = open("user.txt", "a")
    file.write(ID_info)
    file.write(", ")
    file.write(Name_info) 
    file.write(", ")
    file.write(DOB_info) 
    file.write(", ")    
    file.write(Age_info)
    file.write(", ")
    file.write(Gender_info) 
    file.write(", ")
    file.write(School_info) 
    file.write(", ")    
    file.write(City_info)
    file.write("\n") 
    return
    
  
def search_info():
    # Python Program to Print Lines
    # Containing Given String in File

    # input file name with extension
    # file_name = input("Enter The File's Name: ")

    # using try catch except to
    # handle file not found error.
    # entering try block
    try:
        # opening and reading the file
        file_read = open("user.txt", "r")
        # asking the user to enter the string to be
        # searched
        # text = input("Enter the String: ")
        # search_info 
        text  = search_entry.get()

        # reading file content line by line.
        lines = file_read.readlines()

        new_list = []
        idx = 0

        # looping through each line in the file
        for line in lines:
            
            # if line have the input string, get the index
            # of that line and put the
            # line into newly created list
            if text in line:
                new_list.insert(idx, line)
                idx += 1
        # closing file after reading
        file_read.close()
        # if length of new list is 0 that means
        # the input string doesn't
        # found in the text file
        if len(new_list)==0:
            print("\n\"" +text+ "\" is not found in \""+ "\"!")
        else:
            # displaying the line
            # containing given string
            lineLen = len(new_list)
            print("\n**** Lines containing \"" +text+ "\" ****\n")
            for i in range(lineLen):
                # listbox.insert(end=new_list[i])
                print(end=new_list[i])
            print()

    # entering except block
    # if input file doesn't exist
    except :
        print("\nThe file doesn't exist!")
    # listbox.insert(END, "how are you")

    # line = file.readline()
    # word = line.split()
    # if search_info in word:
    #     print(line)
    #     return
    # else:
    #     print("invalid please try again")
    #     return
    

    
    

app = Tk()

app.geometry("500x700")
#Minimum Size(W, H)
app.minsize(400, 400)

heading = Label(text="Data Entery Application",font=20)
heading.place(x=100,    y=10 )

#Making Label
ID_text = Label(text="ID :")
Name_text = Label(text="Name :")
DOB_text = Label(text="DOB :")
Age_text = Label(text="Age :")
Gender_text = Label(text="Gender :")
School_text = Label(text="School :")
City_text = Label(text="City :")



#Placement of Label on the GUI
ID_text.place(x=70,    y=90 )
Name_text.place(x=70,  y=120)
DOB_text.place(x=70,   y=150)
Age_text.place(x=70,   y=180)
Gender_text.place(x=70,y=210)
School_text.place(x=70,y=240)
City_text.place(x=70,  y=270)

#defining the data type
ID     = StringVar()
Name   = StringVar()
DOB    = StringVar()
Age    = StringVar()
Gender = StringVar()
School = StringVar()
City   = StringVar()


#Extracting the the data from the input
ID_entry     = Entry(textvariable=ID,    width="30")
Name_entry   = Entry(textvariable=Name,  width="30")
DOB_entry    = Entry(textvariable=DOB,   width="30")
Age_entry    = Entry(textvariable=Age,   width="30")
Gender_entry = Entry(textvariable=Gender,width="30")
School_entry = Entry(textvariable=School,width="30")
City_entry   = Entry(textvariable=City,  width="30")


#Placement of insertion box on the GUI
ID_entry.place(x=120,    y=92)
Name_entry.place(x=120,  y=120)
DOB_entry.place(x=120,   y=150)
Age_entry.place(x=120,   y=180)
Gender_entry.place(x=120,y=210)
School_entry.place(x=120,y=240)
City_entry.place(x=120,  y=270)


#creating Entry for search
search_entry = StringVar()
search_entry = Entry(textvariable=search_entry,  width="30")
search_entry.place(x=130,    y=380)

listbox = Listbox(app, height= 10, width=50)
listbox.grid(row=12, column=0, columnspan=40, rowspan=6, padx=130, pady=440)

#Creating the the submit button
button = Button(app,text="Submit Data",command=save_info,width="15",fg="white", bg="grey", font="2")
button.place(x=320,y=180)


#Creating the the search button
button = Button(app,text="Search",command=search_info,width="15",fg="white", bg="grey", font="1")
button.place(x=130,y=320)
# listbox.pack()
# listbox.insert("how are you")


mainloop()