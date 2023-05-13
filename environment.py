# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 19:57:45 2023

@author: Admin
"""

from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk
import time

root = Tk()
root.config(bg="white")
root.title("Environment")
root.geometry("910x750")


close = ImageTk.PhotoImage(Image.open("close.jpg"))
next_img = ImageTk.PhotoImage(Image.open("next.jpg"))
prev_img = ImageTk.PhotoImage(Image.open("previous.jpg"))
dpsmisLogo = ImageTk.PhotoImage(Image.open("logo.jpg"))


dpsmisLogo_image = Label(root, image=dpsmisLogo, bg="white")
dpsmisLogo_image.place(relx=0.5, rely=0.375, anchor=CENTER)


def environmentInfo():
    time.sleep(1/5)
    dpsmisLogo_image.pack()
    dpsmisLogo_image.pack_forget()
    information_corner_title.pack()
    information_corner_title.pack_forget()
    welcome_dpsmis_title.pack()
    welcome_dpsmis_title.pack_forget()
    welcome_dpsmis.pack()
    welcome_dpsmis.pack_forget()
    read_more_button1.pack()
    read_more_button1.pack_forget()
    read_more_button2.pack()
    read_more_button2.pack_forget()
    title2.pack()
    title2.pack_forget()
    information_corner.pack()
    information_corner.pack_forget()
    close_button.config(command=close_welcomedpsmis)
    
    
    

major_features_info = Label(root, text="1. 3 blocks (buildings) housing the Administration , Junior, Middle and Senior Schools\n2. Total around 200 classrooms\n3. Naturally lit Labs for Sciences, Maths, Information Technology and the Libraries\n4. Well equipped auditorium for 1000 seating capacity\n5. Indoor swimming pool, gymnasium and badminton courts\n6. Well arranged pathways leading to all utilities\n7. Parking for 300 cars and buses\n8. Large size football ground and athletic track\n9. Energy efficient building and services\n10. Secured WIFI enabled campus\n11. Digital Signage, E Notice Boards and Video enabled announcement system", font=("Calibri", 15), fg="black", bg="white", justify="left")
major_features_title = Label(root, text="The school has the following major features:", font=("Calibri", 20, "bold"), fg="black", bg="white")

def previous_info():
    time.sleep(1/5)
    global dpsmisAreaAndBuildingTitle
    global dpsmisAreaAndBuildingInfo
    global dpsmisInfo
    global major_features_title
    global major_features_info
    
    dpsmisAreaAndBuildingTitle.place(relx=0.12, rely=0.45, anchor=CENTER)
    dpsmisAreaAndBuildingInfo.place(relx=0.5, rely=0.7, anchor=CENTER)
    dpsmisInfo.place(relx=0.5, rely=0.325, anchor=CENTER)
    dpsmisAreaAndBuildingInfo["text"] = "The campus has been thoughtfully designed to create a dynamic environment which triggers learning and facilitates the teaching process. It has been designed to miniscule details and addresses the contemporary needs of the Learners.\n\nThe academic buildings (Block A, Block B and Block C (First Floor and 2nd Floor)) has 158 classrooms. Each room has adequate storage provisions for the entire class. The building is networked and provided with computers.\n\nIn addition to regular classroom, the building has classrooms equipped with Smart Interactive Boards for Senior School and LCD Televisions for Junior School, language rooms, science labs, computer labs, music and dance rooms, staff rooms, art rooms and adequate toilet facilities for boys and girls.\n\nThe building also has one state of art Auditorium and an Olympic Size Swimming Pool. The total area of the academic building is 22,000 sq ft."
    dpsmisInfo["text"] = "The school was established in 2001. In nineteen years, the school has carved a niche for itself and is counted among the best schools in Doha-Qatar. Bettering the best in Academics, Extra-curricular activities and sports, the school has succeeded in bringing out well-rounded personalities-students who are academically bright, physically strong, mentally agile, emotionally balanced, socially committed and spiritually serene."
    dpsmisAreaAndBuildingTitle["text"] = "Area and Building"
    
    
    major_features_info.pack()
    major_features_info.pack_forget()
    major_features_title.pack()
    major_features_title.pack_forget()

def next_info():
    time.sleep(1/5)
    global major_features_title
    global dpsmisAreaAndBuildingTitle
    global dpsmisAreaAndBuildingInfo
    global dpsmisInfo
    global major_features_info
    
    dpsmisAreaAndBuildingInfo.pack()
    dpsmisAreaAndBuildingTitle.pack()
    dpsmisAreaAndBuildingInfo.pack_forget()
    dpsmisAreaAndBuildingTitle.pack_forget()
    dpsmisInfo.pack()
    dpsmisInfo.pack_forget()
    
    major_features_title.place(relx=0.285, rely=0.25, anchor=CENTER)
    
    major_features_info.place(relx=0.405, rely=0.465, anchor=CENTER)

def dpsmis_read_more():
    global dpsmisAreaAndBuildingTitle
    global dpsmisAreaAndBuildingInfo
    global dpsmisInfo
    global next_button
    global prev_button
    global major_features_title
    global major_features_info
    global dpsmisLogo_image
    
    time.sleep(1/5)
    dpsmisLogo_image.pack()
    dpsmisLogo_image.pack_forget()
    information_corner_title.pack()
    information_corner_title.pack_forget()
    welcome_dpsmis_title.pack()
    welcome_dpsmis_title.pack_forget()
    welcome_dpsmis.pack()
    welcome_dpsmis.pack_forget()
    read_more_button1.pack()
    read_more_button1.pack_forget()
    read_more_button2.pack()
    read_more_button2.pack_forget()
    title2.pack()
    title2.pack_forget()
    information_corner.pack()
    information_corner.pack_forget()
    title1["text"] = "Welcome to\nDPS Modern Indian School"
    title1.config(fg="black")
    title1.place(relx=0.5, rely=0.1, anchor=CENTER)
    close_button.config(command=close_welcomedpsmis)
    
    dpsmisInfo = Label(root, text="The school was established in 2001. In nineteen years, the school has carved a niche for itself and is counted among the best schools in Doha-Qatar. Bettering the best in Academics, Extra-curricular activities and sports, the school has succeeded in bringing out well-rounded personalities-students who are academically bright, physically strong, mentally agile, emotionally balanced, socially committed and spiritually serene.", font=("Calibri", 15), fg="black", bg="white", justify="left", wraplength=900)
    dpsmisInfo.place(relx=0.5, rely=0.325, anchor=CENTER)
    
    dpsmisAreaAndBuildingTitle= Label(root, text="Area and Building", font=("Calibri", 20, "bold"), fg="black", bg="white")
    dpsmisAreaAndBuildingTitle.place(relx=0.12, rely=0.45, anchor=CENTER)
    
    dpsmisAreaAndBuildingInfo = Label(root, text="The campus has been thoughtfully designed to create a dynamic environment which triggers learning and facilitates the teaching process. It has been designed to miniscule details and addresses the contemporary needs of the Learners.\n\nThe academic buildings (Block A, Block B and Block C (First Floor and 2nd Floor)) has 158 classrooms. Each room has adequate storage provisions for the entire class. The building is networked and provided with computers.\n\nIn addition to regular classroom, the building has classrooms equipped with Smart Interactive Boards for Senior School and LCD Televisions for Junior School, language rooms, science labs, computer labs, music and dance rooms, staff rooms, art rooms and adequate toilet facilities for boys and girls.\n\nThe building also has one state of art Auditorium and an Olympic Size Swimming Pool. The total area of the academic building is 22,000 sq ft.", font=("Calibri", 15), fg="black", bg="white", justify="left", wraplength=900)
    dpsmisAreaAndBuildingInfo.place(relx=0.5, rely=0.7, anchor=CENTER)
    
    next_button = Button(root, image=next_img, relief=FLAT, bg="white")
    next_button.place(relx=0.9, rely=0.96, anchor=CENTER)
    next_button.config(command=next_info)
    
    prev_button = Button(root, image=prev_img, relief=FLAT, bg="white")
    prev_button.place(relx=0.1, rely=0.96, anchor=CENTER)
    prev_button.config(command=previous_info)

def close_root():
    time.sleep(1/5)
    root.destroy()
    
def close_welcomedpsmis():
    global dpsmisAreaAndBuildingTitle
    global dpsmisAreaAndBuildingInfo
    global dpsmisInfo
    global next_button
    global prev_button
    global major_features_title
    global major_features_info
    global dpsmisLogo_image
    
    time.sleep(1/5)
    close_button.config(command=close_root)
    
    dpsmisLogo_image.place(relx=0.5, rely=0.375, anchor=CENTER)
    
    title1["text"] = "DPS Modern Indian School"
    title1.place(relx=0.5, rely=0.05, anchor=CENTER)
    title2.place(relx=0.5, rely=0.15, anchor=CENTER)
    
    information_corner_title.place(relx=0.8, rely=0.6, anchor=CENTER)
    
    welcome_dpsmis_title.place(relx=0.2, rely=0.6, anchor=CENTER)
    welcome_dpsmis.place(relx=0.2, rely=0.8, anchor=CENTER)
    
    read_more_button1.place(relx=0.2, rely=0.95, anchor=CENTER)
    read_more_button2.place(relx=0.8, rely=0.95, anchor=CENTER)
    
    information_corner.place(relx=0.8, rely=0.8, anchor=CENTER)
    
    title1.config(fg="darkgreen")
    
    next_button.pack()
    next_button.pack_forget()
    prev_button.pack()
    prev_button.pack_forget()
    
    dpsmisInfo.pack()
    dpsmisInfo.pack_forget()
    dpsmisAreaAndBuildingInfo.pack()
    dpsmisAreaAndBuildingInfo.pack_forget()
    dpsmisAreaAndBuildingTitle.pack()
    dpsmisAreaAndBuildingTitle.pack_forget()
    
    major_features_title.pack()
    major_features_title.pack_forget()
    major_features_info.pack()
    major_features_info.pack_forget()
    


title1 = Label(root, text="DPS Modern Indian School", font=("agency FB", 50, "bold", "underline"), bg="white", fg="darkgreen")
title1.place(relx=0.5, rely=0.05, anchor=CENTER)

title2 = Label(root, text="Environment Club", font=("algerian", 40, "bold", "italic"), bg="white", fg="green")
title2.place(relx=0.5, rely=0.15, anchor=CENTER)

information_corner_title = Label(root, text="Environment \nCorner", font=("calibri", 25, "bold"), bg="white", fg="black", highlightthickness=4, highlightcolor="black", highlightbackground="black", borderwidth=4)
information_corner_title.place(relx=0.8, rely=0.6, anchor=CENTER)

information_corner = Label(root, text="DPS-MIS Envorionment Information and Events Corner. DPS-MIS has won 2nd place in the school debate competion. DPS-MIS Environment Inter-School Tree Planting Competion....", font=("calibri", 15), wraplength=300, fg="black", bg="white")
information_corner.place(relx=0.8, rely=0.8, anchor=CENTER)

welcome_dpsmis_title = Label(root, text="Welcome To \nDPS-MIS", font=("calibri", 25, "bold"), bg="white", fg="black", highlightthickness=4, highlightcolor="black", highlightbackground="black", borderwidth=4)
welcome_dpsmis_title.place(relx=0.2, rely=0.6, anchor=CENTER)

welcome_dpsmis = Label(root, text="The school was established in 2001. In nineteen years, the school has carved a niche for itself and is counted among the best schools in Doha-Qatar. Bettering the best in Academics, Extra-curricular activities.....", bg="white", fg="black", wraplength=300, font=("Calibri", 15))
welcome_dpsmis.place(relx=0.2, rely=0.8, anchor=CENTER)

read_more_button1 = Button(root, text="Read More", font=("calibri", 17, "bold"),fg="white", bg="green", relief=RIDGE, highlightthickness=4, highlightcolor="lightgreen", highlightbackground="lightgreen", borderwidth=2, command=dpsmis_read_more)
read_more_button1.place(relx=0.2, rely=0.95, anchor=CENTER)

read_more_button2 = Button(root, text="Read More", font=("calibri", 17, "bold"),fg="white", bg="green", relief=RIDGE, highlightthickness=4, highlightcolor="lightgreen", highlightbackground="lightgreen", borderwidth=2, command=environmentInfo)
read_more_button2.place(relx=0.8, rely=0.95, anchor=CENTER)

close_button = Button(root, image=close, relief=FLAT, command=close_root, bg="darkred")
close_button.place(relx=0.925, rely=0.01)

root.mainloop()