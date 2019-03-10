# converts csv data to json lines fail
import jsonlines
import csv

number = 0
# declare column headers
veerupealkirjad = ['kuupaev', 'teema', 'pealkiri', 'kysimus_ja_vastus', 'vastaja_nimi', 'vastaja_asutus', 'vastaja_tiitel', 'url']

# open csv file
with open('kliinik_ee.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')

    # write column headers
    writer.writerow(veerupealkirjad)

    # open json ilnes file for reading
    with jsonlines.open('kliinik_ee.jl') as reader:

        #iterate over lines of data in json lines file
        for item in reader:
            
            kuupaev = item['teema'].split()[0] # valib kuupäeva stringi algusest
            teema = item['teema'].split()[2] # võtab stringist teema sõna
            pealkiri = item['pealkiri']
            kysimus = item['kysimus']
            vastus = item['vastus']
            kysimus_ja_vastus = kysimus + '\n\n' + vastus
            vastaja_nimi = item['vastaja_nimi']
            vastaja_tiitel = item['vastaja_tiitel']
            vastaja_asutus = item['vastaja_asutus']
            url = str(item['url'])

            # write converted data to a new line
            writer.writerow((kuupaev, teema, pealkiri, kysimus_ja_vastus, vastaja_nimi, vastaja_asutus, vastaja_tiitel, url))

            number = number + 1
            # break for testing
            # if number == 30: 
            #     break
        
    reader.close()
