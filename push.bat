git init
git add .
git commit -m "New version"
git remote rm origin
git remote add origin https://github.com/szcarr/Mr.Mine.git
git pull origin master
git push origin master
pause