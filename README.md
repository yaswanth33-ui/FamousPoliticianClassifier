# Famous Politician Classifier

## Overview
This project is designed to classify famous politicians using machine learning. It consists of:
- A **backend server** Flask for handling API requests.
- A **frontend UI**  for user interaction.
- A **trained model** Support Vector Classifier for politician classification.

## Prerequisites
- Python 3.8+ and Node.js 14+ installed.
- `pip` for Python dependencies.
- `npm` or `yarn` for frontend dependencies.

## Project Structure
- `server/`: Contains the backend code for handling requests and serving the model.
- `UI/`: Contains the frontend code for the user interface.
- `model/`: Contains the trained machine learning model and related files.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yaswanth33-ui/FamousPoliticianClassifier.git
   cd FamousPoliticianClassifier
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the server**:
   Navigate to the `server/` directory and run the following command to start the server:
   ```bash
   python server.py
   ```
   The server will start on `http://localhost:5000` by default.
4. **Run the UI**:
   Navigate to the `UI/` directory and install the required dependencies:
   ```bash
   npm install
   ```
   Then, start the frontend application:
   ```bash
   npm start
   ```
   The UI will be available at `http://localhost:3000/app.html`.

## Usage
### Backend
- The server exposes the following API endpoints:
  - `POST /classify`: Accepts an image of a politician and returns the 

### Frontend
- The UI allows users to upload an image of a politician and view the classification result.
- It communicates with the backend API to fetch and display data.

## Model Details
- **Architecture**: Support Vector Classifier trained on various images available dataset folder.
- **Accuracy**: ~82% on the test set.
- **Supported Politicians**: 20+ (e.g., "Narendra Modi", "Joe Biden").

## Future Work
- Expand the dataset to include more politicians.
- Add real-time video classification.
- Improve UI with historical results.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/xyz`).
3. Commit changes (`git commit -m 'Add xyz'`).
4. Push to the branch (`git push origin feature/xyz`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. 

## Support

For any issues or questions, please open an issue on the [GitHub repository](https://github.com/yaswanth33-ui/FamousPoliticianClassifier/issues).
