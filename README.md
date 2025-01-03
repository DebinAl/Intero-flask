# VENTIX - Microservices-Based Ticketing Application
This repository contains the VENTIX project, a microservices-based ticketing application. The project was developed collaboratively using various technologies, with a focus on scalability, modularity, and reliability.

## 📜 Project Overview
VENTIX is a robust ticketing application designed to handle ticket bookings, user management, event management, and multimedia handling through a distributed microservices architecture. Each service is independently developed, maintained, and deployed, ensuring flexibility and resilience.

For a detailed explanation of the application's architecture, features, and technology stack, refer to the [Project Report](https://1drv.ms/w/c/7a8f2b2853bae142/ERX0eqf0NVRKoZt18yTekfYBRw-A_bXOiHCJc6tccRp1Uw?e=rTxWNs).

## 🔧 My Contribution
As part of the development team, I worked on the Flask-Python microservice to handle the following functionalities:

**1. Talent Service**
- **Purpose**: Manages data related to event talents such as groups, singers, and bands. This service enables users to view the list of talents associated with specific events on the website.
- **Features**:
  - CRUD (Create, Read, Update, Delete) operations for talent data.
  - Integration with the event service to display relevant talent data for each event.
  - Technology Stack:
    - Framework: Flask (Python)
    - Database: Shared MongoDB instance
**2. Image Service**
- **Purpose**: Acts as a Content Delivery Network (CDN) to manage all images used throughout the website. Handles image uploads, metadata storage, and retrieval.
- **Features**:
  - Saves new images to ImgBB and stores their metadata (ID, URL, etc.) in the database.
  - CRUD operations for image metadata.
  - Provides efficient access to image assets for other services and the frontend.
  - Technology Stack:
  - Framework: Flask (Python)
    - Database: Shared MongoDB instance
    - External Tool: ImgBB API for image hosting
