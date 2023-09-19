- [ara-tool](#ara-tool)
  - [test and run during development](#test-and-run-during-development)
  - [upload to test pypi](#upload-to-test-pypi)
  - [upload to live pypi](#upload-to-live-pypi)


# ara-tool

## test and run during development
1. run `bash deploy.sh`
2. run `bash login.sh`
3. --> in container --> `bash test-feature.sh`
4. if change is successfull always commit before proceeding with next change
5. if change was successfully reviewd merge in gitlab: https://git.talsen.team/talsen-products/ara-tool/-/merge_requests/new

## upload to test pypi
1. run `bash deploy.sh`
2. run `login.sh`
3. in `setup.py` increment `version` otherwise upload will fail! 
4. from inside container run `python setup.py sdist bdist_wheel`
5. run the following command: 
```bash
twine upload --repository testpypi dist/* --verbose -u __token__ -p pypi-AgENdGVzdC5weXBpLm9yZwIkZGI5YzUyZTUtNDhjMy00NmI3LTgxNmMtY2QwMTRjYjZmZjlmAAIqWzMsImM3ZTM0MDRmLWU1MzUtNDliMi05ZDhiLWQ0NGUyNzlmYTU0MiJdAAAGID-dX7aQZZimTyUQeKPzbP0TlqMEpLQlzRW7VJr1JKab
```

this will upload to a test pypi account
5. run `python3 -m pip install --index-url https://test.pypi.org/simple/ ara_tools`
6. run `ara -h`
7. if everything has worked (upload, installation and usage) you can now continue to upload the package to pypi (live)


## upload to live pypi
1. run `bash deploy.sh`
2. run `login.sh`
3. `dist`should still be there from the testupload, do NOT upload to live without previously testing in test pypi!
4. run the following command: 
```bash
twine upload dist/* --verbose -u __token__ -p pypi-AgEIcHlwaS5vcmcCJGUwODIwYWE0LWVmZGEtNDE3MS04MzQzLWY4NTlkYWZlYTNkZQACKlszLCIwMjI2ZWZjZS05OTFjLTRmNmUtYmVlMS0zMjQ1YTcxN2Q1OTMiXQAABiBCoPI8XrCK6pvwFq8uMvjlotUpagAqlcH7Q40uE2kANQ
``` 