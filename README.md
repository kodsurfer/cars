Code snippets of EO:

```
[args...] > app
  QQ.io.stdout > @
    "Hello, world!\n"
```

Compile it like this (may take a minute or so):

```
eoc link
```

Then, run it:

```
eoc --alone dataize app
```



```
QQ.io.stdout
  "Hello, world!"
```

This code can also be written
in a "horizontal" notation:

```
QQ.io.stdout "Hello, world!"
```

instead of using a plain string `"Hello, world!"`
we may want to create a copy of the object `stdout` with a more complex
argument: a copy of the object `sprintf`:

```
[] > app
  QQ.io.stdout > @
    QQ.txt.sprintf
      "Hello, %s!"
      "Jeffrey"
```

This program
can be written using horizontal notation:

```
+alias org.eolang.io.stdout
+alias org.eolang.txt.sprintf

[] > app
  (stdout (sprintf "Hello, %s!" "Jeffrey")) > @
```

it's possible to define a new abstract object
inside `app` and use it to build the output string:

```
[] > app
  QQ.io.stdout (msg "Jeffrey") > @
  [name] > msg
    QQ.txt.sprintf "Hello, %s!" name > @
```

Now, the object `app` has two "bound" attributes: `@` and `msg`. The attribute
`msg` has an abstract object attached to it, with a single "free" attribute
`name`.

This is how you iterate:

```
[args...] > app
  memory 0 > x
  seq > @
    *
      x.write 2
      while.
        x.lt 6
        [i]
          seq > @
            * 
              QQ.io.stdout
                QQ.txt.sprintf
                  "%d x %d = %d\n"
                  x
                  x
                  x.times x
              x.write
                x.plus 1
    true
```


