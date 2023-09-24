# A simple wrapper for fuff fuzzer in python

## Install!

```bash
pip install pyfuf
```

or 

```bash
git clone git@github.com:0xleft/pyfuf.git
cd pyfuf
pip install .
```

## Usage

There is a good example in (example.py)[example.py]

```python
# import
import pyfuf

# command builder
args = pyfuf.FuffCommandBuilder(starting_dir="/FUZZ.php")
args.set_url("http://localhost")
args.set_wordlist("wordlist.txt")

# start fuzzing
pyfuf.fuzz(args, lambda x: print(pyfuf.parse_finding_line(x)))
```

# TODO

- Add tests
- Add docs
- Make codebase cleaner