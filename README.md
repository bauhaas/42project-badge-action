# 42project-badges-action

This action allows you to generates badges related to your 42 project for your README.md with [shields.io](https://shields.io). 

## Configuration

**/!\\ You don't have to repeat step 1 & 2 for each of your repo project. 3 & 4 are needed steps everytime  /!\\**
1. Head over to [gist.github.com](https://gist.github.com/) and create a new gist. You can name the file `test.json`, but this can be changed later as well. You will need the ID of the gist (this is the long alphanumerical part of its URL) later.
2. Navigate to [github.com/settings/tokens](https://github.com/settings/tokens) and create a new token with the *gist* scope.
3. Go to the *Secrets* page of the settings of your repository and add this token as a new secret. You can give it any name, for example `GIST_SECRET`.
4. Add something like the following to your workflow:
```yml
- name: 42 Project Badges
  uses: Korkrane/42project-badges-action@v1.1.3
  with:
    login: <your-42-login>
    project: <your-42-project>
    auth: ${{ secrets.GIST_SECRET }}
    gistID: <gist-ID>
```

### Required Input Parameters

Parameter | Description
----------|------------
`login` | Your 42 login
`project` | A 42 project name
`auth` | A secret token with the *gist* scope.
`gistID` | The ID of the target gist. Something like `8f6459c2417de7534f64d98360dde866`.

## How Does It Work?

Whenever this action is executed, it creates 3 JSON objects based on the input parameters.
This JSON object may look like this:

```json
{
  "schemaVersion":1,
  "label":"grade",
  "message":"125 / 100",
  "color":"success",
  "style":"flat-square"
}
```

This JSON object is then uploaded as a file to a *gist* ([click here for an example](https://gist.github.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143)) and can be transformed to a badge like [![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_grade.json)](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_grade.json) with the **shields.io/endpoint**. Here is the URL of this example badge:

```
https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_grade.json
```

Once the action is executed, go to your gist.
There should be 3 new file called : `<your-42-project>_grade.json`, `<your-42-project>_bon.json`, `<your-42-project>_corr.json`.

You can view the raw content of this file at `https://gist.githubusercontent.com/<user>/<gist-ID>/raw/<filename>.json`.

Embed the badge with:

```markdown
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/<user>/<gist-ID>/raw/<filename>.json)
```

## Example usage
```yml
# .github/workflows/main.yml
name: 42-project-badges
on:

  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo content
        uses: actions/checkout@v3

      - name: 42 Project Badges
        uses: Korkrane/42project-badges-action@v1.1.3
        with:
          login: bahhas
          project: dr-quine
          auth: ${{ secrets.GIST_SECRET }}
          gistID: e68282bd835f9dab85e2c6b9b5522143
```

## Example badge display 

Project you subscribed to but didn't finish yet :

![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/subscribed_grade.json)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/subscribed_bon.json)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/subscribed_corr.json)

Valid project with bonus:

![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_grade.json)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_bon.json)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_corr.json)

Valid project without bonus:

![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_grade2.json)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/fail_bon.json)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_corr.json)

Failed project:

![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/fail_grade.json)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/fail_bon.json)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Korkrane/e68282bd835f9dab85e2c6b9b5522143/raw/finished_corr.json)

