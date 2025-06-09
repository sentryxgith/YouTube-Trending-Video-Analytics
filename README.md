# YouTube-Trending-Video-Analytics

A Python-based project for collecting and analyzing YouTube data using the YouTube Data API. This project demonstrates how to fetch YouTube video metadata, preprocess the data, and perform exploratory data analysis (EDA) to gain insights into video trends, performance, and content engagement.

---

## Features
- **Data Collection**: Fetch video data such as titles, descriptions, view counts, likes, dislikes, and more using the YouTube Data API.
- **Data Preprocessing**: Handle missing values, clean data, and transform it for analysis.
- **Exploratory Data Analysis (EDA)**:
  - Analyze video performance metrics.
  - Visualize trends such as popular categories, top-performing videos, and engagement rates.
  - Detect correlations between features.
- **Flexible Framework**: Modular code structure for easy extension and maintenance.

---

## Technologies Used
- **Python**: Core programming language.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualization.
- **YouTube Data API**: For accessing YouTube video metadata.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sentryxgith/YouTube-Data-Collection-and-Analysis-with-Python.git
   cd YouTube-Data-Collection-and-Analysis-with-Python
   ```

2. Obtain your YouTube Data API key:
   - Visit [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project and enable the YouTube Data API v3.
   - Generate an API key and replace the placeholder in the script.

---

## Usage

1. **Set up the API key**:
   Open the script where the API key is required, and replace:
   ```python
   API_KEY = "YOUR_API_KEY_HERE"
   ```

2. **Run the script**:
   - Use `main.py` to fetch YouTube data.
   - Perform analysis using the Jupyter Notebooks provided.

3. **Explore the results**:
   - View processed data in CSV format.
   - Open the EDA notebook to visualize insights.

---

## Project Structure

```
YouTube-Data-Collection-and-Analysis-with-Python/
├── main.py                 # Script for data fetching
├── data.py                 # Script for data preprocessing
├── distribution.py         # Script for analyzing data by distribution
├── category.py             # Script for analyzing data by categories
├── duration.py             # Script for analyzing data by duration
├── tags.py                 # Script for analyzing data by tags
├── publish hour.py         # Script for analyzing data by publish hour
├── README.md               # Project documentation
```

---

## Examples of Analysis

- **Category Popularity**: Identify which categories have the most videos trending.
- **Engagement Metrics**: Compare likes, dislikes, and comment counts for videos.
- **Time Trends**: Understand how upload times affect video popularity.

---
## Charts
![View, Like and Comment Count Distribution](https://github.com/user-attachments/assets/b762e8dc-0f14-4741-bc74-9ae3115dea7e)
![Correlation Matrix of Engagement Metrics](https://github.com/user-attachments/assets/02a549dd-59f0-4831-931e-7c1cc3863e1f)
![Number of Trending Videos by Category](https://github.com/user-attachments/assets/805e3b21-c877-4511-9d30-8e3c366195a0)
![Average View, Like and Comment Count by Category](https://github.com/user-attachments/assets/fc59cf4e-2f5f-412f-94d7-de2c53805394)
![Video Length vs View Count](https://github.com/user-attachments/assets/06b4f0ab-3d39-440a-9a92-a31e484ebe9d)
![Average View, Like and Comment Count by Duration Range](https://github.com/user-attachments/assets/b8a5f2f7-1fbc-46b6-8bf3-cdd760c350cf)
![Number of Tags vs View Count](https://github.com/user-attachments/assets/42b7e579-6ece-4df9-97fd-794c726130b7)
![Distribution of Videos by Publish Hour](https://github.com/user-attachments/assets/c686a67e-d0de-436f-9cd6-50b3684757a0)
![Publish Hour vs View Count](https://github.com/user-attachments/assets/6a92b764-59b0-43a3-a7d2-437f196f632d)

## Contributing

Contributions are welcome! Please fork the repository, create a branch, and submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- The YouTube Data API team for providing an excellent API.
- The open-source Python community for their amazing libraries.

---

Happy analyzing! 🎉
```

Feel free to adjust this based on additional project-specific details!
