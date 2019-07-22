# 2019 Intern Team 1
This repository hosts source files of OpenStax Notes by 2019 Intern Team 1. Please see [work management & contribution guidelines](https://github.com/openstax/2019-interns-team1/blob/master/CONTRIBUTING.md) before contributing to this project.

## Team Members
| Name | Role | Email | Slack | GitHub | 
| :---- | :---- | :---- | :---- | :---- |
| Ashley D'Souza | Back End Development | akd6@rice.edu | @Ashley D'Souza | @ashdza
| Moses Glickman | Business Operations | | @Moses |
| Sean Zhang     | Project Management | shz1@rice.edu | @seanz | @shz12
| Miao Zhang     | Marketing and Communications | | @Miao Zhang
| Yidi Wang      | Content Development | yw73@rice.edu| @Yidi Wang| @Yidi0213
| Alp Yakici     | Back End Development | bay@rice.edu | @Alp Yakici | @berkalpyakici | |
| Esther Plants  | QA/Software Testing | ejp3@rice.edu | @Esther Plants | @ejp3
| Andy Cheng     | User Experience | amc34@rice.edu | @Andy Cheng | @andy-m-cheng

## Team Ceremonies
- **Every Monday, 11am-12pm at Riggs**
- **Every Wednesday, 1pm-2pm at Damphousse**
- **Remotes:** Join the call in the #team-1 slack channel

## About
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

Head to [Google Doc API page](https://developers.google.com/docs/api/quickstart/python) and then click `ENABLE THE GOOGLE DOCS API` button and download the `credentials.json` file and move it to `cms/` directory where `manage.py` is located in.


Finally, start the server:

```bash
python3 manage.py runserver
```

## Admin Panel
After the server is initialized using the commands above, head to `http://localhost:8000` to login to admin panel. Authenticate using the credentials generated using `createsuperuser` command.

## API Endpoints
OpenStax Notes CMS provides a number of API endpoints that allow clients to add/alter/remove data to/from the database.

---

### `GET /api/notes/<id>`
Lists all the notes, ordering by the id DESC. If `<id>` is provided, then shows a single entry of the given id.

### `GET /api/notes/?account=<id>`
Lists all notes created by the specific account.

### `GET /api/notes/?title=<note_title>`
Lists all notes that include `note_title` in their titles.

### `GET /api/notes/?tags=<tag,tag2,tag3>`
Lists all notes that are tagged with either one of `tag`, `tag2`, or `tag3`.

### All these GET parameters can be used together.

---

### `POST /api/notes/`
Creates a new note. The request should include a header titled  `Authorization`, which takes the value `Basic <auth>`, where `<auth>` is basic authentication (such as an encoded form of `username:password` that matches with any account created on admin panel).