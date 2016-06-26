# SolutecHackathonTeam1
Repository pour l'équipe 1 du hackathon organisé par l'entreprise Solutec

## Hackathon Solutec : 

Répertoire de l’équipe 1 : Happy Hours

## L’équipe : 
L’équipe est composé de 6 jeunes étudiants de CPE Lyon, tous en première année du cycle ingénieur et participant à leur premier hackathon.
L’équipe est divisée en 3 : 2 personnes s’occupe du front, 2 du back et 2 flexible en fonction de l’avancement des parties.

**Membres :** Azzano Guilhem, Blanc Baptiste, El Ouard Ibrahim, Migaud Sylvain, Montvernay Nicolas et Piquet Anthony

## Projet : 
Marre de passer 30 minutes à chercher une place de parking en rentrant du boulot le soir ? Grace à notre application Smart City, trouvez facilement les places libres autour de vous !
L’objectif final du projet est de récupéré les flux vidéos des caméras installer en ville et de détecter les places utilisés ou non.

## Technologie utilisées : 
**-	Analyse d’image :**

L’analyse d’image est effectuée en C++ avec la bibliothèque OpenCV après un premier traitement d’image sur Python.
**-	BDD mySQL**

**-	Application :**

L’application est développée pour Android Natif.

## Avancement du projet : 
**Pour l’analyse d’image :**
Nous travaillons pour l’instant sur des photos  de rue.  On effectue un premier filtrage pour garder que les bandes de stationnement. On détecte ensuite le nombre de voiture présente sur les places de stationnement avec OpenCV.

**Pour la BDD :**
La base de données est fonctionnelle, nous sommes en train de l’implémenter dans l’application.

**Pour l’application :**
L’application commence à prendre forme, les coordonnées des caméras ainsi que le nombre de place libre sont géré mais elles ne sont pas encore connecter avec la BDD, la géolocalisation est elle aussi en cour. 
Le design de l’application est fini, il sera très prochainement intégré à l’application.
