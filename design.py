from tkinter.ttk import Combobox
import mysql.connector
import csv
import numpy as np
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from tkinter import *
from tkinter.messagebox import askyesno
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import dataBase


class designSim:

    global btn_frame

    def __init__(self):
        self.screen_dS = Tk()
        self.screen_dS.title("Design Metric Simulation")
        self.screen_dS.geometry("2560x1600")

        # self.label1 = Label(self.screen_s, text="Enter required data", bg="grey", width="300", height="2",
        # font=("Calibri", 13)).pack()

        # Sustainability Metrics
        color = StringVar()
        barrier = StringVar()
        closures = StringVar()
        closures_ln = StringVar()
        labell = StringVar()
        sleeves = StringVar()
        btl_size = StringVar()
        preform = StringVar()
        base_shape = StringVar()
        cap = StringVar()

        head_entry = StringVar()

        def iexits():  # DONE
            iexits = askyesno("Sustainability Design Simulation System ", "Confirm to Exit")
            if iexits > 0:
                self.screen_dS.destroy()
                return

        # Linking to the Listbox

        def cleard():  # DONE

            self.entclos.delete(0, END)
            self.entsleev.delete(0, END)
            self.entclosln.delete(0, END)
            self.entcol_ch.delete(0, END)
            self.entlabell.delete(0, END)
            self.entbar_coat.delete(0, END)
            self.entbtlsize.delete(0, END)


        def show_impact():

            global alert_rw
            file_fr =  open("ref_fr", "r")
            verify_reffr = file_fr.read().splitlines()

            file_con = open("ref_con", "r")
            verify_refcon = file_con.read().splitlines()

            file_wr = open("ref_wr", "r")
            verify_refwr = file_wr.read().splitlines()

            alert_rw = []

            # Color
            if self.entcol_ch.get() in verify_reffr:
                alert_rw.append("Color is recycle FRIENDLY")

            elif self.entcol_ch.get() in verify_refcon:
                alert_rw.append("Color is CONDITIONAL")

            elif self.entcol_ch.get() in verify_refwr:
                alert_rw.append("Color is PROBLEMATIC for recycling")

            # Coatings
            if self.entbar_coat.get() in verify_reffr:
                alert_rw.append("Coatings is recycle FRIENDLY")

            elif self.entbar_coat.get() in verify_refcon:
                alert_rw.append("Coatings is CONDITIONAL")

            elif self.entbar_coat.get() in verify_refwr:
                alert_rw.append("Coatings is PROBLEMATIC for recycling")


            # Closures
            if self.entclos.get() in verify_reffr:
                alert_rw.append("Closures is recycle FRIENDLY")

            elif self.entclos.get() in verify_refcon:
                alert_rw.append("Closures is CONDITIONAL")

            elif self.entclos.get() in verify_refwr:
                alert_rw.append("Closures is PROBLEMATIC for recycling")


            # Closures liners
            if self.entclosln.get() in verify_reffr:
                alert_rw.append("Closure liners is recycle FRIENDLY")

            elif self.entclosln.get() in verify_refcon:
                alert_rw.append("Closure liners is CONDITIONAL")

            elif self.entclosln.get() in verify_refwr:
                alert_rw.append("Closure liners is PROBLEMATIC for recycling")


            # Label
            if self.entlabell.get() in verify_reffr:
                alert_rw.append("Label is recycle FRIENDLY")

            elif self.entlabell.get() in verify_refcon:
                alert_rw.append("Label is CONDITIONAL")

            elif self.entlabell.get() in verify_refwr:
                alert_rw.append("Label is PROBLEMATIC for recycling")


            # Sleeves
            if self.entsleev.get() in verify_reffr:
                alert_rw.append("Sleeves is recycle FRIENDLY")

            elif self.entsleev.get() in verify_refcon:
                alert_rw.append("Sleeves is CONDITIONAL")

            elif self.entsleev.get() in verify_refwr:
                alert_rw.append("Sleeves is PROBLEMATIC for recycling")


            # Bottle size
            if self.entbtlsize.get() in verify_reffr:
                alert_rw.append("Bottle size is recycle FRIENDLY")

            elif self.entbtlsize.get() in verify_refcon:
                alert_rw.append("Bottle size is CONDITIONAL")

            elif self.entbtlsize.get() in verify_refwr:
                alert_rw.append("Bottle size is PROBLEMATIC for recycling")

            # Cap
            if self.entcap.get() in verify_reffr:
                alert_rw.append("Cap is recycle FRIENDLY")

            elif self.entcap.get() in verify_refcon:
                alert_rw.append("Cap is CONDITIONAL")

            elif self.entcap.get() in verify_refwr:
                alert_rw.append("Cap is PROBLEMATIC for recycling")

            showdat()

        def susval(event):

            global record
            searchsus = dtlist.curselection()[0]
            record = dtlist.get(searchsus)

        def showdat(): # DONE

            dtlist.delete(0, END)
            for rows in alert_rw:

                dtlist.insert(END, rows, str(""))

        def con_excl():

            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="cs20SF94",
                database="sustainable_dat_B001"

            )
            db_cursor = db_connection.cursor()

            query = "SELECT * FROM sustainable_tabl_M001"
            db_cursor.execute(query)

            with open('converted.csv', 'w') as f:
                writer = csv.writer(f)
                headings = ['N:', 'CM', 'PS', 'VM', 'REC', 'REU', 'RED', 'WM', 'WT', 'FL', 'EL', 'TR', 'CY', 'OP', 'NL', 'EP', 'CO2']
                writer.writerow(headings)
                for row in db_cursor.fetchall():
                    writer.writerow(row)

        con_excl()


        def delete_can():

            canvas.get_tk_widget().destroy()
            canvas1.get_tk_widget().destroy()
            canvas2.get_tk_widget().destroy()

            con_excl()
            vis_graphs()


        def vis_graphs():

            con_excl()

            df = pd.read_csv(r"/Users/c_safarli/Documents/Master Thesis/Data Ex App/exchange__DAT/converted.csv")
            df.info()
            df.head()

            df = df.reset_index()

            df.columns = df.columns.str.replace(' ', '')

            df.info()

            df = df.dropna()  # null values

            # %%!!!!!!!!!!!!!!!

            def create_plot():

                sns.set(style="white")

                # Set up the matplotlib figure

                f, ax = plt.subplots(figsize=(3.55, 3.6))

                # Set up the matplotlib figure

                a = self.enthd_ch.get()
                df1 = df[['CM', 'CO2', a]]

                sns.lineplot(x='CO2', y=a, hue='CM', data=df1)

                plt.title('Trend lines')

                return f

            def create_plot1():

                sns.set(style="white")

                # Set up the matplotlib figure

                f1, ax2 = plt.subplots(figsize=(3.55, 3.6))

                plt.title('Correlation Matrix')

                rs = sns.heatmap(df.corr(), cbar_kws={"shrink": .82},
                  linewidths=0.1, linecolor='gray')

                rs.set_xticklabels(rs.get_xmajorticklabels(), fontsize=8)
                rs.set_yticklabels(rs.get_ymajorticklabels(), fontsize=8)

                return f1

            def create_plot2():

                sns.set(style="white")

                from matplotlib.gridspec import GridSpec
                import matplotlib.pyplot as plt

                # Set up the matplotlib figure

                f2, ax3 = plt.subplots(figsize=(3.55, 3.6))

                h3 = df.groupby('CM').agg('sum')
                print(h3)

                h3_labels = h3.CO2.sort_values().index
                plt.title('CO2 Emission')

                h3_counts = h3.CO2.sort_values()
                cmap = plt.get_cmap('Spectral')
                colors = [cmap(i) for i in np.linspace(0, 1, 8)]
                h3_show_ids = plt.pie(h3_counts, labels=h3_labels, autopct='%1.1f%%', shadow=True, colors=colors)
                plt.tight_layout()
                plt.show()

                return f2

            fig = create_plot()
            fig1 = create_plot1()
            fig2 = create_plot2()

            global canvas
            global canvas1
            global canvas2

            canvas = FigureCanvasTkAgg(fig, master=datgrp_frame)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=1)

            canvas1 = FigureCanvasTkAgg(fig1, master=datgrp_frame)  # A tk.DrawingArea.
            canvas1.draw()
            canvas1.get_tk_widget().grid(row=1, column=2)

            canvas2 = FigureCanvasTkAgg(fig2, master=datgrp_frame)  # A tk.DrawingArea.
            canvas2.draw()
            canvas2.get_tk_widget().grid(row=1, column=0)

        sns.set_style(style='white')  # plots now have a white background

        # Main Frame for Dahsboard

        supplier_frm = Frame(self.screen_dS, width=2560, height=1800)
        supplier_frm.grid()

        tt_frame = Frame(supplier_frm, bd=2, width=2560, height=20, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        tt_frame.pack(side=TOP)

        lbltt = Label(tt_frame, text="Design Simulation", font=('arial', 30, 'bold'), bg="Ghost White")
        lbltt.grid()

        global btn_frame
        btn_frame = Frame(supplier_frm, bd=2, width=2560, height=30, padx=18, pady=10, bg="Ghost White",
                          relief=RIDGE)
        btn_frame.pack(side=BOTTOM)

        dat_frm = Frame(supplier_frm, bd=2, width=2560, height=1550, relief=RIDGE)
        dat_frm.pack(side=BOTTOM)

        datent_frame = LabelFrame(dat_frm, bd=1, width=700, height=1550, bg="SkyBlue2",
                                  relief=RIDGE,
                                  font=('arial', 18, 'bold'), text="Data Entry\n")
        datent_frame.pack(side=LEFT)

        datvis_frame = LabelFrame(dat_frm, bd=1, width=1860, height=1550, bg="SkyBlue2",
                                  relief=RIDGE,
                                  font=('arial', 18, 'bold'), text="Data Visualisation\n")
        datvis_frame.pack(side=RIGHT)

        datgrp_frame = LabelFrame(datvis_frame, bd=1, height=20, bg="SkyBlue2",
                                  relief=RIDGE,
                                  font=('arial', 18, 'bold'), text="Visualisation\n")
        datgrp_frame.pack(side=TOP)

        datlst_frame = LabelFrame(datvis_frame, bd=1, height=10, bg="SkyBlue2",
                                  relief=RIDGE,
                                  font=('arial', 18, 'bold'), text="Warnings\n")
        datlst_frame.pack(side=BOTTOM)

        # Entry Widgets
        # Metrics

        self.lblcolor = Label(datent_frame, bg="SkyBlue2", font=('arial', 14), text="Color:", padx=2,
                            pady=2, width=20)
        self.lblcolor.grid(row=0, column=0, sticky=W)

        self.entcol_ch = Combobox(datent_frame, width=20, textvariable=color)
        self.entcol_ch['values'] = ('Clear', 'Natural', 'Light Blue/Green' 'Dark Blue/Green', 'Black', 'Metallic', 'Solid')
        self.entcol_ch.current(0)
        self.entcol_ch.grid(row=0, column=1)

        self.lblbar_coat = Label(datent_frame, bg="SkyBlue2", font=('arial', 14), text="Barrier Coatings: \n *BW-Bottle Weight",
                               padx=2, pady=2, width=20)
        self.lblbar_coat.grid(row=1, column=0, sticky=W)

        self.entbar_coat = Combobox(datent_frame, width=20, textvariable=barrier)
        self.entbar_coat['values'] = (
        'CVD', 'SiOx', 'Monox',  'PEN <%3 of *BW ', 'Amosorb <%3 of *BW', 'MXD6 <%3 of *BW', 'EVOH', 'MXD6 > 5% of *BW')
        self.entbar_coat.current(0)
        self.entbar_coat.grid(row=1, column=1)

        self.lblclos = Label(datent_frame, bg="SkyBlue2", font=('arial', 14), text="Closures:",
                               padx=2, pady=2, width=20)
        self.lblclos.grid(row=2, column=0, sticky=W)
        self.entclos = Combobox(datent_frame, width=20, textvariable=closures)
        self.entclos['values'] = (
            'HDPE', 'LDPE', 'PP', 'Metals', 'PS', 'PVC')
        self.entclos.current(0)
        self.entclos.grid(row=2, column=1)

        self.lblclosln = Label(datent_frame, bg="SkyBlue2", font=('arial', 14), text="Closure liners and seals:",
                             padx=2, pady=2, width=20)
        self.lblclosln.grid(row=3, column=0, sticky=W)
        self.entclosln = Combobox(datent_frame, width=20, textvariable=closures_ln)
        self.entclosln['values'] = (
            'PE+EVA', 'Foamed Silicone', 'PET', 'Paper', 'Silicone „swimming‟ valves density < 1 g/cm3', 'Neck Foils Metal', 'PVC', 'EVA Silicone density > 1 g/cm3')
        self.entclosln.current(0)
        self.entclosln.grid(row=3, column=1)

        self.lbllabell = Label(datent_frame, bg="SkyBlue2", font=('arial', 14), text="Label:",
                               padx=2, pady=2, width=20)
        self.lbllabell.grid(row=4, column=0, sticky=W)
        self.entlabell = Combobox(datent_frame, width=20, textvariable=labell)
        self.entlabell['values'] = (
            'MDPE', 'LLDPE', 'Wraparound plastic', 'Wraparound paper labels', 'Metallic foils', 'Self-adhesive labels.', 'Pressure sensitive', 'Metallised')
        self.entlabell.current(0)
        self.entlabell.grid(row=4, column=1)

        self.lblsleev = Label(datent_frame, bg="SkyBlue2", font=('arial', 14), text="Sleeves:",
                               padx=2, pady=2, width=20)
        self.lblsleev.grid(row=5, column=0, sticky=W)
        self.entsleev = Combobox(datent_frame, width=20, textvariable=sleeves)
        self.entsleev['values'] = (
            'PE', 'EPS', 'Foamed PET & PET-G density < 1g/cm3', 'Full body PET shrink sleeves', 'PVC', 'PS', 'PET-G')
        self.entsleev.current(0)
        self.entsleev.grid(row=5, column=1)

        self.lblsize = Label(datent_frame, bg="SkyBlue2", font=('arial', 14), text="Bottle Size:",
                              padx=2, pady=2, width=20)
        self.lblsize.grid(row=6, column=0, sticky=W)
        self.entbtlsize = Combobox(datent_frame, width=20, textvariable=btl_size)
        self.entbtlsize['values'] = (
            'Diameter > 50mm, Length > 100mm', 'Diameter 40 -50mm', 'Diameter < 30mm, Length < 100mm')
        self.entbtlsize.current(0)
        self.entbtlsize.grid(row=6, column=1)


        self.lblcap = Label(datent_frame, bg="SkyBlue2", font=('arial', 14), text="Cap:",
                             padx=2, pady=2, width=20)
        self.lblcap.grid(row=9, column=0, sticky=W)
        self.entcap = Combobox(datent_frame, width=20, textvariable=cap)
        self.entcap['values'] = ('Tethered cap', 'Standard', 'Thermal seal inside', 'Waxy paper inserts')
        self.entcap.current(0)
        self.entcap.grid(row=9, column=1)

        self.lblinfo = Label(datent_frame, bg="SkyBlue2", foreground="lavender", font=('arial', 14, 'bold'), text="Info:", padx=2,
                            pady=2, width=20)
        self.lblinfo.grid(row=10, column=0)

        self.lblinfo1 = Label(datent_frame, bg="SkyBlue2", font=('arial', 12),
                             text="Press \n Apply", padx=2, pady=2, width=10)
        self.lblinfo1.grid(row=10, column=1)

        self.lblinfo2 = Label(datent_frame, bg="SkyBlue2", font=('arial', 12),
                             text="To simulate \n metrics", padx=2, pady=2, width=10)
        self.lblinfo2.grid(row=11, column=1)

        # Graph
        self.lblhd = Label(datgrp_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Metrics for C02 trend lines::",
                           padx=2,
                           pady=2, width=25)
        self.lblhd.grid(row=0, column=0)

        self.enthd_ch = Combobox(datgrp_frame, width=25, textvariable=head_entry)
        self.enthd_ch['values'] = (
        'VM', 'REC', 'REU', 'RED', 'WM', 'WT', 'FL', 'EL', 'TR', 'CY', 'OP', 'NL', 'EP')
        self.enthd_ch.current(0)
        self.enthd_ch.grid(row=0, column=1)

        self.btn_set_s = Button(datgrp_frame, text="Draw", height=2, width=10, command=vis_graphs)
        self.btn_set_s.grid(row=0, column=2)

        # Visualisation
        scrolbr = Scrollbar(datlst_frame)
        scrolbr.grid(row=0, column=1, sticky='ns')
        dtlist = Listbox(datlst_frame, font=('arial', 12, 'bold'), width=110, height=10, yscrollcommand=scrolbr.set)
        dtlist.bind('<<ListboxSelect>>', susval)
        scrolbr.config(command=dtlist.yview)
        dtlist.grid(row=0, column=0, padx=8)

        # Main Frame Buttons
        self.btn_entr_s = Button(btn_frame, text="Apply", height=2, width=10, command=show_impact)
        self.btn_entr_s.grid(row=0, column=0)

        self.btn_clr_s = Button(btn_frame, text="Clear Data", height=2, width=10, command=cleard)
        self.btn_clr_s.grid(row=0, column=1)

        self.btn_ext_s = Button(btn_frame, text="Exit", height=2, width=10, command=iexits)
        self.btn_ext_s.grid(row=0, column=6)

    def run(self):
        self.screen_dS.mainloop()

