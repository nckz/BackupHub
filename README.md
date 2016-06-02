# BackupHub
A cron-able script that will mirror all repositories of central git hub
(currently supports GitHub and GitLab).

## Requirements
1. SSH keys deployed to the backup host machine.
2. An API token for the target website.
3. python 3 and git.
    - see the
      [environment.yml](https://github.com/nckz/BackupHub/blob/master/environment.yml)
      for python dependencies

## Crontab
A weekly backup of your GitLab initiated by the cron at 3am each Saturday would
look something like this (assuming BackupHub.py is in your PATH):

```
0 3 * * 6 BackupHub.py --path ~/backup --token <your-gitlab-api-token> --website http://gitlab.com --move-aside --ignore-errors >> ~/backup/BackupHub.log
```

or for GitHub:


```
0 3 * * 6 BackupHub.py --path ~/backup --github --token <your-github-api-token> --move-aside --ignore-errors >> ~/backup/BackupHub.log
```
