# =============================================================================
# Permutacije
#
# Permutacijo običajno predstavimo s seznamom slik posameznih elementov,
# npr. [5, 1, 6, 4, 2, 3], lahko pa tudi s seznamom disjunktnih ciklov, npr.
# [[1, 5, 2], [3, 6], [4]]. Ciklov dolžine 1 (fiksnih točk) običajno ne
# navajamo, a moramo v tem primeru navesti še velikost permutacije
# (v tem primeru 6).
# ===========================================================================@=
# Sestavite funkcijo `je_permutacija`, ki sprejme seznam in preveri,
# ali je v njem zapisana permutacija v običajnem zapisu. V seznamu je zapisana
# permutacija, če se vsak element od $1$ do $n$, kjer je $n$ dolžina
# permutacije, pojavi natanko enkrat.
# 
#     >>> je_permutacija([7, 3, 4, 5, 2, 1])
#     False
#     >>> je_permutacija([7, 3, 4, 5, 2, 6, 1])
#     True
# =============================================================================
def je_permutacija(l):
    n = len(l)
    for i in range(1, n+1):
        if i not in l:
            return False
    return True

# ===========================================================================@=
# Sestavite funkcijo `je_seznam_ciklov`, ki sprejme seznam seznamov in preveri,
# ali vsebuje disjunktne cikle neke permutacije. Preveriti je torej treba,
# ali so vsi elementi pozitivni ter ali se vsak element v stiku vseh ciklov
# pojavi natanko enkrat.
# 
#     >>> je_seznam_ciklov([[8,3,4],[5,7,1]])
#     True
#     >>> je_seznam_ciklov([[8,1,4],[5,7,1]])
#     False
# =============================================================================

def je_seznam_ciklov(l):
    elements = []
    for ccl in l:
        for e in ccl:
            if e in elements or e <= 0:
                return False
            else: 
                elements.append(e)
    return True

# ===========================================================================@=
# Sestavite funkcijo `urejeni_cikli`, ki seznam ciklov pretvori v nov seznam
# tako, da je najmanjši element posameznega cikla vedno na začetku cikla,
# cikli v seznamu pa so urejeni po velikosti prvih elementov. Morebitne prazne
# cikle in cikle dolžine 1 naj odstrani.
# 
#     >>> urejeni_cikli([[7, 3], [4], [5, 2, 1], [8, 2, 14]])
#     [[1, 5, 2], [3, 7], [2, 14, 8]]
# =============================================================================

def urejeni_cikli(l):
    ccl_order = []
    for ccl in l: 
        if len(ccl) < 2:
            pass
        else:
            min_ccl = min(ccl)
            while ccl[0] != min_ccl:
                ccl.append(ccl.pop(0))
            ccl_order.append(ccl)   

    return sorted(ccl_order, key=lambda x: x[0])
    
# ===========================================================================@=
# Sestavite funkcijo `iz_ciklov(cikli, dolzina)`, ki iz seznama ciklov `cikli`
# sestavi običajen zapis permutacije dolzine `dolzina`. Če parametra `dolzina`
# ne podamo, ali pa je ta premajhna, naj bo dolžina enaka največjemu elementu,
# ki se pojavi v ciklih.
# 
#     >>> iz_ciklov([[7, 3], [4], [5, 2, 1]])
#     [5, 1, 7, 4, 2, 6, 3]
#     >>> iz_ciklov([[7, 3], [4], [5, 2, 1]], 9)
#     [5, 1, 7, 4, 2, 6, 3, 8, 9]
# =============================================================================

def iz_ciklov(cycle, length = 0):
    result = []
    n = 1
    maximal = 0
    found = False
    for ccl in cycle:
        if max(ccl) > maximal:
            maximal = max(ccl) 
    if maximal < length:
        maximal = length
    while n <= maximal:
        for ccl in cycle:
            try:
                result.append(ccl[ccl.index(n) + 1])
                found = True
            except ValueError:
                pass
            except IndexError:
                result.append(ccl[0])
                found = True
        if not found:
            result.append(n)
        found = False
        n += 1
    return result


