from datetime import datetime
import uuid
import os
import logging

logging.info('Projet gestion de comptes bancaires')

def DernierCompte():
    fichier = open(r"//home//user//PycharmProjects//gestionCompteBancaire//compte.txt", "r")
    if os.stat(r'//home//user//PycharmProjects//gestionCompteBancaire//compte.txt').st_size == 0:
        print('fichier vide')
    else:
        dernierL = fichier.readlines()[-1]
        ligne = dernierL.split(';')
        fichier.close()
        return ligne[0]

#DernierCompte()

def creationCompte():
    type = {"O": "compte courant", "N": "autre compte"}
    fichier = open(r"//home//user//PycharmProjects//gestionCompteBancaire//proprietaire.txt", "a")
    fichier2 = open(r"//home//user//PycharmProjects//gestionCompteBancaire//compte.txt", "a")
    idProprietaire = str(uuid.uuid4())
    nom = input("Saisir le Nom : ")
    CIN = input("Saisir le Numéro CIN : ")
    telephone = input("Saisir le numéro de téléphone : ")
    adresse = input("Saisir l'adresse : ")
    idCompte = int(DernierCompte()) + 1
    solde = float(input("Saisir le solde du compte : "))
    date = str(datetime.now().strftime("%d-%m-%Y"))
    t = input("Ce compte est-il un compte courant, (O / N) ?")
    ligne = idProprietaire + ';' + nom + ';' + CIN + ';' + telephone + ';' + adresse + '\n'
    ligne2 = str(idCompte) + ';' + idProprietaire + ';' + str(solde) + ';' + date + ';' + type[t] + '\n'
    fichier.write(ligne)
    fichier2.write(ligne2)
    fichier.close()
    fichier2.close()

creationCompte()

def AfficherTousProprietaires():
    fichier = open(r"//home//user//PycharmProjects//gestionCompteBancaire//proprietaire.txt", "r")
    for ligne in fichier:
        L = ligne.split(';')
        print(L[1], "est propriétaire d'un compte")
    fichier.close()

#AfficherTousProprietaires()

def RechercherCompte(idCompte):
    fichier = open(r"//home//user//PycharmProjects//gestionCompteBancaire//compte.txt", "r")
    for ligne in fichier:
        F = ligne.split(';')
        dico = {'idC': F[0], 'idProp': F[1], 'solde': F[2], 'date': F[3], 'type': F[4]}
        if idCompte == F[0]:
            print(dico)

#RechercherCompte('3440923')

def RetirerCompte(idCompte):
    fichier = open(r"//home//user//PycharmProjects//gestionCompteBancaire//compte.txt", "r")
    comptes = []
    for ligne in fichier:
        F = ligne.split(';')
        if F[0] != idCompte:
            comptes.append(ligne)
    fichier.close()
    fichier = open(r"//home//user//PycharmProjects//gestionCompteBancaire//compte.txt", "w")
    fichier.writelines(comptes)
    print("Compte supprimé avec succès !")
    fichier.close()

#RetirerCompte('3')

def verserment():
    fichierrrrrrrr = open(r"//home//user//PycharmProjects//gestionCompteBancaire//compte.txt", "a")
    idProprietaire = input("Saisir l'id propriétaire : ")
    VER = input("Saisir le montant du versement : ")
    for ligne in fichier:
        L = ligne.split(";")
        if L[1].strip() == idProprietaire:
            L[2] = int(VER) + int(L[2])
            fichier.write(L[2])
    fichier.close()

#verserment()