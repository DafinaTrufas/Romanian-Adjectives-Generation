import pandas as pd
from transitions import Machine

indeclinable_adjectives = [
    'acaju', 'acătărea', 'acătării', 'afro', 'aievea', 'alene', 'anevoie', 'anticorupție', 'anticriză', 'antidoping', 'antidumping', 'antifading', 'antiglonț', 'antigrindină', 'antiîmbătrânire', 'antimafia', 'antipersonal',
    'antiporno', 'antirachetă', 'antistres', 'antisubmarin', 'antitetanos', 'antitrust', 'anume', 'asăminea', 'asemenea', 'atare', 'atroce', 'audio', 'audiovideo', 'bej', 'bengali', 'beton', 'bine', 'biv', 'blană', 'bleu',
    'bordo', 'bun ca pâinea caldă', 'ca lumea', 'cașto', 'căcălău', 'călare', 'câtea', 'chit', 'cilibi', 'cogeamite', 'cogemite', 'color', 'cool', 'coșcogeme', 'coz', 'cringe', 'cu capul în nori', 'cumsecade', 'cușer',
    'cutare', 'cvasi', 'de', 'de baltă', 'de teren', 'de treabă', 'dentăiu', 'dentâiu', 'deosebi', 'disco', 'ditai', 'ditamai', 'doldora', 'drive-in', 'dry', 'eficace', 'evghenichi', 'expre', 'farin', 'fărădelege', 'ferice',
    'forte', 'fucking', 'fucsia', 'fugace', 'full-time', 'gaga', 'gata', 'gay', 'get-beget', 'gigea', 'gogeamite', 'gratis', 'grena', 'gri', 'hi-fi', 'high', 'hindustani', 'hippy', 'horror', 'ieftin ca braga', 'in-cuarto', 'in-cvarto',
    'incognito', 'indigo', 'indoor', 'instant', 'intercluburi', 'iute ca săgeata', 'iuti', 'ivoar', 'izabel', 'în cauză', 'kaki', 'laiv', 'leoarcă', 'lestie', 'lila', 'liliput', 'live', 'maro', 'maxi', 'merinos',
    'meteo', 'midi', 'mini', 'mișto', 'mov', 'multicanal', 'multimedia', 'multispot', 'muscat', 'nașpa', 'nepereche', 'niscai', 'niscaiva', 'non-stop', 'nonprofit', 'nonstop', 'numai piele și os', 'oareșicare', 'oliv',
    'oranj', 'otova', 'pane', 'papua', 'pe dos', 'pe lângă', 'pendinte', 'pepita', 'plointe', 'pop', 'porno', 'princeps', 'profi', 'prost ca noaptea', 'punk', 'pursânge', 'quechua', 'retard',
    'retro', 'roz', 'sadea', 'second-hand', 'sexy', 'shocking', 'soul', 'standby', 'stereo', 'super', 'șamoa', 'șucada', 'șuco', 'vâlvoi', 'vel', 'verde ca bradul', 'vernil', 'video', 'vivace'
]


class InflectionsFSM():
    def __init__(self, lemma):
        self.lemma = lemma
        self.generated_forms = [lemma]

        states = ['q0', 'fsg', 'mpl', 'fpl']

        self.machine = Machine(model=self, states=states, initial='q0')

        self.machine.add_transition('generate_m_pl', 'q0', 'mpl', after='to_mpl')
        self.machine.add_transition('generate_f_sg', 'q0', 'fsg', after='to_fsg')
        self.machine.add_transition('generate_f_pl', 'q0', 'fpl', after='to_fpl')

    def to_fsg(self):
        self.generated_forms.append(self.lemma + 'ă')

    def to_mpl(self):
        self.generated_forms.append(self.lemma + 'i')

    def to_fpl(self):
        self.generated_forms.append(self.lemma + 'e')

    def generate_all_forms(self):
        for trigger in ['generate_m_pl', 'generate_f_sg', 'generate_f_pl']:
            getattr(self, trigger)()
            self.state = 'q0'
        return self.generated_forms

