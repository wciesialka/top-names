# top-names

Program to scrape from the most common first names (male and female) in the United States from the decades 1880s-2010s.
Data provided by the Social Security Admnistration.
If you do not want to run the program, you can view the results as of October 1st, 2021 in [output.txt](output.txt).

## Running

Program can be ran using `python main.py`. Optional command line arguments include:

```
--output, -o OUTPUT
    Output destination. Expects a file in text write mode. Defaults to sys.stdout.
--verbose, -v
    Optional flag to print verbose output.
```

## Requirements

Project built with Python 3.8.10.
For modules, please read [requirements.txt](requirements.txt).

## Data Source

Data scraped from the [United States Social Security Administration](https://www.ssa.gov/) through their [Popular Baby Names by Decade](https://www.ssa.gov/oact/babynames/decades/) form.

## Authors

- Will Ciesialka

## License

This project is licensed under the MIT License. For more details, please see [LICENSE](LICENSE).