from tkinter.ttk import Combobox
import numpy as np
import mysql.connector
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
from tkinter.messagebox import askyesno
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import dataBase


class supplier:

    global btn_frame

    def __init__(self):
        self.screen_s = Tk()
        self.screen_s.title("Supplier Dashboard")
        self.screen_s.geometry("2560x1600")

        # Sustainability Metrics
        process_step = StringVar()

        virmat_w = StringVar()
        recmat_w = StringVar()
        reumat_w = StringVar()
        redmat_w = StringVar()
        waste_m = StringVar()

        water_w = StringVar()
        fuel = StringVar()
        electricity = StringVar()
        transportation = StringVar()

        co2_em = StringVar()

        cycle = StringVar()
        operator = StringVar()

        noise = StringVar()
        employment = StringVar()

        head_entry = StringVar()


        def iexits():  # DONE
            iexits = askyesno("Sustainability Data Base System ", "Confirm to Exit")
            if iexits > 0:
                self.screen_s.destroy()
                return

        # Linking to the Data Base

        def cleard():  # DONE

            self.entprc.delete(0, END)
            self.entvirmat.delete(0, END)
            self.entrecmat.delete(0, END)
            self.entreumat.delete(0, END)
            self.entredmat.delete(0, END)
            self.entwastemat.delete(0, END)
            self.entwater.delete(0, END)
            self.entfuel.delete(0, END)
            self.entelect.delete(0, END)
            self.enttran.delete(0, END)
            self.entcyc.delete(0, END)
            self.entopr.delete(0, END)
            self.entnl.delete(0, END)
            self.entemp.delete(0, END)

        def addat(): # DONE

            # Calculating CO2 based on Energy entries
            co2_em = 0.80 * (float(self.entfuel.get())) + 0.56 * (float(self.entelect.get())) + (
                        (float(self.enttran.get())) / 3.32) * 2.33

            with open('Session', 'r') as file_s:
                verify_s = file_s.readlines()

            id_KEY = verify_s[0]

            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="cs20SF94",
                database="sustainable_dat_B001"

            )
            db_cursor = db_connection.cursor()

            query = "INSERT INTO sustainable_tabl_M001 VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"
            """(id_KEY, process_step, virmat_w, recmat_w, reumat_w, redmat_w, waste_m, water_w, fuel, electricity, transportation, cycle, operator, noise, employment, co2_em)"""
            VALUES = (
            id_KEY, self.entprc.get(), self.entvirmat.get(), self.entrecmat.get(), self.entreumat.get(), self.entredmat.get(), self.entwastemat.get(),
            self.entwater.get(), self.entfuel.get(), self.entelect.get(), self.enttran.get(),
            self.entcyc.get(), self.entopr.get(), self.entnl.get(), self.entemp.get(), co2_em)
            db_cursor.execute(query, VALUES)
            db_connection.commit()

            print("inserted successfully")

            cleard()
            con_excl()

        def susval(event):

            global record
            searchsus = dtlist.curselection()[0]
            record = dtlist.get(searchsus)

        def showdat(): # DONE

            dtlist.delete(0, END)
            for rows in dataBase.view_data():

                dtlist.insert(END, rows, str(""))


        def deletedat(): # DONE

            dataBase.delete_data(record[0])

            cleard()
            showdat()

        def con_excl():

            with open('Session', 'r') as file_s:
                verify_s = file_s.readlines()
                id_KEY = verify_s[0]

            db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="cs20SF94",
                database="sustainable_dat_B001"

            )
            db_cursor = db_connection.cursor()

            query = "SELECT * FROM sustainable_tabl_M001 WHERE id_KEY=%s"
            db_cursor.execute(query, (id_KEY,))

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

                f, ax = plt.subplots(figsize=(3.55, 3.6))

                # Set up the matplotlib figure

                a = self.enthd_ch.get()

                df1 = df[['PS','CO2',a]]

                sns.lineplot(x='CO2', y=a, hue = 'PS', data=df1)

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

                h3 = df.groupby('PS').agg('sum')
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

        supplier_frm = Frame(self.screen_s, width=2560, height=1800)
        supplier_frm.grid()

        tt_frame = Frame(supplier_frm, bd=2, width=2560, height=10, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        tt_frame.pack(side=TOP)

        lbltt = Label(tt_frame, text="Supplier Data Entry", font=('arial', 20, 'bold'), bg="Ghost White")
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

        datlst_frame = LabelFrame(datvis_frame, bd=1, height=10,  bg="SkyBlue2",
                                  relief=RIDGE,
                                  font=('arial', 18, 'bold'), text="Entries\n")
        datlst_frame.pack(side=BOTTOM)



        # Entry Widgets
        # Circularity Metrics

        # Process steps
        self.lblprc = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Process Step (PS):", padx=2,
                            pady=2, width=25)
        self.lblprc.grid(row=0, column=0, sticky=W)
        self.entprc = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=process_step, width=10)
        self.entprc.grid(row=0, column=1)

        # Circularity Metrics
        self.lblcirc = Label(datent_frame, bg="SkyBlue2", foreground="lavender", font=('arial', 14, 'bold'), text="Circularity Metrics", padx=2,
                             pady=2, width=25)
        self.lblcirc.grid(row=1, column=0)

        self.lblvirmat = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Virgin Material (VM):",
                               padx=2, pady=2, width=25)
        self.lblvirmat.grid(row=2, column=0, sticky=W)
        self.entvirmat = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=virmat_w, width=10)
        self.entvirmat.grid(row=2, column=1)
        self.lblvirmatmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="kg", padx=2, pady=2, width=10)
        self.lblvirmatmt.grid(row=2, column=2, sticky=W)

        self.lblrecmat = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Recycled Material (REC):",
                               padx=2, pady=2, width=25)
        self.lblrecmat.grid(row=3, column=0, sticky=W)
        self.entrecmat = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=recmat_w, width=10)
        self.entrecmat.grid(row=3, column=1)
        self.lblrecmatmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="kg", padx=2, pady=2, width=10)
        self.lblrecmatmt.grid(row=3, column=2, sticky=W)

        self.lblreumat = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Reused Material (REU):",
                               padx=2, pady=2, width=25)
        self.lblreumat.grid(row=4, column=0, sticky=W)
        self.entreumat = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=reumat_w, width=10)
        self.entreumat.grid(row=4, column=1)
        self.lblreumatmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="kg", padx=2, pady=2, width=10)
        self.lblreumatmt.grid(row=4, column=2, sticky=W)

        self.lblredmat = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Reduced Material (RED):",
                               padx=2, pady=2, width=25)
        self.lblredmat.grid(row=5, column=0, sticky=W)
        self.entredmat = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=redmat_w, width=10)
        self.entredmat.grid(row=5, column=1)
        self.lblredmatmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="kg", padx=2, pady=2, width=10)
        self.lblredmatmt.grid(row=5, column=2, sticky=W)

        self.lblwastemat = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Waste Material (WM):",
                               padx=2, pady=2, width=25)
        self.lblwastemat.grid(row=6, column=0, sticky=W)
        self.entwastemat = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=waste_m, width=10)
        self.entwastemat.grid(row=6, column=1)
        self.lblwastematmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="kg", padx=2, pady=2, width=10)
        self.lblwastematmt.grid(row=6, column=2, sticky=W)

        # Environmental Metrics
        self.lblenv = Label(datent_frame, bg="SkyBlue2", foreground="lavender", font=('arial', 14, 'bold'), text="Environmental Metrics", padx=2,
                             pady=2, width=25)
        self.lblenv.grid(row=7, column=0)

        self.lblwaterw = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Water Consumption (WT):", padx=2,
                               pady=2, width=25)
        self.lblwaterw.grid(row=8, column=0, sticky=W)
        self.entwater = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=water_w, width=10)
        self.entwater.grid(row=8, column=1)
        self.lblwatermt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="m3", padx=2, pady=2, width=10)
        self.lblwatermt.grid(row=8, column=2, sticky=W)

        self.lblfuel = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Fuel (FL):", padx=2,
                               pady=2, width=25)
        self.lblfuel.grid(row=9, column=0, sticky=W)
        self.entfuel = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=fuel, width=10)
        self.entfuel.grid(row=9, column=1)
        self.lblfuelmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="kWh", padx=2, pady=2, width=10)
        self.lblfuelmt.grid(row=9, column=2, sticky=W)

        self.lblelect = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Electricity (EL):", padx=2,
                             pady=2, width=25)
        self.lblelect.grid(row=10, column=0, sticky=W)
        self.entelect = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=electricity, width=10)
        self.entelect.grid(row=10, column=1)
        self.lblelectmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="kWh", padx=2, pady=2, width=10)
        self.lblelectmt.grid(row=10, column=2, sticky=W)

        self.lbltran = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Transportation (TR):",
                              padx=2,
                              pady=2, width=25)
        self.lbltran.grid(row=11, column=0, sticky=W)
        self.enttran = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=transportation, width=10)
        self.enttran.grid(row=11, column=1)
        self.lbltranmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="kWh", padx=2, pady=2, width=10)
        self.lbltranmt.grid(row=11, column=2, sticky=W)

        # Economic Metrics
        self.lblecon = Label(datent_frame, bg="SkyBlue2", foreground="lavender", font=('arial', 14, 'bold'), text="Economic Metrics", padx=2,
                            pady=2, width=25)
        self.lblecon.grid(row=12, column=0)

        self.lblcyc = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Cycle Time (CY):",
                             padx=2,
                             pady=2, width=25)
        self.lblcyc.grid(row=13, column=0, sticky=W)
        self.entcyc = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=cycle, width=10)
        self.entcyc.grid(row=13, column=1)
        self.lblcycmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="s", padx=2, pady=2, width=10)
        self.lblcycmt.grid(row=13, column=2, sticky=W)

        self.lblopr = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Operators (OP):",
                            padx=2,
                            pady=2, width=25)
        self.lblopr.grid(row=14, column=0, sticky=W)
        self.entopr = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=operator, width=10)
        self.entopr.grid(row=14, column=1)
        self.lbloprmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="#", padx=2, pady=2, width=10)
        self.lbloprmt.grid(row=14, column=2, sticky=W)

        # Social Metrics
        self.lblsoc = Label(datent_frame, bg="SkyBlue2", foreground="lavender", font=('arial', 14, 'bold'), text="Social Metrics", padx=2,
                            pady=2, width=25)
        self.lblsoc.grid(row=15, column=0)

        self.lblnl = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Noise Level (NL):",
                            padx=2,
                            pady=2, width=25)
        self.lblnl.grid(row=16, column=0, sticky=W)
        self.entnl = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=noise, width=10)
        self.entnl.grid(row=16, column=1)
        self.lblnlmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="db", padx=2, pady=2, width=10)
        self.lblnlmt.grid(row=16, column=2, sticky=W)

        self.lblemp = Label(datent_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Creation of employment (EP):",
                            padx=2,
                            pady=2, width=25)
        self.lblemp.grid(row=17, column=0, sticky=W)
        self.entemp = Entry(datent_frame, font=('arial', 14, 'bold'), textvariable=employment, width=10)
        self.entemp.grid(row=17, column=1)
        self.lblempmt = Label(datent_frame, bg="SkyBlue2", font=('arial', 12), text="#", padx=2, pady=2, width=10)
        self.lblempmt.grid(row=17, column=2, sticky=W)

        self.lblinfo = Label(datent_frame, bg="SkyBlue2", foreground="lavender", font=('arial', 14, 'bold'), text="Info:", padx=2,
                            pady=2, width=25)
        self.lblinfo.grid(row=18, column=0)

        self.lblinfo1 = Label(datent_frame, bg="SkyBlue2", font=('arial', 12),
                             text="Press \n Add Data", padx=2, pady=2, width=10)
        self.lblinfo1.grid(row=18, column=1)

        self.lblinfo2 = Label(datent_frame, bg="SkyBlue2", font=('arial', 12),
                              text="To save", padx=2, pady=2, width=10)
        self.lblinfo2.grid(row=19, column=1)

        self.lblinfo3 = Label(datent_frame, bg="SkyBlue2", font=('arial', 12),
                              text="", padx=2, pady=2, width=10)
        self.lblinfo3.grid(row=20, column=1)

        self.lblinfo4 = Label(datent_frame, bg="SkyBlue2", font=('arial', 12),
                              text="", padx=2, pady=2, width=10)
        self.lblinfo4.grid(row=21, column=1)


        # Graph
        self.lblhd = Label(datgrp_frame, bg="SkyBlue2", font=('arial', 14, 'bold'), text="Metrics for C02 trend lines:",
                            padx=2,
                            pady=2, width=25)
        self.lblhd.grid(row=0, column=0)

        self.enthd_ch = Combobox(datgrp_frame, width=25, textvariable=head_entry)
        self.enthd_ch['values'] = ('VM', 'REC', 'REU', 'RED', 'WM', 'WT', 'FL', 'EL', 'TR', 'CY', 'OP', 'NL', 'EP')
        self.enthd_ch.current(0)
        self.enthd_ch.grid(row=0, column=1)

        self.btn_set_s = Button(datgrp_frame, text="Draw", height=2, width=10, command=vis_graphs)
        self.btn_set_s.grid(row=0, column=2)

        # Listbox
        scrolbr = Scrollbar(datlst_frame)
        scrolbr.grid(row=0, column=1, sticky='ns')
        dtlist = Listbox(datlst_frame, font=('arial', 12, 'bold'), width=110, height=10, yscrollcommand=scrolbr.set)
        dtlist.bind('<<ListboxSelect>>', susval)
        scrolbr.config(command=dtlist.yview)
        dtlist.grid(row=0, column=0, padx=8)

        # Main Frame Buttons
        self.btn_entr_s = Button(btn_frame, text="Add Data", height=2, width=10, command=addat)
        self.btn_entr_s.grid(row=0, column=0)

        self.btn_clr_s = Button(btn_frame, text="Clear Data", height=2, width=10, command=cleard)
        self.btn_clr_s.grid(row=0, column=1)

        self.btn_shw_s = Button(btn_frame, text="View Data", height=2, width=10, command=showdat)
        self.btn_shw_s.grid(row=0, column=2)

        self.btn_dlt_s = Button(btn_frame, text="Delete Data", height=2, width=10, command=deletedat)
        self.btn_dlt_s.grid(row=0, column=3)

        self.btn_ext_s = Button(btn_frame, text="Exit", height=2, width=10, command=iexits)
        self.btn_ext_s.grid(row=0, column=6)

    def run(self):
        self.screen_s.mainloop()

