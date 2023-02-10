#!/usr/bin/env python3.8

from fuzzy_extractor import FuzzyExtractor

extractor = FuzzyExtractor(16, 8)

str1 =['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: t|groupautomot|vesystems bdde|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: adresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014102526 01268000 102526', 'cot|sat|ons', 'partsa|ar|a|e', 'partpatrona|e', 'tauxmontant', 'tauxmontant', 'csgnondeduct|b|e crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement a|dep|afone a|p|afonne assed|c asschemagetranchea asschemagetrancheb', '99450 99450 99450 102526 102526 102526 102526 102526 102526 102526 102526 102526 000', '240% 050% 510% 075% 010% 655% 240% 240% 2387 497 5072 769 103 6715 2461 000', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123 1640 8407 7484 5536 410 103 4101 000', 'tota|descot|sat|ons', '18003', '40805', 'payeparv|rementbanca|re |e:22/02/11', 'netapayer84522', 'net|mposab|e86909']

str2 = ['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: t|groupautomot|vesystems rtede|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: adresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014102526 01268000 102526', 'cot|sat|ons', 'partsa|ar|a|e', 'partpatrona|e', 'tauxmontant', 'tauxmontant', 'csgnondeduct|b|e crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement a|dep|afone a|p|afonne assed|c asssoc|a|etranchea asssoc|a|etrancheb', '99450 99450 99450 102526 102526 102526 102526 102526 102526 102526 102526 102526 000', '240% 050% 510% 075% 010% 655% 240% 240% 2461 000', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123 1640 8407 7484 5536 410 103 4101 000', 'tota|descot|sat|ons', '18003', '40805', 'payeparacc|dentsbanca|re |e:22/02/11', 'netapayer84522', 'net|mposab|e86909f']

key = []
helper = []
n_key = []

for i in range(21):
    if(len(str1[i]) == len(str2[i])):
        pass
    else:
        if(len(str1[i]) > len(str2[i])):
            str2[i] = str2[i]+(' '*abs(len(str1[i]) - len(str2[i])))
            
        else:
            str1[i] = str1[i]+(' '*abs(len(str2[i]) - len(str1[i])))
    extractor = FuzzyExtractor(len(str1[i]), 8)
    k,h = extractor.generate(str1[i])
    key.append(k)
    helper.append(h)
    new_key = extractor.reproduce(str2[i], h)
    n_key.append(new_key)
    
for i in range(21):
    print(str1[i])
    print(str2[i])
    print(key[i])
    print(n_key[i])
    print(key[i] == n_key[i])
    print("***********")
