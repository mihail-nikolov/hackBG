import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE users(id INTEGER PRIMARY KEY,
                                    name TEXT, monthly_salary INTEGER,
                                    yearly_bonus INTEGER, position TEXT )""")
conn.commit()

ivan_ivanov = ("Ivan Ivanov", 5000, 10000, "Software Developer")
cursor.execute("""INSERT INTO users(name, monthly_salary, yearly_bonus,
                            position)VALUES(?, ?, ?, ?)""", ivan_ivanov)

conn.commit()

rado_rado = ("Rado Rado", 500, 0, "Technical Support Intern")
cursor.execute("""INSERT INTO users(name, monthly_salary, yearly_bonus,
                            position)VALUES(?, ?, ?, ?)""", rado_rado)

conn.commit()

ivo_ivo = ("Ivo Ivo", 10000, 100000, "CEO")
cursor.execute("""INSERT INTO users(name, monthly_salary, yearly_bonus,
                            position)VALUES(?, ?, ?, ?)""", ivo_ivo)

conn.commit()

petar_petrov = ("Petar Petrov", 3000, 1000, "Marketing Manager")
cursor.execute("""INSERT INTO users(name, monthly_salary, yearly_bonus,
                            position)VALUES(?, ?, ?, ?)""", petar_petrov)

conn.commit()

maria_georgieva = ("Maria Georgieva", 8000, 10000, "COO")
cursor.execute("""INSERT INTO users(name, monthly_salary, yearly_bonus,
                            position)VALUES(?, ?, ?, ?)""", maria_georgieva)

conn.commit()
