# vininfo contributing

## Submit issues

If you spotted something weird in application behavior or want to propose a feature you are welcome.


## Write code

If you are eager to participate in application development and to work on an existing issue (whether it should
be a bugfix or a feature implementation), fork, write code, and make a pull request right from the forked project page.

When contributing code, follow the rules from [IDLE.md](https://github.com/idlesign/vininfo/blob/master/IDLE.md).

## Project workflow

The development tasks are provided by [makeapp](https://pypi.org/project/makeapp/). Install or update it first:

```shell
$ uv tool install makeapp
# or: uv tool upgrade makeapp
```

Then, from the project directory:

```shell
$ ma tools
$ ma up

# Check code style and run tests before your pull request:
$ ma style
$ ma tests
```


## Spread the word

If you have some tips and tricks or any other words that you think might be of interest for the others — publish it
wherever you find convenient.


See also: https://github.com/idlesign/vininfo
