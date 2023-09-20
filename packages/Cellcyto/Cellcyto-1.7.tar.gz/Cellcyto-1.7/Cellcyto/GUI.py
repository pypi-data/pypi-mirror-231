import tkinter as tk
import tkinter.messagebox
import customtkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import simpledialog
import os
from .GUI_postprocessing import *
from .GUI_POSEA import POSEA, POSEA2, POSEA3
from PIL import Image

customtkinter.set_appearance_mode("Light")  # Modes: "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class CustomInputDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title=None, prompt=None):
        self.prompt = prompt
        super().__init__(parent, title)

    def body(self, master):
        self.prompt_label = tk.Label(master, text=self.prompt)
        self.prompt_label.pack()

        self.entry = tk.Entry(master, width=40)
        self.entry.pack()

    def apply(self):
        self.result = self.entry.get()

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.k_value_input = 1.8

        # configure window
        self.title("PostProcessing & Evaluation")
        self.geometry(f"{1300}x{900}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create menu
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Load original image (*.tif,*.png,*.jpg)", command=self.open_file1)
        self.filemenu.add_command(label="Load segmentation result (*.tif,*.png,*.jpg)", command=self.open_file2)
        self.filemenu.add_command(label="Load reference image (cell mask) (*.tif,*.png,*.jpg)", command=self.open_file3)
        self.filemenu.add_command(label="Load reference image (cytoplasm mask) (*.tif,*.png,*.jpg)", command=self.open_file4)
        self.filemenu.add_command(label="Load reference image (nucleus mask) (*.tif,*.png,*.jpg)", command=self.open_file5)
        self.filemenu.add_command(label="Save cytoplasm mask as tif", command=self.saveimage1)
        self.filemenu.add_command(label="Save nucleus mask as tif", command=self.saveimage2)
        self.filemenu.add_command(label="Save per cell accuracy (*.xlsx)", command=self.savedata)
        self.menubar.add_cascade(menu=self.filemenu, label="File")

        onlyone = tk.BooleanVar()

        self.modelmenu = tk.Menu(self.menubar, tearoff=0)
        self.modelmenu.add_checkbutton(label="isodata", onvalue=1, offvalue=0, variable=onlyone, command=self.isodata_process)
        self.modelmenu.add_checkbutton(label="li", onvalue=2, offvalue=0, variable=onlyone, command=self.li_process)
        self.modelmenu.add_checkbutton(label="mean", onvalue=3, offvalue=0, variable=onlyone, command=self.mean_process)
        self.modelmenu.add_checkbutton(label="otsu", onvalue=4, offvalue=0, variable=onlyone, command=self.otsu_process)
        self.modelmenu.add_checkbutton(label="triangle", onvalue=5, offvalue=0, variable=onlyone, command=self.triangle_process)
        self.modelmenu.add_checkbutton(label="yen", onvalue=6, offvalue=0, variable=onlyone, command=self.yen_process)
        self.modelmenu.add_separator()
        self.modelmenu.add_command(label="find best (cytoplasm)", command=self.findbest_cyto)
        self.modelmenu.add_command(label="find best (nucleus)", command=self.findbest_nucl)
        self.menubar.add_cascade(menu=self.modelmenu, label="Models")

        onlytwo = tk.BooleanVar()

        self.calculatemenu = tk.Menu(self.menubar, tearoff=0)
        self.calculatemenu.add_checkbutton(label="Set a number of k", onvalue=1, offvalue=0, variable=onlytwo, command=self.k_value)
        self.menubar.add_cascade(menu=self.calculatemenu, label="k values")

        onlythree = tk.BooleanVar()

        self.calculatemenu = tk.Menu(self.menubar, tearoff=0)
        self.calculatemenu.add_checkbutton(label="Get cytoplasm & nucleus mask", onvalue=1, offvalue=0, variable=onlythree, command=self.showresult)
        self.menubar.add_cascade(menu=self.calculatemenu, label="Post-processing")

        onlyfour = tk.BooleanVar()

        self.evaluatemenu = tk.Menu(self.menubar, tearoff=0)
        self.evaluatemenu.add_checkbutton(label="POSEA", onvalue=1, offvalue=0, variable=onlyfour, command=self.POSEA_process1)
        self.evaluatemenu.add_separator()
        self.evaluatemenu.add_checkbutton(label="POSEA (cyto)", onvalue=2, offvalue=0, variable=onlyfour, command=self.POSEA_process2)
        self.evaluatemenu.add_checkbutton(label="POSEA (nucl)", onvalue=3, offvalue=0, variable=onlyfour, command=self.POSEA_process3)
        self.menubar.add_cascade(menu=self.evaluatemenu, label="Evaluation")

        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help with GUI", command=self.show_message)
        self.menubar.add_cascade(menu=self.helpmenu, label="Help")
        self.config(menu=self.menubar)



        # create first frame
        self.first_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.first_frame.grid_columnconfigure(0, weight=1)


        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)


        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_columnconfigure(0, weight=1)

        # create fifth frame
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifth_frame.grid_columnconfigure(0, weight=1)

        # create sixth frame
        self.sixth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixth_frame.grid_columnconfigure(0, weight=1)

        # create seventh frame
        self.seventh_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seventh_frame.grid_columnconfigure(0, weight=1)


        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Walsh Lab", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Original Image", fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),command=self.sidebar_button_1_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Segmentation Mask", fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),command=self.sidebar_button_2_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Reference Image (cell mask)", fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),command=self.sidebar_button_3_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Reference Image (cytoplasm mask)", fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),command=self.sidebar_button_4_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Reference Image (nucleus mask)", fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),command=self.sidebar_button_5_event)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(self.sidebar_frame, text="Cytoplasm Mask", font=customtkinter.CTkFont(size=15, weight="bold"), fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),command=self.sidebar_button_6_event)
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_7 = customtkinter.CTkButton(self.sidebar_frame, text="Nucleus Mask", font=customtkinter.CTkFont(size=15, weight="bold"), fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),command=self.sidebar_button_7_event)
        self.sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)


        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 20))

        # create evaluation result frame
        self.evaluation_res_frame = customtkinter.CTkFrame(self)
        self.evaluation_res_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Evaluation Results", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.evaluation_res_1 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Traditional Evaluation", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_1.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=3, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=4, column=2, pady=10, padx=20, sticky="w")

        self.evaluation_res_2 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="POSEA (entire image)", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_2.grid(row=5, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=6, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=7, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=8, column=2, pady=10, padx=20, sticky="w")

        self.evaluation_res_3 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="POSEA (per cell)", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_3.grid(row=9, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=10, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=11, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall:", font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=12, column=2, pady=10, padx=20, sticky="w")

        # kind reminder
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # set default values
        self.appearance_mode_optionemenu.set("Light")
        self.scaling_optionemenu.set("100%")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def on_closing(self):
        if tkinter.messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.destroy()


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.sidebar_button_1.configure(fg_color=("gray75", "gray25") if name == "Original Image" else "transparent")
        self.sidebar_button_2.configure(fg_color=("gray75", "gray25") if name == "Segmentation Mask" else "transparent")
        self.sidebar_button_3.configure(fg_color=("gray75", "gray25") if name == "Reference Image (cell mask)" else "transparent")
        self.sidebar_button_4.configure(fg_color=("gray75", "gray25") if name == "Reference Image (cytoplasm mask)" else "transparent")
        self.sidebar_button_5.configure(fg_color=("gray75", "gray25") if name == "Reference Image (nucleus mask)" else "transparent")
        self.sidebar_button_6.configure(fg_color=("gray75", "gray25") if name == "Cytoplasm Mask" else "transparent")
        self.sidebar_button_7.configure(fg_color=("gray75", "gray25") if name == "Nucleus Mask" else "transparent")


        # show selected frame
        if name == "Original Image":
            self.first_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.first_frame.grid_forget()
        if name == "Segmentation Mask":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Reference Image (cell mask)":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "Reference Image (cytoplasm mask)":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "Reference Image (nucleus mask)":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()
        if name == "Cytoplasm Mask":
            self.sixth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sixth_frame.grid_forget()
        if name == "Nucleus Mask":
            self.seventh_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.seventh_frame.grid_forget()

    def sidebar_button_1_event(self):
        self.select_frame_by_name("Original Image")

    def sidebar_button_2_event(self):
        self.select_frame_by_name("Segmentation Mask")

    def sidebar_button_3_event(self):
        self.select_frame_by_name("Reference Image (cell mask)")

    def sidebar_button_4_event(self):
        self.select_frame_by_name("Reference Image (cytoplasm mask)")

    def sidebar_button_5_event(self):
        self.select_frame_by_name("Reference Image (nucleus mask)")

    def sidebar_button_6_event(self):
        self.select_frame_by_name("Cytoplasm Mask")

    def sidebar_button_7_event(self):
        self.select_frame_by_name("Nucleus Mask")


    def show_message(self):
        tkinter.messagebox.showinfo(title="Help", message="contact nwang27@tamu.edu")


    def open_file1(self):
        curr_directory = os.getcwd()
        self.file1 = askopenfilename(initialdir=curr_directory, title="Select Image",
                                    filetypes=[('tif file', '*.tif'), ('tiff file', '*.tiff'), ('png file', '*.png'), ('jpg file', '*.jpg'), ('all files', '*.')])
        if self.file1 is not None:
            self.img1 = customtkinter.CTkImage(Image.open(self.file1), size=(800, 800))
            self.first_frame_image_label = customtkinter.CTkLabel(self.first_frame, text="", image=self.img1)
            self.first_frame_image_label.grid(row=0, column=1, padx=25, pady=40)
        else:
            tkinter.messagebox.showinfo(title="Error", message="Please upload the original image")


    def open_file2(self):
        curr_directory = os.getcwd()
        self.file2 = askopenfilename(initialdir=curr_directory, title="Select Image",
                                    filetypes=[('tif file', '*.tif'), ('tiff file', '*.tiff'), ('png file', '*.png'), ('jpg file', '*.jpg'), ('all files', '*.')])
        if self.file2 is not None:
            self.img2 = customtkinter.CTkImage(Image.open(self.file2), size=(800, 800))
            self.second_frame_image_label = customtkinter.CTkLabel(self.second_frame, text="", image=self.img2)
            self.second_frame_image_label.grid(row=0, column=1, padx=25, pady=40)
        else:
            tkinter.messagebox.showinfo(title="Error", message="Please upload the segmentation mask")


    def open_file3(self):
        curr_directory = os.getcwd()
        self.file3 = askopenfilename(initialdir=curr_directory, title="Select Image",
                                    filetypes=[('tif file', '*.tif'), ('tiff file', '*.tiff'), ('png file', '*.png'), ('jpg file', '*.jpg'), ('all files', '*.')])
        if self.file3 is not None:
            self.img3 = customtkinter.CTkImage(Image.open(self.file3), size=(800, 800))
            self.third_frame_image_label = customtkinter.CTkLabel(self.third_frame, text="", image=self.img3)
            self.third_frame_image_label.grid(row=0, column=1, padx=25, pady=40)
        else:
            tkinter.messagebox.showinfo(title="Error", message="Please upload the reference image (cell mask)")


    def open_file4(self):
        curr_directory = os.getcwd()
        self.file4 = askopenfilename(initialdir=curr_directory, title="Select Image",
                                    filetypes=[('tif file', '*.tif'), ('tiff file', '*.tiff'), ('png file', '*.png'), ('jpg file', '*.jpg'), ('all files', '*.')])
        if self.file4 is not None:
            self.img4 = customtkinter.CTkImage(Image.open(self.file4), size=(800, 800))
            self.fourth_frame_image_label = customtkinter.CTkLabel(self.fourth_frame, text="", image=self.img4)
            self.fourth_frame_image_label.grid(row=0, column=1, padx=25, pady=40)
        else:
            tkinter.messagebox.showinfo(title="Error", message="Please upload the reference image (cytoplasm mask)")


    def open_file5(self):
        curr_directory = os.getcwd()
        self.file5 = askopenfilename(initialdir=curr_directory, title="Select Image",
                                    filetypes=[('tif file', '*.tif'), ('tiff file', '*.tiff'), ('png file', '*.png'), ('jpg file', '*.jpg'), ('all files', '*.')])
        if self.file5 is not None:
            self.img5 = customtkinter.CTkImage(Image.open(self.file5), size=(800, 800))
            self.fifth_frame_image_label = customtkinter.CTkLabel(self.fifth_frame, text="", image=self.img5)
            self.fifth_frame_image_label.grid(row=0, column=1, padx=25, pady=40)
        else:
            tkinter.messagebox.showinfo(title="Error", message="Please upload the reference image (nucleus mask)")


    def saveimage1(self):
        curr_directory = os.getcwd()
        self.file_save1 = asksaveasfilename(initialdir=curr_directory, defaultextension='.tif', title="Save Image")
        if self.file_save1 is not None:
            self.result_cyto.save(self.file_save1)
        else:
            tkinter.messagebox.showinfo(title="Error", message="There is no result found")

    def saveimage2(self):
        curr_directory = os.getcwd()
        self.file_save2 = asksaveasfilename(initialdir=curr_directory, defaultextension='.tif', title="Save Image")
        if self.file_save2 is not None:
            self.result_nucl.save(self.file_save2)
        else:
            tkinter.messagebox.showinfo(title="Error", message="There is no result found")

    def savedata(self):
        curr_directory = os.getcwd()
        self.file_save3 = asksaveasfilename(initialdir=curr_directory, defaultextension='.xlsx', title="Save Data")
        if self.file_save3 is not None:
            self.data.to_excel(self.file_save3)
        else:
            tkinter.messagebox.showinfo(title="Error", message="There is no result found")


    #########image processing
    def k_value(self):
        dialog = CustomInputDialog(self, title="k Value", prompt=f"Enter the value of k (Current value: {self.k_value_input}):")
        self.k_value_input = float(dialog.result)
        if self.k_value_input:
            print("k value:", self.k_value_input)
        else:
            tk.messagebox.showinfo(title="Error", message="No value entered.")


    def isodata_process(self):
        self.img_cyto, self.img_nucl = isodata(self.file1, self.file2, self.k_value_input)

    def li_process(self):
        self.img_cyto, self.img_nucl = li(self.file1, self.file2, self.k_value_input)

    def mean_process(self):
        self.img_cyto, self.img_nucl = mean(self.file1, self.file2, self.k_value_input)

    def otsu_process(self):
        self.img_cyto, self.img_nucl = otsu(self.file1, self.file2, self.k_value_input)

    def triangle_process(self):
        self.img_cyto, self.img_nucl = triangle(self.file1, self.file2, self.k_value_input)

    def yen_process(self):
        self.img_cyto, self.img_nucl = yen(self.file1, self.file2, self.k_value_input)

    def POSEA_process1(self):
        self.F_mask1, self.Pre_mask1, self.Re_mask1, self.F_obj1, self.Pre_obj1, \
        self.Re_obj1, self.cell_each_F1, self.cell_each_P1, self.cell_each_R1, self.data = POSEA(self.file2, self.file3)
        self.evaluation_res_frame = customtkinter.CTkFrame(self)
        self.evaluation_res_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Evaluation Results", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.evaluation_res_1 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Traditional Evaluation", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_1.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.F_mask1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.Pre_mask1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=3, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.Re_mask1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=4, column=2, pady=10, padx=20, sticky="w")

        self.evaluation_res_2 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="POSEA (entire image)", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_2.grid(row=5, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.F_obj1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=6, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.Pre_obj1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=7, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.Re_obj1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=8, column=2, pady=10, padx=20, sticky="w")

        self.evaluation_res_3 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="POSEA (per cell)", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_3.grid(row=9, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.cell_each_F1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=10, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.cell_each_P1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=11, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.cell_each_R1), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=12, column=2, pady=10, padx=20, sticky="w")

    def POSEA_process2(self):
        self.F_mask2, self.Pre_mask2, self.Re_mask2, self.F_obj2, self.Pre_obj2, \
        self.Re_obj2, self.cell_each_F2, self.cell_each_P2, self.cell_each_R2, self.data = POSEA2(self.result_cyto, self.file3, self.file4)
        self.evaluation_res_frame = customtkinter.CTkFrame(self)
        self.evaluation_res_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Evaluation Results", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.evaluation_res_1 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Traditional Evaluation", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_1.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.F_mask2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.Pre_mask2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=3, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.Re_mask2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=4, column=2, pady=10, padx=20, sticky="w")

        self.evaluation_res_2 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="POSEA (entire image)", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_2.grid(row=5, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.F_obj2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=6, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.Pre_obj2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=7, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.Re_obj2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=8, column=2, pady=10, padx=20, sticky="w")

        self.evaluation_res_3 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="POSEA (per cell)", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_3.grid(row=9, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.cell_each_F2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=10, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.cell_each_P2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=11, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.cell_each_R2), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=12, column=2, pady=10, padx=20, sticky="w")

    def POSEA_process3(self):
        self.F_mask3, self.Pre_mask3, self.Re_mask3, self.F_obj3, self.Pre_obj3, \
        self.Re_obj3, self.cell_each_F3, self.cell_each_P3, self.cell_each_R3, self.data = POSEA2(self.result_nucl, self.file3, self.file5)
        self.evaluation_res_frame = customtkinter.CTkFrame(self)
        self.evaluation_res_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.label_radio_group = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Evaluation Results", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.evaluation_res_1 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Traditional Evaluation", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_1.grid(row=1, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.F_mask3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=2, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.Pre_mask3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=3, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.Re_mask3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=4, column=2, pady=10, padx=20, sticky="w")

        self.evaluation_res_2 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="POSEA (entire image)", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_2.grid(row=5, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.F_obj3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=6, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.Pre_obj3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=7, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.Re_obj3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=8, column=2, pady=10, padx=20, sticky="w")

        self.evaluation_res_3 = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="POSEA (per cell)", font=customtkinter.CTkFont(size=16))
        self.evaluation_res_3.grid(row=9, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_F = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="F-measure: " + str(self.cell_each_F3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_F.grid(row=10, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_P = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Precision: " + str(self.cell_each_P3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_P.grid(row=11, column=2, pady=10, padx=20, sticky="w")
        self.evaluation_res_R = customtkinter.CTkLabel(master=self.evaluation_res_frame, text="Recall: " + str(self.cell_each_R3), font=customtkinter.CTkFont(size=14))
        self.evaluation_res_R.grid(row=12, column=2, pady=10, padx=20, sticky="w")


    def findbest_cyto(self):
        self.img_cyto1, _= isodata(self.file1, self.file2, self.k_value_input)
        self.img_cyto2, _ = li(self.file1, self.file2, self.k_value_input)
        self.img_cyto3, _ = mean(self.file1, self.file2, self.k_value_input)
        self.img_cyto4, _ = otsu(self.file1, self.file2, self.k_value_input)
        self.img_cyto5, _ = triangle(self.file1, self.file2, self.k_value_input)
        self.img_cyto6, _ = yen(self.file1, self.file2, self.k_value_input)

        self.F_isodata1 = POSEA3(self.img_cyto1, self.file3, self.file4)
        self.F_li1 = POSEA3(self.img_cyto2, self.file3, self.file4)
        self.F_mean1 = POSEA3(self.img_cyto3, self.file3, self.file4)
        self.F_otsu1 = POSEA3(self.img_cyto4, self.file3, self.file4)
        self.F_triangle1 = POSEA3(self.img_cyto5, self.file3, self.file4)
        self.F_yen1 = POSEA3(self.img_cyto6, self.file3, self.file4)

        F_list1 = [self.F_isodata1, self.F_li1, self.F_mean1, self.F_otsu1, self.F_triangle1, self.F_yen1]

        if self.F_isodata1 == max(F_list1):
            tkinter.messagebox.showinfo(title="Find best (cytoplasm)", message="Choose isodata")
        elif self.F_li1 == max(F_list1):
            tkinter.messagebox.showinfo(title="Find best (cytoplasm)", message="Choose li")
        elif self.F_mean1 == max(F_list1):
            tkinter.messagebox.showinfo(title="Find best (cytoplasm)", message="Choose mean")
        elif self.F_otsu1 == max(F_list1):
            tkinter.messagebox.showinfo(title="Find best (cytoplasm)", message="Choose otsu")
        elif self.F_triangle1 == max(F_list1):
            tkinter.messagebox.showinfo(title="Find best (cytoplasm)", message="Choose triangle")
        else:
            tkinter.messagebox.showinfo(title="Find best (cytoplasm)", message="Choose yen")

    def findbest_nucl(self):
        _, self.img_nucl1 = isodata(self.file1, self.file2, self.k_value_input)
        _, self.img_nucl2 = li(self.file1, self.file2, self.k_value_input)
        _, self.img_nucl3 = mean(self.file1, self.file2, self.k_value_input)
        _, self.img_nucl4 = otsu(self.file1, self.file2, self.k_value_input)
        _, self.img_nucl5 = triangle(self.file1, self.file2, self.k_value_input)
        _, self.img_nucl6 = yen(self.file1, self.file2, self.k_value_input)

        self.F_isodata2 = POSEA3(self.img_nucl1, self.file3, self.file5)
        self.F_li2 = POSEA3(self.img_nucl2, self.file3, self.file5)
        self.F_mean2 = POSEA3(self.img_nucl3, self.file3, self.file5)
        self.F_otsu2 = POSEA3(self.img_nucl4, self.file3, self.file5)
        self.F_triangle2 = POSEA3(self.img_nucl5, self.file3, self.file5)
        self.F_yen2 = POSEA3(self.img_nucl6, self.file3, self.file5)


        F_list2 = [self.F_isodata2, self.F_li2, self.F_mean2, self.F_otsu2, self.F_triangle2, self.F_yen2]

        if self.F_isodata2 == max(F_list2):
            tkinter.messagebox.showinfo(title="Find best (nucleus)", message="Choose isodata")
        elif self.F_li2 == max(F_list2):
            tkinter.messagebox.showinfo(title="Find best (nucleus)", message="Choose li")
        elif self.F_mean2 == max(F_list2):
            tkinter.messagebox.showinfo(title="Find best (nucleus)", message="Choose mean")
        elif self.F_otsu2 == max(F_list2):
            tkinter.messagebox.showinfo(title="Find best (nucleus)", message="Choose otsu")
        elif self.F_triangle2 == max(F_list2):
            tkinter.messagebox.showinfo(title="Find best (nucleus)", message="Choose triangle")
        else:
            tkinter.messagebox.showinfo(title="Find best (nucleus)", message="Choose yen")


    def showresult(self):
        if self.img_cyto is not None:
            self.result_cyto = Image.fromarray(self.img_cyto)
            self.img6 = customtkinter.CTkImage(Image.fromarray(self.img_cyto), size=(800, 800))
            self.sixth_frame_image_label = customtkinter.CTkLabel(self.sixth_frame, text="", image=self.img6)
            self.sixth_frame_image_label.grid(row=0, column=1, padx=25, pady=40)
        if self.img_nucl is not None:
            self.result_nucl = Image.fromarray(self.img_nucl)
            self.img7 = customtkinter.CTkImage(Image.fromarray(self.img_nucl), size=(800, 800))
            self.seventh_frame_image_label = customtkinter.CTkLabel(self.seventh_frame, text="", image=self.img7)
            self.seventh_frame_image_label.grid(row=0, column=1, padx=25, pady=40)

def run_gui():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    run_gui()


