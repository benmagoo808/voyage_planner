# voyage_planner

This is a program to automate some of the voyage planning tasks normally 
associated with a voyage through the inside passage to Alaska from Seattle. It
takes the input cruising speed of a vessel, estimated time of 
departure, and intended routing. It then determines estimated time of arrival
 at each way point and calculates tide 
windows for Seymour Narrows, Current information at each way point and 
pertinent weather data.

## Project Background

While this project should be a functional tool when complete, it's main 
purpose is to refresh and expand the python programming knowledge of it's 
author. Goals for this project include:

1. Create a functional piece of software
2. Utilize a GUI or web front end for ease of use
3. Utilize data found online in whatever format it is available
4. Do the above in a manner which is smart, but uses libraries and methods 
the author is unfamiliar with.

### Project Notes
- Canada does not offer tide or current predictions through a reliable API or
 as a usable format of annual predictions. Options for acquiring the data 
 include: Scraping the website and saving the data in a usable format. 
 Extracting the data from the PDF version which may be downloaded, which is 
 in a standard format for tide and current tables, but is not easily machine 
 readable. Access through a paid third party provider.
 
 I am opting to scrape the data from the website as it seems the most 
 practical solution and good practice for something I do not have experience in.
 
- The US offers many different API options for weather data, and tide 
predictions, but not current predictions which are really the more important 
variable. These are easily downloadable in XML or CSV format.

I have opted to utilize the csv format for this project, which is then how I 
intend to save the Canada data, for reusable code.

- I have opted to use classes as data containers for the voyage and way point 
data. This is as opposed to a nested dictionary format. 
Still not certain which would be the best solution for this scenario, but this 
is the path I'm choosing to take. 

### Prerequisites

This program is designed in the following environment:

* [Anaconda python 3.6.0](https://anaconda.org/anaconda/python/files?version=3.6.0)
* [Datetime 4.3](https://pypi.org/project/DateTime/)


## Author

* **Ben McGauhey**

## License

This project is licensed under the GNU GPLv3 license. Please see [LICENSE.md](LICENSE.md)

## Acknowledgments

* [Al Sweigart](www.inventwithpython.com), Author of Automate the Boring 
Stuff With Python, for the great resource.

