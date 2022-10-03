import numpy
import pandas
import string


def genere_donnes_test(taille_population=30, taille_classes=(3, 4, 3), seed=1010):
    """
    Génère des données qui seront utilisées pour tester l'outil de création de groupes hétérogènes

    Args:
        taille_population (int): Taille de la population
        taille_classes (tuple or list): Vecteur dont la taille est le nombre de classes et les éléments sont le nombre de modalités
        de chaque classe

    Returns:
        pandas.DataFrame contenant la population de test
        tuple contenant les noms des variables de catégorie
    """

    hasard = numpy.random.default_rng(seed)
    identifiants = [int(round(k*1e7, 7)) for k in hasard.random(taille_population)]
    population = pandas.DataFrame(data = identifiants, columns=['id'])
    for i_classe, taille_classe in enumerate(taille_classes):
        modalites_classe = list(string.ascii_letters[0:taille_classe])
        population['classe_' + str(i_classe)] = hasard.choice(modalites_classe, size = taille_population)

    return population, ['classe_' + str(i_classe) for i_classe in range(len(taille_classes))]


if __name__ == '__main__':
    population_test, noms_variables = genere_donnes_test()
    print(noms_variables)
