FROM python:3.9  

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "pers_gym" ]  # your-script.pyを実行するPythonファイル名に置き換えてください。
