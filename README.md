# Проект по курсу "Грамматика Конструкций"
## ударила молния vs ударило молнией
*Захарова Елена, БКЛ-142*

### Материалы
[Ссылка на таблицу с данными](https://docs.google.com/spreadsheets/d/1Mfcpu0F07SCs0XTF0nQuijxkYaAqtx_8zJ0DiUGAbRo/edit)  
[Ссылка на код с комментариями](https://github.com/eszakharova/cxg_project/blob/master/lightning_decision_tree.ipynb)

## Рабочая гипотеза
Конструкция с "ударить" и "молния" встречается в русском языке в 5 вариантах.
+ *С другой стороны, буквально **молнией меня ударило** , когда я вдруг понял, что вот я откуда.* - молния INS, пациенс ACC
+ *Мне при его иссиня голубых взглядах как **ударило в сердце молнией**...* - молния INS, пациенс в+ACC
+  *«Не боишься, что **молния в дом ударит**?»* - молния NOM, пациенс в+ACC
+ *Накрываюсь накидкой (это гарантирует, что **молния меня не ударит**)...* - молния NOM, пациенс ACC
  - *Тоненькая **молния ударила эльфа в спину*** - с расщепленным пациенсом
+ *Огромная **молния** беспощадно **ударила по березе**, опалив сердцевину ее ствола.*  - молния NOM, пациенс по+DAT

Предположительно на выбор между употреблением слова "молния" в качестве субъекта и в качестве дополнения в интсрументалисе могут оказывать влияние следующие факторы:
+ оформление пациенса (при предложном оформлениии пациеса - чаще будет "молния ударила", при пациенсе в аккузативе без предлога - "молнией ударило")
  - одушевленность пациенса (кажется, неодушевленный пациенс может быть оформлен только с помощью предлога)
  - расщепленность пациенса ("молния ударила его прямо в грудь")
+ порядок слов в самой конструкции ("его ударило молнией" vs "молния ударила в дом")
+ прямое или переносное значения конструкции (кажется, что в переносном значении чаще будет "молнией" ("его словно молнией ударило")
+ форма глагола "ударить" (по моим ощущениям, конструкция с инструменталисом больше "любит" прошедшее время)


## Данные

### Материал исследования
Я сделала 4 запроса в корпус Araneum Russicum II Maximum (Russian, 17.03), НКРЯ основной подкопус и НКРЯ газетный подкорупс:			
+ "ударить" []{1,2} [word="молния"] 		лемма ударить на расстоянии от 1 до 2 до слова молния (именно в такой форме) 
+ [word="молния"] []{1,2} "ударить" 		то же самое в обратном порядке 
+ "ударить" []{1,2} [word="молнией"] 	  лемма ударить на расстоянии от 1 до 2 до слова молнией (именно в такой форме) 
+ [word="молнией"] []{1,2} "ударить" 		то же самое в обратном порядке 

Данные были очищены от мусора, от примеров, где arg1 отсутвует (типа *Грянул гром и ударила молния.*) , от примеров, где выражен агенс (типа X ударил Y-а/в Y-а молнией).
___________________________________________________________

Итоговый размер выборки - 225 примеров.
+ 201 - молния субъект
+ 24 - молния не субъект


### Факторы выбора конструкции
Завиисимая переменная (Subject) - является ли слово "молния" субъектом глагольной формы.
#### Признаки использованные при анализе:
+ **Order** - порядок слов в конструкции. Категориальный - 6 вариантов - X молния ударить / X ударить молния	/ молния X ударить / молния ударить X /	ударить X молния / ударить молния X 
+ **Arg1_anim**	- одушевленность пациенса. Бинарный.
+ **Verb_fin**	- стоит ли глалог в финитной форме. Бинарный.
+ **Obj**	- пациенс является прямым дополнение в аккузативе (его vs в него).  Бинарный. 
+ **Has_arg2** - расщепленность пациенса (молния ударила его в спину). Бинарный. 
+ **Direct_meaning** - прямое значение (Его ударила молния vs Меня как будто молнией ударило/его словно молнией ударило и т.д.). Бинарный	
+ **Fact** - состоялся ли удар молнии в реальности (Его ударила молния vs Вас может ударить молния/вдруг меня ударит молния и т.д.) Бинарный. 
+ **Tense** - время глагола "ударить". Категориальный - 3 значения:  пе=непрош - настоящее/будущее, пе=прош - прошедшее время, пе=инф - начальная форма (в конструкции типа "может ударить" и т.д.)

## Анализ: дескриптивная статистика
#### Коэффициенты корреляции признаков с целевой переменнй и друг с другом
Категориальные признак Order и Tense были преобразованы в бинарные (OneHotEncoding)

|  | Subject | X молния ударить | X ударить молния | молния X ударить | молния ударить X | ударить X молния | ударить молния X | Arg1_anim | Verb_fin | Obj | Has_arg2 | Direct_meaning | Fact | пе=инф | пе=непрош | пе=прош |
|------------------|---------|------------------|------------------|------------------|------------------|------------------|------------------|-----------|----------|--------|----------|----------------|--------|--------|-----------|---------|
| Subject | 1.0 | -0.256 | -0.02 | -0.264 | 0.3 | -0.038 | 0.033 | -0.324 | -0.057 | -0.519 | 0.052 | 0.449 | 0.295 | 0.099 | 0.083 | -0.134 |
| X молния ударить | -0.256 | 1.0 | -0.151 | -0.077 | -0.216 | -0.056 | -0.021 | 0.186 | 0.071 | 0.252 | -0.034 | -0.364 | -0.2 | -0.065 | -0.02 | 0.06 |
| X ударить молния | -0.02 | -0.151 | 1.0 | -0.224 | -0.633 | -0.165 | -0.063 | 0.283 | 0.208 | 0.037 | -0.1 | 0.072 | 0.033 | -0.117 | -0.068 | 0.133 |
| молния X ударить | -0.264 | -0.077 | -0.224 | 1.0 | -0.321 | -0.084 | -0.032 | 0.134 | 0.054 | 0.167 | -0.051 | -0.204 | -0.208 | -0.096 | 0.146 | -0.056 |
| молния ударить X | 0.3 | -0.216 | -0.633 | -0.321 | 1.0 | -0.236 | -0.09 | -0.329 | -0.14 | -0.178 | 0.158 | 0.204 | 0.125 | 0.233 | -0.023 | -0.136 |
| ударить X молния | -0.038 | -0.056 | -0.165 | -0.084 | -0.236 | 1.0 | -0.023 | -0.169 | -0.257 | -0.122 | -0.037 | 0.01 | 0.1 | -0.071 | 0.026 | 0.026 |
| ударить молния X | 0.033 | -0.021 | -0.063 | -0.032 | -0.09 | -0.023 | 1.0 | -0.079 | 0.03 | -0.047 | -0.014 | 0.03 | 0.055 | -0.027 | -0.035 | 0.047 |
| Arg1_anim | -0.324 | 0.186 | 0.283 | 0.134 | -0.329 | -0.169 | -0.079 | 1.0 | 0.199 | 0.565 | 0.18 | -0.34 | -0.424 | -0.103 | -0.004 | 0.073 |
| Verb_fin | -0.057 | 0.071 | 0.208 | 0.054 | -0.14 | -0.257 | 0.03 | 0.199 | 1.0 | 0.115 | -0.059 | -0.098 | -0.182 | 0.089 | 0.115 | -0.154 |
| Obj | -0.519 | 0.252 | 0.037 | 0.167 | -0.178 | -0.122 | -0.047 | 0.565 | 0.115 | 1.0 | 0.306 | -0.397 | -0.28 | -0.056 | -0.113 | 0.13 |
| Has_arg2 | 0.052 | -0.034 | -0.1 | -0.051 | 0.158 | -0.037 | -0.014 | 0.18 | -0.059 | 0.306 | 1.0 | -0.059 | 0.018 | -0.043 | -0.056 | 0.074 |
| Direct_meaning | 0.449 | -0.364 | 0.072 | -0.204 | 0.204 | 0.01 | 0.03 | -0.34 | -0.098 | -0.397 | -0.059 | 1.0 | 0.536 | 0.089 | 0.115 | -0.154 |
| Fact | 0.295 | -0.2 | 0.033 | -0.208 | 0.125 | 0.1 | 0.055 | -0.424 | -0.182 | -0.28 | 0.018 | 0.536 | 1.0 | -0.452 | -0.131 | 0.408 |
| пе=инф | 0.099 | -0.065 | -0.117 | -0.096 | 0.233 | -0.071 | -0.027 | -0.103 | 0.089 | -0.056 | -0.043 | 0.089 | -0.452 | 1.0 | -0.106 | -0.58 |
| пе=непрош | 0.083 | -0.02 | -0.068 | 0.146 | -0.023 | 0.026 | -0.035 | -0.004 | 0.115 | -0.113 | -0.056 | 0.115 | -0.131 | -0.106 | 1.0 | -0.749 |
| пе=прош | -0.134 | 0.06 | 0.133 | -0.056 | -0.136 | 0.026 | 0.047 | 0.073 | -0.154 | 0.13 | 0.074 | -0.154 | 0.408 | -0.58 | -0.749 | 1.0 |

![correlation](https://github.com/eszakharova/cxg_project/blob/master/corr.png)

Сильнее всего коррелируют с целевой переменной следующие признаки:
+ оформление пациенса с предлогом <--> молния - субъект
+ прямое значение <--> молния - субъект
+ неодушевленный пациенс <--> молния - субъект

Сильнее всего коррелируют между собой следующие признаки (не учитывая столбцы, являющиеся разными значениями одного категориального признака):
+ неодушевленный пациенс <--> оформление пациенса с предлогом
+ непрямое значение <--> оформление пациенса прямым дополнением

## Мультифакторный анализ
Для анализа было построено дерево решений с помощью библиотеки sklearn для Python. Параметры дерева: критерий разбиения - Джини, ограничений на максимальную глубину и количесвто листов нет.   
Предыдущий запуск дерева и рандомного леса показал, что у признака "Has_arg2" нулевой вес, поэтому он не использовался для обучения и построения дерева.  
                                                      
![tree_visualizaton](https://github.com/eszakharova/cxg_project/blob/master/dtree_subject.png)
### Веса признаков в дереве
+ Obj: 0.402163689155
+ молния ударить X: 0.239561738303
+ Direct_meaning: 0.0903024409244
+ Fact: 0.0585131946014
+ Arg1_anim: 0.0511453255354
+ X ударить молния: 0.0463642686037
+ молния X ударить: 0.0429136565822
+ X молния ударить: 0.0393763525222
+ пе=инф: 0.0164715164776
+ Verb_fin: 0.00835548583927
+ ударить X молния: 0.00454944558613
+ пе=прош: 0.00028288586914
+ ударить молния X: 0.0
+ пе=непрош: 0.0

### Веса признаков - решающий лес
Дополнительно на данных была обучена модель Random Forest (10 деревьев, критерий разбиения Джини,ограничений на максимальную глубину и количесвто листов нет).
+ Obj: 0.338357823583
+ Direct_meaning: 0.17480596781
+ молния ударить X: 0.106226034457
+ X молния ударить: 0.0718962692788
+ молния X ударить: 0.0658744098906
+ Arg1_anim: 0.0615940326082
+ Fact: 0.0524478396582
+ X ударить молния: 0.0412543027801
+ пе=прош: 0.028909251386
+ пе=непрош: 0.0168144709081
+ Verb_fin: 0.0166699545917
+ ударить X молния: 0.0126179664652
+ пе=инф: 0.0124663437492
+ ударить молния X: 6.5332834357e-05

## Содержательный лингвистический анализ результатов статистического анализа
Наиболее важными являются признаки Obj - оформление пациенса прямым дополнением, Direct_meaning - прямое или переносное значение и порядок слов "молния ударить X".   
Офрмление пациенса предлогом,говорит о том, что вероятнее всего "молния" будет подлежащим. Вариант "в X-a ударило молнией" встречается крайне редко, "X-а ударило молнией" мне, как носителю, кажется намного более удачным.
Вариант с "молнией" тяготеет к употреблению в непрямом значении, а именно вместе с "будто", "словно" и т.д. Возможно это связано с тем, что пациенс при данном варианте конструкции чаще одушевленный. 
Порядок слов "молния ударить X" более типичен для варианта с предложным оформлением пациенса, а в таких случаях "молния" скорее всего будет субъектом. 




## Обсуждение использованных квантитативных методов
### Качество классификации (на обучающей выборке, в этом случае вроде так делать можно)

|  | precision | recall | f1-score | support |
|-----------|-----------|--------|----------|---------|
| 0 | 0.69 | 0.92 | 0.79 | 24 |
| 1 | 0.99 | 0.95 | 0.97 | 201 |
| avg/total | 0.96 | 0.95 | 0.95 | 225 |

**Реальное распределение**

+ 1  -  201
+ 0  -   24

**Предсказанное распределение**

+ 1  -  193
+ 0  -  32

