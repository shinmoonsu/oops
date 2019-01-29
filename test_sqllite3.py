import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("drop table if exists towns")

conn.commit()

c.execute("""create table towns (
        이름    text,
        피코드        text,
		값	int)""")

# c.execute("""create table hotels (
#         hid     int     primary key not NULL ,
#         tid     int,
#         name    text,
#         address text,
#         rooms   int,
#         rate    float)""")

c.execute("""insert into towns values ("소쿠리", "토큰", 0)""")
c.execute("""insert into towns values ("대박소쿠리", "CB1", 0)""")
c.execute("""insert into towns values ("광주리", "CB22", 0)""")

# c.execute("""insert into hotels values (1, 2, "Hamilkilo Hotel", "Chesterton Road", 15, 40.)""")
# c.execute("""insert into hotels values (2, 2, "Arun Dell", "Chesterton Road", 60, 70.)""")
# c.execute("""insert into hotels values (3, 2, "Crown Plaza", "Downing Street", 100, 105.)""")
# c.execute("""insert into hotels values (4, 1, "Well House Manor", "Spa Road", 5, 80.)""")
# c.execute("""insert into hotels values (5, 1, "Beechfield House", "The Main Road", 26, 110.)""")

# conn.commit()

c.execute ("select * from towns")

for row in c:
        print (row)

c.close()