import os , random
import string


for i in range(175):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('test.txt','a') as file:
        file.write(d+'\n')
    def get_random_word(word):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(5))
    os.system('git add test.txt')
    os.system('git commit -m ')  # This command records or snapshots the file permanently in git with a message
    os.system('git commit --date=" 2020-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')

#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600" 
#git fetch origin master
#git rebase origin/master