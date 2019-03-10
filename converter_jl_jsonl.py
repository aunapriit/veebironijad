# convert json lines fail
# adds items 'kysimus' & 'vastus', separates dates
import jsonlines


number = 0

# open output file in append mode
with jsonlines.open('kliinik_ee.jsonl', mode='a') as writer:
    
    # open json ilnes file for reading
    with jsonlines.open('kliinik_ee.jl') as reader:

        #iterate over lines of data in json lines file
        for item in reader:
            
            # do some magic with items
            kuupaev = item['teema'].split()[0] # select date from the beginning of the string
            teema = item['teema'].split()[2] # select the theme word from the string
            pealkiri = item['pealkiri']
            kysimus = item['kysimus']
            vastus = item['vastus']
            kysimus_ja_vastus = kysimus + '\n\n' + vastus
            vastaja_nimi = item['vastaja_nimi']
            vastaja_tiitel = item['vastaja_tiitel']
            vastaja_asutus = item['vastaja_asutus']
            url = str(item['url'])

            # compose dict line
            dict = {'kuupaev': kuupaev, 'teema': teema, 'pealkiri': pealkiri, 'kysimus_ja_vastus': kysimus_ja_vastus, 'vastaja_nimi': vastaja_nimi, 'vastaja_asutus':vastaja_asutus, 'vastaja_tiitel': vastaja_tiitel, 'url': url}

            # write converted data to new json line
            writer.write(dict)

            number = number + 1
            # break for testing
            # if number == 30: 
            #     break
        
    reader.close()
writer.close()
