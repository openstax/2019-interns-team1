# 2019 Intern Team 1

## Team Members
| Name | Role | Email | Slack | GitHub | 
| :---- | :---- | :---- | :---- | :---- |
| Ashley D'Souza | Back End Development | | @Ashley D'Souza |
| Moses Glickman | Business Operations | | @Moses |
| Sean Zhang     | Project Management | shz1@rice.edu | @seanz | @shz12
| Miao Zhang     | Marketing and Communications | | @Miao Zhang
| Yidi Wang      | Content Development | | @Yidi Wang
| Alp Yakici     | Back End Development | bay@rice.edu | @Alp Yakici | @berkalpyakici | |
| Esther Plants  | QA/Software Testing | ejp3@rice.edu | @Esther Plants | @ejp3
| Andy Cheng     | User Experience | amc34@rice.edu | @Andy Cheng | @andy-m-cheng

## Team Ceremonies
- **Every Monday, 11am-12pm at Riggs**
- **Every Wednesday, 1pm-2pm at Damphousse**
- **Remotes:** Join the call in the #team-1 slack channel

## Installation
CMS is built with [Django Framework](https://www.djangoproject.com). All installation instructions assume you already have [Homebrew](http://brew.sh) installed. If you are not running on MacOS or a Linux distribution, see the hyperlinks for dependencies.

## Dependencies
* [Python](https://www.python.org/) (≥ 3.7)
* [PIP](https://github.com/pypa/pip) (≥ 19.0.0)
```bash
brew install python3
```

## Installation
Verify you have Python ≥ 3.7 installed:  
```bash
python --version
python3 --version
```

Now we can install the repository. Run the following commands line by line:

```bash
git clone https://github.com/openstax/2019-interns-team1
cd 2019-interns-team1/cms/
pip3 install -r requirements/dev.txt
```

After all the modules in requirements are installed, run the migration script:

```bash
python3 manage.py migrate
```
Now, create a super user. Run the following command and then proceed with the instructions:

```bash
python3 manage.py createsuperuser
```

Finally, start the server:

```bash
python3 manage.py runserver
```