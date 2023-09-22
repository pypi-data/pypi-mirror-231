# Running in dev-mode
* Create a new Python virtual environment for the template:
```
$ cd template
$ python3 -m venv venv  # create venv
$ . venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```
* Initialize and run the component template frontend:
```
$ cd template/my_component/frontend
$ npm install    # Install npm dependencies
$ npm run start  # Start the Webpack dev server
```
* From a separate terminal, run the template's Streamlit app:
```
$ cd template
$ . venv/bin/activate  # activate the venv you created earlier
$ streamlit run my_component/__init__.py  # run the example
```


# streamlit-custom-component

Streamlit component that allows you to do X

## Installation instructions

```sh
pip install geoflow-capability-search
```

## Usage instructions

```python
import streamlit as st

from my_component import my_component

value = my_component()

st.write(value)
```

Component receives 3 callback functions - make sure to pass it to receive the values from the component

- Search - triggers when search is being performed
- Submit - triggers when user clicks "Suggest" for capabilities
- Details - when user clicks particular capability and request for related terms and description is being fired

## Puslishing
To publish component to pip

make sure to check: 
- __init__.py that the app is pointing to the build file and not localhost
- setup.py that the version is updated
- change _RELEASE variable
- push the lates version to main
- create release in the github
- New pypi release will be created automatically

## Component API

Component has 4 types of action: 
- Search - triggers when search is being performed
- Submit - triggers when user clicks "Suggest" for capabilities
- Details - when user clicks particular capability and request for related terms and description is being fired
- Reset - when user resets the autocomplete value 
