#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

Male_first_names = ("Aaron", "Adam", "Adrian", "Adolf", "Albert", "Artur", "Alfred", "Aleksander", "Arkadiusz",
                    "Bartlomiej", "Bartosz", "Beniamin", "Blazej", "Bogdan", "Boguslaw", "Bryan",
                    "Cezary", "Czeslaw",
                    "Daniel", "Damian", "Dawid", "Darek", "Dominik",
                    "Edward", "Ernest", "Eryk", "Eustachy",
                    "Filip", "Florian", "Felix", "Franciszek",
                    "Gabriel", "Gracjan", "Grzegorz",
                    "Henryk", "Hubert",
                    "Ignacy", "Igor", "Ireneusz",
                    "Jacek", "Jakub", "Janusz", "Jaroslaw", "Jan", "Jedrzej", "Jozef", "Julian",
                    "Kacper", "Kajetan", "Klaudiusz", "Kamil", "Karol", "Kornel", "Konrad", "Krystian", "Krzysztof",
                    "Kazimierz",
                    "Leonard", "Ludwik",
                    "Lukasz",
                    "Maciej", "Maksymilian", "Marcel", "Marek", "Marian", "Mateusz", "Mariusz", "Mikolaj", "Miroslaw",
                    "Max", "Marcin",
                    "Nikodem", "Norbert",
                    "Oliwier", "Oskar",
                    "Patryk", "Pawel", "Piotr", "Przemyslaw",
                    "Radoslaw", "Rafal", "Ryszard", "Roman", "Robert", "Remigiusz",
                    "Samuel", "Sebastian", "Szymon", "Stanislaw",
                    "Tadeusz", "Tytus", "Tomasz",
                    "Waclaw", "Wiktor", "Witold", "Wladyslaw", "Wojciech",
                    "Zdzislaw", "Zbigniew", "Zygmunt"
                    )

Female_first_names = (
    "Ada", "Adrianna", "Agata", "Agnieszka", "Aleksandra", "Alicja", "Amanda", "Amelia", "Anastazja", "Aneta",
    "Angelika",
    "Aniela", "Anita", "Anna", "Asia",
    "Barbara", "Beata", "Bozena", "Boguslawa", "Bianka", "Bernadetta",
    "Celina",
    "Dagmara", "Daria", "Dominika", "Diana", "Dorota", "Danuta",
    "Edyta", "Elzbieta", "Emilia", "Ewelina", "Ewa", "Eliza",
    "Franciszka", "Faustyna",
    "Gabriela", "Genowefa", "Greta",
    "Halina", "Hanna", "Helena", "Honorata",
    "Ida", "Iga", "Ilona", "Irena", "Irmina", "Iwona", "Iza", "Izabela",
    "Jadwiga", "Jagoda", "Janina", "Jola", "Julia", "Justyna", "Jowita",
    "Kaja", "Kamila", "Karina", "Karolina", "Kinga", "Katarzyna", "Kornelia", "Klaudia",
    "Lara", "Laura", "Luiza",
    "Lucja",
    "Magda", "Magdalena", "Maja", "Marcelina", "Mariola", "Marysia", "Marlena", "Marta", "Marzena", "Matylda",
    "Michalina",
    "Milena", "Monika",
    "Nadia", "Natalia", "Natasza", "Nikola", "Nina",
    "Ola", "Oliwia", "Olga",
    "Patrycja", "Pamela", "Paulina",
    "Roksana", "Rozalia", "Renata",
    "Sandra", "Sara", "Sylwia", "Stefania", "Stanislawa",
    "Teresa",
    "Vanessa",
    "Wanda", "Weronika", "Wiktoria", "Wioletta", "Wladyslawa",
    "Zofia", "Zuzanna"
)

Male_last_names = ("Nowak", "Kowalski", "Wisniewski", "Wojcik", "Kowalczyk", "Kaminski", "Lewandowski", "Zielinski",
                   "Szymanski", "Wozniak", "Kozlowski", "Jankowski", "Mazur", "Wojciechowski",
                   "Kwiatkowski", "Krawczyk", "Kaczmarek", "Piotrowski", "Grabowski", "Zajac", "Pawlowski", "Michalski",
                   "Krol", "Nowakowski", "Wieczorek", "Wrobel", "Jablonski", "Dudek",
                   "Adamczyk", "Majewski", "Nowicki", "Olszewski", "Stepien", "Jaworski", "Malinowski", "Pawlak",
                   "Gorski", "Witkowski", "Walczak", "Sikora", "Butkowski", "Baran", "Michalak", "Szewczyk",
                   "Ostrowski",
                   "Tomaszewski", "Pietrzak", "Duda", "Zalewski", "Wroblewski"
                   )

Female_last_names = ("Nowak", "Kowalska", "Wisniewska", "Wojcik", "Kowalczyk", "Kaminska", "Lewandowska", "Zielinska",
                     "Szymanska", "Dabrowska", "Wozniak", "Kozlowska", "Jankowska", "Mazur", "Kwiatkowska",
                     "Wojciechowska",
                     "Krawczyk", "Kaczmarek", "Piotrowska", "Grabowska", "Pawlowska", "Michalska", "Zajac", "Krol",
                     "Wieczorek",
                     "Jablonska", "Wrobel", "Nowakowska", "Majewska", "Olszewska", "Adamczyk", "Jaworska", "Malinowska",
                     "Stepien", "Dudek", "Gorska", "Nowicka", "Pawlak", "Witkowska"
                     )


def generate_user_data(n: int) -> list:
    """
    This function generate n of tuples (username, password) and return it as a list of tuples
    :return
    list(tuple)
    """
    users_credentials = list()
    for _ in range(n):
        if randint(0, 1) % 2 == 0:
            user = (Male_first_names[randint(0, len(Male_first_names ) - 1)], Male_last_names[randint(0, len(Male_last_names)-1)])
        else:
            user = (Female_first_names[randint(0, len(Female_first_names ) - 1)], Female_last_names[randint(0, len(Female_last_names)-1)])
        rand_ending = randint(1, 99)
        email = user[0] + user[1] + str(rand_ending) + "@gmail.com"
        password = user[0] + str(rand_ending)
        # users_credentials.append(email)
        users_credentials.append((email, password))
    return users_credentials


if __name__ == "__main__":
    print(generate_user_data(100))