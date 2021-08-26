# Shell

## Intro

A shell is an interpreter / purely text-based user interface for managing your computer.

There are several different kinds of shells, but the most ubiquitous is Bash. In this series, we will use Bash \(or something similar\) to interface with our machine.

## Setup

* [ ] Open the terminal / command line application on your machine.

{% hint style="warning" %}
The above instruction is very system-specific and subject to change. As an EECS learner, it is important to feel comfortable using the web to fill in gaps in your understanding. I suggest entering "how to open a Bash shell in &lt;my\_os&gt;" into your favorite search engine. \("os" is short for operating system. Examples of these include MacOS, Windows, and Linux distributions such as Ubuntu.\)
{% endhint %}

## Conventions

When discussing shell code, there are general conventions people use to avoid confusion. One of them, which you will probably dislike, \(because it makes copy-pasting code from the internet a pain\), is to prefix all shell commands with a `$`symbol, and all additional lines of input with a `>` symbol. This is useful because it helps delineate the difference between typed lines of input and expected output. In the example below, only the first line is a shell command. The second is the expected output.

```text
$ echo "When copying this command to your computer, remove the $."
When copying this command to your computer, remove the $.
```

{% hint style="info" %}
Later we will discuss the usefulness of `$` and `>` within shell commands. Do not mistake these with the starts and continuations of user input.
{% endhint %}

There are several different conventions for denoting a location where the user must enter information pertaining to their own environment or use-case. I will use `<description>` to denote a field that needs to be entered by the user. 

For instance, the `echo` command can be used to 'echo' input text to standard output. By default, standard output is displayed to the console user. Using quotes is optional \(though I prefer to use them, because it is more explicit about the bounds of the text\).

```text
$ echo <text>
<text>

$ echo "<text>"
<text>
```

## Shell Environment

The shell is not too different from an interpreter for any other language. In the reference manual's own words, "A Unix shell is both a command interpreter and a programming language." \(@source [Bash Reference Manual](https://www.gnu.org/software/bash/manual/bash.html#What-is-a-shell_003f)\)

At any given point in time, your command line has a mapping from variable names to values stored in its environment. These environment variables guide how the command line will respond to your input.

For instance, your HOME environment variable points to your home directory. This directory typically contains personal information like Documents, Downloads, and application data.

```text
$ echo HOME
```

Well that wasn't too useful. Lets indicate to our shell that we want to treat HOME as a variable and replace it with its value by using a `$` symbol.

```text
$ echo $HOME
```

That's better. Our shell just told us the filepath of our home directory. Let's use the `ls` command to print out the files in our home directory. `~` is shorthand for `$HOME`.

```text
$ ls ~
```

You can temporarily reset your home environment variable by directly setting it to a different folder. Any directory will do, but let's see what happens if we set our home directory to the binaries folder on our computer. On systems where this folder is present, it usually contains shell-related programs.

```text
$ HOME=/bin
```

Go ahead and retry the `ls` command again. You will see that the state has changed, resulting in a new set of filenames. You may be able to spot the `ls` program itself.

```text
$ ls ~
```

