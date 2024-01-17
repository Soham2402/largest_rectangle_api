# Project Title

## Overview

This assignment involved finding the biggest rectangle of a given 2d non binary array and then providing an endpoint which users can use to find it. I also had to store the results in a database along with the time taken for analysis.

It was an especially difficult challenge as I had to work with fastapi which i have never worked with as well as dabble into a hard level Leetcode question which was an another journey.

## Setup Instructions

1. **Clone Repository:**

   ```bash
   git clone github.com/Soham2402/largest_rectangle_api
   ```

2. **Create Virtual Environment:**

   ```bash
   python -m venv env
   ```

3. **Activate Virtual Environment:**

   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up PostgreSQL Database:**

   - Open pgAdmin and create a new database named `MatrixDb`.
   - Replace the database connection URL in `database.py`:
     ```python
     # Update the following line with your PostgreSQL credentials
     DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/MatrixDb"
     ```

6. **Run the Server:**
   ```bash
   uvicorn main:app --reload
   ```

## Project Structure

### 1. `utils.py`

- **Largest Rectangle Algorithm:**
  The heart of the algorithm for finding the largest rectangle in the array.

- **Occurrences Calculation:**
  Function to find occurrences of each number based on the one above it.

- **Rectangle Calculation:**
  Function to calculate the biggest rectangle using the parsed array.

### 2. `main.py`

- **Endpoints:**
  `get_stats`,`get_stats_by_id`,`get_matrix_size`

- **Pydantic Models:**
  Models used in the project with their definitions.

- **Database Insert Logic:**
  Logic for inserting data into the PostgreSQL database.

### 3. `models.py`

- **Database Schema:**
  The schema includes 4 rows, `matrix` which is the input matrix,`value` which shows the integer with the biggest rectangle along with its `occurances` and `time_taken` which is the time taken to calculate this rectangle.

### 4. `database.py`

- **Database Connection:**
  Creation of the connection between the PostgreSQL server and the API.

## Additional Notes

##### Sources:

`NeetCode`
`fastAPI Documentation`
`Eric Roby`
