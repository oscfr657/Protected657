# Software Requirements Specification #

## Content ##

* Background
* Purpose
* Problems
* Organisation
* Fuctional requirements
* Non-functional requirements
* Documentation
* Delivery requirements
* Special requirements

## Background ##

There is a need to always have access to private and or personal files from any type of device, desktop, laptop or smartphone,
regardless the device is private or work issued.

## Purpose ##

A service that provide file storage.
The service should list uploaded files and if so
the service must list right files for right users and 
the service must not list or in any other way show other users files to others.
The service alows upload and download of files.
The service must store the files in a secure and safe way.
The service must give correct people access to correct files.
The service must restrict access to files for incorrect devices and or users.

## Problems ##

Hackers target specific file storage providers.
If a file storage provider is attacked by hackers all of its customers can be impacted.

* The customers can lose all their files and the hackers can get access to sensitive and or private information.
* Denial of service (DoS) attacks, result in the customers losing access to their files and can't upload new ones.

## Organisation ##

The targeted audience is software developers.

## Functional requirements ##

A user must be able to upload files to the service.
A user must be able to download the files that the user have uploaded.
A user must be able to delete the files that the user have uploaded.

## Non-functional requirements ##

The service should always be available.
The service must always be secure and safe.
The service must be accessible from both desktops, laptops and smartphones.

## Ducumentation ##

There shall be a manual in the form of a README.md.
The README.md shall have installation and setup instructions.
THe README.md shall contain information for developers of how to:
* Run the service in a local development environment.
* How to run the tests.
* How to contribute to the project.

## Delivery requirements ##

The base framework for the delivered service must be upgradable.

## Special requirements ##

The code must be licensed "WITHOUT WARRANTY OF ANY KIND" and "IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE" of anything, so the MIT License should be used.
