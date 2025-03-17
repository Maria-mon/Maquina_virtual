FROM python:3.9

WORKDIR /work
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token=''"]
