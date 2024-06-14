# requestSCIHUB
批量下载工具
# testofliearn
echo "# testofliearn" >> README.md
#创建文件
git init
#创建git环境
git add README.md
#把文件同步到git，如果同步所有则 git add .
git commit -m "first commit"
#好，我接下来要改了
#填写git日志git commit -m "first commit" 是 Git 的一条常用命令，以下是每个部分的含义：
git commit: 这个命令是用来将你的更改提交到本地的 Git 仓库。在这之前，你应该已经使用 git add 命令将你想要提交的更改添加到了暂存区。
-m: 这是 --message 的简写，这个参数的作用是让你能够在命令行里直接输入你的提交信息，省略了会弹出编辑器让你写提交信息的步骤。
"first commit": 这是你的提交信息。提交信息是一个简短的描述，用来解释这次提交做了什么更改。在这个例子中，“first commit”通常是你第一次提交时的信息。
所以，整体来看，git commit -m "first commit" 的意思就是，将你已经添加到暂存区的更改提交到本地仓库，并附带了一个叫做 "first commit" 的提交信息。
git branch -M main
#分枝
git remote add origin https://github.com/FlypigW/testofliearn.git
#git remote add: 该命令用于在本地 Git 仓库中添加一个新的远程仓库。
#origin https://github.com/FlypigW/testofliearn.git: 这里的 origin 是给这个远程仓库的一个别名，方便以后的使用。（就是这个网页给他命名称了origin）
#而 https://github.com/FlypigW/testofliearn.git 则是这个远程仓库的 URL，也就是那个仓库的位置。
#进行这个操作之后，你就可以使用 git push origin master 这样的命令，来将你的本地更改推送到这个远程仓库中。
git push -u origin main
##git push: 这个命令的主要功能是将本地仓库的更改推送到远程仓库中。
-u：这是 --set-upstream 的简写。如果你希望在下次提交修改时记住你所用的远程名和分支名，可以在 push 的时候加上 -u 或者 --set-upstream 。这样在下次 git push 或者 git pull 时，就可以省略远程名和分支名了。可以说，这个参数主要的作用就是记住推送的地址和分支，方便下次直接使用 git push 或者 git pull。
origin: 这是远程仓库的别名，在你执行 git remote add origin [url] 时，你就已经定义了一个叫做 origin 的远程仓库别名。
main: 这是你想要推送的本地分支的名字。通常在最近的版本中，默认的分支名是 main。在早期版本中，默认的分支名是 master。
所以，整体来看，git push -u origin main 的意思就是，将本地的 main 分支推送到别名为 origin 的远程仓库，并记住这次的推送，以方便以后可以直接使用 git push 这条命令。

https://gitee.com/wht1275930132/paper-crawler.git

我现在改了第一次
 https://github.com/FlypigW/requestSCIHUB.git