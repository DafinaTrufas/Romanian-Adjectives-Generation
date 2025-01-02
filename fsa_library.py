from transitions import Machine


class RegularInflectionsFSM:
    def __init__(self, lemma):
        self.lemma = lemma
        self.generated_forms = [lemma]

        states = ['q0', 'fsg', 'mpl', 'fpl']

        self.machine = Machine(model=self, states=states, initial='q0')

        self.machine.add_transition('generate_f_sg', 'q0', 'fsg', after='to_fsg')
        self.machine.add_transition('generate_m_pl', 'q0', 'mpl', after='to_mpl')
        self.machine.add_transition('generate_f_pl', 'q0', 'fpl', after='to_fpl')

    def to_fsg(self):
        self.generated_forms.append(self.lemma + 'ă')

    def to_mpl(self):
        self.generated_forms.append(self.lemma + 'i')

    def to_fpl(self):
        self.generated_forms.append(self.lemma + 'e')

    def generate_all_forms(self):
        for trigger in ['generate_f_sg', 'generate_m_pl', 'generate_f_pl']:
            getattr(self, trigger)()
            self.state = 'q0'
        for form in self.generated_forms:
            print(form, end = ', ')
        print()

class EOConsonantInflectionsFSM(RegularInflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-2] + self.lemma[-2] + 'a' + self.lemma[-1] + 'ă')

    def to_mpl(self):
        if self.lemma[-1] == 's':
            self.generated_forms.append(self.lemma[:-1] + 'și')
        elif self.lemma[-1] == 'l':
            self.generated_forms.append(self.lemma[:-1] + 'i')
        else:
            self.generated_forms.append(self.lemma + 'i')

    def to_fpl(self):
        if self.lemma[-1] == 'g':
            self.generated_forms.append(self.lemma[:-2] + self.lemma[-2] + self.lemma[-1] + 'i')
        elif self.lemma[-2] == 'e':
            self.generated_forms.append(self.lemma[:-2] + self.lemma[-2] + self.lemma[-1] + 'e')
        else:
            self.generated_forms.append(self.lemma[:-2] + self.lemma[-2] + 'a' + self.lemma[-1] + 'e')

class TORInflectionsFSM(RegularInflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-2] + 'oare')

    def to_fpl(self):
        self.generated_forms.append(self.lemma[:-2] + 'oare')

class DSTZInflectionsFSM(RegularInflectionsFSM):
    def to_mpl(self):
        if self.lemma[-1] == 'd':
            self.generated_forms.append(self.lemma[:-1] + 'zi')
        elif self.lemma[-1] == 's':
            self.generated_forms.append(self.lemma[:-1] + 'și')
        elif self.lemma[-1] == 't':
            if self.lemma[-2] == 's':
                self.generated_forms.append(self.lemma[:-2] + 'ști')
            else:
                self.generated_forms.append(self.lemma[:-1] + 'ți')
        if self.lemma[-1] == 'z':
            if self.lemma.endswith('eaz'):
                self.generated_forms.append(self.lemma[:-2] + 'ji')
            else:
                self.generated_forms.append(self.lemma[:-1] + 'ji')

    def to_fpl(self):
        if self.lemma.endswith('eaz'):
            self.generated_forms.append(self.lemma[:-2] + 'ze')
        else:
            self.generated_forms.append(self.lemma + 'e')

class UVowelInfectionsFSM(RegularInflectionsFSM):
    def to_fsg(self):
        if self.lemma == 'roșu':
            self.generated_forms.append(self.lemma[:-1] + 'ie')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'ă')

    def to_mpl(self):
        if self.lemma == 'roșu':
            self.generated_forms.append(self.lemma[:-1] + 'ii')
        elif self.lemma.endswith('stru'):
            self.generated_forms.append(self.lemma[:-4] + 'ștri')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'i')

    def to_fpl(self):
        if self.lemma == 'roșu':
            self.generated_forms.append(self.lemma[:-1] + 'ii')
        else:
            self.generated_forms.append(self.lemma[:-1] + 'e')

