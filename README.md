## Bib-Scholarly
A simple wrapper of [scholarly](https://github.com/OrganicIrradiation/scholarly) to search BibTex through almost the same title.

### Usage
* `pip install -r requirements.txt`
* Save the titles of journal articles in `examples.txt`. One article title per line or save them in a different file and change the `with open(...)` line in `retrieve.py` to point to that file.
* Use `python retrieve.py`, then you will get the result in standard output. To save, use redirect operation in shell `python retrieve.py > ref.bib`