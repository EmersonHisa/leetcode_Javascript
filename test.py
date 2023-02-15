import os

def makeCommits (days):
    if days < 1:
        os.system('git push')
    else:
        dates = f"{days} days ago"
        with open('data.txt', 'a') as file:
            file.write(f'{dates} <- this was today')

    os.system('git add data.txt');
    os.system('git commit --date="' + dates + '"-m "First commit"')
    return days * makeCommits(days - 1);

makeCommits(1);