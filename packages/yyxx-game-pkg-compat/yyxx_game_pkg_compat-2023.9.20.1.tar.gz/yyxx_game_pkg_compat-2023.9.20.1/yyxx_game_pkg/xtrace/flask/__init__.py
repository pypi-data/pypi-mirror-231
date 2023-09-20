# -*- coding: utf-8 -*-
# @Author   : LvWenQi
# @Time     : 2023/06/12
from flask import g, current_app
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.pymysql import PyMySQLInstrumentor
from opentelemetry.trace import get_current_span
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

from yyxx_game_pkg.xtrace import helper


class FlaskJaegerInstrumentor:
    def __init__(self):
        pass

    @staticmethod
    def _after_request(response):
        try:
            jaeger_config = current_app.config["JAEGER"]
            log_max_size = jaeger_config.get("log_max_size", 2048)
            span = get_current_span()
            # request event
            request_params = g.get("request_params")
            span.add_event("request", {"params": str(request_params)[:log_max_size]})
            # response event
            if jaeger_config.get("is_log"):
                response_params = g.get("response_params")
                if response_params:
                    span.add_event("response", {"params": str(response_params)[:log_max_size]})
            # inject trace parent to response header
            TraceContextTextMapPropagator().inject(response.headers)
        except Exception as e:
            print(e)
        return response

    def instrument(
            self,
            app,
            request_hook=None,
            response_hook=None,
            tracer_provider=None,
            excluded_urls=None,
            meter_provider=None,
            trace_requests=True,
            trace_redis=True,
            trace_pymysql=True
    ):
        try:
            # auto generate span
            if trace_requests:
                RequestsInstrumentor().instrument()
            if trace_redis:
                RedisInstrumentor().instrument()
            if trace_pymysql:
                PyMySQLInstrumentor().instrument()

            jaeger_config = app.config["JAEGER"]
            helper.register_to_jaeger(jaeger_config['service_name'], jaeger_config['jaeger_host'],
                                      jaeger_config['jaeger_port'])
            FlaskInstrumentor().instrument_app(
                app,
                request_hook=request_hook,
                response_hook=response_hook,
                tracer_provider=tracer_provider,
                excluded_urls=excluded_urls,
                meter_provider=meter_provider
            )
            # add after request trace middleware
            app.after_request_funcs.setdefault(None, []).append(self._after_request)
        except Exception as e:
            print(e)
