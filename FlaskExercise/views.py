from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    # TODO: Appropriately log the different button presses
    #   with the appropriate log level.
    if log == 'info':
        app.logger.info("INFO button clicked")

    elif log == 'warning':
        app.logger.warning("WARNING button clicked")

    elif log == 'error':
        app.logger.error("ERROR button clicked")

    elif log == 'critical':
        app.logger.critical("CRITICAL button clicked")
    return render_template(
        'index.html',
        log=log
    )
