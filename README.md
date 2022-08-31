# Api Demostración Soluciones Andinas

Requistitos Git y Docker

git clone https://github.com/luisdalmasso/Fast_Api_Andina.git
cd Fast_Api_Andina
docker build -t fast_api_andina .
docker run -d --name fast_api_andina -p 8000:80 fast_api_andina
ingresar a http://127.0.0.1:8000/docs
