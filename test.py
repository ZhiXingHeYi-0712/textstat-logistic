#!/usr/bin/python
# -*- coding:utf-8 -*-

"""Test suite for textstat
"""

import textstat_logistic

short_test = "Cool dogs wear da sunglasses."

punct_text = """
I said: 'This is a test sentence to test the remove_punctuation function.
It's short and not the work of a singer-songwriter. But it'll suffice.'
Your answer was: "I don't know. If I were you I'd write a test; just to make
sure, you're really just removing the characters you want to remove!" Didn't
"""

punct_text_result_w_apostr = """
I said This is a test sentence to test the remove_punctuation function
It's short and not the work of a singersongwriter But it'll suffice
Your answer was I don't know If I were you I'd write a test just to make
sure you're really just removing the characters you want to remove Didn't
"""

punct_text_result_wo_apostr = """
I said This is a test sentence to test the remove_punctuation function
Its short and not the work of a singersongwriter But itll suffice
Your answer was I dont know If I were you Id write a test just to make
sure youre really just removing the characters you want to remove Didnt
"""

long_test = (
    "Playing ... games has always been thought to be "
    "important to the development of well-balanced and "
    "creative children; however, what part, if any, "
    "they should play in the lives of adults has never "
    "been researched that deeply. I believe that "
    "playing games is every bit as important for adults "
    "as for children. Not only is taking time out to "
    "play games with our children and other adults "
    "valuable to building interpersonal relationships "
    "but is also a wonderful way to release built up "
    "tension.\n"
    "There's nothing my husband enjoys more after a "
    "hard day of work than to come home and play a game "
    "of Chess with someone. This enables him to unwind "
    "from the day's activities and to discuss the highs "
    "and lows of the day in a non-threatening, kick back "
    "environment. One of my most memorable wedding "
    "gifts, a Backgammon set, was received by a close "
    "friend. I asked him why in the world he had given "
    "us such a gift. He replied that he felt that an "
    "important aspect of marriage was for a couple to "
    "never quit playing games together. Over the years, "
    "as I have come to purchase and play, with other "
    "couples & coworkers, many games like: Monopoly, "
    "Chutes & Ladders, Mastermind, Dweebs, Geeks, & "
    "Weirdos, etc. I can reflect on the integral part "
    "they have played in our weekends and our "
    "\"shut-off the T.V. and do something more "
    "stimulating\" weeks. They have enriched my life and "
    "made it more interesting. Sadly, many adults "
    "forget that games even exist and have put them "
    "away in the cupboards, forgotten until the "
    "grandchildren come over.\n"
    "All too often, adults get so caught up in working "
    "to pay the bills and keeping up with the "
    "\"Joneses'\" that they neglect to harness the fun "
    "in life; the fun that can be the reward of "
    "enjoying a relaxing game with another person. It "
    "has been said that \"man is that he might have "
    "joy\" but all too often we skate through life "
    "without much of it. Playing games allows us to: "
    "relax, learn something new and stimulating, "
    "interact with people on a different more "
    "comfortable level, and to enjoy non-threatening "
    "competition. For these reasons, adults should "
    "place a higher priority on playing games in their "
    "lives"
)

easy_text = (
    "Anna and her family love doing puzzles. Anna is best at "
    "little puzzles. Anna and her brother work on medium size "
    "puzzles together. Anna's Brother likes puzzles with cars "
    "in them. When the whole family does a puzzle, they do really "
    "big puzzles. It can take them a week to finish a really "
    "big puzzle. Last year they did a puzzle with 500 pieces! "
    "Anna tries to finish one small puzzle a day by her. "
    "Her puzzles have about 50 pieces. They all glue their "
    "favorite puzzles together and frame them. The puzzles look "
    "so nice on the wall."
)

