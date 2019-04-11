#!/usr/bin/env python3
import argparse
from cheroot.wsgi import Server as WSGIServer
from cheroot.wsgi import PathInfoDispatcher as WSGIPathInfoDispatcher
from requestlogger import WSGILogger, ApacheFormatter
from logging import StreamHandler, getLogger, INFO

from webapp.app import app

argument_parser = argparse.ArgumentParser("Converter Webapp")
argument_parser.add_argument("-p", "--listen-port", type=int, default=8000, help="The port to listen on.")
argument_parser.add_argument("-H", "--bind-host", type=str, default="127.0.0.1", help="The host address to bind on.")

if __name__ == "__main__":
    logger = getLogger('')
    handler = StreamHandler()
    logger.addHandler(handler)
    logger.setLevel(INFO)
    args = argument_parser.parse_args()
    logged_app = WSGILogger(app, [handler], ApacheFormatter())

    app_dispatcher = WSGIPathInfoDispatcher({'/': logged_app})
    app_server = WSGIServer((args.bind_host, args.listen_port), app_dispatcher)
    try:
        logger.info("Listening on http://{0}:{1}/ ...".format(args.bind_host, args.listen_port))
        app_server.start()
    except KeyboardInterrupt:
        app_server.stop()
