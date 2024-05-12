# Banknote Authentication using Machine Learning

This project demonstrates how to authenticate banknotes using machine learning techniques. It provides a Flask-based web application where users can input features related to banknotes, such as variance, skewness, curtosis, and entropy, and get predictions on whether the banknote is authentic or not.

## Usage

To use this application, follow these steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/banknote-authentication.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the Flask application:

```
python app.py
```

4. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

5. Input the values for variance, skewness, curtosis, and entropy in the provided fields.

6. Click on the "Authenticate" button to get the prediction.

## Dependencies

- Flask
- scikit-learn

## How it works

The application uses a RandomForestClassifier from the scikit-learn library to make predictions. The classifier is trained on a dataset containing features extracted from banknotes. When a user inputs values for variance, skewness, curtosis, and entropy, the application passes these values to the classifier and returns the prediction as to whether the banknote is authentic or not.

## License

This project is licensed under the MIT License - see the (alihassanml) file for details.

---

Feel free to customize the README further according to your project's specifics!
