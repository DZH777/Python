https://docs.python.org/3/using/windows.html#the-full-installer
https://pypi.org/project/Flask/

1. ������������� �� ���������: python-3.7.4-amd64.exe
2. ��������� ������������������: 
	- ��������� ������
	- ������� � ��� �����
	- ��������� py hello1.py
   ������ ����������: hello1 from Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)]
3. ������������� Flask:
	pip install -U Flask
4. ��������� ������������������: 
	- ��������� ������
	- ������� � ��� �����
	- ��������� set FLASK_APP=hello2.py
	- ��������� flask run
   ������ ����������: Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
5. ��������� Flask-Session:
	pip install Flask-Session