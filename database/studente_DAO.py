# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


def get_studente(matricola):
    cnx = get_connection()

    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = "select DISTINCT * from studente s where s.matricola = %s"
        cursor.execute(query, (matricola,))
        row = cursor.fetchone()
        if row is not None:
            result = Studente(**row)
        else:
            result = None
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

