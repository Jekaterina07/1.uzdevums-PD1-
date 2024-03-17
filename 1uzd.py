# KLASI IZVEIDOŠANA, KUR PARAMETRI IR (VĀRDS, UZVĀRDS, LOMA UN VECUMS)

class Persona:

  def __init__(self, vards, uzvards, loma, vecums):
    self.vards = vards
    self.uzvards = uzvards
    self.loma = loma
    self.vecums = vecums


# DATU APVIENOŠANA

def apvienot_datus(fails_pirmais, fails_otrais):
  dati = []
  with open(fails_pirmais, "r") as f:
    for line in f:
      vards, uzvards, loma, vecums = line.strip().split(",")
      dati.append(Persona(vards, uzvards, loma, int(vecums)))
  with open(fails_otrais, "r") as f:
    for line in f:
      vards, uzvards, loma, vecums = line.strip().split(",")
      dati.append(Persona(vards, uzvards, loma, int(vecums)))
  return dati


def izdrukat_datus(dati):
  for persona in dati:
    print(f"{persona.vards} {persona.uzvards} ({persona.loma}): {persona.vecums}")

# -------------------------------------------------------------------------------------

# VISI APRĒĶINĀJAMIE LIELUMI...

# ADMINISTRATORA PIETEIKUMS

def aprekinat_administratoru(dati):
  administratori = []
  for persona in dati:
    if persona.loma == "administrators":
      administratori.append(persona)
  return administratori


# VIDĒJAIS VECUMS

def vidējais_vecums(administratori):
  if len(administratori) == 0:
    return None
  summa = 0
  for admin in administratori:
    summa += admin.vecums
  return summa / len(administratori)


# VECĀKAIS UN JAUNĀKAIS ADMIN MEKLĒŠANA

def vecākais_jaunākais(administratori):
  if len(administratori) == 0:
    return None, None
  vecākais = administratori[0]
  jaunākais = administratori[0]
  for admin in administratori:
    if admin.vecums > vecākais.vecums:
      vecākais = admin
    if admin.vecums < jaunākais.vecums:
      jaunākais = admin
  return vecākais, jaunākais


# FAILU ATVERŠANA, SAGLABĀŠANA UN DATU IERAKSTĪŠANA FAILOS

with open("admin.txt", "w") as f:
  f.write("Antons,Berziņš,administrators,19\n")
  f.write("Antonina,Zunda,administrators,54\n")
  f.write("Mihails,Porzingis,administrators,35\n")

with open("viesis.txt", "w") as f:
  f.write("Bogdans,Liepiņš,viesis,45\n")
  f.write("Ernests,Karkliņš,viesis,30\n")
  f.write("Ilja,Serenkovs,viesis,24\n")
  f.write("Kristaps,Bļodiņš,viesis,42\n")
  f.write("Andrejs,Černovs,viesis,58\n")

# DATU APVIENOŠANA (FAILU APVIENOŠANA))

dati = apvienot_datus("admin.txt", "viesis.txt")

# -----------------------

administratori = aprekinat_administratoru(dati)

avg_vecums = vidējais_vecums(administratori)
max, min = vecākais_jaunākais(administratori)

# -----------------------


# REZULTĀTU IZDRUKĀŠANA

# print("\n") - tukša rinda ar jauno rindkopu

print(f"Administratoriem vidējais vecums ir: {avg_vecums}")
print("\n")
print(f"Vecākais administrators ir: {max.vards} {max.uzvards} ({max.vecums})")
print("\n")
print(f"Jaunākais administrators ir: {min.vards} {min.uzvards} ({min.vecums})")
print("\n")
kop_skaits = len(dati) - len(administratori)
print(f"Apvienotajās datnēs kopā ir {len(administratori)} administratori un {kop_skaits} viesi")
print("\n")

# REZULĀTU IZDRUKĀŠANA

# print() - tukša rinda

print("Pilna informācija par visiem:")
print()
izdrukat_datus(dati)
