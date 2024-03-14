# ML_ops

<!-- Add mes librairies -->
pip freeze > requirements.txt
<!-- Importer mes librairies dans votre code -->
pip install -r requirements.txt


<!-- Creation du projet -->
creation des dossiers src et data
dans src creation des fichier load_data.py, train.py et features.py

<!--  src/Load data -->
Nous permet d'importer nos données et nous les transformer en fichier de données csv
Maintenant lancer 
> python .\src\load_data.py

<!--  src/features.py-->
Faire un travail sur nos features. 
Run notre feature > python .\src\features.py


<!-- Installer black pour reformatter nos codes -->
pip install black 
<!-- Reformatter tous nos code dans src -->
black -l 100 ./src*.py
<!-- Analyse notre code avec pylint -->
pip install pylint
analyser le code avec > pylint .\src*.py