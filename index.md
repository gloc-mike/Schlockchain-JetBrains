# Schlockchain Homepage

Welcome to the future.

```{toctree}
:maxdepth: 2
:caption: "Table of Contents:"

posts/first_post
api
first
second
some/folder/index
Custom "About Us" Page Title <about_us>
```

## Some examples

### This is to fix heading errors :)

#### Referencing the `role` called `logo-target`.
The Python Logo is at {ref}`logo-target`.

#### Referencing the `role` called `logo-target` but using MyST extended syntax.
The Python Logo is at {ref}`the Python logo on the about us page<logo-target>`.

Use the `:glob:` option plus `*` in the `toctree` if not caring for the order of the pages and for the convenience of not having to add new pages to the ToC whenever they are added to the project.

More information about Schlockchain is available in [Custom About Us Link Text](about_us).

Again, more information about Schlockchain is available in [](about_us) but this time the link text is sourced from the 'About Us' page itself.

#### Linking to a custom role called `investors` on the 'About Us' page.
You can also visit our {ref}`investors`. ☺️

Testing auto-generated link test - linking to [](./about_us.md#quoted-text). 
