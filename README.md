# python_crypto

liste des commande avec explication

/connect <ip> <port>                                            connection a un client en renseignant son ip, la commande est obligatoire. seul encrypt                                                                     peut être lancé sans la connexion
/msg <message>                                                  envoyer un message, lmes messages sont en clairs tant qu'aucun cryptage n'a été demandé
/exit                                                           quitter le programme
/encrypt <crypto_name> <param>                                  crypter ses message en précisant le type d'encodage, HUFF ou RSA, non case sensitive
    if MAN == param:                                            les param en soit sont soit la clées de cryptage RSA, soit man ou auto pour HUFF,
                                                                en mode manuel il sera demandé de rentrer 26 nombre différents qui compose la clée
        26x check pondérations caractères
/send key                                                       envoyer la clée a l'autre personne dans la messagerie
    si aucun crypto choose alors choose one                     si pas de crypto, va chier
    si aucune key de décrypte affiche message en claire         