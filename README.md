# Soda Vault – Full Stack Development Project
Soda Vault is a full-stack development project designed to give users instant access to a comprehensive drink recipe database, featuring over 16,000 drink recipes. The project leverages modern mobile and backend technologies to provide seamless user experiences, efficient data handling, and cost-effective image generation solutions.

## Features
- **Mobile Application (React Native managed by Expo):**
  - Provides users with instant access to a database of 16,000+ drink recipes.
  - User-friendly interface with search functionality, supporting filtering by drink names or ingredients.
  - Users can create, edit, and manage their own drink collections.
  
- **REST API (Django & PostgreSQL):**
  - Facilitates CRUD operations for drink recipes and user collections.
  - Asynchronous data handling and pagination, improving response times for large queries by up to 80%.
  
- **Image Generation System:**
  - Integrates OpenAI’s DALL-E 3 and Google’s Gemini 1.5 Flash.
  - Cuts image generation costs by 50% through automated prompt engineering and validation processes.

## Key Technologies & Tools
- **Frontend:** React Native, Expo
- **Backend:** Django (REST Framework), PostgreSQL
- **Image Generation:** OpenAI's DALL-E 3, Google Gemini 1.5 Flash
- **API Communication:** Axios for handling API requests
- **Testing:** Postman for API testing and validation
- **Continuous Integration (CI) Pipeline:**
  - Originally used GitHub Actions for automating builds and tests and AWS EC2 for deployment
  - Currently self-hosting on a personal home server, using Cloudflare for DNS and Nginx for reverse proxy
  - Docker Compose for containerized development and deployment

## Project Highlights
- **Image Generation Optimization:** Reduced costs of image generation by 50% using automated prompt engineering and validation processes, ensuring accurate and efficient generation of drink images on demand.
- **Enhanced API Performance:** Implemented asynchronous handling and pagination, resulting in significant performance improvements for large queries.
- **Continuous Development Cycle:** Established a continuous integration pipeline, enabling rapid development and deployment cycles with AWS EC2, GitHub Actions, and Docker Compose.

## Future Plans
- **ESP32 Integration:** Planning to establish server-client connections with an ESP32 microcontroller for automating drink creation based on users' available ingredients.

## Active Repositories

![IMG_6264](https://github.com/MurkyPuma/CocktailCrafterDemo/assets/74885743/15d9b212-1f21-4dc1-a6d0-fab2db89a3b1)

I am actively working on a private repository to ensure that sensitive project details such as database backups, proprietary code, and experimental features remain confidential during development. This approach allows for a controlled environment where I can iterate and refine the application without exposing unfinished work to the public.

## 10/14 Update
<img width="1508" alt="image" src="https://github.com/user-attachments/assets/9839e4d0-2f54-4ae1-8bdc-b1235084149f">
The app is currently under review by Apple for release on the App Store. This review process is an essential step to ensure that the application meets Apple’s quality and safety standards. During this time, the app is evaluated for its functionality, user experience, and adherence to guidelines, which can take several days. I’m looking forward to receiving feedback and hopefully getting the green light for launch, so users can start enjoying the features and functionality I’ve worked hard to develop.

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/72bba6d4-8a4b-4ff3-b945-7aa7c578618f" width="30%" />
  <img src="https://github.com/user-attachments/assets/cd171109-dce4-4051-b8e6-1f87931354fa" width="30%" />
  <img src="https://github.com/user-attachments/assets/6e303791-d830-4439-914d-7fc29b714c38" width="30%" />
  <img src="https://github.com/user-attachments/assets/1c5d9509-22dc-4c98-bfde-2ee51a6b7632" width="30%" />
  <img src="https://github.com/user-attachments/assets/0d4a8fc9-be17-4efd-9622-54c2a7448609" width="30%" />
  <img src="https://github.com/user-attachments/assets/a03d3518-dd12-4e92-8109-0dc652cca519" width="30%" />
</div>

## 03/14 Update
Cocktail Crafter is an ongoing project for a drink making machine. The purpose of this website is to allow users to interface with a local PostgreSQL server containing 2,700+ drinks. Images are generated and saved on demand with OpenAI's API. The program currently handles user accounts, allowing users to add their own drinks to the database. Users are also able to search asynchronously by name or single ingredient. Results are displayed quickly with the use of progressive JPEG images and infinite scrolling, meaning only x amount of results are fetched from the server until more are called while scrolling. The goal of this project is to send instructions to a machine and create drinks based on user's bar/ingredients. The RESTful API's functionality is verified through Postman testing. Axios is used to manage API requests, adhering to CRUD principles.

The upcoming phases involve developing a mobile application for the app store using React Native for the frontend interface. I also plan to establish a server-client connection with an ESP32 to recieve data and create drinks in the near future.

Technologies used include Django, PostgreSQL, HTML, CSS, JavaScript, Axios, and C++ for the initial parsing of CSV files to SQL.

![image](https://github.com/MurkyPuma/CocktailCrafterDemo/assets/74885743/61776365-49c1-4fcb-9d93-315727dfb635)
![306352207-3f7539d4-2c15-4cb0-8065-b03ad6993ac7](https://github.com/MurkyPuma/CocktailCrafterDemo/assets/74885743/cdbfc04d-5cf7-41d2-960b-db14b81402bb)
![306352503-920c99d6-806f-4914-ab48-9c8cba59f4b7](https://github.com/MurkyPuma/CocktailCrafterDemo/assets/74885743/15012789-2fe6-48c5-8996-d7a1ceb1f243)
![306352937-cbdcee58-9c40-4dbe-b4be-61eac0a2b999](https://github.com/MurkyPuma/CocktailCrafterDemo/assets/74885743/b45b0e71-c4b2-415e-8e8f-c0bd2e38efd7)
