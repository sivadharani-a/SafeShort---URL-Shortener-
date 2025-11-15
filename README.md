Project Overview

SafeShort is a secure, fast, and lightweight URL shortening platform that integrates malicious URL detection, hash-based short code generation, and safe redirection logic.
Built using Python, Flask, and SQLite.

This project demonstrates skills in:

-Backend API development
-Secure input handling
-Database operations
-Hashing algorithms
-Web application security
-Clean UI development

Key Features
1. Malicious URL Detection

Identifies harmful URLs using predefined keyword patterns
Protects users from phishing / malware / scam domains
Rejects suspicious URLs and alerts the user

2. 6-Character Hash-Based Short Codes

Uses MD5 hashing (truncated) for a deterministic short code
Ensures minimal collision and fast generation

3. SQLite Database Integration

Stores URL mappings locally
Many-to-one mapping (same long URL → same short code)

4. Secure & Fast Redirection

Secure lookup of long URLs using parameterized queries
Automatic redirect from /<shortcode> to the original URL

5. Clean User Interface

Simple input form
Easy-to-read success pages
Professional CSS styling

Technical Concepts Demonstrated
-Area	Implementation
-Backend	Flask routes, POST/GET requests, redirects
-Security	Malicious URL detection, input validation
-Hashing	MD5-based short code generation
-Database	SQLite schema creation + CRUD
-Frontend	HTML, CSS
-Deployment Ready	Lightweight, easy to host anywhere

Tech Stack

Python 3
Flask
SQLite
HTML5
CSS3