class USemiVowelInfectionsFSM(RegularInflectionsFSM):
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

class IUInflectionsFSM(RegularInflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-1] + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma[:-1] + 'i')

    def to_fpl(self):
        self.generated_forms.append(self.lemma[:-1] + 'i')

class VelarConsonantInflectionsFSM(RegularInflectionsFSM):
    def to_fsg(self):
        if self.lemma.endswith('esc'):
            self.generated_forms.append(self.lemma[:-3] + 'ească')
        else:
            self.generated_forms.append(self.lemma + 'ă')

    def to_mpl(self):
        if self.lemma.endswith('esc'):
            self.generated_forms.append(self.lemma[:-3] + 'ești')
        elif self.lemma.endswith('eag'):
            self.generated_forms.append(self.lemma[:-2] + 'gi')
        else:
            self.generated_forms.append(self.lemma + 'i')

    def to_fpl(self):
        if self.lemma.endswith('esc'):
            self.generated_forms.append(self.lemma[:-3] + 'ești')
        elif self.lemma.endswith('eag'):
            self.generated_forms.append(self.lemma[:-2] + 'ge')
        elif self.lemma.endswith('ic') and self.lemma != 'mic':
            self.generated_forms.append(self.lemma + 'e')
        else:
            self.generated_forms.append(self.lemma + 'i')

class EInflectionsFSM(RegularInflectionsFSM):
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

class UIInflectionsFSM(RegularInflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma)

    def to_fpl(self):
        self.generated_forms.append(self.lemma)

class PalatalConsonantFSM(RegularInflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-1] + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma)

    def to_fpl(self):
        if self.lemma == 'vechi':
            self.generated_forms.append(self.lemma)
        else:
            self.generated_forms.append(self.lemma[:-1] + 'e')

class ISemiVowelInflectionsFSM(RegularInflectionsFSM):
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

class CAffricatedVelarConsonantInflectionsFSM(RegularInflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-1] + 'e')

    def to_mpl(self):
        self.generated_forms.append(self.lemma)

    def to_fpl(self):
        self.generated_forms.append(self.lemma[:-1] + 'e')

class JuneInflectionsFSM(RegularInflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma[:-1] + 'ă')

    def to_mpl(self):
        self.generated_forms.append(self.lemma[:-1] + 'i')

    def to_fpl(self):
        self.generated_forms.append(self.lemma)

class ÂInflectionsFSM(RegularInflectionsFSM):
    def to_mpl(self):
        self.generated_forms.append(self.lemma[:1] + 'i' + self.lemma[2] + 'e' + self.lemma[4:] + 'i')

    def to_fpl(self):
        self.generated_forms.append(self.lemma[:1] + 'i' + self.lemma[2] + 'e' + self.lemma[4:] + 'e')

class InvariableFSM(RegularInflectionsFSM):
    def to_fsg(self):
        self.generated_forms.append(self.lemma)

    def to_mpl(self):
        self.generated_forms.append(self.lemma)

    def to_fpl(self):
        self.generated_forms.append(self.lemma)

def generate_inflections(lemma):
    fsm = None
    if lemma.endswith('tor'):
        fsm = TORInflectionsFSM(lemma)
    elif lemma[-2] in 'eo' and lemma[-1] not in 'aeiu':
        fsm = EOConsonantInflectionsFSM(lemma)
    elif lemma[1] == 'â' and not lemma.endswith('esc'):
        fsm = ÂInflectionsFSM(lemma)
    elif lemma[-1] not in 'aeioucgdstz':
        fsm = RegularInflectionsFSM(lemma)
    elif lemma[-1] in 'dstz':
        fsm = DSTZInflectionsFSM(lemma)
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
        fsm = InvariableFSM(lemma)
    fsm.generate_all_forms()

with open('romanian_adjectives.txt', 'r', encoding="utf-8") as f:
    for adj in f.readlines():
        if adj[-1] == '\n':
            generate_inflections(adj[:-1])
        else:
            generate_inflections(adj)