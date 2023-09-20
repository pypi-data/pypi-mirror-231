import os
def recursive_sql(sql_file, basepath=None):
    """
    Cette fonction lit les scripts SQL récursivement s'ils contiennent la commande ".read".

    Si `basepath` n'est pas spécifié, le répertoire du fichier SQL est utilisé comme chemin de base.

    :param sql_file: Le chemin du fichier SQL à exécuter.
    :type sql_file: str
    :param basepath: Le chemin de base à utiliser comme référence, par défaut None.
    :type basepath: str, optional
    :return: Liste des scripts SQL exécutés.
    :rtype: list[str]
    :raises ValueError: Si le fichier SQL spécifié n'existe pas.

    """
    if basepath is None:
        basepath = os.path.dirname(sql_file) if os.path.dirname(sql_file) else "."
        sql_file = os.path.basename(sql_file)
    #
    ancien_repertoire = os.getcwd()
    os.chdir(basepath)

    # Exécution du script SQL
    sql_file=os.path.join(".", sql_file)
    if not os.path.exists(sql_file):
        raise ValueError(sql_file)
    #
    with open(sql_file, 'r') as fichier_sql:
        sql_script = fichier_sql.read()
        #cursor.executescript(script_sql)
    #
    # Exécution des commandes SQL du fichier

    to_add = []

    for lines in sql_script.split("\n"):
        if lines[0:5] == ".read":
            to_add.append(lines.split(".read")[1].strip())
        #
    #
    os.chdir(ancien_repertoire)
    return [recursive_sql(e, basepath) for e in to_add] if to_add else sql_script
#
