# Nilearn

A lightweight digital library for Sudanese Grade 12 students.

Nilearn is a Flask-based web application designed to make educational resources easier to find and access in one place. It focuses on a simple, low-bandwidth-friendly experience for students who may have limited or unreliable internet access.

The project provides a centralized library where students can browse, search, filter, view, and download educational resources such as past papers, books, notes, and study guides.

## Why Nilearn?

Educational resources for Sudanese high-school students can be scattered across different websites, messaging groups, and other platforms.

Nilearn was built as a small solution to that problem:

* Bring resources into one organized library.
* Make resources easier to search and filter.
* Keep the interface simple and lightweight.
* Provide direct access to downloadable PDF resources.
* Organize resources by subject, type, and year.

The project was also an opportunity to practice building a complete web application from the database layer to the user interface and deployment.

---

## Features

### Resource Library

Students can browse available educational resources from a centralized library.

Each resource contains information such as:

* Title
* Subject
* Resource type
* Year
* Description
* File size

### Search

Users can search the library by resource title or subject.

### Subject Filtering

Resources can be filtered by subject to make it easier to find relevant material.

### Resource Details

Each resource has its own page containing its information before downloading.

### PDF Downloads

Students can directly download the available PDF resource from the resource page.

### Arabic Student Interface

The student-facing interface is presented in Arabic to make the platform more appropriate for its intended audience.

### Lightweight Design

The application intentionally avoids unnecessary features and focuses on the core flow:

**Browse → Find → Open → Download**

This keeps the project simple and suitable for users who may have limited bandwidth.

---

## Technology Stack

### Backend

  Python
  Flask

Flask handles the application routes, resource queries, search and filtering, and PDF delivery.

### Database

SQLite

SQLite is used to store the resource metadata, including titles, subjects, resource types, years, descriptions, file paths, and file sizes.

### Frontend

  HTML
  CSS
  Jinja2 templates

The frontend uses Flask's Jinja templating system to dynamically display resources and their information.

### Deployment

Render

The application is deployed as a web application using Gunicorn.

### Analytics

Google Analytics

Google Analytics was added to provide basic insight into website activity.

---

## Project Structure

Nilearn/

 app.py
 init_db.py
 nilearn.db
 Procfile
requirements.txt
.gitignore
 static/style.css
 templates/
    index.html
    resources.html
    resource_detail.html
    admin.html
 resources/
     PDF resources


### Important files

**app.py**

Contains the main Flask application, routes, database queries, search/filter functionality, resource pages, and PDF download handling.

**init_db.py**

Creates and initializes the SQLite database structure.

**nilearn.db**

Stores the metadata for the resources in the library.

**templates/**

Contains the HTML templates used by the application.

**static/**

Contains static assets such as CSS.

**resources/**

Contains the PDF resources made available through the application.

**Procfile**

Defines how the application is started on the deployment platform.

---

## How It Works

The main student workflow is intentionally simple:

Nilearn Homepage -> Resource Library -> Search / Filter -> Resource Details -> Download PDF


When a student opens the resource library, Flask retrieves the available resource metadata from SQLite.

The user can then search or filter the library.

After selecting a resource, Nilearn displays its information and provides access to the corresponding PDF.

---

## Database

The resources table stores the information needed to organize each educational resource.

The main fields are:

id: Unique resource identifier 
title: Resource title             
subject: Subject/category          
resource_type: Type of resource          
year: Resource year              
description: Short description
file_path: Location of the PDF        
file_size: PDF size in bytes 

The file size is converted into a readable format such as KB or MB when displayed to users.

---

## Design Decisions

### Why Flask?

Flask was chosen because it provides a lightweight way to build the application while giving me direct control over the routes, database interaction, templates, and file handling.

### Why SQLite?

Nilearn is a relatively small application, so SQLite provides a simple database and appropriate for the MVP 

### Why keep the application simple?

The main purpose of Nilearn is access to educational resources rather than building a large social or educational platform.

Instead of adding unnecessary functionality, the project focuses on the core problem:

 Helping students find educational resources quickly and download them easily.

### Why PDFs?

Many of the resources students need are already distributed as PDF documents. Supporting PDFs allows the application to organize existing educational material without requiring a complicated content system.

---

## Current Project Status

Nilearn is currently a portfolio MVP.

The application has been built and deployed as a working web project. It is designed around the needs of Sudanese Grade 12 students, but this project should not be interpreted as a claim of large-scale adoption or production-level usage.

The current version focuses on demonstrating the core functionality and technical implementation.

---

## Future Improvements

Possible future improvements include:

* More educational resources
* Additional subjects and resource categories
* Improved resource management
* More advanced search
* Better metadata organization
* Persistent cloud storage for a larger resource library
* Authentication and a more complete administration system
* Improved analytics and usage insights

These features are intentionally outside the scope of the current MVP.

---

## What I Learned

Building Nilearn provided practical experience with:

* Python and Flask
* Routing and HTTP requests
* Jinja templates
* SQLite databases
* SQL queries
* CRUD-style database operations
* File handling
* PDF delivery
* Search and filtering
* Arabic web interfaces
* Application deployment
* Structuring a project for a real-world use case

The project also involved making practical trade-offs between functionality, complexity, bandwidth considerations, and development time.

---

## Project Goal

Nilearn started from a simple idea:

Educational resources should be easier for students to find and access.

The project is a small attempt to turn that idea into a working web application while developing practical software engineering skills.
