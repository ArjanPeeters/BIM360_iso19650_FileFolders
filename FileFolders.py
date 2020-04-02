import os

# algemene instellingen en opbouw van het project
base_path = 'C:\Python\BIM360folders'
locations = ['LDN', 'WPK', 'LVN']
companies = ['Royal HaskoningDHV', 'Waternet', 'Arcadis', 'K_Dekker']
structure = ['Work-in-progress', 'Shared', 'Published']
stages = ['S1 Geschikt voor coordinatie', 'S2 Geschikt ter informatie', 'S3 Geschikt voor beoordeling en commentariering',
          'S4 Geschikt voor fase goedkeuring', 'S6 Geschikt voor PIM goedkeuring',
          'S7 Geschikt voor AIM goedkeuring']
sites = {
    'LDN': ['000-00 Algemeen', '000-00 Terrein', '592-02Onthardingsgebouw', '301-13 Naspoeltoren',
            '390-xx Langzame zandfilters 1', '360-01 Snelfilters 1', '420-01 Pompdieselgebouw'],
    'LVN': ['000-00 Algemeen', '000-00 Terrein', '330-08 Pompgebouw Noord', '330-09 Pompgebouw Zuid']
}
Published = ['P00 Fase Volume ontwerp', 'P01 Fase Schets ontwerp', 'P02 Fase Voorlopig Ontwerp', 'P03 Fase Definitief Ontwerp',
              'P04 Fase Technische Ontwerp', 'P05 Fase Uitvoeringsgereed Ontwerp', 'P06 Fase Opleveringsgereed ontwerp',
              'P07 Fase Beheer en onderhoud']
algemeen = ['P10 BIM protocol', 'P20 ILS', 'P30 ILS bijlagen', 'P40 BIM uitvoeringsplan', 'P50 BIM ondersteuning']
folder_selector = {'Shared': stages, 'Work-in-progress': companies, 'Published': Published + algemeen}

# Turn to False if you want real output
test = True

def maakdir(*folders):
    current_folder = folders[0]
    for folder in range(1, len(folders)):
        current_folder = "{0}\{1}".format(current_folder, folders[folder])
    print('making', current_folder)
    if not test:
        os.mkdir(current_folder)


for site in sites:
    maakdir(base_path, site)

    for s in structure:
        maakdir(base_path, site, s)

        for building in sites[site]:
            maakdir(base_path, site,  s, building)

            for f in folder_selector[s]:
                maakdir(base_path, site, s, building, f)

if test:
    print('DIT WAS EEN TEST, DUS FOLDERS ZIJN NIET GEMAAKT')
else:
    print('Folders aangemaakt')