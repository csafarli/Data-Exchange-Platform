import mysql.connector


def susdata():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="cs20SF94",

    )
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE DATABASE IF NOT EXISTS sustainable_dat_B001")


def cr_tabl():

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="cs20SF94",
        database="sustainable_dat_B001"

    )
    db_cursor = db_connection.cursor()

    db_cursor.execute(
        "CREATE TABLE IF NOT EXISTS sustainable_tabl_M001 (id INT NOT NULL AUTO_INCREMENT,id_KEY longtext, process_step longtext, virmat_w longtext , recmat_w longtext, reumat_w longtext, redmat_w longtext, waste_m longtext, water_w longtext, fuel longtext, electricity longtext, transportation longtext, cycle longtext, operator longtext, noise longtext, employment longtext, co2_em longtext, primary key (id))")


def view_data():

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
    filter_rows = "SELECT * FROM sustainable_tabl_M001 WHERE id_KEY=%s"
    db_cursor.execute(filter_rows, (id_KEY,))
    rows = db_cursor.fetchall()
    db_connection.commit()
    db_connection.close()
    return rows


def delete_data(id):

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="cs20SF94",
        database="sustainable_dat_B001"

    )
    db_cursor = db_connection.cursor()
    delete_row = "DELETE FROM sustainable_tabl_M001 WHERE id=%s"
    db_cursor.execute(delete_row, (id,))
    db_connection.commit()
    db_connection.close()


susdata()


