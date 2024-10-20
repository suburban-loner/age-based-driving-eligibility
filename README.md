# Age-Based Driving Eligibility Program
This Python program demonstrates the concept of method overriding by defining a base class Adult and a subclass Child. The program takes user input for personal details (name, age, hair color, and eye color), then determines whether the person is old enough to drive based on their age.

## Features
User Input: The program prompts the user to enter the following details:
Name
Age
Hair Color
Eye Color
### Adult Class: 
Represents an adult with the following attributes:
name: The name of the person.
age: The age of the person.
eye_colour: The eye color of the person.
hair_colour: The hair color of the person.
It includes a method called can_drive() that checks if the person is old enough to drive.

### Child Subclass: 
A subclass of Adult that overrides the can_drive() method to indicate that the person is too young to drive.

### Dynamic Class Assignment: 
Based on the user's age, the program dynamically creates an instance of either the Adult or Child class. If the person is 18 or older, they are classified as an Adult; otherwise, they are classified as a Child. The program then calls the appropriate can_drive() method to display a message indicating driving eligibility.

## Program Logic
The user is asked to input their name, age, eye color, and hair color.
The program checks if the user is 18 or older:
If true, an instance of the Adult class is created, and the can_drive() method prints that the person is old enough to drive.
If false, an instance of the Child class is created, and the overridden can_drive() method prints that the person is too young to drive.