long_spanish_text = (
    "Muchos años después, frente al pelotón de fusilamiento, "
    "el coronel Aureliano Buendía había de recordar aquella "
    "tarde remota en que su padre lo llevó a conocer el hielo. "
    "Macondo era entonces una aldea de veinte casas de barro y "
    "cañabrava construidas a la orilla de un río de aguas "
    "diáfanas que se precipitaban por un lecho de piedras pulidas, "
    "blancas y enormes como huevos prehistóricos. El mundo era tan "
    "reciente, que muchas cosas carecían de nombre, y para mencionarlas "
    "había que señalarlas con el dedo. Todos los años, por el mes de marzo, "
    "una familia de gitanos desarrapados plantaba su carpa cerca "
    "de la aldea, y con un grande alboroto de pitos y timbales daban a "
    "conocer los nuevos inventos. Primero llevaron el imán. "
    "Un gitano corpulento, de barba montaraz y manos de gorrión, que se "
    "presentó con el nombre de Melquíades, hizo una truculenta demostración "
    "pública de lo que él mismo llamaba la octava maravilla de "
    "los sabios alquimistas de Macedonia."
)

easy_spanish_text = "Hoy es un lindo día"

long_russian_text_guillemets = (
    "Игра ... игры всегда считались важными для развития "
    "уравновешенных и творческих детей; однако, какую роль "
    "они должны играть в жизни взрослых, если таковая имеется, "
    "никогда не исследовалась так глубоко. Я считаю, "
    "что игры для взрослых не менее важны, чем для детей. "
    "Выделение времени для игр с нашими детьми и другими "
    "взрослыми не только ценно для построения межличностных "
    "отношений, но также является прекрасным способом снять "
    "накопившееся напряжение.\n"
    "Ничто не доставляет такого же удовольствие для моего мужа "
    "после тяжелого рабочего дня, как прийти домой и поиграть "
    "с кем-нибудь в шахматы. Это позволяет ему расслабиться от "
    "повседневных дел и обсудить плюсы и минусы дня в спокойной "
    "обстановке. Один из самых запоминающихся свадебных "
    "подарков - набор нардов - получил близкий друг. Я спросила "
    "его, зачем он сделал нам такой подарок. Он ответил, что "
    "считает важным аспектом брака никогда не прекращать "
    "совместные игры. По прошествии лет, когда я "
    "начала покупать и проходить с другими парами и коллегами "
    "многие игры, такие как: Monopoly, Chutes & Ladders, "
    "Mastermind, Dweebs, Geeks, & Weirdos и т.д. Я сознаю их "
    "неотъемлемую роль, которую они сыграли в наши выходные и "
    "в наши недели аля «выключите телевизор и займитесь "
    "чем-нибудь более стимулирующим». Они обогатили мою "
    "жизнь и сделали ее интереснее. К сожалению, многие "
    "взрослые забывают, что игры вообще существуют, а "
    "прячут их в шкафы, о которых забывают, пока не придут "
    "внуки.\n"
    "Слишком часто взрослые настолько увлечены работой, чтобы "
    "платить по счетам и не отставать от «Джонсов», что "
    "пренебрегают радостью жизни; удовольствием, которое может "
    "быть наградой за расслабляющую игру с другим человеком. "
    "Было сказано, что «человек - это для того, чтобы иметь "
    "радость», но слишком часто мы идем по жизни без особой "
    "радости. Игры позволяют нам расслабиться, узнать что-то "
    "новое и интересное, взаимодействовать с людьми на другом, "
    "более комфортном уровне и наслаждаться безопасным "
    "соревнованием. По этим причинам взрослые должны уделять "
    "больше внимания играм в своей жизни"
)

italian_text = (
    "Roma è un comune italiano, capitale della Repubblica Italiana, "
    "nonché capoluogo dell'omonima città metropolitana e della regione Lazio."
)

difficult_word = "Regardless"
easy_word = "Dog"

empty_str = ""

