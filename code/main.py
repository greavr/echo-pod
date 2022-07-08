from flask import Flask, request, jsonify
import os

## Config App
app = Flask(__name__)

## Default App Hosting
@app.route("/")
def default():
    ## Output options
    result = {}
    result["method"] = str(request.method)
    result["base_url"] = str(request.base_url)
    result["query_string"] = str(request.query_string)   
    result["url"] = str(request.url)
    result["headers"] = str(request.headers)
    result["host"] = str(request.host)
    result["host_url"] = str(request.host_url)
    result["full_path"] = str(request.full_path)
    result["endpoint"] = str(request.endpoint)
    result["form"] = str(request.form.to_dict())
    result["files"] = str(request.files.to_dict())
    result["data"] = str(request.data)
    result["content_encoding"] = str(request.content_encoding)
    result["content_length"] = str(request.content_length)
    result["content_type"] = str(request.content_type)
    result["stream"] = str(request.stream)
    result["cookies"] = str(request.cookies.to_dict())
    result["user_agent"] = str(request.user_agent)
    result["authorization"] = str(request.authorization)
    result["cache_control"] = str(request.cache_control)
    result["date"] = str(request.date)
    result["mimetype"] = str(request.mimetype)
    result["is_secure"] = str(request.is_secure)
    result["scheme"] = str(request.scheme)
    result["remote_addr"] = str(request.remote_addr)
    result["remote_user"] = str(request.remote_user)
    result["values"] = str(request.values.to_dict())
    result["request"] = str(request)

    if request.content_type == 'application/json':
        result["json"] = request.json

    return jsonify(result)

   # return json.dumps({'success':True, 'values':result}), 201, {'ContentType':'application/json'} 


if __name__ == "__main__":
    ## Setup APP
    if os.environ.get("GOOGLE_APPLICATION_CREDENTIALS") is not None:
        import google.cloud.logging
        LoggingClient = google.cloud.logging.Client()
        LoggingClient.get_default_handler()
        LoggingClient.setup_logging()

    ## Run APP
    app.run(host='0.0.0.0', port=8080, debug=True)