# ===========================================================================@=
# Sestavite funkcijo `v_cikle`, ki iz permutacije sestavi njeno predstavitev s
# cikli.
# 
#     >>> v_cikle([5, 1, 7, 4, 2, 6, 3])
#     [[1, 5, 2], [3, 7]]
# =============================================================================

def v_cikle(perm):
    intermediate = []
    result = []
    temp_var = 1
    n = 0
    visited = [False] * len(perm)
    while n <= len(perm):
        visited[temp_var - 1] = True
        temp_var = perm[temp_var - 1]
        if temp_var not in intermediate:
            intermediate.append(temp_var)
        else:
            temp_var = visited.index(False) + 1
            result.append(intermediate)
            intermediate = []
        n += 1
    result.append(intermediate)
    return urejeni_cikli(result)




def v_cikle_z_solo(perm):
    intermediate = []
    result = []
    temp_var = 1
    n = 0
    visited = [False] * len(perm)
    while n <= len(perm):
        visited[temp_var - 1] = True
        temp_var = perm[temp_var - 1]
        if temp_var not in intermediate:
            intermediate.append(temp_var)
        else:
            temp_var = visited.index(False) + 1
            result.append(intermediate)
            intermediate = []
        n += 1
    result.append(intermediate)
    return result








# ===========================================================================@=
# Sestavite funkcijo `inverz_perm`, ki sestavi in vrne inverz dane permutacije
# v običajni predstavitvi.
# 
#     >>> inverz_perm([7, 3, 4, 5, 2, 1, 6])
#     [6, 5, 2, 3, 4, 7, 1]
# =============================================================================

def inverz_perm(perm):
    result = []
    for i in range(1, len(perm) + 1):
        result.append(perm.index(i) + 1)
    return result

# ===========================================================================@=
# Sestavite funkcijo `inverz_cikli`, ki sestavi in vrne inverz dane
# permutacije, predstavljene s seznamom ciklov. Inverz permutacije dobimo tako,
# da v cikličnem zapisu obrnemo vse cikle (vsakega posebej).
# 
#     >>> inverz_cikli([[7, 3], [4], [5, 2, 1]])
#     [[1, 2, 5], [3, 7]]
# =============================================================================

def inverz_cikli(l):
    ccl_order = []
    intermediate = []
    for ccl in l: 
        if len(ccl) < 2:
            pass
        else:
            min_ccl = min(ccl)
            while ccl != []:
                intermediate.append(ccl.pop())
            ccl_order += [intermediate]
            intermediate = []
    return sorted(ccl_order, key= lambda x: x[0])

# ===========================================================================@=
# Sestavite funkcijo `ciklicni_tip(cikli, dolzina)`, ki vrne ciklični tip
# permutacije dolžine `dolzina`, predstavljene s seznamom ciklov `cikli`.
# To je nabor, ki ima toliko elementov, kot je dolžina najdaljšega cikla.
# Prvi element v tem naboru je število ciklov dolžine 1, drugi element je
# število ciklov dolžine 2, itd. Če parametra `dolzina` ne podamo, ali pa
# je ta premajhna, naj bo dolžina enaka največjemu elementu, ki se pojavi
# v ciklih.
# 
#     >>> ciklicni_tip([[7, 3], [4], [5, 2, 1]])
#     (2, 1, 1)
#     >>> ciklicni_tip([[7, 3], [4], [5, 2, 1]], 9)
#     (4, 1, 1)
# =============================================================================

def ciklicni_tip(l, length = 0):
    intermediate = 0
    maximal = 0
    total = 0
    mlen = 0
    result = []
    for ccl in l:
        total += len(ccl)
        if mlen < len(ccl):
            mlen = len(ccl)
        for n in ccl:
            if n > maximal:
                maximal = n
    if length > maximal:
        maximal = length
    for i in range(1, mlen +1):
        for ccl in l:
            if len(ccl) == i:
                intermediate += 1
        result.append(intermediate)
        intermediate = 0
    result[0] += maximal - total
    return tuple(result)

