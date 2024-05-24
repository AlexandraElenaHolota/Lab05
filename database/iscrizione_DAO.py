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

def get_corsi_studente(matricola):
    cnx = get_connection()
    result = []
    if cnx is not None:
        cursor = cnx.cursor(dictionary=True)
        query = "select *  from iscrizione i where i.matricola = %s "
        cursor.execute(query, (matricola,))
        for row in cursor:
            result.append(Iscrizione(**row))
        cursor.close()
        cnx.close()
        return result
    else:
        print("Could not connect")
        return None

def iscrivi_corso(matricola, codins) -> bool:
    """
    Funzione che aggiunge uno studente agli iscritti di un corso
    :param matricola: la matricola dello studente
    :param codins: il codice del corso
    :return: True se l-operazione va a buon fine, False altrimenti
    """
    cnx = get_connection()
    result = []
    query = """INSERT IGNORE INTO `iscritticorsi`.`iscrizione` 
    (`matricola`, `codins`) 
    VALUES(%s,%s)
    """
    if cnx is not None:
        cursor = cnx.cursor()
        cursor.execute(query, (matricola, codins,))
        cnx.commit()
        cursor.close()
        cnx.close()
        return True
    else:
        print("Could not connect")
        return False

