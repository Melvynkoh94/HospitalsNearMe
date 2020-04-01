#importing necassary modules
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from Hospital import *
import math
listHospitals = []  #List that will hold the records of hospitals
#Main Window class to create a main window
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.config(bg = '#d0e1f3') #Setting the background color
        self.master.geometry('550x760')     #Setting height and width of window
        self.master.title('Hospitals City')
        self.widgets()
    #Function to place widgets
    def widgets(self):
        #Placing the logo and title on main window
        img = Image.open('Assets/logo.png')
        tkimg = ImageTk.PhotoImage(img)
        logoFrame = Frame(self.master,bg = '#d0e1f3')
        logoLabel = Label(logoFrame, image = tkimg, bd = 0)
        logoLabel.image = tkimg
        logoFrame.pack()
        logoLabel.pack()

        labelTitle = Label(logoFrame, text = "HOSPITAL CITY",bg = '#d0e1f3', font=("Arial", 30, 'bold')).pack(pady = 20)

        ttk.Style().configure("TButton", font=('Arial', 20),background="blue", height = 40 ,width = 20)
        buttonFrame = Frame(self.master,bg = '#d0e1f3')
        publicHospitalButton = ttk.Button(buttonFrame, text = "Public Hospitals")
        privateHospitalButton = ttk.Button(buttonFrame, text = "Private Hospitals")
        privateHospitalButton.config(command = self.PrivateHospitals)
        publicHospitalButton.config(command = self.PublicHospitals)
        
        buttonFrame.pack(pady = 70)
        publicHospitalButton.pack(pady=30)
        privateHospitalButton.pack()
    #Function for public button click
    def PublicHospitals(self):
        #Changing button layout and going to next window
        ttk.Style().configure("TButton", font=('Arial', 10),width = 30)
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        LocationWindow(self.newWindow, "Public")
    #Function for private button click
    def PrivateHospitals(self):
        #Changing button layout and going to next window
        ttk.Style().configure("TButton", font=('Arial', 10),width = 30)
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        LocationWindow(self.newWindow, "Private")
    