# ===========================================================================@=
# Sestavite funkcijo `red`, ki izračuna in vrne red permutacije podane s cikli.
# Naj bo $\pi$ permutacija. Red permutacije $\pi$ je najmanjše pozitivno
# število $k$, pri katerem je $\pi^k$ identiteta.
# 
# Namig 1: Red permutacije je najmanjši skupni večkratnik dolžin vseh ciklov.
# 
# Namig 2: Za poljubni dve naravni števili `a` in `b` velja, da je
# `gcd(a, b) * lcm(a, b) == a * b`. (Funkcija `gcd` računa največji
# skupni delitelj, funkcija `lcm` pa najmanjši skupni večkratnik.)
# 
#     >>> red([[7, 3], [4], [5, 2, 1]])
#     6
# =============================================================================

import math
def red(l):
    lengths = []
    for ccl in l:
        lengths.append(len(ccl))
    return math.lcm(*lengths)

    






































































































# ============================@= *-*-*-*-*-*-*-* =@============================

"Če vam Python sporoča, da je v tej vrstici sintaktična napaka,"
"se napaka v resnici skriva v zadnjih vrsticah vaše kode."

"Kode od tu naprej NE SPREMINJAJTE!"

import os
import traceback
import urllib.error

_TOMO_I18N_STRINGS = {
    'ERROR_EQUAL': 'Izraz {0} vrne {1!r} instead of {2!r}.',
    'HINT': 'Namig: {}',
}


import dataclasses
import io
import sys
from contextlib import contextmanager
from typing import List, Optional, Tuple


