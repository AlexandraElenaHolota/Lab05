from database import corso_DAO

corsi = corso_DAO.get_corso()
for c in corsi:
    print(c.codins)
