#Programmer dans language ésotérique

- **langage choisi** : Rockstar (Esolang.org : https://esolangs.org/wiki/Rockstar). Le tutoriel suivant a été utilisé pour avoir les commandes de bases pour construire p : https://codewithrockstar.com/tutorial.  

- **l'interpréteur** : Starship (Github : https://github.com/RockstarLang/rockstar)
> git clone https://github.com/RockstarLang/rockstar.git
> cd rockstar
> dotnet publish ./Starship/Rockstar -o binaries -c Release

- **Commande pour lancer p** : 
> cd DSL_esolangs
> ./binaries/rockstar p.rock

- **Utilisation de l'IA** : Un LLM a été utilisé pour rédiger run.sh pour lire les fichiers 01.in, 02.in, 03.in et 04.in et les comparés avec 01.out, 02.out, 03.out et 04.out. Ces fichiers présents dans tests/ ont été cependant rédigés à la main.
