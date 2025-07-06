FROM python:3.10

RUN apt-get update && apt-get install -y \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && rm -rf /var/lib/apt/lists/* # removes 0.04 GB of size from the image

COPY using_cookies.py insta_cookies.pkl requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "gpt_using_cookies.py"]