class ConsonantFSM(InflectionsFSM):
    def to_fsg(self):
        if self.lemma[-2] == 'o' and self.lemma[-3:] not in ['dor', 'lor', 'for', 'vor', 'fob', 'top', 'rof', 'rop', 'pod', 'rob', 'don', 'dot', 'rom', 'tom', 'ton', 'fon', 'col', 'lof', 'lot', 'got', 'cor', 'rot', 'hor', 'xon', 'zon', 'gon', 'ron', 'nom', 'mon', 'por', 'nop', 'lop', 'mod'] and self.lemma[-2:] not in ['ot', 'ox'] or self.lemma in ['bleot', 'box', 'econom', 'fanfaron', 'idiot', 'netot'] or self.lemma[-2] == 'e' and self.lemma[-3:] not in ['bet', 'fed', 'ped', 'lel', 'let', 'pet'] and self.lemma[-2:] not in ['eh', 'el', 'em', 'ex'] and self.lemma[-1] not in 'nrz':
            self.generated_forms.append(self.lemma[:-1] + 'a' + self.lemma[-1] + 'ă')
        elif self.lemma[-2:] == 'el' and self.lemma[-3] not in 'fl':
            self.generated_forms.append(self.lemma[:-1] + 'a')
        else:
            super().to_fsg()

    def to_mpl(self):
        if self.lemma[-1] == 'd':
            if self.lemma[-2:-1] == 'ea':
                self.generated_forms.append(self.lemma[:-2] + 'zi')
            else:
                self.generated_forms.append(self.lemma[:-1] + 'zi')
        elif self.lemma[-1] == 's':
            self.generated_forms.append(self.lemma[:-1] + 'și')
        elif self.lemma[-1] == 't':
            if self.lemma[-2] == 's':
                self.generated_forms.append(self.lemma[:-2] + 'ști')
            elif self.lemma == 'beat':
                self.generated_forms.append(self.lemma[:-2] + 'ți')
            else:
                self.generated_forms.append(self.lemma[:-1] + 'ți')
        elif self.lemma[-1] == 'x':
            self.generated_forms.append(self.lemma[:-1] + 'cși')
        elif self.lemma[-1] == 'z':
            if self.lemma[-3:-1] == 'ea':
                self.generated_forms.append(self.lemma[:-2] + 'ji')
            else:
                self.generated_forms.append(self.lemma + 'i')
        elif self.lemma[-3:] == 'ian':
            self.generated_forms.append(self.lemma[:-2] + 'eni')
        elif self.lemma[-3:] == 'ean':
            self.generated_forms.append(self.lemma[:-2] + 'ni')
        elif self.lemma[-2:] == 'el' and self.lemma[-3] not in 'fl':
            self.generated_forms.append(self.lemma[:-1] + 'i')
        elif self.lemma[-3:-1] == 'ea' and self.lemma[-1] not in 'lrtv':
            self.generated_forms.append(self.lemma[:-2] + self.lemma[-1] + 'i')
        else:
            super().to_mpl()

    def to_fpl(self):
        if self.lemma[-2] == 'o' and self.lemma[-3:] not in ['dor', 'lor', 'for', 'vor', 'fob', 'top', 'rof', 'rop', 'pod', 'rob', 'don', 'dot', 'rom', 'tom', 'ton', 'fon', 'col', 'lof', 'lot', 'got', 'cor', 'rot', 'hor', 'xon', 'zon', 'gon', 'ron', 'nom', 'mon', 'por', 'nop', 'lop', 'mod'] and self.lemma[-2:] not in ['ot', 'ox'] or self.lemma in ['bleot', 'box', 'econom', 'fanfaron', 'idiot', 'netot']:
            self.generated_forms.append(self.lemma[:-1] + 'a' + self.lemma[-1] + 'e')
        elif self.lemma.endswith('eaz'):
            self.generated_forms.append(self.lemma[:-2] + 'ze')
        elif self.lemma[-3:] == 'ian':
            self.generated_forms.append(self.lemma[:-2] + 'ene')
        elif self.lemma[-3:] == 'ean':
            self.generated_forms.append(self.lemma[:-2] + 'ne')
        elif self.lemma == 'beat':
            self.generated_forms.append(self.lemma[:-2] + 'te')
        elif self.lemma[-3:-1] == 'ea' and self.lemma[-1] not in 'lrtv':
            self.generated_forms.append(self.lemma[:-2] + self.lemma[-1] + 'e')
        else:
            super().to_fpl()

    def generate_all_forms(self):
        for trigger in ['generate_m_pl', 'generate_f_sg', 'generate_f_pl']:
            getattr(self, trigger)()
            self.state = 'q0'
        return self.generated_forms

