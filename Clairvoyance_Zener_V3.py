"""Ce script permet de mesurer le niveau de clairvoyance basé sur les formes de Zener. L'utilisateur doit
deviner la forme que la machine à choisi. Ce test s'effectue sur 25 essais consécutif.
À la fin du test, il affiche le nombre d'essais réussis pour chaque forme ainsi que le pourcentage de 
probabilité du hasard

Pour déterminer si le nombre de bonnes réponses devinées dépasse les probabilités dites normales, vous pouvez calculer la 
probabilité d'obtenir ce nombre de réponses correctes par hasard, en utilisant la distribution binomiale.

La distribution binomiale est utilisée pour calculer la probabilité de réussite ou d'échec dans une série d'essais indépendants et 
identiques. Dans ce cas, chaque essai est une réponse à la devinette, qui peut être correcte ou incorrecte, et nous voulons calculer 
la probabilité d'obtenir un certain nombre de réponses correctes dans un total de 25 essais.

La formule pour calculer la probabilité de x succès dans n essais, avec une probabilité de succès p à chaque essai, est 
: P(X = x) = (nCx) * p^x * (1-p)^(n-x)

où nCx est le coefficient binomial "n choose x", qui peut être calculé avec la formule :

nCx = n! / (x! * (n-x)!)

Dans ce cas, n est égal à 25 (le nombre total d'essais) et p est la probabilité de deviner correctement une réponse, 
qui est de 1/5 ou 0,2 (puisque nous avons 5 formes possibles). Pour calculer la probabilité d'obtenir x réponses correctes, 
vous pouvez remplacer ces valeurs dans la formule ci-dessus.

Une fois que vous avez calculé la probabilité, vous pouvez comparer cette valeur à un seuil de significativité, comme 0,05. 
Si la probabilité d'obtenir le nombre de bonnes réponses devinées par hasard est inférieure à ce seuil, vous pouvez conclure que 
le résultat est statistiquement significatif et que la performance du joueur dépasse ce que l'on pourrait attendre par hasard.
"""

import random
from math import comb

formes = ['étoile', 'carré', 'cercle', 'plus', 'vague']
correspondance = {1: 'étoile', 2: 'carré', 3: 'cercle', 4: 'plus', 5: 'vague'}
comptes = {forme: 0 for forme in formes}
total = 0

for i in range(25):
  réponse = random.choice(formes)
  devine = int(input("Devine la forme (1-étoile, 2-carré, 3-cercle, 4-plus, 5-vague): "))
  devine = correspondance.get(devine, None)
  if devine == réponse:
    print("Exact!")
    comptes[réponse] += 1
    total += 1
  else:
    print("Manqué!")

print("\nRésultats:")
for forme, compte in comptes.items():
  print(f"{forme}: {compte} ({compte/total:.2f})")

p = 0.2 # probabilité de succès (deviner la bonne forme)
n = 25 # nombre d'essais (nombre de devinettes)
seuil = 0.05 # seuil de significativité
probabilite = sum([comb(n, x) * p**x * (1-p)**(n-x) for x in range(total, n+1)])
if probabilite < seuil:
  print(f"La probabilité d'obtenir {total} réponses correctes ou plus par hasard est de {probabilite:.4f}, ce qui est statistiquement significatif (p < {seuil}).")
else:
  print(f"La probabilité d'obtenir {total} réponses correctes ou plus par hasard est de {probabilite:.4f}, ce qui n'est pas statistiquement significatif (p >= {seuil}).")