easy_arabic_text = "ذهب هند وأحمد الى المدرسة. هند تحب الرسم والمطالعة"
hard_arabic_text = (
    "\u062a\u062a\u0631\u0643\u0632 \u0623\u0633\u0633 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0646\u0648\u0648\u064a\u0629 \u0628\u0634\u0643\u0644 \
    \u0639\u0627\u0645 \u0639\u0644\u064a \u0627\u0644\u0630\u0631\u0629 \
    \u0648\u0645\u0643\u0648\u0646\u0627\u062a\u0647\u0627 \
    \u0627\u0644\u062f\u0627\u062e\u0644\u064a\u0629 \
    \u0648\u0627\u0644\u062a\u0639\u0627\u0645\u0644 \
    \u0645\u0639 \u062a\u0644\u0643 \u0627\u0644\u0630\u0631\u0629 \
    \u0648\u0627\u0644\u0639\u0646\u0627\u0635\u0631 \
    \u0648\u062d\u064a\u062b \u0627\u0646 \u0647\u0630\u0627 \u0647\u0648 \
    \u0627\u0644\u0645\u0628\u062d\u062b \u0627\u0644\u0639\u0627\u0645 \
    \u0644\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0646\u0648\u0648\u064a\u0629 \u0641\u0627\u0646\u0647 \
    \u0627\u062d\u064a\u0627\u0646\u0627 \u0645\u0627 \
    \u064a\u0637\u0644\u0642 \u0639\u0644\u064a\u0647\u0627 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0630\u0631\u064a\u0629 \
    \u0627\u0644\u0627 \u0623\u0646 \u0645\u062c\u0627\u0644 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0646\u0648\u0648\u064a\u0629 \
    \u0623\u0639\u0645 \u0648\u0627\u0634\u0645\u0644 \u0645\u0646 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0630\u0631\u064a\u0629 \u0648\u0643\u0630\u0644\u0643 \
    \u0627\u0644\u0641\u064a\u0632\u064a\u0627\u0621 \
    \u0627\u0644\u0630\u0631\u064a\u0629 \u062a\u0647\u062a\u0645 \
    \u0628\u062f\u0627\u0631\u0633\u0629 \
    \u0627\u0644\u0630\u0631\u0629 \u0641\u0649 \
    \u062d\u0627\u0644\u0627\u062a\u0647\u0627 \
    \u0648\u062a\u0641\u0627\u0639\u0644\u0627\u062a\u0647\u0627 \
    \u0627\u0644\u0645\u062e\u062a\u0644\u0641\u0629"
)


def test_char_count():
    textstat_logistic.set_lang("en_US")
    count = textstat_logistic.char_count(long_test)
    count_spaces = textstat_logistic.char_count(
        long_test, ignore_spaces=False
    )

    assert count == 1748
    assert count_spaces == 2123


def test_letter_count():
    textstat_logistic.set_lang("en_US")
    count = textstat_logistic.letter_count(long_test)
    count_spaces = textstat_logistic.letter_count(
        long_test, ignore_spaces=False
    )

    assert count == 1686
    assert count_spaces == 2061


def test_remove_punctuation_incl_apostrophe():
    textstat_logistic.set_lang('en_US')
    textstat_logistic.set_rm_apostrophe(True)
    text = textstat_logistic.remove_punctuation(punct_text)

    # set the __rm_apostrophe attribute back to the default
    textstat_logistic.set_rm_apostrophe(False)

    assert text == punct_text_result_wo_apostr


def test_remove_punctuation_excl_apostrophe():
    textstat_logistic.set_lang('en_US')
    textstat_logistic.set_rm_apostrophe(False)
    text = textstat_logistic.remove_punctuation(punct_text)

    assert text == punct_text_result_w_apostr


def test_lexicon_count():
    textstat_logistic.set_lang("en_US")
    count = textstat_logistic.lexicon_count(long_test)
    count_punc = textstat_logistic.lexicon_count(long_test, removepunct=False)

    assert count == 372
    assert count_punc == 376


def test_syllable_count():
    textstat_logistic.set_lang("en_US")
    count = textstat_logistic.syllable_count(long_test)

    assert count == 519


