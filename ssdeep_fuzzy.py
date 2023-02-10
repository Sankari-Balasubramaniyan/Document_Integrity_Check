#!/usr/bin/env python3.8

import ssdeep

#Original genuine document
reference_str = ['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: t|groupautomot|vesystems bdde|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: adresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014€102526€ 01268€000€ 102526€', 'cot|sat|ons', 'partsa|ar|a|e', 'partpatrona|e', 'tauxmontant', 'tauxmontant', 'csgnondeduct|b|e crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement a|dep|afone a|p|afonne assed|c asschemagetranchea asschemagetrancheb', '99450€ 99450€ 99450€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 000€', '240% 050% 510% 075% 010% 655% 240% 240% 2387€ 497€ 5072€ 769€ 103€ 6715€ 2461€ 000€', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123€ 1640€ 8407€ 7484€ 5536€ 410€ 103€ 4101€ 000€', 'tota|descot|sat|ons', '18003€', '40805€', 'payeparv|rementbanca|re |e:22/02/11', 'netapayer84522€', 'net|mposab|e86909€']

#Genuine 2PS600
str_1 = ['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: t|groupautomot|vesystems bdde|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: adresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014€102526€ 01268€000€ 102526€', 'cot|sat|ons', 'partsa|ar|a|e', 'partpatrona|e', 'tauxmontant', 'tauxmontant', 'csgnondeduct|b|e crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement a|dep|afone a|p|afonne assed|c asschemagetranchea asschemagetrancheb', '99450€ 99450€ 99450€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 000€', '240% 050% 510% 075% 010% 655% 240% 240% 2387€ 497€ 5072€ 769€ 103€ 6715€ 2461€ 000€', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123€ 1640€ 8407€ 7484€ 5536€ 410€ 103€ 4101€ 000€', 'tota|descot|sat|ons', '18003€', '40805€', 'payeparv|rementbanca|re |e:22/02/11', 'netapayer84522€', 'net|mposab|e86909€']

#Genuine PS300
str_2 = ['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: t|groupautomot|vesystems bdde|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: acresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014€102526€ 01268€000€ 102526€', 'cot|sat|ons', 'partsa|ar|a|e', 'partpatrona|e', 'tauxmontant', 'tauxmontant', 'csgnondeduct|b|e crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement a|dep|afone a|p|afonne : assed|c asschemagetranchea asschemagetrancheb', '99450€ 99450€ 99450€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 000€', '240% 050% 510% 075% 010% 655% 240% 240% 2387€ 497€ 5072€ 769€ 103€ 6715€ 2461€ 000€', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123€ 1640€ 8407€ 7484€ 5536€ 410€ 103€ 4101€ 000€', 'tota|descot|sat|ons', '18003€', '40805€', 'payeparv|rementbanca|re |e:22/02/11', 'netapayer84522€', 'net|mposab|e86909€']

#Genuine PS600
str_3 = ['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: t|groupautomot|vesystems bdde|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: adresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014€102526€ 01268€000€ 102526€', 'cot|sat|ons', '', 'partpatrona|e', 'tauxmontant', 'tauxmontant', 'csgnondeduct|b|e crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement a|dep|afone a|p|afonne assed|c asschemagetranchea asschemagetrancheb', '99450€ 99450€ 99450€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 000€', '240% 050% 510% 075% 010% 655% 240% 240% 2387€ 497€ 5072€ 769€ 103€ 6715€ 2461€ 000€', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123€ 1640€ 8407€ 7484€ 5536€ 410€ 103€ 4101€ 000€', 'tota|descot|sat|ons', '18003€', '40805€', 'payeparv|rementbanca|re |e:22/02/11', 'netapayer84522€', 'net|mposab|e86909€']

#Falsification 2PS600 - 1
str_4 = ['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: t|groupautomot|vesystems bdde|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: adresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014€102526€ 01268€000€ 102526€', 'cot|sat|ons', 'partsa|ar|a|e', 'partpatrona|e', 'tauxmontant', 'tauxmontant', 'csgnondeduct|b|e crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement a|dep|afone a|p|afonne assed|c asschemagetranchea asschoemagetrancheb', '99450€ 99450€ 99450€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 000€', '240% 050% 510% 075% 010% 655% 240% 240% 2387€ 497€ 5072€ 769€ 103€ 6715€ 2461€ 000€', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123€ 1640€ 8407€ 7484€ 5536€ 410€ 103€ 4101€ 000€', 'tota|descot|sat|ons', '18003€', '40805€', 'payeparv|rementbanca|re te:22/02/11', 'netapayer184522€', 'net|mposab|e86909€']

#Falsification 2PS600 - 2
str_5 = ['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: t|groupautomot|vesystems rtede|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: adresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014€102526€ 01268€000€ 102526€', 'cot|sat|ons|', 'partsa|ar|a|e', 'partpatrona|e', 'tauxmontant', 'tauxmontant', 'crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement asssoc|a|etranchea asssoc|a|etrancheb csgnondeduct|b|e', '102526€ 102526€ 102526€ 000€', '240% 050% 510% 075% 010% 655% 240%2461€ 240%000€', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123€ 1640€ 8407€ 7484€ 5536€ 410€ 103€ 4101€ 000€', 'tota|descot|sat|ons', '18003€', '40805€', 'payeparacc|dentsbanca|re |e:22/02/11', 'netapayer84522€', 'net|mposab|e86909€']

#Falsification PS300 - 1
str_6 = ['emp|oyeur', "nom: adresse: cpetv|||e: numeroape: numeros|ret: bdde|'|ndustr|e 37530naze||esnegron 24202 54210000300053", 'sa|ar|e', 'nometprenom: adresse: cpetv|||e: numeross: datentre: emp|o|: masson|sabe||e 96a||edescypres 37110monthodon 269038631660073 30/09/06 techn|c|ens', 'sa|a|redebase hsa25% sa|a|rebrut', '101111014€102526€ 01268€000€ 102526€', 'cot|sat|ons', 'partsa|ar|a|e', 'partpatrona|e', 'tauxmontant', '', 'csgnondeduct|b|e crdsnondeduct|b|e csgdeduct|b|e secur|tesoc|a|e assurancema|ad|e assuranceveuvage assurancev|e|||esse avdep|afone avp|afonne acc|dentsdutrava|| a||ocat|onfam|||a|es a|deau|ogement a|dep|afone a|p|afonne assed|c asschemagetranchea asschemagetrancheb', '99450€ 99450€ 99450€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 102526€ 000€', '240% 050% 510% 075% 010% 655% 240% 240% 2387€ 497€ 5072€ 769€ 103€ 6715€ 2461€ 000€', '1280% 160% 820% 730% 540% 040% 010% 400% 400% 13123€ 1640€ 8407€ 7484€ 5536€ 410€ 103€ 4101€ 000€', 'tota|descot|sat|ons', '18003€', '40805€', 'payeparv|rementbanca|re |e:22/02/11', 'netapayer184522€', 'net|mposab|e86909€']



ref_hashes = []
for strs in reference_str:
    h = ssdeep.hash(strs)
    ref_hashes.append(h)
    

hash1 = []
for strs in str_1:
    h = ssdeep.hash(strs)
    hash1.append(h)

hash2 = []
for strs in str_2:
    h = ssdeep.hash(strs)
    hash2.append(h)

hash3 = []
for strs in str_3:
    h = ssdeep.hash(strs)
    hash3.append(h)

hash4 = []
for strs in str_4:
    h = ssdeep.hash(strs)
    hash4.append(h)


hash5 = []
for strs in str_5:
    h = ssdeep.hash(strs)
    hash5.append(h)

hash6 = []
for strs in str_6:
    h = ssdeep.hash(strs)
    hash6.append(h)

output_1 = []
output_2 = []
output_3 = []
output_4 = []
output_5 = []
output_6 = []

for i in range(len(ref_hashes)):
    output_1.append(ssdeep.compare(ref_hashes[i], hash1[i]))
    output_2.append(ssdeep.compare(ref_hashes[i], hash2[i]))
    output_3.append(ssdeep.compare(ref_hashes[i], hash3[i]))
    output_4.append(ssdeep.compare(ref_hashes[i], hash4[i]))
    output_5.append(ssdeep.compare(ref_hashes[i], hash5[i]))
    output_6.append(ssdeep.compare(ref_hashes[i], hash6[i]))

for i in range(21):
    print("Output ",i)
    print()
    print(reference_str[i])
    print()
    print(str_1[i])
    print(str_2[i])
    print(str_3[i])
    print(str_4[i])
    print(str_5[i])
    print(str_6[i])
    print(output_1[i], output_2[i], output_3[i], output_4[i], output_5[i], output_6[i])
    print("----------------------------------------------------------")
    print('\n')

    