class Check:
    class VisibleStringIO(io.StringIO):
        def read(self, size=None):
            x = io.StringIO.read(self, size)
            print(x, end="")
            return x

        def readline(self, size=None):
            line = io.StringIO.readline(self, size)
            print(line, end="")
            return line

    class TimeoutError(Exception):
        pass

    @dataclasses.dataclass(slots=True)
    class Part:
        solution: str
        description: Optional[str] = None
        template: Optional[str] = None
        test_script: Optional[str] = None
        is_valid: bool = True
        feedback: List[str] = dataclasses.field(default_factory=list)
        secret: List[Tuple[str, Optional[str]]] = dataclasses.field(default_factory=list)

    parts: List[Part] = []
    current_part: Optional[Part] = None
    part_counter: Optional[int] = None
    i18n_strings = globals().get('_TOMO_I18N_STRINGS', {})

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part.feedback.append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part.is_valid = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(
                Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed)
            )
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted(
                [
                    (Check.clean(k, digits, typed), Check.clean(v, digits, typed))
                    for (k, v) in x.items()
                ]
            )
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get("clean", clean)
        Check.current_part.secret.append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error(
                Check.i18n_strings['ERROR_EQUAL'],
                expression,
                actual_result,
                expected_result,
            )
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error("Namestiti morate numpy.")
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error("Ta funkcija je namenjena testiranju za tip np.ndarray.")

        if env is None:
            env = dict()
        env.update({"np": np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error(
                "Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                type(expected_result).__name__,
                type(actual_result).__name__,
            )
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error(
                "Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.",
                exp_shape,
                act_shape,
            )
            return False
        try:
            np.testing.assert_allclose(
                expected_result, actual_result, atol=tol, rtol=tol
            )
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        exec(code, global_env)
        errors = []
        for x, v in expected_state.items():
            if x not in global_env:
                errors.append(
                    "morajo nastaviti spremenljivko {0}, vendar je ne".format(x)
                )
            elif clean(global_env[x]) != clean(v):
                errors.append(
                    "nastavijo {0} na {1!r} namesto na {2!r}".format(
                        x, global_env[x], v
                    )
                )
        if errors:
            Check.error("Ukazi\n{0}\n{1}.", statements, ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, "w", encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part.feedback[:]
        yield
        new_feedback = Check.current_part.feedback[len(old_feedback):]
        Check.current_part.feedback = old_feedback
        if new_feedback:
            new_feedback = ["\n    ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}",
                filename,
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part.feedback[:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get("stringio")("\n".join(content) + "\n")
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part.feedback[len(old_feedback):]
        Check.current_part.feedback = old_feedback
        if new_feedback:
            new_feedback = ["\n  ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}",
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error(
                "Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}",
                filename,
                (line_width - 7) * " ",
                "\n  ".join(diff),
            )
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        too_many_read_requests = False
        try:
            exec(expression, global_env)
        except EOFError:
            too_many_read_requests = True
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal and not too_many_read_requests:
            return True
        else:
            if too_many_read_requests:
                Check.error("Program prevečkrat zahteva uporabnikov vnos.")
            if not equal:
                Check.error(
                    "Program izpiše{0}  namesto:\n  {1}",
                    (line_width - 13) * " ",
                    "\n  ".join(diff),
                )
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ["\n"]
        else:
            expected_lines += (actual_len - expected_len) * ["\n"]
        equal = True
        line_width = max(
            len(actual_line.rstrip())
            for actual_line in actual_lines + ["Program izpiše"]
        )
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append(
                "{0} {1} {2}".format(
                    out.ljust(line_width), "|" if out == given else "*", given
                )
            )
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get("update_env", update_env):
            global_env = dict(global_env)
        global_env.update(Check.get("env", env))
        return global_env

    @staticmethod
    def generator(
        expression,
        expected_values,
        should_stop=None,
        further_iter=None,
        clean=None,
        env=None,
        update_env=None,
    ):
        from types import GeneratorType

        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error(
                        "Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                        iteration,
                        expression,
                        actual_value,
                        expected_value,
                    )
                    return False
            for _ in range(Check.get("further_iter", further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get("should_stop", should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        # TODO: update calculating subtask points and stuff
        #if len(subtask_points) != len(Check.parts):
        #    print("Subtask points {} don't match task parts: {}.".format(subtask_points, Check.parts))
        all_valid = True
        for i, part in enumerate(Check.parts):
            if not part.is_valid:
                print("{0}. skupina testov nima veljavne rešitve.".format(i + 1))
                all_valid = False
            else:
                print("{0}. skupina testov ima veljavno rešitev.".format(i + 1))
            for message in part.feedback:
                print("  - {0}".format("\n    ".join(message.splitlines())))
        return all_valid

    settings_stack = [
        {
            "clean": clean.__func__,
            "encoding": None,
            "env": {},
            "further_iter": 0,
            "should_stop": False,
            "stringio": VisibleStringIO,
            "update_env": False,
        }
    ]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs)) if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get("env"))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = Check.VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get("stringio"):
            yield
        else:
            with Check.set(stringio=stringio):
                yield

    @staticmethod
    @contextmanager
    def time_limit(timeout_seconds=1):
        from signal import SIGINT, raise_signal
        from threading import Timer

        def interrupt_main():
            raise_signal(SIGINT)

        timer = Timer(timeout_seconds, interrupt_main)
        timer.start()
        try:
            yield
        except KeyboardInterrupt:
            raise Check.TimeoutError
        finally:
            timer.cancel()


import json
import os
import re
import shutil
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional


class _Tomo_Submit:
    PART_REGEX = re.compile(
        r"# ={20,}+@=\s*\n"  # beginning of header
        r"(:?\s*#(:? [^\n]*)?\n)+?"  # description
        r"\s*# ={20,}\s*?\n"  # end of header
        r"(?P<solution>.*?)"  # solution
        r"(?=\n\s*# ={20,}@=)",  # beginning of next part
        flags=re.DOTALL | re.MULTILINE,
    )

    @staticmethod
    def extract_submission(source: str, n_parts: int) -> list[Check.Part]:
        parts = [
            Check.Part(
                solution=m.group("solution")
            )
            for m in _Tomo_Submit.PART_REGEX.finditer(source)
        ]
        if len(parts) != n_parts:
            raise ValueError("Invalid format.")
        return parts

    @staticmethod
    def submit_parts(url: str, parts: List['Check.Part'], filename: str, session_data: str):
        submitted_parts = []
        submitted_parts = [{
            "solution": part.solution,
            "local_tests_pass": part.is_valid,  # TODO report status (OK/WA/RTE/TLE)
            "remote_test_results": [x[0] for x in part.secret],  # TODO report status (OK/WA/RTE/TLE)
            "feedback": part.feedback,
            } for part in parts
        ]
        payload = {
            "session_data": session_data,
            "parts": submitted_parts,
            "filename": os.path.basename(filename),
        }
        headers = {"content-type": "application/json"}
        data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        return json.loads(response.read().decode("utf-8"))

    @staticmethod
    def backup(filename: str) -> str:
        backup_filename: Optional[str] = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = "{0}.{1}".format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    @staticmethod
    def update_parts(hint_string: str, old_parts: List['Check.Part'], response: Dict[str, Any]):
        for part, feedback in zip(old_parts, response["parts"]):
            part.feedback = feedback["feedback"]
            valid_before = part.is_valid
            part.is_valid = feedback["solved"]
            valid_after = part.is_valid
            if valid_before and not valid_after:
                wa_index = feedback["wa_testcase_idx"]
                hint = part.secret[wa_index][1]
                if hint:
                    part.feedback.append(hint_string.format(hint))






def _tomo_validate_current_file():
    _tomo_user_filename = os.path.abspath(sys.argv[0])
    with open(_tomo_user_filename, 'r', encoding='utf8') as _tomo_user_file:
        _tomo_user_raw_source = _tomo_user_file.read()
    try:
        Check.parts = _Tomo_Submit.extract_submission(_tomo_user_raw_source, 9)
    except ValueError:
        print("Neveljavna oblika datoteke. Ne spreminjaj zadnjega komentarja.")
        exit(1)

    Check.part()
    try:
        Check.equal('je_permutacija([7, 3, 4, 5, 2, 1])', False)
        Check.equal('je_permutacija([7, 3, 4, 5, 2, 6, 1])', True)
        Check.equal('je_permutacija([7, 3, 4, 0, 2, 1])', False)
        Check.equal('je_permutacija([7, 3, 4, 8, 2, 1])', False)
        Check.equal('je_permutacija([2, 3, 4, 5, 2, 1])', False)
        Check.equal('je_permutacija([])', True)
        Check.equal('je_permutacija([1])', True)
        Check.equal('je_permutacija([1, 2])', True)
        Check.equal('je_permutacija([2, 1])', True)
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    Check.part()
    try:
        Check.equal('je_seznam_ciklov([])', True)
        Check.equal('je_seznam_ciklov([[]])', True)
        Check.equal('je_seznam_ciklov([[0]])', False)
        Check.equal('je_seznam_ciklov([[1]])', True)
        Check.equal('je_seznam_ciklov([[2]])', True)
        Check.equal('je_seznam_ciklov([[1,3]])', True)
        Check.equal('je_seznam_ciklov([[3,1]])', True)
        Check.equal('je_seznam_ciklov([[1,3,5,7,4]])', True)
        Check.equal('je_seznam_ciklov([[1,3,5,1,4]])', False)
        Check.equal('je_seznam_ciklov([[8,3,2,4],[5,7,6,1]])', True)
        Check.equal('je_seznam_ciklov([[8,3,4],[5,7,1]])', True)
        Check.equal('je_seznam_ciklov([[8,3,4],[5,7,3,1]])', False)
        Check.equal('je_seznam_ciklov([[8],[7],[1],[3],[6],[4],[2]])', True)
        Check.equal('je_seznam_ciklov([[8],[7],[1],[3],[6],[1],[2]])', False)
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    Check.part()
    try:
        Check.equal('urejeni_cikli([[7, 3], [4], [5, 2, 1]])', [[1, 5, 2], [3, 7]])
        Check.equal('urejeni_cikli([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]])', [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]])
        Check.equal('urejeni_cikli([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]])', [[2, 14, 8], [3, 7, 9, 13, 5], [4, 6, 11, 12], [15, 18]])
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    Check.part()
    try:
        Check.equal('iz_ciklov([[7, 3], [4], [5, 2, 1]])', [5, 1, 7, 4, 2, 6, 3])
        Check.equal('iz_ciklov([[7, 3], [4], [5, 2, 1]], 9)', [5, 1, 7, 4, 2, 6, 3, 8, 9])
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    Check.part()
    try:
        Check.equal('v_cikle([5, 1, 7, 4, 2, 6, 3])', [[1, 5, 2], [3, 7]])
        Check.equal('v_cikle([1, 2, 3, 4, 5, 6, 7])', [])
        Check.equal('v_cikle([7, 6, 5, 4, 3, 2, 1])', [[1, 7], [2, 6], [3, 5]])
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    Check.part()
    try:
        Check.equal('inverz_perm([7, 3, 4, 5, 2, 1, 6])', [6, 5, 2, 3, 4, 7, 1])
        Check.equal('inverz_perm([1, 2, 3, 4, 5, 6, 7])', [1, 2, 3, 4, 5, 6, 7])
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    Check.part()
    try:
        Check.equal('inverz_cikli([[7, 3], [4], [5, 2, 1]])', [[1, 2, 5], [3, 7]])
        Check.equal('inverz_cikli([[10, 7, 3], [4], [5, 2, 1]])', [[1, 2, 5], [3, 7, 10]])
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    Check.part()
    try:
        Check.equal('ciklicni_tip([[7, 3], [4], [5, 2, 1]], 9)', (4, 1, 1))
        Check.equal('ciklicni_tip([[7, 3], [4], [5, 2, 1]])', (2, 1, 1))
        Check.equal('ciklicni_tip([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]])', (0, 7))
        Check.equal('ciklicni_tip([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]], 21)', (7, 7))
        Check.equal('ciklicni_tip([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]])', (4, 1, 1, 1, 1))
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    Check.part()
    try:
        Check.equal('red([[7, 3], [4], [5, 2, 1]])', 6)
        Check.equal('red([[12, 11], [1, 2], [9, 10], [3, 4], [14, 13], [5, 6], [7, 8]])', 2)
        Check.equal('red([[5, 3, 7, 9, 13], [11, 12, 4, 6], [8, 2, 14], [15, 18]])', 60)
        Check.equal('red([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]])', 210)
    except Check.TimeoutError:
        Check.error("Dovoljen čas izvajanja presežen.")
    except Exception:
        Check.error(
            "Testi sprožijo izjemo\n  {0}",
            "\n  ".join(traceback.format_exc().split("\n"))[:-2],
        )

    print("Shranjujem rešitve na strežnik... ", end="")
    try:
        _tomo_url = "https://kokoska.fmf.uni-lj.si/tomo/submit/"
        _tomo_session_data = ""
        _tomo_response = _Tomo_Submit.submit_parts(_tomo_url, Check.parts, _tomo_user_filename, _tomo_session_data)
    except urllib.error.URLError:
        _tomo_error_message = (
            "\n"
            "-------------------------------------------------------------------\n"
            "PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n"
            "Preberite napako in poskusite znova ali se posvetujte z asistentom.\n"
            "-------------------------------------------------------------------\n"
        )
        print(_tomo_error_message)
        traceback.print_exc()
        print(_tomo_error_message)
        sys.exit(0)
    else:
        print("Rešitve so shranjene.")
        if "update" in _tomo_response:
            print("Posodabljam datoteko... ", end="")
            _tomo_backup_filename = _Tomo_Submit.backup(_tomo_user_filename)
            with open(__file__, "wb") as _tomo_f:
                _tomo_f.write(_tomo_response["update"].encode())
            print("Prejšnja datoteka je bila preimenovana v {0}.".format(_tomo_backup_filename))
            print("Če se datoteka ni osvežila v tvojem urejevalniku, jo zapri in ponovno odpri.")
        else:
            _Tomo_Submit.update_parts(Check.i18n_strings['HINT'], Check.parts, _tomo_response)
    Check.summarize()


if __name__ == "__main__":
    _tomo_validate_current_file()
