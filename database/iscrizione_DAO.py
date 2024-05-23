from database.DB_connect import get_connection
from model.iscrizione import Iscrizione


def get_studente_corso(corso):
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = "select * from iscrizione i where i.codins = %s "
        cursor.execute(query,(corso,))
        for row in cursor:
            result.append(Iscrizione(**row))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None
