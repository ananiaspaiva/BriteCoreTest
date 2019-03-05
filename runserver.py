#!/usr/bin/env python
from accounting import app

if __name__ == "__main__":
    print('Vai iniciar o server!')
    app.run(debug=True, host='0.0.0.0')
