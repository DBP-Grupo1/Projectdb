from app import views, models, forms, controller, app
from app import app

if __name__ == '__main__':
    app.run(port=5002, debug=True)

'''
if __name__ == '__main__':
    app.run(port=5002, debug=True)
else:
    print("Using global variables from FLASK")
'''