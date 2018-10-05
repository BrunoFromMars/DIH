#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 15:27:16 2018

@author: jayesh
"""

class mdict(dict):

    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)
    
dtm = mdict()    



    
class dictionary(dict):    
    
    #1
    #dtm['Allergies'] = 'AVIL 2ML AMP     1s'
    dtm['Allergies'] = 'CERN 5 TAB     10s'
    #dtm['Allergies'] = 'COBAVAS TAB     10s'
    dtm['Allergies'] = 'KIOCORT 6 TAB     10s'
    #dtm['Allergies'] = 'LCZ TAB     10s'
    dtm['Allergies'] = 'LECIDE 500MG TAB     10s'
    dtm['Allergies'] = 'MONTAIR LC TAB     10s'
    #dtm['Allergies'] = 'RUPEX 250 TAB     10s'
    #dtm['Allergies'] = 'SNEEZ LM TAB     10s'
    dtm['Allergies'] = 'SNEHCEF FORTE 1.5GM INJ     1s'
    #2
    dtm['Amoebiasis'] = 'METRO 100 ML (SWAROOP) INJ     1s'
    dtm['Amoebiasis'] = 'METRO 100ML (KUNAL)     print(listOfItems) 1s'
    #3
    dtm['Anaemia'] = 'AUTRIN CAP     30s'
    dtm['Anaemia'] = 'EIDO FE TAB     10s'
    dtm['Anaemia'] = 'ELDERVIT 12 INJ     1s'
    dtm['Anaemia'] = 'FOLEY 16 NO (RAMSONS) CATHETER     1s'
    dtm['Anaemia'] = 'HADID CT TAB     15s'
    dtm['Anaemia'] = 'OROFER XT TAB     10s'
    #4
    dtm['Anaesthesia - Local'] = 'LOX 2% ADRENALINE 30ML      1s'
    dtm['Anaesthesia - Local'] = 'LOX 2% JELLY 30GM      1s'
    #5
    dtm['Anaesthesia General'] = 'MEZOLAM 10ML INJ     1S'
    #6
    dtm['Angina'] = 'ANGIFIX 2.6MG TAB     10s'
    dtm['Angina'] = 'EMBETA XR 25 TAB     30s'
    dtm['Angina'] = 'IKORAN 5MG TAB     10s'
    dtm['Angina'] = 'KIPNOL 20 TAB     10s'
    dtm['Angina'] = 'MONIT GTN 2.6 (1X30) TAB     1s'
    dtm['Angina'] = 'MONIT GTN 6.4 (1X30) TAB     1s'
    dtm['Angina'] = 'NICODUCE 5 (1X20) TAB     1s'
    dtm['Angina'] = 'NORAD 2ML AMP     1s'
    dtm['Angina'] = 'NORAD 4ML AMP     1s'
    dtm['Angina'] = 'RANOZEX TAB     10s'
    #7
    dtm['Anxiety'] = 'BALAZAM 0.5MG TAB     10s'
    dtm['Anxiety'] = 'CELRO PLUS TAB     10s '
    dtm['Anxiety'] = 'HYDROZ TAB     10s'
    dtm['Anxiety'] = 'NEOTRALINE 50 TAB     10s'
    dtm['Anxiety'] = 'NOXEP TAB     10s'
    #8
    dtm['Arrhythmiasis'] = 'LANOXIN TAB     10s'
    #9
    dtm['Arthritis'] = 'LEFNO 20MG TAB     10s'
    dtm['Arthritis'] = 'ORCERIN GM CAP     10s'
    #10
    dtm['Asthma/copd'] = 'ASTHALIN RESPULE      1s'
    dtm['Asthma/copd'] = 'BUDATE TRANSPULS      1s'
    dtm['Asthma/copd'] = 'BUDECORT 0.5MG RESPULE     1s'
    dtm['Asthma/copd'] = 'DERIPHYLLIN INJ     1s'
    dtm['Asthma/copd'] = 'DERIPHYLLIN RETARD 150MG TAB     30s'
    dtm['Asthma/copd'] = 'DERIPHYLLIN TAB     10s'
    dtm['Asthma/copd'] = 'DUOLIN RESPULES 2.5ML      1s'
    #11
    dtm['Auto Immune Disease'] = 'PSYORID 1 TAB     10s'
    #12
    dtm['Bladder and Prostate Disorder'] = 'ADULT DIAPERS L (ROMSONS)      10s'
    #13
    dtm['Bleeding Disorder'] = 'KENADION 10MG INJ     1s'
    dtm['Bleeding Disorder'] = 'TRENAXA 500 TAB     6s'
    dtm['Bleeding Disorder'] = 'TRENAXA 5ML INJ     1s'
    #14
    dtm['Blood Clot'] = 'GLUCI 10ML AMP     1s'
    #15
    dtm['Blood Pressure'] = 'BETALAX TAB     10s'
    dtm['Blood Pressure'] = 'FORTINERV TAB     10s'
    #16
    dtm['Cancer'] = 'AIMGLUTA FORT 15 GM SACHET     1s'
    #17
    #dtm['Constipation'] = 'DUPHALAC 150ML SYP     1s'
    #dtm['Constipation'] = 'DUPHALAC 250ML SYP     1s'
    #dtm['Constipation'] = 'ENEMA (PROCTO CLYSIS)      1s'
    dtm['Constipation'] = 'GERBISA  SUPPOSITORIES (A)      1S'
    dtm['Constipation'] = 'GLEROL OS 500GM      1s'
    dtm['Constipation'] = 'LACTIHEP 200ML SYP     1s'
    #dtm['Constipation'] = 'SODIUM BICARBONATE INJ 25 ML    1s'
    #18
    dtm['Cough and Cold'] = 'ALLERCET DC TAB     10s'
    dtm['Cough and Cold'] = 'ANTIC 25 TAB     15s'
    dtm['Cough and Cold'] = 'GRILINCTUS 100ML SYP     1s'
    #dtm['Cough and Cold'] = 'TRUCARB XL TAB     10s'
    #19
    dtm['Diabetes'] = 'HUMINSULIN R (40IU 10ML) INJ     1s'
    dtm['Diabetes'] = 'MEMIN TAB     10s'
    #20
    dtm['Diarrhoea'] = 'IMODIUM CAP     4s'
    dtm['Diarrhoea'] = 'STEPPE 100MG CAP     4s'
    #21
    dtm['Digestion'] = 'APTIVATE 175ML SYP     1s'
    dtm['Digestion'] = 'RISIKA 1 TAB     10s  '
    dtm['Digestion'] = 'SODA BI CARB (RATHI) AMP     1s'
    #22
    dtm['Depression'] = 'AMIXIDE H TAB     10s'
    dtm['Depression'] = 'CEBERO FORTE TAB     10s'
    dtm['Depression'] = 'CEBERO GB TAB     10s'
    dtm['Depression'] = 'ELIWEL 10 TAB     10s'
    dtm['Depression'] = 'KIDEP 25 TAB     10s'
    dtm['Depression'] = 'TRIXIDE H TAB     10s'
    dtm['Depression'] = 'TRYPTOMER 10MG TAB     30s'
    #23
    dtm['Ear Conditions'] = 'OTOFLOX 10ML EYE EAR DROP     1s'
    #24
    dtm['Epilepsy/convulsion'] = 'CARBATOL 100MG TAB     10s'
    dtm['Epilepsy/convulsion'] = 'CARBATOL 200MG TAB     10s'
    dtm['Epilepsy/convulsion'] = 'DIVALGRESS ER 250 TAB     10s'
    dtm['Epilepsy/convulsion'] = 'EPICETAM 5ML INJ     1s'
    dtm['Epilepsy/convulsion'] = 'EPIGOLD XR 150 TAB     10s'
    dtm['Epilepsy/convulsion'] = 'EPIGOLD XR 300 TAB     10s'
    dtm['Epilepsy/convulsion'] = 'EPIGOLD XR 450 TAB     10s'
    dtm['Epilepsy/convulsion'] = 'EPSOLIN 2ML AMP     1s'
    dtm['Epilepsy/convulsion'] = 'EPTOIN 100MG (1 X 120) TAB     1s'
    dtm['Epilepsy/convulsion'] = 'LEVERA 500 TAB     15s'
    dtm['Epilepsy/convulsion'] = 'LEVERA 5ML INJ     1s'
    dtm['Epilepsy/convulsion'] = 'LEVIGRESS 500MG TAB     10s'
    dtm['Epilepsy/convulsion'] = 'LEVIGRESS 5ML INJ     1s'
    dtm['Epilepsy/convulsion'] = 'LEVIPIL 500 TAB     10s'
    dtm['Epilepsy/convulsion'] = 'OXETOL 300 TAB     10s'
    dtm['Epilepsy/convulsion'] = 'VALPARIN CHRONO 300 TAB     10s'
    dtm['Epilepsy/convulsion'] = 'VALPROL 100MG 5ML INJ     1s'
    #25
    dtm['Fever'] = 'ANEMOL 100ML I.V.     1s'
    #dtm['Fever'] = 'AQWAROL T TAB     10s'
    #dtm['Fever'] = 'CROPEN CAP     10s'
    #dtm['Fever'] = 'FEVRIDOL I.V INJ 100ML    1s'
    dtm['Fever'] = 'FEVASTIN 2ML INJ     1s'
    #dtm['Fever'] = 'P 650 TAB     10s'
    #dtm['Fever'] = 'PACINOVA 100 MG 100ML INFUSION     1s'
    #dtm['Fever'] = 'PACINOVA 1000MG 100ML INFUSION     1s'
    dtm['Fever'] = 'PARANIR 100ML INFUSION      1s'
    dtm['Fever'] = 'PM O LINE 150 (ROMSONS)      1s'
    #dtm['Fever'] = 'SLIDE P TAB     10s'
    #dtm['Fever'] = 'URTI 5MG TAB     10s'
    #26
    dtm['Fungal'] = 'FORCAN 150MG (1 X 1) TAB     1s'
    dtm['Fungal'] = 'SERTAVAN 20GM CREAM     1s'
    dtm['Fungal'] = 'VAXICAL K2 TAB     10s'
    #27
    dtm['Gastro Intestinal Motility Disorders'] = 'PERINORM TAB     10s'
    #28
    dtm['Gastroesophageal Reflux Disease'] = 'ALKALI P TAB     10s'
    #29
    #dtm['Glaucoma'] = 'DIAMOX 250MG TAB     15s'
    dtm['Glaucoma'] = 'LASILACTONE 50 TAB     10s'
    dtm['Glaucoma'] = 'ORYN 100ML MOUTHWASH     1s'
    #30
    dtm['Gout'] = 'INDOCAP SR CAP     10s'
    #31
    dtm['Heart Failure'] = 'DOMIN AMP     1s'
    #32
    dtm['High Cholesterol'] = 'ARVAST A 75 TAB     10s'
    #33
    dtm['Hepatitis B Infection'] = 'HBSAG TEST KIT      1s'
    dtm['Hepatitis B Infection'] = 'HCV TEST KIT ( STANDARD Q)      1s'
    #34print(dtm[])
    dtm['Hormonal Therapy'] = 'BENADON 40MG TAB     10s'
    dtm['Hormonal Therapy'] = 'CORT S INJ     1s'
    dtm['Hormonal Therapy'] = 'DEFCORT 6MG TAB     10s'
    dtm['Hormonal Therapy'] = 'DEXADRAN 2ML INJ     1s'
    dtm['Hormonal Therapy'] = 'OMNACORTIL 10 TAB     10s'
    dtm['Hormonal Therapy'] = 'OMNACORTIL 20 TAB     10s'
    dtm['Hormonal Therapy'] = 'OMNACORTIL 5 TAB     10s'
    dtm['Hormonal Therapy'] = 'PH EQUAL TAB     10s'
    #35
    dtm ['Hypertension'] = 'AMLOVAS 5 TAB     15s'
    dtm ['Hypertension'] = 'BETACAP TR 20MG CAP     10s'
    dtm ['Hypertension'] = 'BETACAP TR 40MG CAP     10s'
    dtm ['Hypertension'] = 'CARDIVAS 3.125MG TAB     10s'
    dtm ['Hypertension'] = 'CARNI Q XP SACHET     1s'
    dtm ['Hypertension'] = 'CIPLAR LA 20 TAB     15s'
    dtm ['Hypertension'] = 'CIPLAR LA 40 TAB     15s'
    dtm ['Hypertension'] = 'DILZEM CD 90 CAP     10s'
    dtm ['Hypertension'] = 'DYTOR 10MG TAB     15s'
    dtm ['Hypertension'] = 'DYTOR 20MG TAB     15s'
    dtm ['Hypertension'] = 'DYTOR 40MG TAB     10s'
    dtm ['Hypertension'] = 'DYTOR PLUS 10 TAB     15s'
    dtm ['Hypertension'] = 'DYTOR PLUS 20 TAB     15s'
    dtm ['Hypertension'] = 'LIFEPILL 4 KIT      1s'
    dtm ['Hypertension'] = 'LOBET 4ML INJ     1s'
    dtm ['Hypertension'] = 'METCY 25 MG TAB     10s'
    dtm ['Hypertension'] = 'NICARDIA RETARD 20 TAB     15s'
    dtm ['Hypertension'] = 'RL 500ML (PENTAGON) GLASS      1s'
    #36
    dtm['Hypnosis'] = 'KABIZOLAM 1MG ML INJ     1s'
    #37
    dtm['Impotence/ Erectile Dysfunction'] = 'PHYTON 4.5GM INJ     1s'
    #38
    dtm['Kidney Diseases/ Stones'] = 'AFEROL SACHET     1s'
    dtm['Kidney Diseases/ Stones'] = 'LEOTOL TAB     10s   '
    dtm['Kidney Diseases/ Stones'] = 'NEUROTOL 100ML INJ     1s'
    dtm['Kidney Diseases/ Stones'] = 'SEVELAM 400MG      10s'
    #39
    #dtm['Malarial'] = 'HCQS 200MG TAB     15s'
    dtm['Malarial'] = 'LARINATE 120MG INJ     1s'
    #40
    dtm['Migraine'] = 'INDERAL 10 MG TAB     15s'
    #41
    dtm['Muscles Cramp/Spasticity'] = 'BACLOF 10 TAB     10s'
    dtm['Muscles Cramp/Spasticity'] = 'NUCOXIA MR TAB     10s'
    #42
    dtm['Muscle Spasm'] = 'DROTIN 2ML INJ     1s'
    dtm['Muscle Spasm'] = 'LIBRAX 5MG TAB     20s'
    dtm['Muscle Spasm'] = 'MEFTAL SPAS TAB     10s'
    dtm['Muscle Spasm'] = 'SPASMO PROXYVON 2ML AMP     1s'
    #43
    dtm['Neuropathic Pain'] = 'AUCTA GB TAB     10s'
    dtm['Neuropathic Pain'] = 'BALACOBAL GB TAB     10s'
    dtm['Neuropathic Pain'] = 'FINES TAB     10s   '
    dtm['Neuropathic Pain'] = 'NEUROGAB P CAP     10s'
    dtm['Neuropathic Pain'] = 'TARIDOL 2ML INJ     1s '
    #44
    dtm['Nootropics & Neurotrophics'] = 'NEUROBION FORTE TAB     10s'
    #45
    dtm['Oral Care'] = 'EXICHLOR 100ML MOUTHWASH     1s'
    dtm['Oral Care'] = 'HEXIMINT A MOUTH WASH      1s'
    dtm['Oral Care'] = 'JHEX 100ML MOUTHWASH     1s'
    #46
    dtm['Osteoarthritis'] = 'TENDOACE TAB     15s'
    #47
    dtm['Osteoporosis'] = 'BLASTOCAL TAB     15s'
    dtm['Osteoporosis'] = 'CALMODULIN TAB     10s'
    dtm['Osteoporosis'] = 'DEPURA KID 15ML DROP     1s'
    dtm['Osteoporosis'] = 'SERCHCAL CT CAP     10s'
    dtm['Osteoporosis'] = 'SHELCAL 500 TAB     15s'
    dtm['Osteoporosis'] = 'SHELCAL CT TAB     15s'
    dtm['Osteoporosis'] = 'SHELCAL HD TAB     15s'
    #48
    dtm['Osteomalacia']  = 'CALCIGEN CAP     10s'
    #49
    dtm['Eye Condition'] = 'ACIVIR 250 10ML INJ     1s'
    dtm['Eye Condition'] = 'AURAPHEN 2ML 50MG ML INJ     1s'
    #50
    dtm['Pain'] = 'ANEMOL 100ML I.V.     1s'
    dtm['Pain'] = 'AQUADOL 1ML INJ     1s'
    dtm['Pain'] = 'BALAFEN 10MG TAB     10s'
    dtm['Pain'] = 'BUTRUM 2MG 1ML INJ     1s'
    dtm['Pain'] = 'CHYMORAL FORTE TAB     20s'
    dtm['Pain'] = 'CHYMOTHAL FORTE TAB     20s'
    dtm['Pain'] = 'DONA PLUS TAB     10s'
    dtm['Pain'] = 'DYNAPAR AQ 1ML INJ     1s'
    dtm['Pain'] = 'DYNAPAR TAB     10s'
    dtm['Pain'] = 'ENZOMEND TAB     10s'
    dtm['Pain'] = 'FACE P TAB     10s  '
    dtm['Pain'] = 'FEVRIDOL I.V INJ 100ML    1s'
    dtm['Pain'] = 'INCIN SR TAB     10s'
    dtm['Pain'] = 'KETANOV 1ML INJ     1s'
    dtm['Pain'] = 'KORFENAC S 1 GM INJ     1s'
    dtm['Pain'] = 'LORSAID P 4MG TAB     10s'
    dtm['Pain'] = 'LYSOFLAM AQ INJ     1s'
    dtm['Pain'] = 'LYSOFLAM TAB     10s'
    dtm['Pain'] = 'NAXDOM 500MG TAB     10s'
    dtm['Pain'] = 'NEXDOL 100 INJ     1s'
    dtm['Pain'] = 'NUCOXIA 90 TAB     10s'
    dtm['Pain'] = 'PACINOVA 100 MG 100ML INFUSION     1s'
    dtm['Pain'] = 'PACINOVA 1000MG 100ML INFUSION     1s'
    dtm['Pain'] = 'THIOCOX MR TAB     10s'
    dtm['Pain'] = 'ULTRACET TAB     15s'
    dtm['Pain'] = 'ZERODOL MR TAB     10s'
    dtm['Pain'] = 'ZERODOL P TAB     10s'
    dtm['Pain'] = 'ZERODOL SP TAB     10s'
    dtm['Pain'] = 'ZYMOFLAM D TAB     10s'
    #51
    dtm['Parasitic Worms'] = 'BANDY PLUS (1 X 1) TAB     1s'
    dtm['Parasitic Worms'] = 'ZENTEL 400MG TAB     1s'
    #52
    dtm['Parkinson'] = 'HEKSI 2 TAB     10s'
    dtm['Parkinson'] = 'SYNDOPA PLUS TAB     10s'
    #53
    dtm['Poisoning/Overdose'] = 'PHOSCUT 400 TAB     10s'
    #54
    dtm['Pyrexia'] = 'CALPOL 500MG TAB     15s'
    dtm['Pyrexia'] = 'CALPOL 650MG TAB     15s'
    dtm['Pyrexia'] = 'CALPOL T TAB     15s'
    #55
    dtm['Seizures'] = 'BALARKA 10 TAB     10s'
    dtm['Seizures'] = 'BALARKA 5 TAB     10s'
    dtm['Seizures'] = 'BALATAM 250 TAB     10s'
    dtm['Seizures'] = 'BALATAM 500 TAB     10s'
    dtm['Seizures'] = 'BALATOIN 100 TAB     10s'
    dtm['Seizures'] = 'BALATOIN 50 TAB     10s'
    dtm['Seizures'] = 'KIRABE DSR CAP     10s'
    dtm['Seizures'] = 'KLOPAM LITE TAB     10s'
    dtm['Seizures'] = 'KLOPAM PLUS TAB     10s'
    dtm['Seizures'] = 'NOVALEPT CHRONO 200 TAB     10s'
    dtm['Seizures'] = 'NOVALEPT CHRONO 300 TAB     10s'
    #56
    dtm['Skin Infections'] = 'OMCEF S 1.5 GM INJ     1s'
    #57
    dtm['Stroke'] = 'BALCOTIN 5 TAB     10s'
    dtm['Stroke'] = 'OSTEODEX FORTE TAB     10s'
    #58
    dtm['Supplement'] = 'CALVITAL TAB     10s'
    #59
    dtm['Thrombotic Disorder'] = 'CAPRIN 5000IU      1s'
    dtm['Thrombotic Disorder'] = 'CLOBEST 250 MG TAB     10s'
    dtm['Thrombotic Disorder'] = 'ECOSPRIN AV 75 CAP     15s'
    dtm['Thrombotic Disorder'] = 'ECOSPRIN AV 75/20 TAB     10s'
    dtm['Thrombotic Disorder'] = 'LMWX 60MG INJ     1s'
    #60
    dtm['Tuberculosis'] = 'AKT 3 KIT TAB     1s'
    dtm['Tuberculosis'] = 'AKT 4 KIT (1 X 4) TAB     1s'
    dtm['Tuberculosis'] = 'AKURIT 3 TAB     10s'
    dtm['Tuberculosis'] = 'AKURIT 4 TAB     10s'
    dtm['Tuberculosis'] = 'AMBISTRYN S 0.75GM VAIL     1s'
    dtm['Tuberculosis'] = 'COMBUTOL 800MG TAB     10s'
    dtm['Tuberculosis'] = 'FORECOX KIT CAP     1s'
    dtm['Tuberculosis'] = 'FORECOX TAB     6s'
    dtm['Tuberculosis'] = 'PYZINA 750 TAB     10s'
    dtm['Tuberculosis'] = 'R CIN 600MG CAP     3s'
    dtm['Tuberculosis'] = 'R CINEX 600 TAB     3s'
    dtm['Tuberculosis'] = 'R CINEX CAP     10s'
    #61
    dtm['Ulcer'] = 'ACILOC 150MG TAB     30s'
    dtm['Ulcer'] = 'ACILOC 2ML INJ     1s'
    dtm['Ulcer'] = 'COSE DSR TAB     10s'
    dtm['Ulcer'] = 'DEREK L  TAB    10s'
    dtm['Ulcer'] = 'GAM DSR CAP     10s'
    dtm['Ulcer'] = 'NEXZOLE 150 (1 X 1) TAB     1s'
    dtm['Ulcer'] = 'OMETRON 10MG TAB     10s'
    dtm['Ulcer'] = 'OMIFLUX CAP     10s'
    dtm['Ulcer'] = 'PAN 40MG TAB     15s'
    dtm['Ulcer'] = 'PAN D CAP     15s'
    dtm['Ulcere'] = 'PANSA I.V 40MG INJ     1s'
    dtm['Ulcer'] = 'PANSEC 40MG TAB     15s'
    dtm['Ulcer'] = 'PANSEC DSR CAP     15s'
    dtm['Ulcer'] = 'PANSEC IV INJ     1s'
    dtm['Ulcer'] = 'PANTALOX DSR CAP     10s'
    dtm['Ulcer'] = 'PANTIAC 40 MG INJ     1s'
    dtm['Ulcer'] = 'PANTOCID DSR CAP     15s'
    dtm['Ulcer'] = 'PANTODAC INJ     1s'
    dtm['Ulcere'] = 'RANOZEX TAB     10s'
    dtm['Ulcer'] = 'SHEATH P CAP     10s'
    dtm['Ulcer'] = 'SOMPRAZ D 40 CAP     10s'
    dtm['Ulcere'] = 'TRIORAB DSR CAP     10s'
    #62
    dtm['Ulcerative Colitis/bowel Inflammatory Disease'] = 'CYRA D CAP     10s'
    dtm['Ulcerative Colitis/bowel Inflammatory Disease'] = 'CYRA TAB     10s'
    dtm['Ulcerative Colitis/bowel Inflammatory Disease'] = 'ROWASA 1GM SACHET     1s'
    dtm['Ulcerative Colitis/bowel Inflammatory Disease'] = 'SAAZ 500 TAB     10s'
    dtm['Ulcerative Colitis/bowel Inflammatory Disease'] = 'SAAZ DS TAB     10s'
    #63
    dtm['Urinary Retention'] = 'LASIX 4ML AMP     1s'
    dtm['Urinary Retention'] = 'MANNITOL 20% 100ML (KUNAL)      1s'
    dtm['Urinary Retention'] = 'ORGIROSE CAP     10s'
    dtm['Urinary Retention'] = 'SOBISIS 500MG TAB     10s'
    #64
    dtm['Vaginal Conditions'] = 'BETT 0.5ML (VACCINE) INJ     1s'
    dtm['Vaginal Conditions'] = 'CALINTOS TAB     15s'
    dtm['Vaginal Conditions'] = 'SYNTOCINON AMP     1s'
    #65
    dtm['Vertigo'] = 'KVERT 25 TAB     10s'
    dtm['Vertigo'] = 'VERTIN 16MG TAB     15s'
    #66
    dtm['Viral'] = 'ACIVIR 250 10ML INJ     1s'
    #67
    dtm['Vomitting/emesis'] = 'EMESET 2ML INJ     1s'
    dtm['Vomitting/emesis'] = 'EMESET 4 TAB     10s'
    dtm['Vomitting/emesis'] = 'EMESET 4ML INJ     1s'
    dtm['Vomitting/emesis'] = 'EMESET 8 TAB     10s'
    dtm['Vomitting/emesis'] = 'ONDEM MD 4MG TAB     10s'
    dtm['Vomitting/emesis'] = 'ONDINORM  2 ML INJ     1s'
    #68
    dtm['Wound'] = 'HANSAPLAST (WASHPROOF)      1s'
    dtm['Wound'] = 'WOKADINE 10% 100ML SOL     1s'
    
    
    #print(dtm)
    

if __name__ == '__main__':
    
    dictionary.show(dtm)


def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
     
    for item in range(len(dictOfElements)):
        for item2 in range( len(dictOfElements[item][1])):
            if dictOfElements[item][1][item2] == valueToFind:
                listOfKeys.append(dictOfElements[item][0])
    return listOfKeys



dtm_list = list(dtm.items())
for i in range(len(dtm_list)):
    dtm_list[i] = list(dtm_list[i])
sbcd = getKeysByValue(dtm_list,'VERTIN 16MG TAB     15s')
            