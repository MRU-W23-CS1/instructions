# COMP 1501 Instructions Repo
Instructions for assignments and lab exercises will be published in this repository.

## Lab Exercise Submission Summary
Labs are marked pass/fail based on passing a minimum threshold. They are automatically graded through GitHub, but manually updated in D2L each week.

Labs do not need to be submitted separately through D2L - just push your changes and you're done! All lab exercises are due by the last day of classes (April 5, 2023).

## Assignment Submission Summary
Assignment submission requires 4 steps:
1. you **commit** your changes to your local git repository
2. you **push** your changes to GitHub, then
3. you **verify** your changes are now on GitHub, then
4. you **copy/paste** the URL of your GitHub repo into the D2L submission box

## Git and GitHub Summary
Words in `<brackets>` are just placeholders - do not type the `<>`.
### To start an assignment or lab
1. To start your assignment, click on the GitHub Classroom link in D2L and click "accept this assignment". Refresh the page to get your unique assignment URL.
2. Clone the repo to your local computer, either using the graphical interface in VS Code or the `git clone` command on the terminal.

### Working on an assignment or lab
1. Make sure your terminal (Git Bash or VS Code's integrated terminal) **working directory** is the same as your assignment directory.
2. Pull changes from GitHub, just in case.
3. Make edits to your text file(s). Don't forget to save changes!
4. Add/commit/push changes, either from the graphical interface in VS Code or using the following commands:
   1. First, stage the file(s) you want to commit:
        ```
        git add <filename>
        ```
   2. Then, commit all the files with a message describing the changes you made:
        ```
        git commit -m "<message>"
        ```
   3. Push all your commits to GitHub
        ```
        git push
        ```
> You can add/commit/push as many times as you like up until you submit your assignment.

### Final submission: assignments only
1. When you are happy with the state of your code, add/commit/push one last time and go to your assignment repository URL. You can find this from the GitHub homepage after logging in.
2. Double check that the last commit on GitHub is the last one you made on your computer.
3. Copy and paste the assignment repository URL into the D2L assignment text box. This is your signal to your instructor that you are done the assignment. It should look something like:
    ```
    https://github.com/MRU-W23-CS1/assign-####-<github username>
    ```
    > There may be slight variations in how your instructor named your assignment repo

## Troubleshooting
For more details, you can also refer back to the [lab 1](labs/01-intro-to-git.md) instructions.

### Changes aren't showing on GitHub.com
Make sure that you have done all of the following:

 1. **Save the file(s)** from your text editor.
 2. **Stage** the file(s) for committing.
 3. **Commit** the file(s) with a useful message.
 4. **Push** your commits to GitHub.

 If you still aren't seeing your changes on GitHub, make sure that you don't accidentally have multiple copies of your repo on your local computer. It's easy to edit one copy while pushing changes from another.

 And if you **still** still aren't seeing your changes, get in touch with an IA or your instructor.

### git commit opened a weird looking window
If you forget the `-m` flag and just execute the command `git commit`, git will launch a text editor. By default, this is a command-line editor called [vim](https://www.vim.org/). Command line editors are really useful and worth learning, but if you want to go back to where you were, do the following:
- Press `Esc` (escape, top-left corner of your keyboard)
- Type `:q!`. That's colon, lowercase "q", then exclamation mark.
- Press `enter`

### macOS GitHub Token
If you are using a Mac, you will need to generate a "Personal access token" from your GitHub account and then use it instead of your password. [Here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) are GitHub's instructions, and [here's](https://www.youtube.com/watch?v=s-CN4RaNq8A) a video that walks through how to use it with the macOS Keychain Access tool. You'll need to check the "repo" box in Scope settings and set the expiry date for at least the end of the semester so you're not having to constantly regenerate it.

After generating a token you can use it instead of your GitHub password in the terminal. Copying and pasting is a bit odd as it will not actually show the text when you paste into a password prompt.

