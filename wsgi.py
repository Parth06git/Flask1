from distutils.log import debug
from app import app

# from OpenSSL import SSL

# # context = SSL.Context(SSL.TLSv1_2_METHOD)
# # context.use_privatekey_file("server.key")
# # context.use_certificate_file("server.crt")

if __name__ == "__main__":
    app.run(debug=True,ssl_context="adhoc")
