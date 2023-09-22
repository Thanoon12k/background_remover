## Image Background Remover Website 🖼️

An online tool for effortlessly removing image backgrounds. Designed for precision and user-friendliness, users can instantly upload and download edited photos. Ideal for both professionals and personal use.


## Beneficiaries 🎯

- Users Seeking Quick Edits: For those in need of rapid background removals.
- Good First Commit Project For New Django Developers

## Features 🛠️

- Remove Background in One Click And Download it as PNG
- Very Fast Processing
- Easy To Use ( just upload your image )
- Friendly  UI
- No Lags Or Adds In It
- Flexible API: 
Whether you're on a desktop, mobile or any other platform, our API endpoint    ```api/remove-bg/``` ensures you can fetch your images anytime, anywhere.
- Efficient Workflow:
 Each day, the initial 50 operations are driven by [remove.bg ](https://www.remove.bg/) Subsequently, our reliable Python backend seamlessly steps in, guaranteeing unlimited, consistent, and flawless service.




 ## Getting Started with Development 🚀

### Prerequisites
Ensure you have Python - version 3.11.5 recommanded - and pip installed on your machine.
### Installation

## Steps:

1. **Clone the repository.**
   ```bash
   git clone git@github.com:Thanoon12k/backgroud_remover.git
   ```
2. **Navigate to the project directory.**
    ```bash
    cd path-to-project-directory
    ```
3. **Create a virtual environment.**

    ```bash
    python -m venv venv        
    ```
4. **Activate the virtual environment.**
    -  On Windows:
        ```bash
        venv\Scripts\activate
         ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
         ```

3. **Install the required packages.**
    ```bash   
    pip install -r requirements.txt
    ```
6. **Run the Django server.**
    ```bash   
    python manage.py runserver
    ```
Visit http://localhost:8000 in your browser to see the website in action! .

# Developer Usage 🛠️

For those interested in integrating our background removal service into their applications, we offer a straightforward API endpoint.

## Accessing the API

**Endpoint**: `api/remove-bg/`

To use our API:

1. **POST Request**: Send a POST request to the endpoint with your image attached.
2. **Response**: You will receive the processed image with the background removed in PNG format.


### Example using `curl`:

  ```bash
     curl -X POST -F "image=@path_to_your_image jpg" http://127.0.0.1:8000/api/remove-bg/
  ```



## Contributing 🤝

Open to developers and enthusiasts who'd like to collaborate and enhance this project. Let's make this even more fantastic together!

## Acknowledgments:

- [Background Remover API](https://www.remove.bg/) for their API which powers this project.
- [ rembg Project ](https://github.com/danielgatis/rembg) for their Python Package which powers this project.


For live demonstrations, visit our website [ Live-WebSite](http://background1remover.pythonanywhere.com/)