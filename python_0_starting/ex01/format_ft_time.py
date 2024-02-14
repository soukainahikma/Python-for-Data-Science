from datetime import datetime
import time

epoch = time.time()
print(f'Seconds since January 1, 1970: {"{:,.4f}".format(epoch)} or {"{:.2e}".format(epoch)} in\
      scientific notation\n{datetime.now().strftime("%b %d %Y")}')

