import os
import sys

sys.path.append(os.path.dirname(__name__))

from sirclo import create_app
app = create_app()

if __name__ == "__main__":
  app.run(
    host="0.0.0.0",
    debug=True
    )
