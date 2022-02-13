# bodh

**bodh** stands for Binary Octal Decimal Hexadecimal...

It is very simple to use: invoke the command with any number as its (only) argument (*), and it displays it in the 4 formats aforementioned.

(*) If the number is not decimal write it with the proper prefix convention that **bodh** follows: `0b` for binary, `0o` for octal, `0x` for hexadecimal).

*Incise (for beginners! skip it otherwise)*

To use it, simply download and extract, or clone, this repo:

```bash
git clone git@github.com:idealtitude/bodh.git
```

Check that `bodh.py` has the adequate permissions to be executed. Then, you can also copy/move/link it in your `~/bin` or `~/.local/bin` directory (1):

```bash
mkdir -p ~/bin
cp /path/to/bodh.py ~/bin/bodh
chmod 755 ~/bin/bodh
source ~/.bashrc # see note #1 below
```

**Examples**

Do `bodh 547`, and it will output the following:

  bin:	0b1000100011
  oct:	0o0000001043
  dec:	0d0000000547
  hex:	0x0000000223

Or `bodh 0x223`, `bodh 0b1000100011`, `bodh 0o1043` (same output for the three of them because it's the same number, 547).

Other than that, **bodh** is internally uselessly convoluted and I should rewrite it from scratch in a clean, efficient, and pythonic way (this third adjective is indeed a pleonasm in view of the [infamous pep 8](https://www.python.org/dev/peps/pep-0008/ "PEP 8 -- Style Guide for Python Code") (2)).
Nevertheless it's pretty fast on my machine:

```bash
time bodh 0xffffffffffffffff
bin:	0b1111111111111111111111111111111111111111111111111111111111111111
oct:	0o0000000000000000000000000000000000000000001777777777777777777777
dec:	0d0000000000000000000000000000000000000000000018446744073709551615
hex:	0x000000000000000000000000000000000000000000000000ffffffffffffffff

real	0m0,069s
user	0m0,054s
sys	0m0,012s
```

I had fun to write it, even if I almost got lost from time to time while doing it (I didn't plan it enough beforehand); if you find it useful and enjoyable, it will be an additional gratification for me!

**N.B.**

Incidentally, [“bodh”](https://translate.google.fr/?sl=auto&tl=en&text=%E0%A6%AC%E0%A7%8B%E0%A6%A7&op=translate "Google translation of the word 'bodh'") in Bengali means "feeling" (3).

*Incise:* For my projects I often try to use a name of which the acronym can be a word in other languages.

---

#### Notes

**(1)** How to create a `bin` directory in your `$HOME` directory and add it to your `$PATH`:

*1.1*

```bash
nano ~/.bashr
```

*1.2*

Write the following in your `.bashrc`:

```bash
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH
```

*1.3*

Write the content and exit nano; then do `source ~/.bashrc`, and that's it, you can now invoke `bodh` from your terminal (type `bodh -h` or `bodh --help` to see the help message).

**(2)** ”Style Guide for Python Code”

**(3)** spelling of “bodh”: *বোধ*
