import os
# set environment variable to use typescript
os.environ['NODE_OPTIONS'] = '--import tsx'
from typing import Callable
from javascript import require


js_test: Callable[..., int] = require('./js/index.js')
print(f"got {js_test()} from js in py")

ts_test: Callable[..., int] = require('./js/index.ts').default
print(f"got {ts_test()} from ts in py")