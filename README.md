# Adding Sentry to Django Demo Application

## Setup Instructions

First sign up for [Sentry](https://sentry.io/welcome/) to get a `dsn` value. Copy your `dsn` value from the Sentry console and paste it in the `/sentrydjango/settings.py` file on `line 19` as the value for the `dsn` parameter.

Secondly, sign up for a MySQL database at [db4free](https://www.db4free.net/) or alternatively use a sqlite database that comes with a django project. Whichever option you choose, be sure to update the database configuration section (line 101 - 110) in the `/sentrydjango/settings.py` file with the details for your database.
