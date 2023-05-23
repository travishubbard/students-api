# Student API


I love data, but it does no good sitting on a machine collecting lint.

So I create APIs that we can get to it and do fun things.

Here is a very basic API to a Student database, created using Flask.

Yes, there are "better options" than Flask, but who cares?

It's easy and fast, just like me.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Run](#run)

## Background

## Install

1. I'm running Python 3.11.3

2. You might need to:

```
pip3 install Flask
```

3. I've included the SQLite database, but also the SQL (STUDENTS.sql) you can use to create the database on your own if you'd like.

## Run

From the command line:

```
python3 student-api.py
```

1. Go to home:

```
http://127.0.0.1:8888/
```


2. See all students in the database:

```
http://127.0.0.1:8888/getStudents
```

3. Get student by ID:

```
http://127.0.0.1:8888/getStudentById/2
```

