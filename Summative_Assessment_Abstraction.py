def start():
    global gender
    global name
    global list
    list = []
    name = input("What is the name of your avatar?")
    name = "Name:" + name
    list.append(name)
    gender = input("What is the gender of " + name + " ? 1. Female 2. Male")
    if gender == "1":
        gender = "Gender:Female"
        list.append(gender)
        eyecolor()
    elif gender == "2":
        gender = "Gender:Male"
        list.append(gender)
        eyecolor()
    else:
        start()

def eyecolor():
    global color_options
    global Veye_color
    Veyecolor = input("What eye color does your " + name + " have?")
    color_options = ["brown","blue","green","black", "red"]
    if Veyecolor in color_options:
        Veye_color = "Eyecolor:" + Veyecolor
        list.append(Veye_color)
        haircolor()
    else:
        eyecolor()

def haircolor():
    global hair_color
    Vhaircolor = input("What hair color does your " + name + " have?")
    if Vhaircolor in color_options:
        hair_color = "Hair color:" + Vhaircolor
        list.append(hair_color)
        top()
    else:
        haircolor()

def top():
    global Vtop
    Vtop = input("What top do you want " + name + " to wear? Options: shirt, blouse, collar shirt")
    top_options = ["shirt","blouse","collar shirt"]
    if Vtop in top_options:
        Vtop = "Top:" + Vtop
        list.append(Vtop)
        bottom()
    else:
        Vtop()

def bottom():
    global Vbottom
    Vbottom = input("What bottom do you want " + name + " to wear? Options: sweat pants, jeans, leggings")
    bottom_options = ["sweat pants","jeans","leggings"]
    if Vbottom in bottom_options:
        Vbottom = "Bottom:" + Vbottom
        list.append(Vbottom)
        input_descriptions()
    else:
        Vbottom()

def input_descriptions():
    global info
    print(list)

start()










