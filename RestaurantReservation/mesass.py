from app import models,db

m1 = models.Mesa(id=1, capacidad= 2)
m2 = models.Mesa(id=2, capacidad= 2)
m3 = models.Mesa(id=3, capacidad= 4)
m4 = models.Mesa(id=4, capacidad= 4)
m5 = models.Mesa(id=5, capacidad= 2)
m6 = models.Mesa(id=6, capacidad= 4)
m7 = models.Mesa(id=7, capacidad= 2)
m8 = models.Mesa(id=8, capacidad= 5)
m9 = models.Mesa(id=9, capacidad= 6)
m10 = models.Mesa(id=10, capacidad= 7)
m11 = models.Mesa(id=11, capacidad= 7)
m12 = models.Mesa(id=12, capacidad= 3)
m13 = models.Mesa(id=13, capacidad= 5)
m14 = models.Mesa(id=14, capacidad= 3)
m15 = models.Mesa(id=15, capacidad= 4)
m16 = models.Mesa(id=16, capacidad= 1)
m17 = models.Mesa(id=17, capacidad= 1)
m18 = models.Mesa(id=18, capacidad= 1)
m19 = models.Mesa(id=19, capacidad= 1)

db.session.add_all([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19])
db.session.commit()


