rep="Repondez par 'oui' ou 'non' svp."
rep2="Repondez par '13h' ou '15h' svp."

lun="Lundi 17-18h ? "
mar="Mardi 17-18h ? "
mer="Mercredi 13h ou 15h ? "
jeu="Jeudi 17-18h ? "

q1 = raw_input ("Bonjour, avez vous 1h par semaine pour m'aider en reseau svp ? " + rep)

if (q1=='oui' or q1=='Oui') :
  print ("Merci, alors on va trouver le jour et l'heure en commun alors. Repondez par le jour.")  

  q2 = raw_input ("Quel jour sera possible pour nous deux ? Repondez en 3 caracteres 'lun', 'mar', 'mer' ou 'jeu' svp.")
  if (q2=='lun' or q2=='Lun') :
    q3 = raw_input (lun + rep)
    if (q3=='oui') :
      print ("merci et a ", lun)
    else :
      print ("dommage !")

  if (q2=='mar' or q2=='Mar') :
    q3 = raw_input (mar + rep)
    if (q3=='oui') :
      print ("merci et a ", mar)
    else :
      print ("dommage !")

  if (q2=='mer' or q2=='Mer') :
    q3 = raw_input (mer + rep)
    if (q3=='oui') :
      q4 = raw_input ("merci et mercredi a quelle heure svp ? " + rep2)
      if (q4=='13h') :
        print ("merci et a mercredi 13h.")
      if (q4=='15h') :
        print ("merci et a mercredi 15h.")
    else :
      print ("dommage !")

  if (q2=='jeu' or q2=='Jeu') :
    q3 = raw_input (jeu, rep)
    if (q3=='oui') :
      print ("merci et a ", jeu)
    else :
      print ("dommage !")