#Second window on which the user can select his location or enter post code
class LocationWindow:
    def __init__(self, master, public_or_private):
        #Placing widgets and defining window structure
        self.public_or_private = public_or_private
        self.master = master
        self.master.config(bg = '#d0e1f3')
        self.master.geometry('850x960')
        self.master.title('Hospitals City')
        self.widgets()
    def widgets(self):
        #Function to place widgets
        img = Image.open('Assets/logo2.png')
        tkimg = ImageTk.PhotoImage(img)
        logoFrame = Frame(self.master,bg = '#d0e1f3')
        logoLabel = Label(logoFrame, image = tkimg, bd = 0)
        logoLabel.image = tkimg
        logoFrame.pack()
        logoLabel.pack(side = LEFT)

        labelTitle = Label(logoFrame, text = "HOSPITAL CITY",bg = '#d0e1f3', font=("Arial", 20, 'bold'))
        labelTitle.pack(side = RIGHT, pady = 20)
        labelFrame = Frame(self.master)
        labelFrame.pack(pady = 15)
        labelI = Label(labelFrame, text = "Please click your location on the map", font=("Arial", 15),bg = '#d0e1f3')
        labelI.pack()
        canvas = Canvas(self.master, bg = '#d0e1f3', width=614, height=357)
        img = ImageTk.PhotoImage(Image.open('Assets/SG_Map.png'))
        canvas.create_image(0,0,image=img)
        canvas.config(scrollregion=canvas.bbox(ALL))

        
        #Canvas.bind triggers a function on mouse click on map
        canvas.bind("<Button 1>",self.mouseClick)
        canvas.image = img
        canvas.pack(pady = 15)

        labelFrame2 = Frame(self.master,bg = '#d0e1f3')
        labelFrame2.pack(pady = 15)
        labelI2 = Label(labelFrame, text = "OR Enter 6-Digit Postal Code Below", font=("Arial", 15),bg = '#d0e1f3')
        labelI2.pack()
        self.postCodeEntry = Entry(labelFrame2, width = 30, font=("Arial", 15), fg = "#65a4e6",justify='center')
        self.postCodeEntry.pack(pady = 30)
        buttonFrame = Frame(self.master,bg = '#d0e1f3')
        buttonFrame.pack(pady = 40)
        backButton = ttk.Button(buttonFrame, text = "Back to previous window", command = self.backButtonClicked)
        backButton.pack(side = LEFT, padx = 10)
        nextButton =  ttk.Button(buttonFrame, text = "Continue with postal code", command = self.postButtonClicked)
        nextButton.pack(side = RIGHT, padx = 10)

    #Back button clicked function
    def backButtonClicked(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        MainWindow(self.newWindow)

    #Post code button clicked function
    #This function takes the input from the user and goes to next window
    def postButtonClicked(self):
        stringPostCode = self.postCodeEntry.get()
        if(len(stringPostCode) == 6):
           if(stringPostCode.isdigit() == True):
               import random
               self.master.withdraw()
               self.newWindow = Toplevel(self.master)
               ttk.Style().configure("TButton", font=('Arial', 10),width = 10)
               ShowHospitalsWindow(self.newWindow, [random.randrange(300), random.randrange(200)] ,self.public_or_private)
           else:
                messagebox.showerror("Error", "Please enter a valid post code")
        else:
           messagebox.showerror("Error", "Please enter a 6 digit post code") 


    #Function when the location is specified
    def mouseClick(self,event):
        ttk.Style().configure("TButton", font=('Arial', 10),width = 10)
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        ShowHospitalsWindow(self.newWindow, [event.x,event.y],self.public_or_private)
        print("Clicked on ({},{})".format(event.x, event.y))
        # print(event.x,event.y)

#Show Hospitals Window class show the hospitals w.r.t distance nearest to furthest
class ShowHospitalsWindow:
    def __init__(self, master, cords_OR_postal , public_or_private):
        #Construct to initiaze some items and place widgets
        self.public_or_private = public_or_private
        self.master = master
        self.cords_OR_postal = cords_OR_postal
        self.master.config(bg = '#d0e1f3')
        self.master.geometry('550x760')
        self.master.title('Hospitals City')
        self.widgets()

    #Function to calculate distance
    def distance_a_b(self, a , b):
        import math
        dist = math.sqrt( (b[0] - a[0])**2 + (b[1] - a[1])**2 )
        print(dist)
        return dist
    
    # Calculate the distance between two points
    def distance_ab(self, location_a, location_b):
        distance = math.hypot(location_a[0]-location_b[0], location_a[1]-location_b[1])
        print(distance)
        return distance

    #Function to sort hospitals according to the distance
    def sort_distance(self):
        self.listHospital = []
        for h in listHospitals:
            h2 = []
            h2.clear()
            h2.append(h.hName)
            h2.append(h.hAddress)
            h2.append(h.hContact)
            h2.append(h.hLocation)
            h2.append(h.hNearestSubway)
            h2.append(h.hType)
            h2.append(h.hImage)
            h2.append(h.hPostalCode)
            distance = self.distance_a_b(self.cords_OR_postal, h.hLocation)
            h2.append(distance)
            self.listHospital.append(h2)
        self.listHospital.sort(key = lambda x: x[8])
        print(self.listHospital)
        return self.listHospital

    #Fnction to create and place widgets
    def widgets(self):
        
        img = Image.open('Assets/logo2.png')
        tkimg = ImageTk.PhotoImage(img)
        logoFrame = Frame(self.master,bg = '#d0e1f3')
        logoLabel = Label(logoFrame, image = tkimg, bd = 0)
        logoLabel.image = tkimg
        logoFrame.pack()
        logoLabel.pack(side = LEFT)

        labelTitle = Label(logoFrame, text = "HOSPITAL CITY",bg = '#d0e1f3', font=("Arial", 20, 'bold')).pack(side = RIGHT, pady = 20)

        labelFrame = Frame(self.master, bg = '#d0e1f3')
        self.labelCurrent = Label(labelFrame, text = "Currently results are sorted by distance (nearest to furthest)", font=("Arial", 13), bg = '#d0e1f3')
        self.labelHospital = Label(labelFrame, text = "You have chosen to view PUBLIC HOSPITALS",font=("Arial", 13), bg = '#d0e1f3')

        labelFrame.pack()
        self.labelCurrent.pack()
        self.labelHospital.pack()

        tkvarSort = StringVar(self.master)
        tkvarHostpital = StringVar(self.master)
        self.tkvarHostpital = tkvarHostpital
        choicesSort = {'Name' , 'Distance'}
        choicesHospital = {'Public' , 'Private'}

        tkvarSort.set("Sort by")
        tkvarHostpital.set("Hospitals")
        
        
        optionFrame = Frame(self.master, bg = '#d0e1f3', width = 30)
        sortOption = OptionMenu(optionFrame,tkvarSort,*choicesSort, command = self.switchSortType)
        sortOption.config(width = 15)
        hospitalOption = OptionMenu(optionFrame,tkvarHostpital,*choicesHospital ,command = self.switchHospitalType)
        self.hospitalOption = hospitalOption
        hospitalOption.config(width = 15)
        optionFrame.pack(pady = 20)
        sortOption.pack(side = LEFT, padx = 50)
        hospitalOption.pack(side = RIGHT, padx = 50)

        listBoxFrame = Frame(self.master,bg = '#d0e1f3')
        self.listBox = Listbox(listBoxFrame, height = 15, width = 40,font=("Arial", 20) ,justify='center',bg = '#d0e1f3',fg = "brown")
        self.listBox.bind("<Double-Button-1>", self.HospitalClicked)
        listBoxFrame.pack()
        self.listBox.pack()

        buttonFrame = Frame(self.master)
        buttonFrame.pack(pady = 15)
        backButton = ttk.Button(buttonFrame, text = "Back",command = self.backButtonClicked)
        backButton.pack()

        #If user selected the public hospitals show the [public hospitals
        if(self.public_or_private == "Public"):
            self.setHospitalToListBoxPublic()
        else:
            #Else show private hospitals
            self.setHospitalToListBoxPrivate()
    def setHospitalToListBoxPublic(self):
        self.listBox.delete(0,'end')
        listHospital = self.sort_distance()
        for hospital in listHospital:
            if(hospital[5]!="Private"):
                self.listBox.insert(END, hospital[0])

    #Function to show the private hospitals
    def setHospitalToListBoxPrivate(self):
        self.listBox.delete(0,'end')
        #First clear the list box if it has any items
        listHospital = self.sort_distance()
        #Then sort the hospitals wrt to distance
        for hospital in listHospital:
            #For each hospital if there is public hospital insert it to list box
            if(hospital[5]!="Public"):
                self.listBox.insert(END, hospital[0])

    #Function when a hospital is selected from list box
    def HospitalClicked(self, item):
        lHos = []   #Getting details of that specific hospital
        for h in self.listHospital:
            if(h[0] == self.listBox.get(ACTIVE)):
                lHos = h
        #Then go to the next Screen
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        print("***lHos: ", lHos)
        ShowHospitalRecord(self.newWindow, lHos)

    #Back button clicked function
    def backButtonClicked(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        LocationWindow(self.newWindow, self.public_or_private)

    #Function when the hospital type is changed from public to private or private to public
    def switchHospitalType(self, Type):
        if(Type == "Public"):
            self.labelHospital.config(text = "You have chosen to view PUBLIC HOSPITALS")
            self.setHospitalToListBoxPublic()
        else:
            self.labelHospital.config(text = "You have chosen to view PRIVATE HOSPITALS")
            self.setHospitalToListBoxPrivate()

    #Function when sort type is change from name to distance or distance to name
    def switchSortType(self, Type):
        if(Type == "Name"):
            self.labelCurrent.config(text = "Currently results are sorted by name")
            #If type is name clear the list box
            self.listBox.delete(0,'end')
            listHospital = self.sort_distance()
            #Sort hospital
            listPrivate = [] #List for private hospitals
            listPublic = [] #List for public hospitals
            listPrivate.clear() 
            listPublic.clear()
            for i in listHospital:
                if(i[5]=="Public"):
                    listPublic.append(i)
                else:
                    listPrivate.append(i)
                    
            listHospital.sort(key = lambda x: x[0])  #This statement sorts hospitals wrt name
            
            if(self.tkvarHostpital.get() == "Hospitals"): # IF the hospital type is NOT changed
                if(self.public_or_private == "Public"):     #Show the records according to user selected choice
                    listPublic.sort(key = lambda x: x[0])
                    for h in listPublic:
                        self.listBox.insert(END, h[0])
                if(self.public_or_private == "Private"):
                    listPrivate.sort(key = lambda x: x[0])
                    for h in listPrivate:
                        self.listBox.insert(END, h[0])
            else:                                       #IF the hospital type is changed
                if(self.tkvarHostpital.get() == "Public"):      #If its public then display public hospitals
                    listPublic.sort(key = lambda x: x[0])
                    for h in listPublic:
                        self.listBox.insert(END, h[0])
                if(self.tkvarHostpital.get() == "Private"): #Else display private hospitals
                    listPrivate.sort(key = lambda x: x[0])
                    for h in listPrivate:
                        self.listBox.insert(END, h[0])
                        
        else:   #If the type is distance NOT name
            self.labelCurrent.config(text = "Currently results are sorted by distance (nearest to furthest)")
            if(self.tkvarHostpital.get() != "Hospitals"): #If the hospital type is changed
                if(self.tkvarHostpital.get() == "Public"):  #If it is public then show public hospitals
                    self.setHospitalToListBoxPublic()
                else:                                   #Else show private hospitals
                    self.setHospitalToListBoxPrivate()
            else:                                   #If it is not changed then show the records according to user choice
                if(self.public_or_private == "Public"):
                    self.setHospitalToListBoxPublic()
                else:
                    self.setHospitalToListBoxPrivate()

#Class to show the hospitals records
class ShowHospitalRecord:
    def __init__(self, master , hospitalDetail):
        #Intializing the hospital data and placing widgets
        self.master = master
        self.hos = hospitalDetail
        self.master.config(bg = '#d0e1f3')
        self.master.geometry('850x960')
        self.master.title('Hospitals City')
        self.widgets()
    def widgets(self):
        img = Image.open('Assets/logo2.png')
        tkimg = ImageTk.PhotoImage(img)
        logoFrame = Frame(self.master,bg = '#d0e1f3')
        logoLabel = Label(logoFrame, image = tkimg, bd = 0)
        logoLabel.image = tkimg
        logoFrame.pack()
        logoLabel.pack(side = LEFT)
        labelTitle = Label(logoFrame, text = "HOSPITAL CITY",bg = '#d0e1f3', font=("Arial", 20, 'bold')).pack(side = RIGHT, pady = 20)
        #Creating a canvas on which the image of hospital is placed
        canvas = Canvas(self.master, bg = '#d0e1f3', width=500, height=500)
        #hos[] ==['Changi General Hospital', '2 Simei Street 3, Singapore 529889', '+6583888832', [16, 57], 'Tampines', 'Public', 'Hospitals/h1.jpg', '529889', 293.6153946917634]
        try:
            img = ImageTk.PhotoImage(Image.open(self.hos[6]))
            canvas.create_image(0,0,image=img)
            canvas.image = img
        except Exception as e:
            print(e)
        canvas.pack(pady = 15)
        #Labels to show the record of the selected hospital
        label = Label(self.master, text = "Hospital Name: "+str(self.hos[0]),font=("Arial", 15),bg = '#d0e1f3')
        label.pack()
        label1 = Label(self.master, text = "Contact info: "+str(self.hos[2]),font=("Arial", 15),bg = '#d0e1f3')
        label1.pack()
        label2 = Label(self.master, text = "Nearest Subway: "+str(self.hos[4]),font=("Arial", 15),bg = '#d0e1f3')
        label2.pack()

        buttonFrame = Frame(self.master,bg = '#d0e1f3')
        buttonFrame.pack(pady = 40, side = BOTTOM)
        backButton = Button(buttonFrame, text = "Back", command = self.backButtonClicked, width = 20)
        backButton.pack(side = LEFT, padx = 50)
        nextButton =  Button(buttonFrame, text = "Done", command = self.Done, width = 20)
        nextButton.pack(side = RIGHT, padx = 50)
    #Back button clicked function
    def backButtonClicked(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        MainWindow(self.newWindow)
    def Done(self): #Done button function to exit
        self.master.withdraw()


def main():
    hospital_list = exportFromJson("hospitals_list.json")
    print(hospitals_list[0])
    for i in range(34):
        listHospitals.append(Hospital_TEST(hospitals_list[i]['Hospital Name'],
        hospitals_list[i]['Address'],
        "+6563612345",
        hospital_list[i]['MapLocation'],
        hospitals_list[i]['Region'],
        hospitals_list[i]['Type'],
        hospital_list[i]['Image']))
    print("List of Hospitals imported from JSON: \n", listHospitals[0].__str__())

    root = Tk()
    MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()


