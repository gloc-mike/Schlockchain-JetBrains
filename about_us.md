%--- Commented out to test global version
%title: Welcome to the Site
%substitutions:
%    snippet: "I'm a **substitution**"
%---

# About Us

Let's see the `snippet`: {{ snippet }}

We are Schlockchain, thought leaders in innovation.

## Bold & Italics

We are **bold** and *innovative*.

## Inline & Block Code

Our `def mega_chain` function works really well:

    def mega_chain():
        return

## Quoted Text

Investors say the best things about us:

> I'm so glad I put my life savings in Schlockchain.
> > Said nobody ever!!
> > > Me included! :)

## Unordered & Ordered Lists

We have a patented algorithm:
- Glacially slow
- Which melts glaciers

... and a roadmap to success:

1. Start an LLC
2. Get a Series A investment round
3. Get a Series B investment round
4. Continue

## Links

Schlockchain is written in [Python](https://www.python.org/) for some data science or something reasons.

For a sexy carousel of stock photos, visit this site's [homepage](./index).

For a sexy carousel of stock photos, visit [](./index).

## CommonMark Headings

### Investors

Our investors are very proud to be involved with us.

### Redacted

Upon advice of counsel.

### Redacted

Upon advice of counsel.

## Images

### Image from a URL

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

### Locally Served Images

![Local Python Logo](python-logo.png)

#### Local Image But Using MyST (bigger, centred plus CSS class applied)
```{image} python-logo.png
:alt: Python Logo
:class: bg-primary
:width: 400px
:align: center
```

#### A MyST Figure (add `myst_enable_extensions` to `conf.py`)
This uses a MyST extension plus raw HTML i.e. an \<img\> tag
:::{figure-md} logo-target
:class: myclass

<img src="python-logo.png" alt="Python Logo" class="bg-primary" width="400px">

Python comes from the *Python Software Foundation*.
:::

## Notes, Warnings, and Other Admonitions

### A note about Python
```{note}
Schlockchain is written in [Python](https://www.python.org/) for some data science or somehting reasons.
```

### A warning about Python
```{warning} Awesomeness Warning

Schlockchain is written in [Python](https://www.python.org/) for some data science or something reasons.

- Careful, Python is *AWESOME* ✨🍰✨
- Using it will thus make you *AWESOME* 😎
```

### A warning about Python but using MyST extended syntax
:::{warning} Awesomeness Warning

Schlockchain is written in [Python](https://www.python.org/) for some data science or something reasons.

- Careful, Python is *AWESOME* ✨🍰✨
- Using it will thus make you *AWESOME* 😎
:::

## Downloads

### Using MyST inline syntax
You can download the *Python logo* {download}`python-logo.png` for offline use.

### Using MyST inline syntax but with alt link text
You can {download}`download the Python logo <python-logo.png>` for offline use.

## Headings and Roles
Here is a way to link to a specific part of a document using Sphinx 'roles' e.g. \(link_target\)=

(investors)=
### Investors

Our investors are very proud to be involved with us.

## Code Blocks

Some Python code (default Pygments)
```
def hello(name):
   return f'Hello {name}'
```

Some Javascript code
```javascript
 function hello(msg) {return `Hello ${msg}`}
```

Some more Javascript code
```{code-block} javascript
 function hello(msg) {
   return `Hello ${msg}`
 }
```

Javascript with line numbers
```{code-block} javascript
:linenos:
 function hello(msg) {
   return `Hello ${msg}`
 }
```

A literal include of a python file
```{literalinclude} src/my_demo.py
```

A literal include of a python file highlighting 2 lines
```{literalinclude} src/my_demo.py
:emphasize-lines: 2-3
```

A literal include of a python file start-after
```{literalinclude} src/my_demo.py
:start-after: __init__
```

A literal include of a python file end-before
```{literalinclude} src/my_demo.py
:end-before: def hello
```

## Referencing Symbols in Docs
As we can see in [our Python class](pauls_demo.MyDemo), Python is fun!

### As above but this time using 'python domain' prefix
As we can see in {py:class}`src.pauls_demo.MyDemo`, Python is fun!

### Again, with our own link text
As we can see in {py:class}`HW <src.pauls_demo.MyDemo>`, Python is fun!

## Intersphinx Linking

The LONG URL way

Let's talk about the power of [Sphinx roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role).

Link to a document

Let's talk about the power of [Sphinx roles](sphinx:usage/restructuredtext/roles).

Link using a role ref

Let's talk about the power of [Sphinx roles](sphinx:ref-role).

Same again but with auto link text i.e. `[]`

Let's talk about the power of [](sphinx:ref-role).

### Linking to Domains

Let's talk about the power of {rst:dir}`code-block`.

% Use % to comment out markdown
% :::{note}
% This text is **standard** _Markdown_
% :::

## ASCIINEMA Cast

Here is the player (I hope)!

<asciinema-player 
    src="_static/casts/npm_jshint_install.cast"
    preload=true
    cols=80
    rows=10
    start-at=6
    speed=3
    poster="data:text/plain,\x1B[20C☺️ My Poster Test ☺️\x1B[\x0D\x0A\x1b[3B\x1B[18CClick to play when ready!\x1B[\x0D\x1B[1B\x1B[17CI'm regular \x1b[1;32mI'm bold green"
    font-size=medium
    title="My ASCIINEMA Cast Title for Full Screen Mode"
    author="Michael B"
    author-url=https://gloc-mike.github.io/
    author-img-url=_static/logo/archer_small_405.png
    >
</asciinema-player>

Second one

<asciinema-player 
    src="_static/casts/npm_jshint_install.cast"
    preload="true"
    cols=80
    rows=10
    start-at=6
    speed=3
    loop="loop"
    poster="data:text/plain,\e[5;5HAwesome \e[1;33mdemo!"
    font-size="medium"
    title="My ASCIINEMA Cast Title for Full Screen Mode"
    author="Michael B"
    author-url=https://gloc-mike.github.io/
    author-img-url=_static/logo/archer_small_405.png
    >
</asciinema-player>

Third one in monokai theme

<asciinema-player 
    src="_static/casts/npm_jshint_install.cast"
    preload="true"
    cols=80
    rows=10
    autoplay="true"
    start-at=0
    speed=5
    font-size="large"
    theme="monokai"
    >
</asciinema-player>

Fourth one in monokai theme

<asciinema-player 
    src="_static/casts/npm_jshint_install.cast"
    preload="true"
    cols=80
    rows=10
    start-at=0
    speed=5
    font-size="large"
    theme="monokai"
    poster="npt:2:34"    
    >
</asciinema-player>

Fifth one attempted edit

<asciinema-player 
    src="_static/casts/try_to_edit_it.cast"
    preload="true"
    cols=80
    rows=10
    start-at=0
    speed=5
    font-size="large"
    >
</asciinema-player>

End player
