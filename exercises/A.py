# -*- coding: utf-8 -*-
import json
question_1={'explanation':u'''
A. Flexie participia

Regel: Zodra het hulpwerkwoord ‘zijn’ (être) is, past het voltooid deelwoord zich aan, aan het onderwerp. 
Vb. Elle est partie  (zij is vertrokken)
Zodra het hulpwerkwoord ‘hebben’ (avoir) is, past het voltooid deelwoord zich aan, aan het lijdend voorwerp, indien deze vóór het gezegde staat.
Vb. La voiture que j’ai vue  (‘de auto die ik gezien heb’)

Uitgangen: mann. Enk. –
                  Mann. Mv. +s
	      Vrouw. Enk. +e
	      Vrouw. Mv. +es
''',
			'1':
			{'question':'La fille est tombé____ dans l’escalier',
			'possible_answers':(u'tombé', u'tombée', u'tombés', u'tombées'),
			'correct_answer': u'tombée'},
			'2':
			{'question':'Les tables sont installé____ par le congierge',
			 'possible_answers': (u'installé', u'installée', u'installés', u'installées'),
			 'correct_answer': u'installées'},
			 '3':
			 {'question':'Les émissions télévisées qu’on a regardé____ hier soir, étaient formidables',
			 'possible_answers': (u'regardé', u'regardée', u'regardés', u'regardées'),
			 'correct_answer': u'regardées'},
			 '4':{
			 'question':'La femme a remis___ sa valise au grenier',
			 'possible_answers': (u'remis', u'remise', u'remis(mv)', u'remises'),
			 'correct_answer': u'remis'},
			'5':
			{'question': 'Les garçons que tu as réprimandé__, étaient émus',
			'possible_answers': (u'réprimandé', u'réprimandée', u'réprimandés', u'réprimandées'),
			'correct_answer': u'réprimandés'},
			'6':
			{'question': 'Le père est mort___ il y a quelques années',
			'possible_answers': (u'mort', u'morte', u'morts', u'mortes'),
			'correct_answer': u'mort'},
			'7':
			{'question': 'Les stylos ont été retrouvé___ dans le tiroir',
			'possible_answers': (u'retrouvé', u'retrouvée', u'retrouvés', u'retrouvées'),
			'correct_answer': u'retrouvés'},
			'8':
			{'question': 'La recherche a mené___ à de nouvelles questions',
			'possible_answers': (u'mené', u'menée', u'menés', u'menées'),
			'correct_answer': u'mené'}
			}

question_2 = {'explanation':u'''
B. Subjonctif

Regel: Indien er sprake is van uitdrukking van: gevoel, noodzaak, mogelijkheid of twijfel gebruik je de subjonctif in plaats van de ‘normale’ werkwoordsvorm achter het woord ‘que’.
Hoe maak je de vorm bij onregelmatige werkwoorden: 
	-	Subjonctif-stam (uit je hoofd leren)
	-	Uitgang erachter (-e, -es, -e, -ions, -iez, -ent)
Vb. Je veux que tu partes  (‘ik wil dat je weggaat’) (uitdrukking wens)
''',
			'1':
			{'question':'Elle voudrait que je ____ quoi faire    (savoir)',
			'possible_answers':(u'sais', u'sait', u'savons', u'savez', u'savent', u'sache', u'saches', u'sachions', u'sachiez', u'sachent'),
			'correct_answer': u'sache'},
			'2':
			{'question':'Je doute que nous _____ travailler ce projet  (devoir)',
			 'possible_answers': (u'dois', u'doit', u'devons', u'devez', u'doivent', u'doive', u'doives', u'devions', u'deviez'),
			 'correct_answer': u'devions'},
			 '3':
			 {'question':'Il est possible que vous ____ raison   (avoir)',
			 'possible_answers': (u'ai', u'as', u'a', u'avons', u'avez', u'ont', u'aie', u'aies', u'aie', u'ayons', u'ayez', u'aient'),
			 'correct_answer': u'ayez'},
			 '4':{
			 'question':'Il faut que ce système ____ intégré   (être)',
			 'possible_answers': (u'sois', u'soit', u'soyons', u'soyez', u'soient', u'suis', u'es', u'est', u'sommes', u'êtes', u'sont'),
			 'correct_answer': u'soit'},
			'5':
			{'question': 'Nous voulons qu’elle _________ directrice de cet établissement   (devenir)',
			'possible_answers': (u'deviens', u'devient', u'devenons', u'devenez', u'deviennent', u'devienne', u'deviennes', u'devenions', u'deveniez'),
			'correct_answer': u'devienne'},
			'6':
			{'question': 'Est-il certain que tout le monde ________ postuler?   (pouvoir)',
			'possible_answers': (u'peux', u'peut', u'pouvons', u'pouvez', u'peuvent', u'puisse', u'puisses', u'puissions', u'puissiez', u'puissent'),
			'correct_answer': u'puisse'},
			'7':
			{'question': 'Il se peut qu’elle ______ des risques     (prendre)',
			'possible_answers': (u'prends', u'prend', u'prenons', u'prenez', u'prennent', u'prenne', u'prennes', u'prenions', u'preniez'),
			'correct_answer': u'prenne'},
			'8':
			{'question': 'Il faudra que les employés se _____________ rencontrés      (être)',
			'possible_answers': (u'suis', u'es', u'est', u'sommes', u'êtes', u'sont', u'sois', u'soit', u'soyons', u'soyez', u'soient'),
			'correct_answer': u'soient'}
			}

