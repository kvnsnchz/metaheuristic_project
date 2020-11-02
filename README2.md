Projet IA308 - Kevin Sanchez
========================================

# La fonction objective:

> Les différents algorithmes ont été comparés à un problème beaucoup plus difficile que celui original, avec 15 capteurs (```-n 15```) de 0,15*dim de radio (```-r 0.15```), et avec un maximum de 200 itérations (```-i 200```). Ce problème m'a permis de distinguer les 3 meilleurs entre les 34 algorithmes que j'ai comparé. Le budget a été fixé à au moins 1000 appels de la fonction cible (```-C 1000```), et si un algorithme n'atteint pas cette valeur lors d'une exécution, il est relancé jusqu'à ce que le nombre minimum d'appels soit atteint.


# Les script principaux

## Le script ```ert_ecdf.py```


> Ce script montre l'ert-ecdf des 10 meilleurs algorithmes, chaque graphe a un delta différent (700, 750, 800), les données pour le graphe sont obtenues à partir des fichiers générés par l'exécution de runs.py, il y a déjà des données que j'ai générées pour les comparaisons donc vous pouvez exécuter ce script directement.


## Le script ```snp.py```

> Ce script a été modifié principalement pour ne pas afficher les logs pendant l'exécution, exécuter les algorithmes au nombre minimum d'appels, appeler le wrapper de la fonction objective au lieu de la fonction objective directe, et ajouter les nouveaux solveurs: ```num_annealing```, ```bit_annealing```, ```num_genetic``` y ```bit_genetic```.


## Le script ```runs.py```

>  Par défaut, il exécute 50 fois chaque algorithme décrit dans ```experiment.py``` en appelant le ```snp.py``` et en passant les paramètres correspondant à chaque algorithme, avec un minimum d'appels à la fonction objective de 1000 et 200 itérations maximum, ceci est fait en parallèle.

# Meilleurs algorithmes

1. ```num_genetic_0```:
    ```bash
    python3 snp.py
    ```
2. ```num_genetic_3```:
    ```bash
    python3 snp.py -p 15
    ```
3. ```num_genetic_6```:
    ```bash
    python3 snp.py -p 20
    ```