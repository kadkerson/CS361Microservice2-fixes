import tkinter as tk
import os

FILENAME = "pipeline"
PROPERTY = "{author;Christopher Paolini}"         # change if needed during video presentation



# setting up ui

root = tk.Tk()

root.configure(background="white")
root.title("example program")
root.geometry("700x600")

global title
title = tk.Label(root, text="Click the button to send a data request!", font="Courier", background="white")
title.pack(pady=(150,10))

searchButton = tk.Button(root, text=f"Search for objects with property {PROPERTY[0]}", bg="white", command=lambda: make_request())
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
        f.write(PROPERTY)

    for widget in scrollableFrame.winfo_children():
        widget.destroy()

    root.after(2000, check_for_reply)



def check_for_reply():

    with open(FILENAME, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if len(lines) > 1 and lines[0].lower() == "reply":
        display_results(lines[1:])

    root.after(2000, check_for_reply)



def display_results(data_lines):

    obj_index = 0

    for widget in scrollableFrame.winfo_children():
        widget.destroy()

    if not data_lines:
        tk.Label(frame, text="No objects have that property...", font="Courier", bg="white").pack(side="left", padx=10)

    for line in data_lines:

        if not (line.startswith("{") and line.endswith("}")):
            continue

        #content = line[1:-1]
        #parts = [p for p in content.split(";") if p]

        #if len(parts) != 3:
            #continue

        #prop1, prop2, prop3 = parts
        frame = tk.Frame(scrollableFrame, bg="white", bd=1, relief="flat")
        frame.pack(pady=5, padx=(115,5))

        #obj_index += 1
        tk.Label(frame, text=f"{line}").pack(side="left", padx=(0,10))
        #tk.Label(frame, text=f"Object {obj_index} properties:", font="Courier", bg="white").pack(side="left", padx=(0,10))
        #tk.Label(frame, text=f"{parts[0]},", font="Courier", bg="white").pack(side="left", padx=(0,10))
        #tk.Label(frame, text=f"{parts[1]},", font="Courier", bg="white").pack(side="left", padx=(0,10))
        #tk.Label(frame, text=f"{parts[2]}", font="Courier", bg="white").pack(side="left", padx=(0,10))



root.mainloop()
