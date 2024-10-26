# Movie Recommendation System

## Project Description

The Movie Recommendation System is a web application designed to help users find movie suggestions based on their preferences. Utilizing collaborative filtering techniques and a similarity matrix, the system recommends movies that are similar to those a user has liked before. The application is built using Python, Streamlit, and other libraries, and it fetches movie posters and details from the TMDB (The Movie Database) API.

### Features

- **Movie Recommendations**: Users can select a movie, and the system will recommend similar titles.
- **Movie Posters**: Displays posters of the recommended movies fetched from TMDB.
- **User-Friendly Interface**: Built with Streamlit for an interactive and responsive experience.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Required libraries:
  - Streamlit
  - Pandas
  - Requests

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
2. Install the required packages:
   pip install -r requirements.txt
3. Run the Streamlit application:
   streamlit run app.py

   This will start a local server on your machine. You can access the web app through the displayed 
   local URL (usually http://localhost:8501/)

### Usage
 1. Select a movie from the dropdown.
 2. Click on the Show Recommendation button.
 3.The system will display five recommended movies along with their posters.

### Screenshots
1. Homepage:
  This is the initial page of the application where users can start their movie recommendations.
![image alt](https://github.com/UttamKumar25/Movie-Recommendation-System/blob/f2e08bae2f425544bf9907c1676cbc34ff8e11ae/1.png)

2. Movie Selection:
  Users can select their desired movie from the dropdown list here.
![image alt](https://github.com/UttamKumar25/Movie-Recommendation-System/blob/f2e08bae2f425544bf9907c1676cbc34ff8e11ae/2.png)

3.Recommendations Output:
  This shows the recommended movies along with their posters after a selection is made.
![image alt](https://github.com/UttamKumar25/Movie-Recommendation-System/blob/f2e08bae2f425544bf9907c1676cbc34ff8e11ae/3.png)



