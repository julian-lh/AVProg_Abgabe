# AVProg_Abgabe
 
## 0_Training Vorbereitung
Enthält die Originalen Bilddateien für Hintergründe und Gesten,
sowie Auszüge archivierte Positiv- und Negativbilder der Trainings.
Um die Dateimengen klein zu halten, sind hier nur Bilder jeweils eines
Trainings-Duschlaufs je Geste.

## 1_HaarCascadeTraining
In diesem Verzeichnis wurden unter Linux mittels OpenCV die Trainings durchgeführt.
Die vorhandenen Dateien sind vom letzten Training (Geste "G").
Enthalten sind:
	neg4-6: 		Negativbilder (falsche Gesten + Hintergründe)
	neg: 			alle Negativbilder gesammelt
	g1-6.jpg: 		echte Positivbilder (geschossen)
	bg4-6 & bgAll.txt: 	Dateipfade für "createsamples" und "traincascade"
	nohup.out:		Terminal-Output während des Trainings
	data:			Output-Verzeichnis: "cascade.xml" ist die finale Kaskade

## 2_Hilfsskripte
Alle verwendeten Hilfsskripte gesammelt.
Sie wurden zur Vorbereitung der "createsamples", "traincascade" und der finalen GUI-Anwendung benötigt.

## 3_Anwendung
Finale Anwendung zum Einsetzen der trainierten Kaskaden.
"detection.py" ist das Herzstück der Gestenerkennung.
"main_script.py" enthält die Programmschleife und muss zum 
Start der Anwendung ausgeführt werden.
