from atexit import register
import re
from flask import Flask, render_template, request

from .form import ResiterForm, Filtre, Scan






app = Flask(__name__)

app.config.from_object('config')
