# 🗳️ Poll Voting System

A full-stack, professional-grade Poll Voting Web App built using **Flask** and **Chart.js**. This platform allows users to create polls, vote securely, and view results in both **tabular** and **graphical (bar + pie)** formats with a modern **sky blue & white** themed interface.

---

## 🌟 Features

- ✅ **Create Polls:** Custom questions with 3 user-defined options.
- ✅ **Vote Once:** Secure voting system using browser session.
- ✅ **Live Results:** Instant result display with Bar and Pie Charts.
- ✅ **Modern UI:** Fully responsive, clean interface with a professional blue/white theme.
- ✅ **Error Handling:** Form validation and duplicate vote protection.
- ✅ **Client-Side Charts:** Integrated with Chart.js for real-time visual analytics.

---

## 🖼️ UI Preview

![Preview](https://dummyimage.com/800x400/a1c4fd/005792&text=Poll+Voting+System+Preview)

---

## 📁 Project Structure

    poll-app/
    ├── app.py
    ├── requirements.txt
    ├── static/
    │ └── styles.css
    └── templates/
    ├── layout.html
    ├── index.html
    ├── poll.html
    └── results.html
## Setup Virtual Environment
    python -m venv .venv
    .venv\Scripts\activate       # On Windows
## Install Dependencies
    pip install -r requirements.txt
## Run the Application
    python app.py
## Access the Web App
    Visit http://127.0.0.1:5000 in your browser.
## 🧠 Tech Stack
   
    | Layer        | Technology       |
    |--------------|------------------|
    | Backend      | Flask (Python)   |
    | Frontend     | HTML, CSS        |
    | Charts       | Chart.js         |
    | Styling      | Custom CSS (Sky Blue + White Theme) |
    | Hosting      | Localhost (Can be deployed on Render/Heroku) |
## 🔮 Future Enhancements
| 🔧 Feature Name             | 📝 Description                                                           | 🎯 Purpose / Benefit                                      | ⏳ Priority |
| --------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------- | ---------- |
| IP + Browser Fingerprinting | Track user's IP address and browser/device fingerprint to block revoting | Prevents circumvention of session-based vote restriction  | 🔼 High    |
| User Authentication System  | Add login/signup functionality with user management                      | Assign votes to authenticated users; enables vote history | 🔼 High    |
| Persistent Database Storage | Integrate SQLite/PostgreSQL to store polls and votes persistently        | Data durability, analytics, and large-scale poll handling | 🔼 High    |
| Poll Expiration Timer       | Add scheduling feature to auto-close polls after a specific duration     | Enables time-bound event participation                    | 🔼 High    |
| Shareable Public Poll URLs  | Generate unique URLs to share polls with external users                  | Enables public distribution and wider engagement          | 🔼 Medium  |
| Admin Analytics Dashboard   | Create a backend panel showing participation trends and insights         | Provides poll owners deeper visibility into responses     | 🔼 Medium  |
| Mobile UI Optimization      | Optimize layouts for smaller screens and touch interactions              | Ensures smooth experience across all devices              | 🔼 Medium  |
| Multiple Question Types     | Add Yes/No, star rating, dropdown, or multiple selection polls           | Broadens usability for surveys and detailed forms         | 🔼 Medium  |
| Exportable Reports          | Generate downloadable reports (PDF/CSV) of poll results                  | Useful for documentation, audits, or sharing offline      | 🔽 Low     |
| Cloud Deployment            | Deploy on Heroku, Render, or PythonAnywhere                              | Makes app accessible on the internet                      | 🔽 Low     |
| CAPTCHA Integration         | Prevent bot submissions by integrating CAPTCHA on vote form              | Improves security and integrity                           | 🔽 Low     |
| Dark Mode Toggle            | Add light/dark mode switch in UI                                         | Improves accessibility and aesthetic for users            | 🔽 Low     |
## 📄 License


Licensed under the MIT License. You are free to use, modify, and distribute this software with proper credit.

