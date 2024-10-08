# Django Project: Custom User Model with Permissions and Groups

This Django project demonstrates how to customize the user model, implement role-based access control using permissions and groups, and apply them to control access to different features in the application.

## Project Overview

This project is designed to manage books, where different user roles (like Editors, Viewers, and Admins) have specific permissions to create, edit, view, and delete books.

## Features

- Custom user model extending Django’s `AbstractUser` with additional fields like `date_of_birth` and `profile_photo`.
- Role-based access control using custom permissions and groups.
- Function-based views for handling book creation, editing, deletion, and listing.
- Permission checks implemented to restrict access to views based on user roles.

## Project Structure

