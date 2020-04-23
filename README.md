# rest_api
Infectious disease api

It aggregates the sources and provide consistent data format through api
Note: Currently it looks up only one source.

* How to run the app:
Run the app as follows:
$ python app.py 
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
192.168.1.29 - - [22/Apr/2020 21:01:35] "GET /covid HTTP/1.1" 200 -



* How to get data through client:
Client like curl can pull the json data as follows:
$ curl -o covid.json http://192.168.1.29:5000/covid
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 42200  100 42200    0     0   303k      0 --:--:-- --:--:-- --:--:--  303k


The sample covid.json is added to the repo.