def test_sentence_count():
    textstat_logistic.set_lang("en_US")
    count = textstat_logistic.sentence_count(long_test)

    assert count == 17


def test_sentence_count_russian():
    textstat_logistic.set_lang('ru_RU')
    count = textstat_logistic.sentence_count(long_russian_text_guillemets)

    assert count == 16


def test_avg_sentence_length():
    textstat_logistic.set_lang("en_US")
    avg = textstat_logistic.avg_sentence_length(long_test)

    assert avg == 21.9


def test_avg_syllables_per_word():
    textstat_logistic.set_lang("en_US")
    avg = textstat_logistic.avg_syllables_per_word(long_test)

    assert avg == 1.4


def test_avg_letter_per_word():
    textstat_logistic.set_lang("en_US")
    avg = textstat_logistic.avg_letter_per_word(long_test)

    assert avg == 4.53


def test_avg_sentence_per_word():
    textstat_logistic.set_lang("en_US")
    avg = textstat_logistic.avg_sentence_per_word(long_test)

    assert avg == 0.05


def test_flesch_reading_ease():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.flesch_reading_ease(long_test)

    assert score == 66.17

    textstat_logistic.set_lang("de_DE")
    score = textstat_logistic.flesch_reading_ease(long_test)

    assert score == 64.5

    textstat_logistic.set_lang("es_ES")
    score = textstat_logistic.flesch_reading_ease(long_test)

    assert score == 86.76

    textstat_logistic.set_lang("fr_FR")
    score = textstat_logistic.flesch_reading_ease(long_test)

    assert score == 81.73

    textstat_logistic.set_lang("it_IT")
    score = textstat_logistic.flesch_reading_ease(long_test)

    assert score == 91.57

    textstat_logistic.set_lang("nl_NL")
    score = textstat_logistic.flesch_reading_ease(long_test)

    assert score == 63.27

    textstat_logistic.set_lang("ru_RU")
    score = textstat_logistic.flesch_reading_ease(long_test)

    assert score == 118.27


def test_flesch_kincaid_grade():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.flesch_kincaid_grade(long_test)

    assert score == 9.5


def test_polysyllabcount():
    textstat_logistic.set_lang("en_US")
    count = textstat_logistic.polysyllabcount(long_test)

    assert count == 32


def test_smog_index():
    textstat_logistic.set_lang("en_US")
    index = textstat_logistic.smog_index(long_test)

    assert index == 11.0


def test_coleman_liau_index():
    textstat_logistic.set_lang("en_US")
    index = textstat_logistic.coleman_liau_index(long_test)

    assert index == 8.99


def test_automated_readability_index():
    textstat_logistic.set_lang("en_US")
    index = textstat_logistic.automated_readability_index(long_test)

    assert index == 11.6


def test_linsear_write_formula():
    textstat_logistic.set_lang("en_US")
    result = textstat_logistic.linsear_write_formula(long_test)

    assert result == 14.5

    result = textstat_logistic.linsear_write_formula(empty_str)

    assert result == -1.0


def test_difficult_words():
    textstat_logistic.set_lang("en_US")
    result = textstat_logistic.difficult_words(long_test)

    assert result == 49


def test_difficult_words_list():
    textstat_logistic.set_lang("en_US")
    result = textstat_logistic.difficult_words_list(short_test)

    assert result == ["sunglasses"]


def test_is_difficult_word():
    textstat_logistic.set_lang("en_US")
    result = textstat_logistic.is_difficult_word(difficult_word)

    assert result is True


def test_is_easy_word():
    textstat_logistic.set_lang("en_US")
    result = textstat_logistic.is_easy_word(easy_word)

    assert result is True


def test_dale_chall_readability_score():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.dale_chall_readability_score(long_test)

    assert score == 7.78

    score = textstat_logistic.dale_chall_readability_score(empty_str)

    assert score == 0.0


