#Explications du programme p.rock

Le programme p.rock commence par attendre une saisie d'une chaîne de caractère au clavier, appelée **music**.
Si cette chaîne est vide (la personne utilisant p.rock a appuyé sur Entrée), un message est affiché.
Dans le cas contraire, on découpe la chaîne caractère par caractère que l'on stocke dans la variable **feelings**. On construit ensuite le compteur de caractère, **Brian**, en lui affectant la valeur 0 avant de lui ajouter +1 à chaque caractère enlevé à **feelings**. Ainsi, on arrête d'incrémenter **Brian** quand **feelings** est vide.
On décrit ensuite les 10 valeurs possibles de nombres premiers à tester : 2, 3, 5, 7, 11, 13, 17, 19, 23 et 29, contenues dans **love**. Une variable agissant comme un boolean est créé : **the fidelity**.
En parcourant **love**, on convertit ensuite les nombres de **love** en chaîne de caractère pour effectuer la comparaison avec le nombre de caractère de **music** stocké dans **Brian**. Si il y a une égalité, on affecte true à **the fidelity**. Sinon, cette variable garde sa valeur par défaut.
Enfin, en fonction de la valeur de **the fidelity**, on renvoit le message de fin approprié.
