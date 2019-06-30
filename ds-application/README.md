# 1️⃣ Quake Viewer

You can find the project at [https://quakespect.herokuapp.com/](https://quakespect.herokuapp.com/).

## 5️⃣ Contributors

🚫Add contributor info below, make sure add images and edit the social links for each member. Add to or delete these place-holders as needed

| [Chris Luedtke](https://github.com/chrisluedtke)                                                               | [Danielle Romanoff](https://github.com/)                                        |                                       [Student 3](https://github.com/)                                        |                                       [Shilpa Singh](https://github.com/ssingh1187)                                        |                                       [Student 5](https://github.com/)                                        |
| :-----------------------------------------------------------------------------------------------------------:  | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
| [<img src="https://avatars0.githubusercontent.com/u/20371880?s=400&v=4" width = "200" />](https://github.com/) |                      [<img src="https://avatars0.githubusercontent.com/u/36670930?s=400&u=c63d43b9d073e117fb8ac5c44e3e9dcdbd421eff&v=4" width = "200" />](https://github.com/)                       |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/)                       |                      [<img src="https://user-images.githubusercontent.com/46456911/60288323-cce5bc80-98c8-11e9-9a03-9719acf9c994.jpg" width = "200" />](https://github.com/)                       |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/)                       |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/)                  |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/DanielleRomanoff)             |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Mister-Corn)            |          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/ssingh1187)           |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/wvandolah)             |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/)  | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/danielle-romanoff/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/shilpa-singh-13b37b2b/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) |


![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Typescript](https://img.shields.io/npm/types/typescript.svg?style=flat)
[![Netlify Status](https://api.netlify.com/api/v1/badges/b5c4db1c-b10d-42c3-b157-3746edd9e81d/deploy-status)](netlify link goes in these parenthesis)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

🚫 more info on using badges [here](https://github.com/badges/shields)

## Project Overview


1️⃣ [Trello Board](https://trello.com/b/ATMw5fyp/labs-13-quake-viewer)

1️⃣ [Product Canvas](https://docs.google.com/document/d/1VORgfy4NYIVwX3FbBquFEKgTRFTOAEilD66AOqFRFjY/)

Visualizations of earthquakes by location, magnitude, and depth on a world map. Have the ability to zoom in and scroll over the world map. Statistical information about the data ie. are there correlations between magnitude and depth or any other variables. Average magnitude based on timeline and region.

1️⃣ [Deployed Front End](https://quakespect.herokuapp.com/)

### Tech Stack

Flask (Python web framework)
Folium (leaflet.js Python API)
Heroku hosting

### 2️⃣ Predictions

🚫 Describe your models here

### 2️⃣ Explanatory Variables

-   Explanatory Variable 1
-   Explanatory Variable 2
-   Explanatory Variable 3
-   Explanatory Variable 4
-   Explanatory Variable 5

### Data Sources
🚫  Add to or delete souce links as needed for your project


-   [Source 1] (🚫add link to python notebook here)
-   [Source 2] (🚫add link to python notebook here)
-   [Source 3] (🚫add link to python notebook here)
-   [Source 4] (🚫add link to python notebook here)
-   [Source 5] (🚫add link to python notebook here)

### Python Notebooks

🚫  Add to or delete python notebook links as needed for your project

[Python Notebook 1](🚫add link to python notebook here)

[Python Notebook 2](🚫add link to python notebook here)

[Python Notebook 3](🚫add link to python notebook here)

### 3️⃣ How to connect to the web API

🚫 List directions on how to connect to the API here

### 3️⃣ How to connect to the data API

🚫 List directions on how to connect to the API here

### How to Build Application for Local Development

1. Clone/fork this repo. In the root of the directory, create  virtual environment ([guide](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/))
    ```
    python -m venv env
    ```

2. Activate the environment

    Windows
    ```
    env\Scripts\activate
    ```

    macOS and Linux
    ```
    source env/bin/activate
    ```

3. Install requirements
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    pip install -r requirements_dev.txt
    ```

4. Create a `.env` in the root directory of this repo with the following info. **This file is not version controlled**. This is where we place secret credentials.
    ```
    FLASK_APP=app:APP
    FLASK_ENV="development"
    ```

5. Run the server in development
    ```
    flask run
    ```

6. _Optional:_ Create an ipython kernel to use Jupyter Notebook with this environment. After calling `jupyter notebook`, you'll need to select this kernel in the interface (see [documentation](https://ipython.readthedocs.io/en/stable/install/kernel_install.html)).
    ```
    ipython kernel install --user --name=earthquakes-env
    ```

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](_link to your backend readme here_) for details on the backend of our project.

See [Front End Documentation](_link to your front end readme here_) for details on the front end of our project.