class STZORInflectionsFSM(InflectionsFSM):
    def to_fsg(self):
        if self.lemma == 'accesor':
            self.generated_forms.append(self.lemma[:-2] + 'oară')
        else:
            self.generated_forms.append(self.lemma[:-2] + 'oare')

    def to_fpl(self):
        self.to_fsg()

class UVowelInfectionsFSM(InflectionsFSM):
    def to_fsg(self):
        if self.lemma.endswith('roșu'):
            self.generated_forms.append(self.lemma[:-1] + 'ie')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'ă')

    def to_mpl(self):
        if self.lemma.endswith('roșu'):
            self.generated_forms.append(self.lemma[:-1] + 'ii')
        elif self.lemma.endswith('stru'):
            self.generated_forms.append(self.lemma[:-4] + 'ștri')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'i')

    def to_fpl(self):
        if self.lemma.endswith('roșu'):
            self.generated_forms.append(self.lemma[:-1] + 'ii')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'e')

class USemiVowelInfectionsFSM(InflectionsFSM):
    def to_fsg(self):
        if self.lemma == 'nou':
            self.generated_forms.append(self.lemma + 'ă')
        elif self.lemma == 'rău':
            self.generated_forms.append(self.lemma[:-2] + 'ea')
        elif self.lemma == 'nătărău':
            self.generated_forms.append(self.lemma[:-2] + 'oaică')
        elif self.lemma.endswith('ău'):
            self.generated_forms.append('Nu există formă de feminin singular.')
        elif self.lemma.endswith('âu'):
            self.generated_forms.append(self.lemma[:-2] + 'âie')
        elif self.lemma.endswith('eu'):
            self.generated_forms.append(self.lemma[:-1] + 'e')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'a')

    def to_mpl(self):
        self.generated_forms.append(self.lemma[:-1] + 'i')

    def to_fpl(self):
        if self.lemma == 'nou':
            self.generated_forms.append(self.lemma[:-1] + 'i')
        elif self.lemma == 'rău':
            self.generated_forms.append(self.lemma[:-2] + 'ele')
        elif self.lemma == 'nătărău':
            self.generated_forms.append(self.lemma[:-2] + 'oaice')
        elif self.lemma.endswith('ău'):
            self.generated_forms.append('Nu există formă de feminin plural.')
        elif self.lemma.endswith('âu'):
            self.generated_forms.append(self.lemma[:-2] + 'âi')
        elif self.lemma.endswith('eu'):
            self.generated_forms.append(self.lemma[:-1] + 'e')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'le')

class IUInflectionsFSM(InflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-1] + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma[:-1] + 'i')

    def to_fpl(self):
        self.to_mpl()

class VelarConsonantInflectionsFSM(InflectionsFSM):
    def to_fsg(self):
        if self.lemma.endswith('esc'):
            if self.lemma[-4] == 'i':
                self.generated_forms.append(self.lemma[:-3] + 'ască')
            else:
                self.generated_forms.append(self.lemma[:-3] + 'ească')
        else:
            super().to_fsg()

    def to_mpl(self):
        if self.lemma.endswith('esc'):
            self.generated_forms.append(self.lemma[:-3] + 'ești')
        elif self.lemma.endswith('eag'):
            self.generated_forms.append(self.lemma[:-2] + 'gi')
        else:
            super().to_mpl()

    def to_fpl(self):
        if self.lemma.endswith('esc'):
            self.generated_forms.append(self.lemma[:-3] + 'ești')
        elif self.lemma.endswith('eag'):
            self.generated_forms.append(self.lemma[:-2] + 'ge')
        elif self.lemma.endswith('ic') and self.lemma != 'mic':
            self.generated_forms.append(self.lemma + 'e')
        else:
            self.generated_forms.append(self.lemma + 'i')

class EInflectionsFSM(InflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma)

    def to_mpl(self):
        if self.lemma[-2] == 'd':
            self.generated_forms.append(self.lemma[:-2] + 'zi')
        elif self.lemma == 'moale':
            self.generated_forms.append('moi')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'i')

    def to_fpl(self):
        if self.lemma[-2] == 'd':
            self.generated_forms.append(self.lemma[:-2] + 'zi')
        elif self.lemma == 'moale':
            self.generated_forms.append('moi')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'i')

