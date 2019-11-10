# Lisbon Subway Scrapper

This is a scrip that download the current information from the Lisbon Subway API page.

## Installation

Just clone the repo.

```
git clone https://github.com/plapa/lx_subway_scrapper.git
```

## Usage

One can simply execute the script: 

```
python main.py
```

This willl create  a `data.csv` file with information corresponding to the four lines in the current moment.

### Using a cron job
To make the data retrieval more reliable I recommend setting up a cron job, that periodically runs the script and saves the data.

In the console run:
```
crontatab -e
```
This will open a text file where you can set up your cronjobs.

To run the script in a 10 minute interval just add this line to the end of the file: 

```
*/10 * * * * python3 /home/pi/lx_subway_scrapper/main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)