def test_gunning_fog():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.gunning_fog(long_test)

    assert score == 10.7

    # FOG-PL
    textstat_logistic.set_lang("pl_PL")
    score_pl = textstat_logistic.gunning_fog(long_test)

    assert score_pl == 9.84


def test_lix():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.lix(long_test)

    assert score == 43.71

    result = textstat_logistic.lix(empty_str)

    assert result == 0.0


def test_rix():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.rix(long_test)

    assert score == 4.59


def test_text_standard():
    textstat_logistic.set_lang("en_US")
    standard = textstat_logistic.text_standard(long_test)

    assert standard == "10th and 11th grade"

    standard = textstat_logistic.text_standard(short_test)

    assert standard == "2nd and 3rd grade"


def test_reading_time():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.reading_time(long_test)

    assert score == 25.68


def test_lru_caching():
    textstat_logistic.set_lang("en_US")
    # Clear any cache
    textstat_logistic.sentence_count.cache_clear()
    textstat_logistic.avg_sentence_length.cache_clear()

    # Make a call that uses `sentence_count`
    textstat_logistic.avg_sentence_length(long_test)

    # Test that `sentence_count` was called
    assert textstat_logistic.sentence_count.cache_info().misses == 1

    # Call `avg_sentence_length` again, but clear it's cache first
    textstat_logistic.avg_sentence_length.cache_clear()
    textstat_logistic.avg_sentence_length(long_test)

    # Test that `sentence_count` wasn't called again
    assert textstat_logistic.sentence_count.cache_info().hits == 1


def test_changing_lang_clears_cache():
    textstat_logistic.set_lang("en_US")

    # Clear any cache and call reading ease
    textstat_logistic.flesch_reading_ease.cache_clear()
    textstat_logistic.flesch_reading_ease(short_test)

    # Check the cache has only been missed once
    assert textstat_logistic.flesch_reading_ease.cache_info().misses == 1

    # Change the language and recall reading ease
    textstat_logistic.set_lang("fr")
    textstat_logistic.flesch_reading_ease(short_test)

    # Check the cache hasn't been hit again
    assert textstat_logistic.flesch_reading_ease.cache_info().misses == 1


def test_unicode_support():
    textstat_logistic.set_lang("en_US")
    textstat_logistic.text_standard(
        "\u3042\u308a\u304c\u3068\u3046\u3054\u3056\u3044\u307e\u3059")

    textstat_logistic.text_standard("ありがとうございます")


def test_spache_readability():
    textstat_logistic.set_lang("en_US")
    spache = textstat_logistic.spache_readability(easy_text, False)

    assert spache == 2

    score = textstat_logistic.spache_readability(empty_str)

    assert score == 0.0


def test_dale_chall_readability_score_v2():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.dale_chall_readability_score_v2(long_test)

    assert score == 6.8


def test_fernandez_huerta():
    textstat_logistic.set_lang("es")
    score = textstat_logistic.fernandez_huerta(long_spanish_text)

    assert score == 65.3

    score = textstat_logistic.fernandez_huerta(empty_str)

    assert score == 206.84


def test_szigriszt_pazos():
    textstat_logistic.set_lang("es")
    score = textstat_logistic.szigriszt_pazos(long_spanish_text)

    assert score == 62.16

    score = textstat_logistic.szigriszt_pazos(empty_str)

    assert score == 0.0


def test_gutierrez_polini():
    textstat_logistic.set_lang("es")
    score = textstat_logistic.gutierrez_polini(easy_spanish_text)

    assert score == 64.35

    score = textstat_logistic.gutierrez_polini(empty_str)

    assert score == 0.0


def test_crawford():
    textstat_logistic.set_lang("es")
    score = textstat_logistic.crawford(long_spanish_text)

    assert score == 5.1

    score = textstat_logistic.crawford(empty_str)

    assert score == 0.0


