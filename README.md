# Telefonbog
Et program, som gemmer kontakter som navne og numre i en json fil 'contacts.json'

## Funktioner
Dokumentation af funktionerne,herunder beskrivelse og funktion, ses nedenfor.

### add_contacts()
tager et input som er mellemrumssepareret ved navn og nummer. 
        
Nummeret må gerne have mellemrum, men ikke landkoder.
Mellemrummet af tallene fjernes og gemmes i en JSON fil.

### find_contact()
Finder telefonnummeret af en person. Første navn kræves kun.

Dette betyder at flere brugere kan ikke have samme navn, så
eventuelt brug denne funktion til at finde brugernavne kun. 

### get_contacts()
Henter kontaktoplysningerne fra 'contacts.json'

### show_contacts()
Printer kontakterne ud gennem get_contacts() i formatet [rækkefølge]. [bruger]: [nummer].

eksempel: ```42. Jørgen: 12345678```

### exit()
Afslutter programmet ved at lukke while-lykken.

