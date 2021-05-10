#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Author : Jean-Damien Généro
Date : 28 janvier 2021
"""

import csv
import os
import subprocess


def open_file(file):
    """
    Function that opens a csv file and read it with csv module.
    :param file: path to a csv file
    :type file: str
    :return: a csv reader object named file_open_csv
    :rtype: _csv.reader
    """
    with open(file, 'r', encoding='utf8') as new_file:
        opened_csvfile = csv.reader(new_file)
    return opened_csvfile


class File:
    def __init__(self, file) -> None:
        self.file = file
        self.opening_csv_file = open_file(self.file)

    def iterate_over_rows(self, item):
        with open(self.file, 'r', encoding='utf8') as csv_file:
            file_open_csv = csv.reader(csv_file)
            row = [rows[item] for rows in file_open_csv]
        return row


class Document(File):
    def __init__(self, file: str) -> None:
        File.__init__(self, file)
        self.file_object = File(file)
        self.id = self.file_object.iterate_over_rows(0)
        self.name1 = self.file_object.iterate_over_rows(2)
        self.name2 = self.file_object.iterate_over_rows(3)
        self.firstname = self.file_object.iterate_over_rows(4)
        self.signatures = self.file_object.iterate_over_rows(6)
        self.coauthorCRH = self.file_object.iterate_over_rows(7)
        self.coauthorEXT = self.file_object.iterate_over_rows(8)
        self.type = self.file_object.iterate_over_rows(9)
        self.title = self.file_object.iterate_over_rows(10)
        self.journal = self.file_object.iterate_over_rows(11)
        self.editor = self.file_object.iterate_over_rows(12)
        self.booktitle = self.file_object.iterate_over_rows(13)
        self.preface = self.file_object.iterate_over_rows(14)
        self.dedicataire = self.file_object.iterate_over_rows(15)
        self.dict_title = self.file_object.iterate_over_rows(16)
        self.date = self.file_object.iterate_over_rows(17)
        self.location = self.file_object.iterate_over_rows(18)
        self.publisher = self.file_object.iterate_over_rows(19)
        self.series = self.file_object.iterate_over_rows(20)
        self.organization = self.file_object.iterate_over_rows(22)
        self.language = self.file_object.iterate_over_rows(23)
        self.page = self.file_object.iterate_over_rows(24)


subprocess.call(["mkdir", "./annual-bibliography"])
subprocess.call(["mkdir", "./retro-biblio"])
reference = Document('./csv/publications_retrospectives.csv')
article_ls = []
book_ls = []
inproceedings_ls = []
dict_entry_ls = []
proceedings_ls = []
exposition_ls = []
melanges_ls = []
art_in_collectif_ls = []
intro_ls = []
intro_preface_ls = []
intro_book_ls = []
intro_journal_ls = []
preface_ls = []
preface_journal_ls = []
preface_book_ls = []
edition_ls = []
report_ls = []
trad_ls = []
new_edition_ls = []
outil_ls = []
thesis_ls = []
art_rapport_ls = []
compte_rendu_ls = []
conference_ls = []

sorted_all_date = sorted(set([Date for Date in reference.date]))
# print(sorted_all_date)


for ID, Name1, Name2, Firstname, Signatures, CoCRH, CoEXT, Type, Title, Journal, Editor, Booktitle, Preface, Dedicataire, Dict_title, Date, Location, Publisher, Series, Organization, Language, Pages \
        in zip(reference.id, reference.name1, reference.name2, reference.firstname, reference.signatures, reference.coauthorCRH, reference.coauthorEXT, reference.type, reference.title, reference.journal, reference.editor, reference.booktitle, reference.preface, reference.dedicataire, reference.dict_title, reference.date, reference.location, reference.publisher, reference.series, reference.organization, reference.language, reference.page):
    if Name2 != "":
        Name = Name1.title() + '-' + Name2.title() + ', ' + Firstname
    else:
        Name = Name1.title() + ', ' + Firstname
    Name1 = Name1.title().replace(" ", "") # pour les clefs des entrées
    CoCRH = CoCRH.replace(" et ", " and ")
    CoCRH = CoCRH.replace(" & ", " and ")
    CoCRH = CoCRH.replace(", ", " and ")
    CoEXT = CoEXT.replace(" et ", " and ")
    CoEXT = CoEXT.replace(" & ", " and ")
    CoEXT = CoEXT.replace(", ", " and ")
    Editor = Editor.title().replace(" Et ", " and ")
    Editor = Editor.replace(", ", " and ")
    Editor = Editor.replace(" & ", " and ")
    Journal = Journal.replace(" & ", " \\& ")
    Title = Title.replace(" & ", " \\& ")
    Publisher = Publisher.replace(" & ", " \\& ")
    if Signatures != "1":
        if CoCRH != "" and CoEXT != "":
            authors = Name + ' and ' + CoCRH + ' and ' + CoEXT
        elif CoCRH == "" and CoEXT != "":
            authors = Name + ' and ' + CoEXT
        elif CoEXT == "" and CoCRH != "":
            authors = Name + ' and ' + CoCRH
    else:
        authors = Name
    # ARTICLES DE REVUE
    if Type == "article dans une revue":
        article = f"""@article{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    journal = {{{Journal}}},
    year = {Date},
    language = {{{Language}}},
    keywords = {{art-crh, crh-{Date}}}
    }}"""
        article_ls.append(article)
    # MONOGRAPHIES
    elif Type == "livre":
        book = f"""@book{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{book-crh, crh-{Date}}}
    }}"""
        book_ls.append(book)
    # CHAPITRES D'ACTES DE COLLOQUE
    elif Type == "article dans des actes de colloque":
        inproceedings = f"""@inproceedings{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Booktitle}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{inproceedings-crh, crh-{Date}}}
    }}"""
        inproceedings_ls.append(inproceedings)
    # ENTRÉE DE DICT
    elif Type == "article de dictionnaire":
        dict_entry = f"""@inreference{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Dict_title}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{dict-crh, crh-{Date}}}
    }}"""
        dict_entry_ls.append(dict_entry)
    # DIRECTION D'OUVRAGE
    elif Type == "direction d'un livre collectif":
        proceedings = f"""@proceedings{{{Name1}{ID}-{Date},
    editor = {{{authors}}},
    editortype = {{dir.}},
    title = {{{Title}}},
    booktitle = {{{Title}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{proceedings-crh, crh-{Date}}}
    }}"""
        # print(proceedings)
        proceedings_ls.append(proceedings)
    # CATALOGUE D'EXPO
    elif Type == "catalogue d'exposition":
        exposition = f"""@collection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Booktitle}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{expo-crh, crh-{Date}}}
    }}"""
        exposition_ls.append(exposition)
    # CHAPITRES DE MELANGES
    elif Type == "contribution dans des Mélanges":
        melanges = f"""@incollection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Booktitle}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{melanges-crh, crh-{Date}}}
    }}"""
        # addendum = {{{Dedicataire}}},
        melanges_ls.append(melanges)
    # CHAPITRE D'OUVRAGE COLLECTIF
    elif Type == "contribution dans un livre collectif":
        art_in_collectif = f"""@incollection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Booktitle}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{collectif-crh, crh-{Date}}}
    }}"""
        art_in_collectif_ls.append(art_in_collectif)
    # INTRODUCTION, PRÉSENTATION, CONCLUSION
    elif Type == "introduction":  # introduction, présentation, conclusion
        # DANS UNE REVUE > ARTICLE
        if Journal != "" and Booktitle == "" and Preface == "":
            intro_journal = f"""@article{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    journal = {{{Journal}}},
    year = {Date},
    language = {{{Language}}},
    keywords = {{intro-journal-crh, crh-{Date}}}
    }}"""
            intro_journal_ls.append(intro_journal)
        # DANS UN LIVRE > CHAPITRE
        elif Journal == "" and Booktitle != "" and Preface == "":
            intro_book = f"""@incollection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Booktitle}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{intro-book-crh, crh-{Date}}}
    }}"""
            intro_book_ls.append(intro_book)
        # DANS UN LIVRE > CHAPITRE
        elif Journal == "" and Booktitle == "" and Preface != "":
            intro_preface = f"""@incollection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Preface}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{intro-preface-crh, crh-{Date}}}
    }}"""
            intro_preface_ls.append(intro_preface)
        # DANS UNE REVUE > ARTICLE
        else:
            # print("error for {}.\nJournal = +{}+\nBooktitle = +{}+\nPreface = +{}+\n\n".format(ID, Journal, Booktitle, Preface))
            intro_journal = f"""@article{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    journal = {{{Journal}}},
    issuetitle = {{{Preface}}},
    year = {Date},
    language = {{{Language}}},
    keywords = {{intro-journal-crh, crh-{Date}}}
    }}"""
            intro_journal_ls.append(intro_journal)
    # PRÉFACE, POSTFACE, ÉDITO
    elif Type == "préface":  # préface, postface, éditorial
        # DANS UNE REVUE > ARTICLE
        if Journal != "" and Preface == "" and Booktitle == "":
            preface_journal = f"""@article{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    journal = {{{Journal}}},
    issuetitle = {{{Preface}}},
    year = {Date},
    language = {{{Language}}},
    keywords = {{preface-journal-crh, crh-{Date}}}
    }}"""
            preface_journal_ls.append(preface_journal)
        # DANS UN OUVRAGE > CHAPITRE
        elif Journal == "" and Preface != "" and Booktitle == "":
            preface_book = f"""@incollection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Preface}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{preface-book-crh, crh-{Date}}}
    }}"""
            preface_book_ls.append(preface_book)
        # DANS UN OUVRAGE > CHAPITRE
        elif Journal == "" and Preface == "" and Booktitle != "":
            preface_book = f"""@incollection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Booktitle}}},
    publisher = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{preface-book-crh, crh-{Date}}}
    }}"""
            preface_book_ls.append(preface_book)
        else:
            print("Error for Preface in {}".format(ID))
    # ÉDITONS
    elif Type == "édition de texte":
        if Preface != "":
            edition = f"""@book{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Preface}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    % addendum = {{{Title}}},
    keywords = {{edition-txt-crh, crh-{Date}}}
    }}"""
            edition_ls.append(edition)
        else:
            edition = f"""@book{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{edition-txt-crh, crh-{Date}}}
    }}"""
            edition_ls.append(edition)
    # RAPPORTS
    elif Type == "rapport":
        report = f"""@report{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    publisher = {{{Publisher}}},
    institution = {{{Organization}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{report-crh, crh-{Date}}}
    }}"""
        report_ls.append(report)
    # TRADUCTIONS
    elif Type == "traduction":
        trad = f"""@book{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{traduction-crh, crh-{Date}}}
    }}"""
        trad_ls.append(trad)
    # REPRINTS > MONOGRPAHIES
    elif Type == "réédition d'un livre":
        new_ed = f"""@book{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    addendum = {{réédition}},
    keywords = {{reedition-crh, crh-{Date}}}
    }}"""
        new_edition_ls.append(new_ed)
    # OUTILS POUR LA RECHERCHES > AUTRES
    elif Type == "outil pour la recherche":
        # CHAPITRE
        if Booktitle != "" :
            outil = f"""@incollection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Booktitle}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{outil-recherche-crh, crh-{Date}}}
    }}"""
            outil_ls.append(outil)
        # MONOGRAPHIES
        else:
            outil = f"""@book{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{outil-recherche-crh, crh-{Date}}}
    }}"""
            outil_ls.append(outil)
    # THÈSES
    elif Type == "thèse":
        thesis = f"""@thesis{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    institution = {{{Publisher}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{theses-crh, crh-{Date}}}
    }}"""
        thesis_ls.append(thesis)
    # ARTICLES DANS UN RAPPORT > CHAPITRE ET ARTICLE
    elif Type == "article dans un rapport":
        if Booktitle != "" and Journal == "":
            art_rapport = f"""@incollection{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    editor = {{{Editor}}},
    title = {{{Title}}},
    booktitle = {{{Booktitle}}},
    publisher = {{{Publisher}}},
    series = {{{Series}}},
    location = {{{Location}}},
    year = {Date},
    pagetotal = {{{Pages}}},
    language = {{{Language}}},
    keywords = {{art-rapport-crh, crh-{Date}}}
    }}"""
            art_rapport_ls.append(art_rapport)
        elif Booktitle == "" and Journal != "":
            art_rapport = f"""@article{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    journal = {{{Journal}}},
    year = {Date},
    language = {{{Language}}},
    keywords = {{art-rapport-crh, crh-{Date}}}
    }}"""
            art_rapport_ls.append(art_rapport)
            # un rapport non pris en compte = l'id #1901
    # COMTPE RENDU
    elif Type == "compte-rendu":
        if Journal != "":
            compte_rendu = f"""@article{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    journal = {{{Journal}}},
    year = {Date},
    language = {{{Language}}},
    keywords = {{cr-crh, crh-{Date}}}
    }}"""
            compte_rendu_ls.append(compte_rendu)
        else :
            compte_rendu = f"""@misc{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    year = {Date},
    language = {{{Language}}},
    addendum = {{compte-rendu}},
    keywords = {{cr-crh, crh-{Date}}}
    }}"""
            compte_rendu_ls.append(compte_rendu)
    # CONFÉRENCE
    elif Type == "conférence":
        conference = f"""@misc{{{Name1}{ID}-{Date},
    author = {{{authors}}},
    title = {{{Title}}},
    year = {Date},
    language = {{{Language}}},
    keywords = {{conf-crh, crh-{Date}}}
    }}"""
        conference_ls.append(conference)
    else:
        print(ID, Title)

intro_ls = intro_preface_ls + intro_book_ls + intro_journal_ls
preface_ls = preface_journal_ls + preface_book_ls
biblio_retro_all = [article_ls, book_ls, inproceedings_ls, dict_entry_ls, proceedings_ls, exposition_ls, melanges_ls, art_in_collectif_ls, intro_ls, preface_ls, edition_ls, report_ls, trad_ls, new_edition_ls, outil_ls, thesis_ls, art_rapport_ls, compte_rendu_ls, conference_ls]
with open('./retro-biblio/biblio-retro-all.bib', 'w', encoding='utf-8') as bibfile:
    for ls_biblio in biblio_retro_all:
        for item in ls_biblio:
            bibfile.write('{}\n\n'.format(item))

biblio_names = ["articles_revues", "livres", "articles_actes_colloque", "notices_dictionnaires", "dir_ouvrages_collectifs", "catalogues_exposition", "melanges", "art_ouvrages_collectifs", "intro_presentation_conclusion", "prefaces_postfaces_edito", "editions_textes", "rapports", "traductions", "reeditions", "outils_recherche", "theses", "article_rapport", "compte_rendu", "conferences"]
dict_ls = {biblio_names[item]: biblio_retro_all[item] for item in range(len(biblio_names))}
for ls_biblio in dict_ls:
    with open(os.path.join("./retro-biblio/", str(ls_biblio) + ".bib"), 'w', encoding='utf-8') as biblio_file:
        for item in dict_ls[ls_biblio]:
            biblio_file.write('{}\n\n'.format(item))

for year in sorted_all_date:
    annual_list = []
    for doc_type in biblio_retro_all:
        for doc in doc_type:
            if "year = {}".format(year) in doc:
                annual_list.append(doc)
    current_file = os.path.join("./annual-bibliography/", year + "-bibliography" + ".bib")
    with open(current_file, 'w', encoding="utf-8") as file:
        for document in annual_list:
            file.write("{}\n\n".format(document))
    print("{} ---> Done !".format(os.path.join("./annual-bibliography", year + "-bibliography" + ".bib")))

subprocess.call(["rm", "./annual-bibliography/Date 17-bibliography.bib"])
print("./annual-bibliography/Date 17-bibliography.bib ---> Deleted")