def test_wienersachtext_formula():
    textstat_logistic.set_lang("de")
    sample_text = 'Alle meine Entchen schwimmen auf dem See, \
    Köpfchen unters Wasser, Schwänzchen in die Höh.'
    wstf = textstat_logistic.wiener_sachtextformel(sample_text, variant=1)

    assert wstf == 3.8

    sample_text = 'Alle Parteien widmen dem Thema rein quantitativ \
    betrachtet nennenswerte Aufmerksamkeit, die Grünen wenig überraschend \
    am meisten.'
    wstf = textstat_logistic.wiener_sachtextformel(sample_text, variant=1)

    assert wstf == 13.9


def test_gulpease_index():
    textstat_logistic.set_lang("it")
    score = textstat_logistic.gulpease_index(italian_text)

    assert score == 40.1


def test_default_lang_configs():
    # Config from default en_US should be used
    textstat_logistic.set_lang("en_GB")
    score = textstat_logistic.flesch_reading_ease(long_test)

    assert score == 66.17


def test_osman():
    easy_score = textstat_logistic.osman(easy_arabic_text)
    hard_score = textstat_logistic.osman(hard_arabic_text)

    assert easy_score == 102.19
    assert hard_score == 39.29


def test_disabling_rounding():
    textstat_logistic.set_lang("en_US")
    textstat_logistic.set_rounding(False)

    index = textstat_logistic.spache_readability(long_test)

    textstat_logistic.set_rounding(True)

    assert index == 5.057207463630613


def test_changing_rounding_points():
    textstat_logistic.set_lang("en_US")
    textstat_logistic.set_rounding(True, points=5)

    index = textstat_logistic.spache_readability(long_test)

    textstat_logistic.set_rounding(True)

    assert index == 5.05721


def test_instanced_textstat_rounding():
    textstat_logistic.set_lang("en_US")

    from textstat_logistic.textstat import textstatistics

    my_textstat = textstatistics()
    my_textstat.set_rounding(False)

    my_not_rounded_index = my_textstat.spache_readability(long_test)

    assert my_not_rounded_index == 5.057207463630613

    default_rounded_index = textstat_logistic.spache_readability(long_test)

    assert default_rounded_index == 5.06


def test_mcalpine_eflaw():
    textstat_logistic.set_lang("en_US")
    score = textstat_logistic.mcalpine_eflaw(long_test)

    assert score == 30.8


def test_miniword_count():
    textstat_logistic.set_lang("en_US")
    count = textstat_logistic.miniword_count(long_test)

    assert count == 151


# Hungarian tests

easy_hungarian_text = "A ló zabot eszik és én a csillagos ég alatt alszom ma."

easy_hungarian_text2 = """
    Mondok neked egy nyelvtani fejtöröt.Melyik több?
    Hat tucat tucat vagy fél tucat tucat?
    """

hard_hungarian_text = (
    """
    A mai fagylalt elődjének számító hideg édességet több ezer éve
    készítettek először. Egyes feljegyzések szerint az ó kori kínaiak a
    mézzel édesített gyümölcsleveket hóval, jéggel hűtötték, és ezen hideg
    édességeket szolgálták fel a kiváltságosoknak. Annyi bizonyos, hogy a
    római császárok kedvelt csemegéi voltak a hegyekből hozatott hóval
    kevert gyümölcs levek, melyek sűrűn folyó, hideg, fagylaltszerű
    italkülönlegességet eredményeztek.
    """
    )

hard_academic_hungarian_text = (
    """
    Az Amerikai Egyesült Államokban már a múlt század közepétől
    alkalmazzák az angol nyelv matematikai elemzésére szolgáló olvashatósági
    formulákat. Ezek közül hármat a neveléstudomány is használ a tengerentúli
    oktatásban,a különböző rendeltetési célú szövegek elemzésére. A
    vizsgálatok célja az, hogy meghatározzák a tanítási folyamatban használt
    könyvek és tankönyvek érthető megfogalmazásának korcsoport vagy iskolai
    osztályok alapján besorolható szintjét. Figyelembe véve az elméleti
    hátteret, magyar szövegeken is teszteltük a formulákat, hogy
    megállapítsuk, érvényesek-e az angol nyelvű szövegek következtetései.
    Az olvashatósági tesztek eredeti célja meghatározni azt a fogalmazási
    szintet, amely a legtöbb embernek érthető, és elkerüli az
    olvasásértelmezést zavaró szakkifejezéseket, illetve bonyolult szavak
    alkalmazását. Az 1920-as évektől kezdődően Edward Thorndike a tankönyvek
    olvasásának nehézségi fokát vizsgálta, és különböző szószedeteket
    javasolt iskolai használatra, az életkornak és az iskolai évfolyamoknak
    megfelelően."""
)


