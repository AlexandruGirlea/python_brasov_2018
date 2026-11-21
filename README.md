# Python Brașov 2018

Python course materials from Brașov, Romania, delivered in 2018 by Alex Girlea in collaboration with AgileHub. This repository is a historical reference to the course, with 26 notebooks covering Python fundamentals, data analysis, object-oriented programming, and testing.

**English edition:** this branch · **Original Romanian edition:** [romanian](https://github.com/AlexandruGirlea/python_brasov_2018/tree/romanian)

## Course contents

| Module | Topics |
| --- | --- |
| [1 — Python fundamentals](module_1/) | Data types, operators, functions, namespaces, scopes, and homework |
| [2 — Containers and libraries](module_2/) | Collections, dictionaries, mutable and immutable objects, imports, and small scripts |
| [3 — Control flow](module_3/) | Conditions, loops, and iterators |
| [4 — Working with functions](module_4/) | Arguments, scope, return values, recursion, lambdas, and built-ins |
| [5 — Comprehensions and generators](module_5/) | Comprehensions, generators, variable scope, and analysis of historical Romanian lottery draws |
| [6 — Object-oriented Python](module_6/) | Classes, inheritance, properties, decorators, and a custom iterator |
| [7 — Testing applications](module_7/) | Unit tests, fixtures, assertions, and exception testing |

## Browse or run the notebooks

Open any `.ipynb` file on GitHub to read it. To explore locally, the notebooks use Jupyter, NumPy, pandas, and Matplotlib:

```bash
git clone https://github.com/AlexandruGirlea/python_brasov_2018.git
cd python_brasov_2018
python3 -m venv .venv
source .venv/bin/activate
python -m pip install jupyter numpy pandas matplotlib
jupyter notebook
```

The original notebooks used Python 3.5 and 3.7. Some APIs reflect that period, and several examples deliberately raise errors to illustrate a concept. This English edition preserves those lessons and clears saved outputs; it is an archive rather than an updated course for current Python releases. The lottery notebook reads `module_5/lottery_numbers.txt` from its own directory.

To run the standalone testing example from the repository root:

```bash
python -m unittest discover -s module_7/testing
```

## Course photos

- [AgileHub on LinkedIn](https://www.linkedin.com/posts/agilehub_python-it-comunitate-activity-6508984711979757568-NbfW/)
- [AgileHub photo album on Facebook](https://www.facebook.com/agilehub/photos/pcb.1030748847087095/1030748753753771/?type=1&theater)

## Acknowledgments

The course drew on several educational resources, including *Python: Journey from Novice to Expert* by Fabrizio Romano, Dusty Phillips, and other contributors (Packt).