question_3 = {'explanation':u'''
C. Betrekkelijk voornaamwoord (met voorzetsel)

Regel: Betrekkelijke voornaamwoorden met voorzetsel (bv. Waarvan, aan wie, waarover etc.) vorm je in het Frans als volgt: 
Voorwerpen:
voorzetsel + lequel (mann.enk) / lesquels (mann.mv.) / laquelle (vr.enk.) + lesquelles (vr. mv.)
personen: voorzetsel + qui

vb1. Le stylo avec lequel j’écris   (‘De pen waarmee ik schrijf’)
vb2. L’homme avec qui je parle    (‘De man met wie ik praat’)
''',
			'1':
			{'question':'La cathédrale devant ________ on s’est réuni',
			'possible_answers':(u'lequel', u'laquelle', u'lesquels', u'lesquelles', u'qui'),
			'correct_answer': u'laquelle'},
			'2':
			{'question':'L’ordinateur sur _______ je travaille, est rapide',
			 'possible_answers': (u'lequel', u'laquelle', u'lesquels', u'lesquelles', u'qui'),
			 'correct_answer': u'lequel'},
			 '3':
			 {'question':'Ce sont les copains avec ______ je suis parti pour Paris',
			 'possible_answers': (u'lequel', u'laquelle', u'lesquels', u'lesquelles', u'qui'),
			 'correct_answer': u'qui'},
			 '4':{
			 'question':'Le portable sur ______ je regarde l’heure',
			 'possible_answers': (u'lequel', u'laquelle', u'lesquels', u'lesquelles', u'qui'),
			 'correct_answer': u'lequel'},
			'5':
			{'question': 'Le collègue à _______ j’ai donné le livre',
			'possible_answers': (u'lequel', u'laquelle', u'lesquels', u'lesquelles', u'qui'),
			'correct_answer': u'qui'},
			'6':
			{'question': 'Toutes les personnes de ______ j’ai parlé, étaient célèbres',
			'possible_answers': (u'lequel', u'laquelle', u'lesquels', u'lesquelles', u'qui'),
			'correct_answer': u'qui'},
			'7':
			{'question': 'Les livres sur _______ elle a basé sa recherche',
			'possible_answers': (u'lequel', u'laquelle', u'lesquels', u'lesquelles', u'qui'),
			'correct_answer': u'lesquels'},
			'8':
			{'question': 'Les cuillères avec _______ nous remuons la sauce',
			'possible_answers': (u'lequel', u'laquelle', u'lesquels', u'lesquelles', u'qui'),
			'correct_answer': u'lesquelles'}
			}


if __name__=='__main__':
	d = dict()
	d['EX_1'] = question_1
	d['EX_2'] = question_2
	d['EX_3'] = question_3
	json.dump(d, open('../v2/questions_dict.json', 'w+'))






