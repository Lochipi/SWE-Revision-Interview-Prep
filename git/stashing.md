# stashing

### a problem we face
You have made a change... but you need to pull in changes from a remote repo, what do you do?

## `stash`
`git stash` will take every change tracked by git (change to index + change to work tree) and store that result, much like a commit, into the "stash."

## when would you need to use git bash

To quote from the man page

Use git stash when you want to record the current state of the working directory and the index, but want to go back to a clean working directory. The command saves your local modifications away and reverts the working directory to match the HEAD commit.

**Stash** is a STACK of temporary changes


### Operations
You can push your changes into the stack by using

`git stash`

Stashes, much like commits, can come with a message (-m "<your message>")

`git stash -m "my lovely message here"`


### Stashes can be listed out:

`git stash list`
`git stash show [--index <index>]`


### To pop the latest stash:

`git stash pop`


#### To pop a stash at an index:

`git stash pop --index <index>` # works well with git stash list

### Remember
man git-stash is your friend. if you forget how a command works, please review the manual first! Its the authority of how to use the tool
RFM - read the friendly manual
