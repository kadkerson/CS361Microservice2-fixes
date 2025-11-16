import tkinter as tk
import os
import json

FILENAME = "examplepipeline.txt"
PROPERTY = ["001", "", "", "", "", ""]         # change if needed during video presentation



# setting up ui

root = tk.Tk()

root.configure(background="white")
root.title("example program")
root.geometry("1050x600")

global title
title = tk.Label(root, text="Click the button to send a data request!", font="Courier", background="white")
title.pack(pady=(150,10))

searchButton = tk.Button(root, text=f"Search for objects with ID {PROPERTY[0]}", bg="white", command=lambda: make_request())
searchButton.pack()

canvasFrame = tk.Frame(root, bg="white")
canvasFrame.pack(fill="both", expand=True, padx=10, pady=(35, 20))

canvas = tk.Canvas(canvasFrame, bg="white", highlightthickness=0)
scrollbar = tk.Scrollbar(canvasFrame, orient="vertical", command=canvas.yview)
scrollableFrame = tk.Frame(canvas, bg="white")

scrollableFrame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")



# functions to print request, read reply, and display data from reply

def make_request():

    with open(FILENAME, "w") as f:
        f.write("request\n")
        obj = {"id": f"{PROPERTY[0]}", "title": f"{PROPERTY[1]}", "author": f"{PROPERTY[2]}", "genre": f"{PROPERTY[3]}", "year": f"{PROPERTY[4]}", "pages": f"{PROPERTY[5]}"}
        f.write(json.dumps(obj))

    for widget in scrollableFrame.winfo_children():
        widget.destroy()

    root.after(2000, check_for_reply)



def check_for_reply():

    with open(FILENAME, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if len(lines) > 1 and lines[0].lower() == "reply":
        objects = []
        for line in lines[1:]:
            obj = json.loads(line)
            objects.append(obj)
        display_results(objects)

    root.after(2000, check_for_reply)



def display_results(data_lines):

    for widget in scrollableFrame.winfo_children():
        widget.destroy()

    if not data_lines:
        tk.Label(frame, text="No objects have that property...", font="Courier", bg="white").pack(side="left", padx=10)
        return

    for a, obj in enumerate(data_lines, start=1):

        frame = tk.Frame(scrollableFrame, bg="white", bd=1, relief="flat")
        frame.pack(pady=5, padx=(25,5))
        
        for key, value in obj.items():
            tk.Label(frame, text=f"{key}: {value}", font="Courier", bg="white").pack(side="left", padx=(0,20))



root.mainloop()
