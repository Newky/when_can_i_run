# When Can I Run?

## Overview

This script is the definition of laziness, and inspired by my dislike for running in the rain.

It looks up the weather for my area, and looks at precipitation levels to determine when you should run.

It allows you to set a time range for when you would like to run, and a precipitation threshold over which you are not willing to run.

## Setting your location.

For now, there is no automatic location detection, and it's actually quite a manual process.

You will need to download the source and change the `WEBSITE` global variable, to the same you get when you visit weather.com and navigate to hour-by-hour for your location.

An example from my town is currently used.

(I intend replacing this with something a little less difficult as soon as I can).

## Examples

```
$ when_can_i_run -p 30 --lunch-hours
```

This uses my configured lunch hours (12 - 3PM), and checks for any hours that have a less than 30% precipitation percentage.

```
$ when_can_i_run -p 10 --start_from=9 --until=16
```

This is a more configurable interface which allows you to set a to and until (both in 24 hour format). This will return the
hours between these to, that have precipitation levels below 10%. They will be sorted in ascending order of precipitation.

An example output might look like:

```
The following hours are available (results are sorted by precip):
18:00: Expected Precip %: 0
19:00: Expected Precip %: 0
20:00: Expected Precip %: 0
22:00: Expected Precip %: 0
21:00: Expected Precip %: 5
```