class UIInflectionsFSM(InflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma)

    def to_fpl(self):
        self.to_mpl()

class PalatalConsonantFSM(InflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-1] + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma)

    def to_fpl(self):
        if self.lemma == 'vechi':
            self.to_mpl()
        else:
            self.generated_forms.append(self.lemma[:-1] + 'e')

class ISemiVowelInflectionsFSM(InflectionsFSM):
    def to_fsg(self):
        if self.lemma.endswith('oi'):
            self.generated_forms.append(self.lemma[:-2] + 'oaie')
        else:
            self.generated_forms.append(self.lemma + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma)

    def to_fpl(self):
        if self.lemma.endswith('oi'):
            self.generated_forms.append(self.lemma[:-2] + 'oaie')
        else:
            self.generated_forms.append(self.lemma + 'e')

class CAffricatedVelarConsonantInflectionsFSM(InflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-1] + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma)

    def to_fpl(self):
        self.generated_forms.append(self.lemma[:-1] + 'e')

class JuneInflectionsFSM(InflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-1] + 'ă')

    def to_mpl(self):
        self.generated_forms.append(self.lemma[:-1] + 'i')

    def to_fpl(self):
        self.generated_forms.append(self.lemma)

class ÂInflectionsFSM(InflectionsFSM):
    def to_mpl(self):
        self.generated_forms.append(self.lemma[:1] + 'i' + self.lemma[2] + 'e' + self.lemma[4:] + 'i')

    def to_fpl(self):
        self.generated_forms.append(self.lemma[:1] + 'i' + self.lemma[2] + 'e' + self.lemma[4:] + 'e')

class IndeclinableFSM(InflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma)

    def to_mpl(self):
        self.to_fsg()

    def to_fpl(self):
        self.to_fsg()

def generate_inflections(lemma):
    if lemma in indeclinable_adjectives:
        fsm = IndeclinableFSM(lemma)
    elif lemma[-3:] in ['sor', 'tor', 'zor']:
        fsm = STZORInflectionsFSM(lemma)
    # elif len(lemma) >= 2 and lemma[1] == 'â' and not lemma.endswith('esc'):
    #     fsm = ÂInflectionsFSM(lemma)
    elif lemma[-1] not in 'aeioucg':
        fsm = ConsonantFSM(lemma)
    elif lemma[-1] == 'u' and lemma[-2] not in 'aâăeiou':
        fsm = UVowelInfectionsFSM(lemma)
    elif lemma[-1] == 'u' and lemma[-2] in 'aăâeo':
        fsm = USemiVowelInfectionsFSM(lemma)
    elif lemma.endswith('iu'):
        fsm = IUInflectionsFSM(lemma)
    elif lemma[-1] in 'cg':
        fsm = VelarConsonantInflectionsFSM(lemma)
    elif lemma == 'june':
        fsm = JuneInflectionsFSM(lemma)
    elif lemma[-1] == 'e':
        fsm = EInflectionsFSM(lemma)
    elif lemma.endswith('ui'):
        fsm = UIInflectionsFSM(lemma)
    elif lemma.endswith('chi') or lemma.endswith('ghi'):
        fsm = PalatalConsonantFSM(lemma)
    elif lemma.endswith('ai') or lemma.endswith('ei') or lemma.endswith('oi'):
        fsm = ISemiVowelInflectionsFSM(lemma)
    elif lemma.endswith('ci'):
        fsm = CAffricatedVelarConsonantInflectionsFSM(lemma)
    else:
        fsm = IndeclinableFSM(lemma)
    return fsm.generate_all_forms()

def test_on_dex():
    df_adj_forme = pd.read_csv("adjective_forme.csv")

    unique_adjectives = df_adj_forme["base_form"].unique().tolist()
    num_adj = len(unique_adjectives)

    good_adjectives = 0
    corrupt = 0
    for adj in unique_adjectives:
        forms = generate_inflections(adj)
        ok = 1
        for form in forms:
            if form not in df_adj_forme["inflection"].tolist():
                corrupt += 1
                ok = 0
                print(forms)
                break
        if ok:
            good_adjectives += 1

    print(f"Good: {good_adjectives}")
    print(f"Corrupt: {corrupt}")
    print(f"Total: {num_adj}")

    print(f"Covered: {good_adjectives / num_adj * 100:.2f}%")

test_on_dex()