def test_char_count_hungarian():
    # Arrange
    textstat_logistic.set_lang("hu_HU")
    expected_easy_count = 43
    expected_easy_count_spaces = 54

    # Act
    actual_count = textstat_logistic.char_count(easy_hungarian_text)
    actual_count_spaces = textstat_logistic.char_count(
        easy_hungarian_text, ignore_spaces=False
    )

    # Assert
    assert actual_count == expected_easy_count
    assert actual_count_spaces == expected_easy_count_spaces


def test_letter_count_hungarian():
    # Arrange
    textstat_logistic.set_lang("hu_HU")
    expected_easy_count = 42
    expected_easy_count_spaces = 53

    actual_count = textstat_logistic.letter_count(easy_hungarian_text)
    actual_count_spaces = textstat_logistic.letter_count(
        easy_hungarian_text, ignore_spaces=False
    )

    # Assert
    assert actual_count == expected_easy_count
    assert actual_count_spaces == expected_easy_count_spaces


def test_sentence_count_hungarian():
    # Arrange
    textstat_logistic.set_lang('hu_HU')
    expected_hard = 3
    expected_hard_academic = 6

    # Act
    actual_hard = textstat_logistic.sentence_count(hard_hungarian_text)
    actual_academic = textstat_logistic.sentence_count(hard_academic_hungarian_text)

    # Assert
    assert actual_hard == expected_hard
    assert actual_academic == expected_hard_academic


def test_flesch_reading_ease_hungarian():
    # Arrange
    textstat_logistic.set_lang("hu_HU")
    expected_easy = 89.09
    expected_hard = 53.0
    expected_hard_academic = 22.02

    # Act
    actual_easy = textstat_logistic.flesch_reading_ease(easy_hungarian_text2)
    actual_hard = textstat_logistic.flesch_reading_ease(hard_hungarian_text)
    actual_academic = textstat_logistic.flesch_reading_ease(
        hard_academic_hungarian_text
    )

    # Assert
    assert actual_easy == expected_easy
    assert actual_hard == expected_hard
    assert actual_academic == expected_hard_academic


def test_smog_index_hungarian():
    # Arrange
    textstat_logistic.set_lang("hu_HU")
    expected_easy = 0
    expected_hard = 17.9
    expected_hard_academic = 21.9

    # Act
    actual_easy = textstat_logistic.smog_index(easy_hungarian_text)
    actual_hard = textstat_logistic.smog_index(hard_hungarian_text)
    actual_academic = textstat_logistic.smog_index(hard_academic_hungarian_text)

    # Assert
    assert actual_easy == expected_easy
    assert actual_hard == expected_hard
    assert actual_academic == expected_hard_academic


def test_gunning_fog_hungarian():
    # Arrange
    textstat_logistic.set_lang("hu_HU")
    expected_easy = 2.6
    expected_hard = 9.71
    expected_hard_academic = 14.41

    # Act
    actual_easy = textstat_logistic.gunning_fog(easy_hungarian_text2)
    actual_hard = textstat_logistic.gunning_fog(hard_hungarian_text)
    actual_academic = textstat_logistic.gunning_fog(hard_academic_hungarian_text)

    # Assert
    assert actual_easy == expected_easy
    assert actual_hard == expected_hard
    assert actual_academic == expected_hard_academic
