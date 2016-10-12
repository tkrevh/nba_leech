# NBA Leecher

NBA Leecher is a lightweight application written in Python/Django.
There are no models, just two views:
- index view where users can enter their player first and last name
- playerinfo view, where data about the player is fetched using nba_py
  library and displayed to the user
  
Boostrap framework is used for styling.

## Installation

Fork or download and install.
```
$ pip install -r requirements.txt
```
And then
```
$ manage.py migrate
```

## Usage

Enter the players First and Last name and click Search.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


