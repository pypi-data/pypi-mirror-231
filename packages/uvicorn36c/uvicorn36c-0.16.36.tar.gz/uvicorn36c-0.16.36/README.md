# uvicorn-36c

A version of Uvicorn which works with Python 3.6 and passes client certificates in the request scope.


## Notes

This version fixes the h11 HTTP implementation to pass the client certificate through to the app, together with other request details as part of the scope. 

Make sure to use the H11 Worker. E.g., when using `gunicorn`: 

    gunicorn -k uvicorn.workers.UvicornH11Worker src.main:app --reload --certfile cert.pem --keyfile key.pem --cert-reqs 2 --ca-certs cert.pem --timeout 1200

