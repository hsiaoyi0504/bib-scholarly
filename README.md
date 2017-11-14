## Bib-Scholarly
A simple wrapper of [scholarly](https://github.com/OrganicIrradiation/scholarly) to search BibTex through almost the same title.

### Usage
* `pip install -r requirements.txt`
* Save the titles of journal articles in `examples.txt`. One article title per line or save them in a different file and change the `with open(...)` line in `retrieve.py` to point to that file.
* Use `python retrieve.py`, then you will get the result in standard output. To save, use redirect operation in shell `python retrieve.py > ref.bib`
* Sample command: `python retrieve.py` will generate following sample output: 
```
@article{czodrowski2013herg,
  title={hERG me out},
  author={Czodrowski, Paul},
  journal={Journal of chemical information and modeling},
  volume={53},
  number={9},
  pages={2240--2251},
  year={2013},
  publisher={ACS Publications}
}

@article{pires2015pkcsm,
  title={pkCSM: predicting small-molecule pharmacokinetic and toxicity properties using graph-based signatures},
  author={Pires, Douglas EV and Blundell, Tom L and Ascher, David B},
  journal={Journal of medicinal chemistry},
  volume={58},
  number={9},
  pages={4066--4072},
  year={2015},
  publisher={ACS Publications}
}

@article{daina2017swissadme,
  title={SwissADME: a free web tool to evaluate pharmacokinetics, drug-likeness and medicinal chemistry friendliness of small molecules},
  author={Daina, Antoine and Michielin, Olivier and Zoete, Vincent},
  journal={Scientific Reports},
  volume={7},
  pages={42717},
  year={2017},
  publisher={Nature Publishing Group}
}
```
