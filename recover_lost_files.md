# Git got your back. How to recover accidentally deleted files

## Intro
To begin with, git is a tool and it is essential for every developer working with a team. Being good at it feels really awesome and can get your work done easily when working with a team on the same project.

You might find yourself accidentally deleting a branch containing a file or maybe a folder containing files you've been working on. Yes the chances of encoutering this is minimal but when you do, in this guide, I have demonstrated all the scenarios of recovering it - manually and using **`cherry pick`**.

**Prerequisites:** you probably know git by this time, so no need to go into it. If yes you dont know much about git please [check out my other intro to git on medium](https://medium.com/@corneliuslochipi/a-comprehensive-guide-to-github-for-data-scientists-38a7a3f89c86) for a clue, basic terminal commands. Otherwise, let's get into it. 
   
### Terms - commands
We will start by defining some commands here. 
 `git reflog`
The git [reflog]((https://git-scm.com/docs/git-cherry-pick)) command is used by Git to record updates made to the tips of branches. It allows you to return to commits even to the ones that are not referenced by any branch or any tag. After rewriting history, the reflog includes information about the previous state of branches and makes it possible to go back to that state if needed. It is important to note it, this would come into play at the later stage. 
`git reflog <number>` 
    <image of doing reflog>
    You can have it followed by the number(optional) to give you how many you want it to show in the front and tail,  `git reflog -5` and `git reflog --tail -3`
    You can check out more about it (here)[https://www.w3docs.com/learn-git/git-reflog.html]

## The Danger Zone: Accidental Deletion
Now, let's get hands on. 
Create a repo initialize it `git init` and have some files in it, let's have 2 the `readme.md`, `contributing.md`. 
Make a directory using this command `mkdir git-practice` and cd into it using `cd <folder_name>`. Create the two files in here.You can then add some texts in the files.
// image of showing files. files_ls.png

Moving forward, let’s add the files to the staging area and commit them. Use the commands `git add .` and `git commit -m 'first commit'`.
As stated earlier, we might work with a team and would want to contribute. Therefore, we need to create a branch where we can make our contributions. You can do this by running the following command from the main branch (it might be different on your end - my branch is named ‘trunk’): `git checkout -b contribute`. This command creates a new branch name **contribution** (if we don’t already have one) and switches to it.
<contribution branch image>


let;s make some changes to the changes to the files, you can edit any of the file. You can run this command to add some text to the contributing file. 
`echo echo 'this is my first message' >> contributing.md` or you can edit it manually, whichever way you like. 
When you check the status you would see that you've modified the file. Add and commit it. 
<updated_contributing.png>

Now let's delete it. We assume that we may delete the branch accidentaly by the command. 
`git branch -D contribing` but first checkout to the your main branch - in my case `trunk`.
<delete a branch image>

if you check the branch you'll find you only have one. 
<check branch img>

#### Now what? 

Your hard work of contribting has gone that way? you've completely deleted your branch. If you check the histroy you wont find it. How can we recover it? well we have 2 ways we can do it.

**a)** **first** - **Manual revovery: the first line of defence**
 We can use reflog to recover our lost data. We can reflog the last 3 histroy commits we made. Run the following command 
    ` git reflog -3` 
   <reflog check image>.

You can see our history and our changes. We see our last commit - `updated contributing file`

Now that we have the 'sha' - **1e3b6f3**. 
With that, we can rebuild the whole repo just from this little tiny sha.

run this command: `git cat-file -p 1e3b6f3`
<image sha contribuing reco>

When you run the above command,you can see it is right here with us. This means that even if we deleted a branch it doesn't mean we deleted what we've changed. Our files are in the computer. And so we can retrieve it from git. 


**b)** **second step** - go into the tree. You can see earlier we have tree, parent, author ... in the reflog of our 'sha' info. 

to check the tree run 
 ` git cat-file -p 5de65aae286245ce2e8f2e011d717fcf52652b7f `

<tree img>
 we can see our blob file, contributing.md.

then if we then cat-file it - ` git cat-file -p 8183366bba8da4a7cdcfd39b29bd53b11ce50ed1 `
we can see what we wrote/updated in earlier.
<catfile contribute img>

<!-- we can take this and cat out in a file. -->
**Optional**: You can cat it out into a different file and save it there. that's it. You can do the same with files that you created differently and cat it out the changes. 

##### You're now getting a promotion. Let's keep going.

That seems hard go by? well we have a quicker and easier way to doing it. This might be your first time hearing it, if not well let's get along, it is by using the **Cherry-pick**.

## Advanced Recovery: Using Git Cherry-Pick
remember we have a our 'sha' earlier and how to get it, right? 1e3b6f3. And if I would need this changes to my 'trunk' branch I would just merge it using the same sha by running:
 `git merge 1e3b6f3`
  <merge sha to trunc> 
  
Look at that, we have our changes we made on contributing branch to our trunk branch.We could just bring it in. This is super easy yeah? we didnt have to do the magical-hacker thing we did earlier right? yaayyy!!

hint: Your commit's sha is a key piece of information

You might think this ends here, **NO**, this doesnt end here, we may have some problems with merge - If histories have diverged far enough, this could cause some problems as you wouldn't just be merging the one commit, but all the commits in betwixt 1e3b6f3 and trunk.

To solve that is much even easier with **cherry pick.** Given one or more existing commits, apply the change each one introduces, recording a new commit for each. This requires your working tree to be clean(no modifications from the HEAD commit).

You can learn a bit from it by running the man's thingy ` man git-cherry-pick `. Cherry pick allows you to take just one or more commits, specifically. Maybe at any time you just have that change and dont want to merge it, you can cherry pick it in. It works with remotes - as long as you're up to date with it and you can cherry pick it in if you need to. 

## This time you can do it;
well the ball this time is on you, if didnt merge the above changes, you can cherry pick it by running the following command.
**git cherry-pick <your-sha>**   `git cherry-pick 1e3b6f3`. 
And that's it, you will merge right in. Fantastic. 

## Last word

Accidentally deleting files in Git can be stressful, but Git offers ways to recover them. You can use `git reflog` to find lost commits and manually restore them, or you can use `git cherry-pick` to bring back specific changes with ease. Understanding these tools gives developers peace of mind, ensuring their work is always retrievable even in the face of mistakes.

## References
- Git Documentation: [git reflog](https://git-scm.com/docs/git-reflog)
- Git Documentation: [git cherry-pick](https://git-scm.com/docs/git-cherry-pick)

##### last words
If you found this guide helpful, feel free to connect with me on Twitter at EmaseLC or on LinkedIn at Cornelius Emase. Your feedback and support mean the world to me. Leave a star ⭐
