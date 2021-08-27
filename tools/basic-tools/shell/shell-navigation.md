# Shell Navigation

## Current Working Directory \(cwd\)

Similar to a graphical file explorer on a computer, a shell has a concept of a current folder. This is referred to as the current working directory \(cwd\).

The `PWD` environment variable holds the filepath of the cwd. Using the `cd` command updates this variable. However, changing this manually \(via assignment\) is undefined behavior \(TODO: ADD LINK\).

Filepaths that begin with a `/` are called 'absolute paths'. These filepaths include the entire directory ancestry of the path starting from the root directory \(`/`\). The root directory contains every user-exposed file on your computer. 

For example, the following command will attempt to execute the program located at `/bin/ls` on my computer, successfully executing `ls`. \[Note: The location of the `ls` program may differ on different machines.\]

```text
$ /bin/ls
```

Paths that do not explicitly start from the root directory \(`/`\) are called 'relative paths', and are interpreted as starting from your cwd. 

For example, the following command will attempt to change the cwd to `$PWD/local-path` where `$PWD` is the cwd.

```text
$ cd local-path
```

## Local Directory References

Two additional directory references exist in every directory, 

1. `.` the directory itself
2. `..` the parent directory. 

You can see these references using `ls -a`, which lists all of the file and folder references in the cwd, even the 'hidden' ones. Hidden files and directories start with a `.` and usually contain meta-data.

The following statement changes the cwd to itself \(so PWD is unchanged\).

```text
$ cd .
```

The following statement changes the cwd to its parent.

```text
$ cd ..
```

All of the following `cd` commands resolve to the cwd itself \(so PWD is unchanged\).

```text
$ cd <local_folder>/./..
$ cd ./<local_folder>/..
$ cd ../<this_folder>
```

{% hint style="info" %}
Even `/` has a parent \(`..`\) reference. What would be a reasonable value for it to take on? Once you have finished reading this page, go ahead and check.
{% endhint %}

## Executing Outside of PATH

If you had some executable in your cwd, you may be tempted to say that you can directly execute it using `<executable_name>` because the name lookup will find the executable using its relative path. However, this will not work in a Bash shell.

The proper way to run an executable that is not located in a directory from your PATH environment variable is to explicitly provide an absolute or relative path \(as opposed to just a filename\). You could execute a file from your cwd using the following.

```text
$ ./<executable_name>
```

{% hint style="info" %}
### Design Discussion

Disabling local-path execution by default and making it 'opt-in' prevents some possible user mistakes and security problems. 

Lets consider a case where local-path execution is enabled by default. A user has two versions of the application `python`, and they almost always intend to use a certain version \(version A\). To facilitate this, they set their `PATH` variable to include just version A. In this case, executing `python` will generally work. 

However, if they happen to be in the directory that contains `python` version B, they might accidentally execute it instead. More problematically, a malicious entity might place a rogue version of `python`, version C, in a directory where they know `python` will be used, allowing them to execute arbitrary malicious code on the user's machine.
{% endhint %}

## Shell Commands

The shell offers a few builtin commands that are helpful for navigating the filesystem.

`pwd` : outputs \(**P**rints\) the filepath of the current **W**orking **D**irectory

```text
$ pwd
```

`ls` : outputs \(**L**i**S**ts\) the contents of the cwd

```text
$ ls
```

`cd <filepath>` : **C**hanges the current working **D**irectory to the specified path

```text
$ cd <filepath>
```

