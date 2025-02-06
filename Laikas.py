#Pradėjo spręsti užduotį, kai buvo v1 valandų, m1 minučių, s1 sekundžių,
#, baigė, kai buvo v2 valandų, m2 minučių, s2 sekundžių
#Kiek laiko sprendė užduotį valandomis minutėmis sekundėmis

v1, m1, s1 = input("Įveskite kiek valandų minuęių ir sekundžių, kai pradėjo spręsti\n").split()

v1=int(v1)
m1=int(m1)
s1=int(s1)

laikas1 = v1*3600+m1*60+s1

v2, m2, s2 = input("Įveskite kiek valandų minuęių ir sekundžių, kai baigė spręsti\n").split()

v2=int(v2)
m2=int(m2)
s2=int(s2)

laikas2 = v2*3600+m2*60+s2

laikas_delta = laikas2-laikas1



v_delta = int(laikas_delta/3600)
m_delta = int((laikas_delta % 3600)/60)
s_delta = laikas_delta%60

print(f"Sprendė užduotį: {v_delta} valandų, {m_delta} minučių, {s_delta} sekundžių")
