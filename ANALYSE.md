# Analyse

## 1) Sémantique : 

D'un point de vue sémantique, les trois propositions du LLM calculent la même sortie pour la même entrée que p. En effet, les trois programmes testent si le nombre de caractères dans l'entrée saisie est égal ou pas au 10 premiers nombres premiers. Cela est très visible avec les différentes lignes de "If". Tout comme p, les trois programmes utilisent "Build ... up" pour construire la variable représentant le compteur de caractères. Les 4 scénarios de tests sont gérés correctement par les programmes p1, p2 et p3 quand on utilise le script **run.py**.

Il est aussi intéressant de noter qu'il a bien été demandé à l'IA de générer trois solutions différentes via, par exemple, le prompt "*Propose-moi une autre solution de code*". Cependant, à part l'utilisation de quelques fonctions différentes comme "take" dans p3, les programmes sont quasiment identiques. Il est même décevant de voir que p1 et p2 sont identiques (aux noms de variables près). Le LLM n'a donc pas complètement compris l'intention de générer des réponses sémantiquement équivalentes mais syntaxiquement différentiables.

On peut noter également que p1, p2 et p3 n'ont aucune dimension "musicale", ce qui fait pourtant parti du langage Rockstar. Le LLM utilise des noms de variables communs, sans poésie ou sens du rythme : "Count", "Length" ou "Number". p a été écrit pour essayer de raconter une histoire avec un champ lexical autour des sentiments, à la manière d'une chanson d'amour.

## 2) Syntaxe :

D'un point de vue syntaxique, p1, p2 et p3 adoptent des stratégies différentes de p. Le programme p utilise comme structure de données (pour les 10 premiers nombres premiers) une liste ordonnée avec une boucle de test parcourant cette liste; tandis que p1, p2 et p3 font des tests unitaires sur chaque valeur possible.

Cependant, les programmes gèrent d'une manière équivalente la construction du compteur. Deux petites différences sont notables : p assigne le compteur ainsi "Let Brian be **null**" et effectue le test "While feelings is greater than 0" tandis que p1, p2 et p3 font simplement "Put **0**" et "While Chars". Les deux techniques mènent au même résultat.
