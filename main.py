"""
The Entry point for this web applicaion

Author: Mathew Owusu Jr
"""


from website import create_app

# Create the flask web app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)