import os
import json

from services import kubernetes
from services import rethinkdb

kubernetes.list_pods()